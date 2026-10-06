import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest
import warnings
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import credentialStore as credentials
import databaseBackup as backups
import serviceControl as services


class CredentialTests(unittest.TestCase):
    def test_missing_token_never_uses_owner(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True), \
                patch.object(credentials.subprocess, 'run') as run:
            with self.assertRaisesRegex(ValueError, 'Supply the test token'):
                credentials.item_fields('vault', 'item', account='test', directory=directory)
            run.assert_not_called()

    def test_runtime_and_owner_authentication_are_distinct(self):
        response = subprocess.CompletedProcess([], 0, '{"fields": []}', '')
        with patch.dict(os.environ, {'OP_SERVICE_ACCOUNT_TOKEN': 'secret', 'OP_CONNECT_TOKEN': 'wrong', 'OP_SESSION_x': 'wrong'}), \
                patch.object(credentials.subprocess, 'run', return_value=response) as run:
            credentials.item_fields('vault', 'item', account='test', directory='/unused')
            self.assertEqual({k:v for k,v in run.call_args.kwargs['env'].items() if k.startswith('OP_')}, {'OP_SERVICE_ACCOUNT_TOKEN':'secret'})
            credentials.item_fields('vault', 'item')
            self.assertFalse(any(k.startswith('OP_') for k in run.call_args.kwargs['env']))

    def test_insecure_token_is_refused(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True):
            p = Path(directory) / 'test-token'; p.write_text('secret'); p.chmod(0o644)
            with self.assertRaisesRegex(ValueError, 'mode 0600'):
                credentials.service_token(directory, 'test')

    def test_wrong_project_and_inherited_overrides(self):
        values = dict(host='test.pooler.supabase.com',port='5432',database='postgres',username='reader.project',password='secret')
        fields = [{'id':k,'value':v} for k,v in values.items()]
        with patch.dict(os.environ, {'PGSERVICE':'wrong','PGOPTIONS':'unsafe','OP_SERVICE_ACCOUNT_TOKEN':'secret'}):
            env = backups.database_environment(fields, 'project', 'reader', Path('/ca'))
        self.assertEqual(env['PGSSLMODE'], 'verify-full')
        self.assertFalse(any(k in env for k in ('PGSERVICE','PGOPTIONS','OP_SERVICE_ACCOUNT_TOKEN')))
        with self.assertRaises(RuntimeError):
            backups.database_environment(fields, 'other', 'reader', Path('/ca'))

    def test_credential_read_closes_unused_stdin(self):
        response = subprocess.CompletedProcess([], 0, '{"fields": []}', '')
        with patch.object(credentials.subprocess, 'run', return_value=response) as run:
            credentials.item_fields('vault', 'item')
        self.assertEqual(run.call_args.kwargs.get('stdin'), subprocess.DEVNULL)

    def test_credential_failure_names_status_and_withholds_output(self):
        response = subprocess.CompletedProcess([], 7, 'synthetic-record', 'synthetic-password')
        with patch.object(credentials.subprocess, 'run', return_value=response):
            with self.assertRaises(ValueError) as failure:
                credentials.item_fields('vault', 'item')
        message = str(failure.exception)
        self.assertIn('op item get', message)
        self.assertIn('exit 7', message)
        self.assertNotIn('synthetic-record', message)
        self.assertNotIn('synthetic-password', message)


