"""Encrypted PostgreSQL exports with a mandatory isolated restore before publication."""
import argparse
import contextlib
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from typing import Callable
from credentialStore import item_fields

IMAGE = 'public.ecr.aws/supabase/postgres:17.6.1.167'
RESTORE_LABEL = 'agent-skills.restore-attempt'


class CryptoFailure(RuntimeError):
    """GnuPG exited unsuccessfully; the cause may be operational."""


class WrongPassphrase(CryptoFailure):
    """GnuPG reported a bad passphrase and failed decryption."""


def run(args, data=None, env=None, *, timeout=900):
    try:
        result = subprocess.run(args, input=data, env=env, capture_output=True,
                                stdin=subprocess.DEVNULL if data is None else None, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f'{args[0]} timed out after {timeout} s; output withheld') from None
    except FileNotFoundError:
        raise RuntimeError(f'{args[0]} is not installed or not available on PATH') from None
    # Output withheld: psql, pg_dump and pg_restore output can hold credentials, queries or records.
    if result.returncode:
        raise RuntimeError(f'{args[0]} failed (exit {result.returncode}); output withheld')
    return result.stdout


def fields_by_name(fields):
    values = {}
    for field in fields:
        for name in (field.get('id'), field.get('label')):
            if name:
                values[name] = field.get('value', '')
    if 'host' not in values and 'server' in values:
        values['host'] = values['server']
    return values


def database_environment(fields, project, username, ca):
    values = fields_by_name(fields)
    if (values.get('username') != f'{username}.{project}' or values.get('port') != '5432'
            or values.get('database') != 'postgres'
            or not values.get('host', '').endswith('.pooler.supabase.com')):
        raise RuntimeError('Unexpected project, login or database endpoint')
    if not values.get('password'):
        raise RuntimeError('Database credential has no password')
    env = {k: v for k, v in os.environ.items() if not k.startswith(('PG', 'OP_'))}
    for name, field in [('PGHOST', 'host'), ('PGPORT', 'port'), ('PGDATABASE', 'database'),
                        ('PGUSER', 'username'), ('PGPASSWORD', 'password')]:
        env[name] = values[field]
    env.update(PGSSLMODE='verify-full', PGSSLROOTCERT=str(ca), PGPASSFILE='/dev/null', PGCONNECT_TIMEOUT='15')
    return env


def crypt(key, data, decrypt=False, *, timeout=900):
    readfd, writefd = os.pipe()
    try:
        os.write(writefd, (key + '\n').encode())
        os.close(writefd)
        writefd = None
        args = ['gpg', '--batch', '--pinentry-mode', 'loopback', '--no-symkey-cache', '--status-fd', '2',
                '--passphrase-fd', str(readfd)]
        args += ['--decrypt'] if decrypt else ['--symmetric', '--cipher-algo', 'AES256']
        try:
            result = subprocess.run(args, input=data, capture_output=True,
                                    pass_fds=(readfd,), timeout=timeout)
        except subprocess.TimeoutExpired:
            raise RuntimeError(f'gpg timed out after {timeout} s; output withheld') from None
        except FileNotFoundError:
            raise RuntimeError('gpg is not installed or not available on PATH') from None
        # GnuPG output can be plaintext; report no output.
        if result.returncode:
            status = result.stderr.splitlines()
            wrong_key = decrypt and b'[GNUPG:] DECRYPTION_FAILED' in status and any(
                len(fields) >= 4 and fields[:3] == [b'[GNUPG:]', b'ERROR', b'symkey_decrypt.maybe_error'] and
                re.fullmatch(rb'(?:[0-9]+_)?BAD_PASSPHRASE', fields[3])
                for fields in (line.split(maxsplit=4) for line in status))
            if wrong_key:
                raise WrongPassphrase(f'gpg rejected the passphrase (exit {result.returncode}); output withheld')
            raise CryptoFailure(f'gpg failed (exit {result.returncode}); encryption/integrity output withheld')
        return result.stdout
    finally:
        os.close(readfd)
        if writefd is not None:
            os.close(writefd)


