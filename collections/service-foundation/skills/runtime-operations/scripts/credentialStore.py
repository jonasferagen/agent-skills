"""1Password item reads with explicit runtime or owner authentication."""
import json
import os
from pathlib import Path
import stat
import subprocess


def clean_environment():
    return {k: v for k, v in os.environ.items() if not k.startswith('OP_')}


def service_token(directory, account):
    value = os.environ.get('OP_SERVICE_ACCOUNT_TOKEN', '')
    path = Path(directory) / f'{account}-token'
    if not value and path.exists():
        info = path.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise ValueError(f'{path} must be owned by you and readable only by you (mode 0600).')
        value = path.read_text().strip()
    if not value:
        raise ValueError(f'Supply the {account} token as OP_SERVICE_ACCOUNT_TOKEN or in {path}.')
    return value


def item_fields(vault, item, *, account=None, directory=None):
    env = clean_environment()
    if account:
        env['OP_SERVICE_ACCOUNT_TOKEN'] = service_token(directory, account)
    identity = account or 'owner'
    try:
        result = subprocess.run(['op', 'item', 'get', item, '--vault', vault, '--format=json'],
                                stdin=subprocess.DEVNULL, capture_output=True,
                                text=True, env=env, timeout=45)
    except subprocess.TimeoutExpired:
        raise ValueError(f'op item get timed out for {identity} after 45 s; output withheld.') from None
    except OSError:
        raise ValueError(f'Unable to run op item get for {identity}; output withheld.') from None
    # op output holds the item's secret fields; report only command, identity and status.
    if result.returncode:
        raise ValueError(f'op item get failed for {identity} (exit {result.returncode}); output withheld.')
    try:
        return json.loads(result.stdout)['fields']
    except (ValueError, KeyError, TypeError):
        raise ValueError(f'Unable to read the {identity} connection from 1Password; output withheld.') from None