class ServiceTests(unittest.TestCase):
    def test_startup_timeout_stops_only_the_selected_unit(self):
        for command in ([], ['python3', 'app.py']):
            with self.subTest(kind='installed' if not command else 'transient'):
                original = subprocess.TimeoutExpired(['synthetic-start'], 1)
                def invoke(args, **kwargs):
                    if args[0] == 'systemd-run' or args[2] == 'start':
                        raise original
                    return subprocess.CompletedProcess(args, 0, '', '')
                service = services.Service('test.service', command, Path('/tmp'), {}, 3199)
                with patch.object(services, 'properties', return_value={'LoadState': 'not-found', 'ActiveState': 'inactive'}), \
                        patch.object(services, 'run', side_effect=invoke) as run:
                    with self.assertRaises(subprocess.TimeoutExpired) as failure:
                        services.control(service, 'start')
                self.assertIs(failure.exception, original)
                self.assertEqual(run.call_args_list[-1].args[0], ['systemctl', '--user', 'stop', 'test.service'])
                self.assertFalse(any('kill' in str(call) for call in run.call_args_list))

    def test_readiness_properties_timeout_stops_the_selected_unit(self):
        original = subprocess.TimeoutExpired(['synthetic-properties'], 1)
        with patch.object(services, 'properties', side_effect=[{'ActiveState': 'inactive'}, original]), \
                patch.object(services, 'run', return_value=subprocess.CompletedProcess([], 0, '', '')) as run:
            with self.assertRaises(subprocess.TimeoutExpired) as failure:
                services.control(services.Service('test.service'), 'start')
        self.assertIs(failure.exception, original)
        self.assertEqual(run.call_args_list[-1].args[0], ['systemctl', '--user', 'stop', 'test.service'])

    def test_cleanup_failure_keeps_the_service_startup_error(self):
        original = subprocess.TimeoutExpired(['synthetic-start'], 1)
        def invoke(args, **kwargs):
            if args[2] == 'start':
                raise original
            raise RuntimeError('synthetic-password')
        with patch.object(services, 'properties', return_value={'ActiveState': 'inactive'}), \
                patch.object(services, 'run', side_effect=invoke), \
                patch.object(services.sys, 'stderr', new_callable=io.StringIO) as diagnostic:
            with self.assertRaises(subprocess.TimeoutExpired) as failure:
                services.control(services.Service('test.service'), 'start')
        self.assertIs(failure.exception, original)
        message = '\n'.join(getattr(original, '__notes__', [])) + diagnostic.getvalue()
        self.assertIn('cleanup', message)
        self.assertNotIn('synthetic-password', message)

    def test_initial_state_timeout_does_not_stop_an_unstarted_unit(self):
        with patch.object(services, 'properties', side_effect=subprocess.TimeoutExpired(['synthetic-properties'], 1)), \
                patch.object(services, 'run') as run:
            with self.assertRaises(subprocess.TimeoutExpired):
                services.control(services.Service('test.service'), 'start')
        run.assert_not_called()

    def test_control_command_is_bounded_and_closes_unused_stdin(self):
        with patch.object(services.subprocess, 'run') as run:
            services.run(['systemctl', '--user', 'show', 'test.service'])
        self.assertEqual(run.call_args.kwargs.get('stdin'), subprocess.DEVNULL)
        self.assertGreater(run.call_args.kwargs.get('timeout', 0), 0)

    def test_start_is_idempotent(self):
        with patch.object(services, 'properties', return_value={'ActiveState':'active'}), patch.object(services, 'run') as run:
            self.assertEqual(services.control(services.Service('test.service'), 'start'), 0)
            run.assert_not_called()

    def test_unrelated_listener_is_not_ready(self):
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = b'1234'
        opener = unittest.mock.Mock(); opener.open.return_value = response
        with patch.object(services, 'properties', return_value={'ActiveState':'active','ControlGroup':'/user/test.service'}), \
                patch.object(services.urllib.request, 'build_opener', return_value=opener), \
                patch.object(Path, 'read_text', return_value='0::/user/other.service\n'):
            self.assertFalse(services.ready(services.Service('test.service',port=3199)))

    def test_failed_preview_stops_only_named_unit(self):
        with patch.object(services, 'properties', return_value={'LoadState':'not-found','ActiveState':'inactive'}), \
                patch.object(services, 'ready', return_value=False), patch.object(services, 'run') as run:
            with self.assertRaises(RuntimeError):
                services.control(services.Service('test.service',['python3','app.py'],Path('/tmp'),{},3199),'start')
            self.assertEqual(run.call_args.args[0], ['systemctl','--user','stop','test.service'])
            self.assertFalse(any('kill' in str(call) for call in run.call_args_list))

    def test_installed_worker_restart_preserves_unit(self):
        with patch.object(services, 'properties', return_value={'ActiveState':'active'}), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run') as run:
            services.control(services.Service('worker.service'),'restart')
            run.assert_called_once_with(['systemctl','--user','restart','worker.service'])