def write_private(path, value):
    fd, temporary = tempfile.mkstemp(prefix='.pending-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(value)
            stream.flush()
            os.fsync(stream.fileno())
        os.link(temporary, path)
    finally:
        os.unlink(temporary)


def local_sql(name, sql, *, timeout=900):
    return run(['docker', 'exec', '-i', name, 'psql', '-h', '/restore', '-U', 'postgres',
                '-d', 'postgres', '-X', '-At', '-v', 'ON_ERROR_STOP=1'],
               sql.encode(), timeout=timeout).decode()


@dataclass
class BackupConfig:
    project: str
    vault: str
    database_item: str
    key_item: str
    root: Path
    ca: Path
    schemas: tuple[str, ...]
    prepare_sql: str
    inspect: Callable[[Callable[[str], str]], dict]
    validate: Callable[[Callable[[str], str], dict], None]
    preserve_owners: bool = True
    compare_source: bool = False
    command_timeout: float = 900


class DatabaseBackup:
    def __init__(self, config):
        if not config.schemas:
            raise ValueError('At least one backup schema must be explicitly configured')
        if not math.isfinite(config.command_timeout) or config.command_timeout <= 0:
            raise ValueError('Backup command_timeout must be positive and finite')
        self.config = config

    def database_env(self):
        c = self.config
        return database_environment(item_fields(c.vault, c.database_item), c.project, 'postgres', c.ca)

    def backup_key(self):
        c = self.config
        fields = item_fields(c.vault, c.key_item)
        values = [f['value'] for f in fields if f.get('type') == 'CONCEALED' and f.get('value')]
        if len(values) != 1 or any(ch in values[0] for ch in ('\n', '\r')):
            raise RuntimeError('Backup item must have exactly one populated single-line concealed field')
        return values[0]

    def client(self, tool, args, env, data=None):
        ca = self.config.ca
        with self._container_attempt('database-client') as (name, label):
            command = ['docker', 'run', '--rm', '-i', '--name', name, '--label', label,
                       '--log-driver=none', '--mount', f'type=bind,src={ca},dst={ca},readonly']
            for variable in ('PGHOST', 'PGPORT', 'PGDATABASE', 'PGUSER', 'PGPASSWORD',
                             'PGSSLMODE', 'PGSSLROOTCERT', 'PGPASSFILE', 'PGCONNECT_TIMEOUT'):
                if variable in env:
                    command += ['--env', variable]
            return run(command + ['--entrypoint', tool, IMAGE] + args, data, env,
                       timeout=self.config.command_timeout)

    @contextlib.contextmanager
    def _container_attempt(self, prefix):
        attempt = secrets.token_hex(16)
        name = prefix + '-' + attempt[:12]
        failure = None
        try:
            yield name, f'{RESTORE_LABEL}={attempt}'
        except BaseException as error:
            failure = error
            raise
        finally:
            try:
                # The daemon may create a container even if docker run fails or times out.
                # Match both attempt identity and name; never remove an unrelated namesake.
                matches = run(['docker', 'container', 'ls', '--all', '--quiet', '--no-trunc',
                               '--filter', f'name=^/{name}$',
                               '--filter', f'label={RESTORE_LABEL}={attempt}'],
                              timeout=self.config.command_timeout).decode().split()
                if len(matches) > 1 or any(len(value) != 64 or
                                           any(ch not in '0123456789abcdef' for ch in value)
                                           for value in matches):
                    raise RuntimeError('Container cleanup did not identify one owned container')
                if matches:
                    run(['docker', 'rm', '-f', '-v', matches[0]], timeout=self.config.command_timeout)
            except Exception as cleanup_error:
                if failure is None:
                    raise
                diagnostic = f'Container cleanup also failed for {name}; output withheld.'
                if callable(getattr(failure, 'add_note', None)):
                    failure.add_note(diagnostic)
                else:
                    # Python 3.10 has no exception notes; keep the primary error intact.
                    try:
                        print(diagnostic, file=sys.stderr)
                    except (OSError, ValueError):
                        # A closed diagnostic stream must not replace the original failure.
                        pass

    @contextlib.contextmanager
    def disposable(self):
        with self._container_attempt('database-restore') as (name, label):
            run(['docker', 'run', '-d', '--name', name, '--network=none', '--log-driver=none',
                 '--label', label, '--user=100:101', '--tmpfs', '/restore:rw,uid=100,gid=101,mode=0700',
                 '--entrypoint', 'sh', IMAGE, '-c',
                 "initdb -D /restore/data -A trust --no-locale >/dev/null && "
                 "exec postgres -D /restore/data -k /restore -c listen_addresses='' "],
                timeout=self.config.command_timeout)
            for _ in range(60):
                ready = subprocess.run(['docker', 'exec', name, 'pg_isready', '-h', '/restore'],
                                       stdin=subprocess.DEVNULL, capture_output=True,
                                       timeout=min(5, self.config.command_timeout))
                if ready.returncode == 0:
                    break
                time.sleep(0.5)
            else:
                raise RuntimeError('Disposable PostgreSQL did not become ready')
            yield name

    def restore_check(self, plain, expected=None):
        with self.disposable() as name:
            query = lambda sql: local_sql(name, sql, timeout=self.config.command_timeout)
            query(self.config.prepare_sql)
            args = ['docker', 'exec', '-i', name, 'pg_restore', '-h', '/restore', '-U', 'postgres',
                    '-d', 'postgres', '--exit-on-error', '--single-transaction']
            if not self.config.preserve_owners:
                args.append('--no-owner')
            run(args, plain, timeout=self.config.command_timeout)
            actual = self.config.inspect(query)
            if expected is not None and actual != expected:
                raise RuntimeError('Restored snapshot mismatch; output withheld')
            self.config.validate(query, actual)
            return actual

    def backup(self):
        c = self.config
        key = self.backup_key()
        env = self.database_env()
        expected = None
        if c.compare_source:
            def query(sql):
                return self.client('psql', ['-X', '-At', '-v', 'ON_ERROR_STOP=1'], env, sql.encode()).decode()
            expected = c.inspect(query)
        plain = self.client('pg_dump', ['--format=custom'] + ['--schema=' + s for s in c.schemas], env)
        encrypted = crypt(key, plain, timeout=c.command_timeout)
        recovered = crypt(key, encrypted, True, timeout=c.command_timeout)
        if recovered != plain:
            raise RuntimeError('Encryption round-trip mismatch')
        restored = self.restore_check(recovered, expected)
        c.root.mkdir(mode=0o700, parents=True, exist_ok=True)
        info = c.root.stat()
        if info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise RuntimeError('Backup directory must be owned by you and mode 0700')
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        archive = c.root / (stamp + '-vault.dump.gpg')
        metadata = {'archive': archive.name, 'project': c.project, 'created_at': stamp,
                    'sha256': hashlib.sha256(encrypted).hexdigest(), 'snapshot': restored,
                    'restore_verified': True, 'client_image': IMAGE}
        write_private(archive, encrypted)
        write_private(archive.with_suffix('.json'), json.dumps(metadata, indent=2).encode())
        print('Encrypted backup and disposable restore verified: ' + str(archive))

    def rehearse(self, archive):
        archive = archive.expanduser().resolve()
        metadata = json.loads(archive.with_suffix('.json').read_text())
        encrypted = archive.read_bytes()
        if metadata['project'] != self.config.project or metadata['archive'] != archive.name:
            raise RuntimeError('Archive metadata identity mismatch')
        if hashlib.sha256(encrypted).hexdigest() != metadata['sha256']:
            raise RuntimeError('Archive checksum mismatch')
        key = self.backup_key()
        plain = crypt(key, encrypted, True, timeout=self.config.command_timeout)
        try:
            crypt(secrets.token_urlsafe(48), encrypted, True, timeout=self.config.command_timeout)
        except WrongPassphrase:
            pass
        else:
            raise RuntimeError('Wrong key unexpectedly accepted')
        restored = self.restore_check(plain, metadata['snapshot'])
        receipt = {'archive': archive.name, 'sha256': metadata['sha256'],
                   'verified_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   'tables_verified': len(restored['tables']), 'client_image': IMAGE,
                   'checks': ['checksum', 'GnuPG integrity', 'wrong-key denial',
                              'transactional restore', 'snapshot comparison', 'project access checks']}
        write_private(archive.parent / ('vault-rehearsal-' + secrets.token_hex(6) + '.json'),
                      json.dumps(receipt, indent=2).encode())
        print('PASS: retained archive restored and verified; disposable container removed.')

    def main(self):
        os.umask(0o077)
        parser = argparse.ArgumentParser(description=__doc__)
        subs = parser.add_subparsers(dest='command', required=True)
        subs.add_parser('backup', help='Encrypt a capture and verify an isolated restore')
        restore = subs.add_parser('rehearse', help='Verify a retained archive in an isolated database')
        restore.add_argument('archive', type=Path)
        admin = subs.add_parser('admin', help='Run a separately authorized administrative command')
        admin.add_argument('args', nargs=argparse.REMAINDER)
        args = parser.parse_args()
        if args.command == 'backup':
            self.backup()
        elif args.command == 'rehearse':
            self.rehearse(args.archive)
        else:
            command = args.args[1:] if args.args[:1] == ['--'] else args.args
            if not command:
                parser.error('admin requires a command after --')
            return subprocess.call(command, env=self.database_env(), timeout=self.config.command_timeout)
        return 0
