import contextlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
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


class ServiceTests(unittest.TestCase):
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


class BackupTests(unittest.TestCase):
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

    def test_errors_withhold_records_and_passwords(self):
        with patch.object(backups.subprocess,'run',return_value=subprocess.CompletedProcess([],1,b'private',b'password')):
            with self.assertRaisesRegex(RuntimeError,'output withheld'): backups.run(['psql'])

    def test_crypto_roundtrip_and_wrong_key(self):
        encrypted=backups.crypt('synthetic-key',b'synthetic archive')
        self.assertEqual(backups.crypt('synthetic-key',encrypted,True),b'synthetic archive')
        with self.assertRaises(RuntimeError): backups.crypt('wrong-key',encrypted,True)

if __name__=='__main__': unittest.main()