class BindingTests(unittest.TestCase):
    """What an omitted binding field selects, as the import contract documents it."""

    def test_no_command_operates_an_installed_unit(self):
        with patch.object(services, 'properties', return_value={'ActiveState':'inactive'}), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run') as run:
            services.control(services.Service('worker.service'), 'start')
            self.assertEqual(run.call_args.args[0], ['systemctl','--user','start','worker.service'])
            self.assertFalse(any('systemd-run' in str(call) for call in run.call_args_list))

    def test_environment_reaches_a_transient_launch_and_never_an_installed_unit(self):
        with patch.object(services, 'properties', return_value={'LoadState':'not-found','ActiveState':'inactive'}), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run') as run:
            services.control(services.Service('preview.service', ['python3','app.py'], Path('/tmp'),
                                              {'MODE':'preview'}, 3199), 'start')
            self.assertIn('--setenv=MODE=preview', run.call_args.args[0])
        with patch.object(services, 'properties', return_value={'ActiveState':'inactive'}), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run') as run:
            services.control(services.Service('worker.service', environment={'MODE':'worker'}), 'start')
            self.assertFalse(any('MODE' in str(call) for call in run.call_args_list))

    def test_a_transient_command_requires_a_usable_port(self):
        for port in (None, 80, 70000):
            with patch.object(services, 'properties', return_value={'LoadState':'not-found','ActiveState':'inactive'}), \
                    patch.object(services, 'run') as run:
                with self.assertRaisesRegex(ValueError, 'port between 1024 and 65535'):
                    services.control(services.Service('preview.service', ['python3','app.py'],
                                                      Path('/tmp'), {}, port), 'start')
                run.assert_not_called()

    def test_an_omitted_checkout_compares_nothing(self):
        state = {'ActiveState':'inactive','WorkingDirectory':'/elsewhere'}
        with patch.object(services, 'properties', return_value=state), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run'):
            self.assertEqual(services.control(services.Service('worker.service'), 'start'), 0)
        with patch.object(services, 'properties', return_value=state), \
                patch.object(services, 'run') as run:
            with self.assertRaisesRegex(ValueError, 'different checkout'):
                services.control(services.Service('worker.service', directory=Path('/tmp'),
                                                  health_service='worker'), 'start')
            run.assert_not_called()

    def test_structured_health_requires_an_expected_checkout(self):
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = b'{"pid": 1}'
        opener = unittest.mock.Mock(); opener.open.return_value = response
        with patch.object(services, 'properties', return_value={'ActiveState':'active'}), \
                patch.object(services.urllib.request, 'build_opener', return_value=opener):
            with self.assertRaisesRegex(ValueError, 'requires an expected checkout'):
                services.check(services.Service('test.service', port=3199, health_service='test'))

    def test_an_uninstalled_structured_service_is_named_rather_than_launched(self):
        with patch.object(services, 'properties', return_value={'LoadState':'not-found','ActiveState':'inactive'}), \
                patch.object(services, 'run') as run:
            with self.assertRaisesRegex(ValueError, 'not installed'):
                services.control(services.Service('worker.service', directory=Path('/tmp'),
                                                  health_service='worker'), 'start')
            run.assert_not_called()

    def test_an_omitted_port_makes_an_active_unit_ready(self):
        with patch.object(services, 'properties', return_value={'ActiveState':'active'}):
            self.assertTrue(services.ready(services.Service('worker.service')))
        with patch.object(services, 'properties', return_value={'ActiveState':'inactive'}):
            self.assertFalse(services.ready(services.Service('worker.service')))

    def test_status_exits_nonzero_when_the_service_is_not_ready(self):
        with patch.object(services, 'properties', return_value={'ActiveState':'active'}), \
                patch.object(services, 'ready', return_value=True), patch('builtins.print'):
            self.assertEqual(services.control(services.Service('worker.service'), 'status'), 0)
        with patch.object(services, 'properties', return_value={'ActiveState':'failed'}), \
                patch.object(services, 'ready', return_value=False), patch('builtins.print'):
            self.assertEqual(services.control(services.Service('worker.service'), 'status'), 1)

    def test_stopping_an_unloaded_unit_succeeds_without_acting(self):
        with patch.object(services, 'properties', return_value={'LoadState':'not-found'}), \
                patch.object(services, 'run') as run:
            self.assertEqual(services.control(services.Service('worker.service'), 'stop'), 0)
            run.assert_not_called()

    def test_a_prerequisite_is_skipped_for_an_already_active_service(self):
        calls = []
        service = services.Service('worker.service', before_start=lambda: calls.append('ran'))
        with patch.object(services, 'properties', return_value={'ActiveState':'active'}), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run'):
            services.control(service, 'start')
        self.assertEqual(calls, [])
        with patch.object(services, 'properties', return_value={'ActiveState':'inactive'}), \
                patch.object(services, 'ready', return_value=True), patch.object(services, 'run'):
            services.control(service, 'start')
        self.assertEqual(calls, ['ran'])

    def test_a_readiness_bound_must_be_positive_and_finite(self):
        for bound in (0, -1, float('inf'), float('nan')):
            with patch.object(services, 'properties') as properties:
                with self.assertRaisesRegex(ValueError, 'positive and finite'):
                    services.control(services.Service('worker.service', ready_seconds=bound), 'status')
                properties.assert_not_called()
        self.assertEqual(services.Service('worker.service').ready_seconds, 60)


class BackupTests(unittest.TestCase):
    def make_tool(self, root):
        config = backups.BackupConfig('project', 'vault', 'db', 'key', root, Path('/ca'),
                                      ('test',), '', lambda q: {}, lambda q, a: None)
        return backups.DatabaseBackup(config)

    def test_client_timeout_removes_only_the_owned_container(self):
        original = RuntimeError('docker timed out')
        env = {'PGPASSWORD': 'synthetic-password', 'PGHOST': 'example.invalid'}
        with patch.object(backups, 'run', side_effect=[original, b'a' * 64 + b'\n', b'']) as run, \
                patch.object(backups.secrets, 'token_hex', return_value='b' * 32):
            with self.assertRaises(RuntimeError) as failure:
                self.make_tool(Path('/unused')).client('pg_dump', ['--format=custom'], env)
        self.assertIs(failure.exception, original)
        launch = run.call_args_list[0].args[0]
        self.assertIn('--name', launch)
        self.assertIn('--label', launch)
        self.assertNotIn('synthetic-password', launch)
        self.assertIs(run.call_args_list[0].args[2], env)
        listing = run.call_args_list[1].args[0]
        self.assertIn('name=^/database-client-bbbbbbbbbbbb$', listing)
        self.assertIn(f'label={backups.RESTORE_LABEL}=' + 'b' * 32, listing)
        self.assertEqual(run.call_args_list[-1].args[0], ['docker', 'rm', '-f', '-v', 'a' * 64])

    def test_client_name_collision_does_not_remove_an_unrelated_container(self):
        with patch.object(backups, 'run', side_effect=[RuntimeError('synthetic name collision'), b'']) as run:
            with self.assertRaisesRegex(RuntimeError, 'name collision'):
                self.make_tool(Path('/unused')).client('psql', [], {})
        self.assertFalse(any(call.args[0][1] == 'rm' for call in run.call_args_list))
        self.assertEqual(len(run.call_args_list), 2)

    def test_client_cleanup_failure_prevents_a_success_result(self):
        with patch.object(backups, 'run', side_effect=[b'synthetic output', RuntimeError('synthetic cleanup failure')]):
            with self.assertRaisesRegex(RuntimeError, 'cleanup failure'):
                self.make_tool(Path('/unused')).client('psql', [], {})

    def test_failed_start_reconciles_only_the_attempt_container(self):
        for error in (RuntimeError('synthetic startup failure'),
                      subprocess.TimeoutExpired(['docker', 'run'], 1)):
            with self.subTest(failure=type(error).__name__):
                def command(args, *unused, **kwargs):
                    if args[1] == 'run':
                        raise error
                    if args[1:3] == ['container', 'ls']:
                        return b'a' * 64 + b'\n'
                    return b''
                with patch.object(backups, 'run', side_effect=command) as run, \
                        patch.object(backups.secrets, 'token_hex', return_value='b' * 32):
                    with self.assertRaises(type(error)):
                        with self.make_tool(Path('/unused')).disposable():
                            self.fail('failed startup must not yield a container')
                listing = run.call_args_list[1].args[0]
                self.assertIn('name=^/database-restore-bbbbbbbbbbbb$', listing)
                self.assertIn(f'label={backups.RESTORE_LABEL}=' + 'b' * 32, listing)
                self.assertEqual(run.call_args_list[-1].args[0], ['docker', 'rm', '-f', '-v', 'a' * 64])

    def test_failed_start_leaves_an_unrelated_namesake_alone(self):
        with patch.object(backups, 'run', side_effect=[RuntimeError('synthetic name collision'), b'']) as run:
            with self.assertRaisesRegex(RuntimeError, 'name collision'):
                with self.make_tool(Path('/unused')).disposable():
                    self.fail('failed startup must not yield a container')
        self.assertFalse(any(call.args[0][1] == 'rm' for call in run.call_args_list))

    def test_cleanup_failure_keeps_the_original_startup_error(self):
        original = RuntimeError('synthetic startup failure')
        with patch.object(backups, 'run', side_effect=[original, RuntimeError('synthetic cleanup failure')]), \
                patch.object(backups.sys, 'stderr', new_callable=io.StringIO) as diagnostic:
            with self.assertRaises(RuntimeError) as failure:
                with self.make_tool(Path('/unused')).disposable():
                    self.fail('failed startup must not yield a container')
        self.assertIs(failure.exception, original)
        message = '\n'.join(getattr(original, '__notes__', [])) + diagnostic.getvalue()
        self.assertIn('cleanup also failed', message)
        self.assertNotIn('synthetic cleanup failure', message)

    def test_cleanup_error_without_exception_notes_keeps_primary_failure(self):
        class LegacyError(RuntimeError):
            add_note = None
        original = LegacyError('synthetic startup failure')
        with patch.object(backups, 'run', side_effect=[original, RuntimeError('synthetic-password')]), \
                patch.object(backups.sys, 'stderr', new_callable=io.StringIO) as diagnostic, \
                warnings.catch_warnings():
            warnings.simplefilter('error')
            with self.assertRaises(LegacyError) as failure:
                with self.make_tool(Path('/unused')).disposable():
                    self.fail('failed startup must not yield a container')
        self.assertIs(failure.exception, original)
        self.assertIn('cleanup also failed', diagnostic.getvalue())
        self.assertNotIn('synthetic-password', diagnostic.getvalue())

    def test_wrong_key_timeout_is_not_verified_denial(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / 'synthetic.dump.gpg'
            archive.write_bytes(b'synthetic encrypted archive')
            metadata = {'project': 'project', 'archive': archive.name,
                        'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(), 'snapshot': {'tables': {}}}
            archive.with_suffix('.json').write_text(json.dumps(metadata))
            tool = self.make_tool(root)
            with patch.object(tool, 'backup_key', return_value='synthetic-key'), \
                    patch.object(backups, 'crypt', side_effect=[b'synthetic plaintext', RuntimeError('gpg timed out')]), \
                    patch.object(tool, 'restore_check') as restore:
                with self.assertRaisesRegex(RuntimeError, 'timed out'):
                    tool.rehearse(archive)
                restore.assert_not_called()
            self.assertEqual(sorted(path.name for path in root.iterdir()),
                             sorted([archive.name, archive.with_suffix('.json').name]))

    def test_empty_schema_scope_is_refused_before_credentials(self):
        config = backups.BackupConfig('project', 'vault', 'db', 'key', Path('/unused'),
                                      Path('/ca'), (), '', lambda q: {}, lambda q, a: None)
        with patch.object(backups, 'item_fields') as read:
            with self.assertRaisesRegex(ValueError, 'schema'):
                backups.DatabaseBackup(config).backup()
            read.assert_not_called()

    def test_command_is_bounded_and_closes_unused_stdin(self):
        response = subprocess.CompletedProcess([], 0, b'output', b'')
        with patch.object(backups.subprocess, 'run', return_value=response) as run:
            self.assertEqual(backups.run(['pg_dump']), b'output')
        self.assertEqual(run.call_args.kwargs.get('stdin'), subprocess.DEVNULL)
        self.assertGreater(run.call_args.kwargs.get('timeout', 0), 0)

    def test_command_timeout_withholds_output(self):
        error = subprocess.TimeoutExpired(['psql'], 1, b'synthetic-record', b'synthetic-password')
        with patch.object(backups.subprocess, 'run', side_effect=error):
            with self.assertRaisesRegex(RuntimeError, 'psql.*timed out') as failure:
                backups.run(['psql'])
        self.assertNotIn('synthetic-record', str(failure.exception))
        self.assertNotIn('synthetic-password', str(failure.exception))

    def test_crypto_failure_names_status_and_withholds_output(self):
        response = subprocess.CompletedProcess([], 2, b'synthetic-record', b'synthetic-password')
        with patch.object(backups.subprocess, 'run', return_value=response):
            with self.assertRaises(RuntimeError) as failure:
                backups.crypt('synthetic-key', b'synthetic archive')
        message = str(failure.exception)
        self.assertIn('gpg', message)
        self.assertIn('exit 2', message)
        self.assertNotIn('synthetic-record', message)
        self.assertNotIn('synthetic-password', message)

    def test_only_reported_bad_passphrase_is_verified_denial(self):
        # GnuPG DETAILS allows symbolic ERROR codes and optional trailing fields.
        cases = {
            'operational failure': (b'gpg agent unavailable', backups.CryptoFailure),
            'unclassified decryption failure': (b'[GNUPG:] DECRYPTION_FAILED\n', backups.CryptoFailure),
            'bad passphrase': (b'[GNUPG:] ERROR symkey_decrypt.maybe_error 11_BAD_PASSPHRASE\n'
                               b'[GNUPG:] DECRYPTION_FAILED\n', backups.WrongPassphrase),
            'symbolic bad passphrase': (b'[GNUPG:] ERROR symkey_decrypt.maybe_error BAD_PASSPHRASE\n'
                                       b'[GNUPG:] DECRYPTION_FAILED\n', backups.WrongPassphrase),
            'bad passphrase with detail': (b'[GNUPG:] ERROR symkey_decrypt.maybe_error 11_BAD_PASSPHRASE synthetic-detail\n'
                                          b'[GNUPG:] DECRYPTION_FAILED\n', backups.WrongPassphrase),
            'unrelated code with misleading detail': (b'[GNUPG:] ERROR symkey_decrypt.maybe_error 77_NO_AGENT 11_BAD_PASSPHRASE\n'
                                                      b'[GNUPG:] DECRYPTION_FAILED\n', backups.CryptoFailure),
            'unrelated symbolic code': (b'[GNUPG:] ERROR symkey_decrypt.maybe_error NOT_BAD_PASSPHRASE\n'
                                       b'[GNUPG:] DECRYPTION_FAILED\n', backups.CryptoFailure),
        }
        for name, (status, expected) in cases.items():
            with self.subTest(outcome=name):
                response = subprocess.CompletedProcess([], 2, b'synthetic-record', status)
                with patch.object(backups.subprocess, 'run', return_value=response):
                    with self.assertRaises(expected) as failure:
                        backups.crypt('synthetic-key', b'synthetic archive', True)
                self.assertIs(type(failure.exception), expected)

    def test_publication_never_overwrites(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'archive'; backups.write_private(p,b'first')
            with self.assertRaises(FileExistsError): backups.write_private(p,b'second')
            self.assertEqual(p.read_bytes(),b'first'); self.assertEqual(p.stat().st_mode & 0o777,0o600)

    def test_failed_restore_does_not_publish(self):
        with tempfile.TemporaryDirectory() as directory:
            c=backups.BackupConfig('project','vault','db','key',Path(directory),Path('/ca'),('test',),'',lambda q:{},lambda q,a:None)
            tool=backups.DatabaseBackup(c)
            with patch.object(tool,'backup_key',return_value='secret'), patch.object(tool,'database_env',return_value={}), \
                    patch.object(tool,'client',return_value=b'archive'), patch.object(backups,'crypt',return_value=b'archive'), \
                    patch.object(tool,'restore_check',side_effect=RuntimeError('restore failed')):
                with self.assertRaisesRegex(RuntimeError,'restore failed'): tool.backup()
            self.assertEqual(list(Path(directory).iterdir()),[])

    def test_failed_crypto_checks_do_not_publish(self):
        cases = {
            'encryption': [RuntimeError('synthetic encryption failure')],
            'integrity': [b'encrypted', RuntimeError('synthetic integrity failure')],
            'roundtrip': [b'encrypted', b'different plaintext'],
        }
        for name, results in cases.items():
            with self.subTest(phase=name), tempfile.TemporaryDirectory() as directory:
                config = backups.BackupConfig('project', 'vault', 'db', 'key', Path(directory),
                                              Path('/ca'), ('test',), '', lambda q: {}, lambda q, a: None)
                tool = backups.DatabaseBackup(config)
                with patch.object(tool, 'backup_key', return_value='synthetic-key'), \
                        patch.object(tool, 'database_env', return_value={}), \
                        patch.object(tool, 'client', return_value=b'archive'), \
                        patch.object(backups, 'crypt', side_effect=results), \
                        patch.object(tool, 'restore_check') as restore:
                    with self.assertRaises(RuntimeError):
                        tool.backup()
                    restore.assert_not_called()
                self.assertEqual(list(Path(directory).iterdir()), [])

    def test_insecure_backup_directory_does_not_publish(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            root.chmod(0o755)
            config = backups.BackupConfig('project', 'vault', 'db', 'key', root, Path('/ca'),
                                          ('test',), '', lambda q: {}, lambda q, a: None)
            tool = backups.DatabaseBackup(config)
            with patch.object(tool, 'backup_key', return_value='synthetic-key'), \
                    patch.object(tool, 'database_env', return_value={}), \
                    patch.object(tool, 'client', return_value=b'archive'), \
                    patch.object(backups, 'crypt', return_value=b'archive'), \
                    patch.object(tool, 'restore_check', return_value={}):
                with self.assertRaisesRegex(RuntimeError, 'mode 0700'):
                    tool.backup()
            self.assertEqual(list(root.iterdir()), [])

    def test_errors_withhold_records_and_passwords(self):
        with patch.object(backups.subprocess,'run',return_value=subprocess.CompletedProcess([],1,b'private',b'password')):
            with self.assertRaisesRegex(RuntimeError,'output withheld'): backups.run(['psql'])

    @unittest.skipUnless(shutil.which('gpg'), 'GnuPG executable is not installed')
    def test_crypto_roundtrip_and_wrong_key(self):
        with tempfile.TemporaryDirectory(prefix='runtime-gpg-') as directory, \
                patch.dict(os.environ, {'GNUPGHOME': directory}):
            Path(directory).chmod(0o700)
            try:
                encrypted = backups.crypt('synthetic-key', b'synthetic archive')
                self.assertEqual(backups.crypt('synthetic-key', encrypted, True), b'synthetic archive')
                with self.assertRaises(backups.WrongPassphrase):
                    backups.crypt('wrong-key', encrypted, True)
            finally:
                # Stop only the agent associated with this test's disposable home.
                if shutil.which('gpgconf'):
                    subprocess.run(['gpgconf', '--homedir', directory, '--kill', 'gpg-agent'],
                                   stdin=subprocess.DEVNULL, capture_output=True, timeout=10)

if __name__=='__main__': unittest.main()
