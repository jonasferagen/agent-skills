"""Control named user-systemd services; never kill a listener by port."""
from dataclasses import dataclass, field
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.error
import urllib.request


@dataclass
class Service:
    unit: str
    command: list[str] = field(default_factory=list)
    directory: Path | None = None
    environment: dict[str, str] = field(default_factory=dict)
    port: int | None = None


def run(args, *, check=True, timeout=45):
    return subprocess.run(args, check=check, stdin=subprocess.DEVNULL,
                          timeout=timeout, text=True, capture_output=True)


def properties(unit):
    result = run(['systemctl', '--user', 'show', unit,
                  '--property=LoadState,ActiveState,ControlGroup,WorkingDirectory'], check=False)
    return dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)


def ready(service):
    state = properties(service.unit)
    if state.get('ActiveState') != 'active':
        return False
    if service.port is None:
        return True
    try:
        # Ignore HTTP proxy configuration for loopback probes.
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(f'http://127.0.0.1:{service.port}/health', timeout=1) as response:
            pid = response.read(32).decode().strip()
        if not pid.isdigit():
            return False
        group = state.get('ControlGroup', '')
        memberships = Path(f'/proc/{pid}/cgroup').read_text().splitlines()
        return bool(group) and any(line.split(':', 2)[-1] == group for line in memberships)
    except (OSError, ValueError, urllib.error.URLError):
        return False


def control(service, action):
    if action not in ('start', 'stop', 'restart', 'status', 'logs'):
        raise ValueError('Action must be start, stop, restart, status or logs')
    if action == 'logs':
        return subprocess.call(['journalctl', '--user', '-u', service.unit, '-n', '50', '--no-pager'],
                               stdin=subprocess.DEVNULL, timeout=45)
    if action == 'status':
        state = properties(service.unit)
        print(f"{service.unit}: {state.get('ActiveState', 'unknown')}; checkout: {state.get('WorkingDirectory', '')}")
        return 0 if state.get('ActiveState') == 'active' else 1
    state = properties(service.unit)
    if action == 'stop':
        if state.get('LoadState') == 'not-found':
            return 0
        run(['systemctl', '--user', 'stop', service.unit])
        return 0
    if action == 'start' and state.get('ActiveState') == 'active':
        print(f'{service.unit} is already active; use restart to apply changes.')
        return 0
    if service.command and (service.port is None or not 1024 <= service.port <= 65535):
        raise ValueError('A transient preview needs a port between 1024 and 65535')
    attempted = False
    try:
        if not service.command:
            # Installed worker: its unit owns release and credential settings.
            attempted = True
            run(['systemctl', '--user', action, service.unit])
        else:
            if state.get('LoadState') != 'not-found':
                run(['systemctl', '--user', 'stop', service.unit])
            run(['systemctl', '--user', 'reset-failed', service.unit], check=False)
            args = ['systemd-run', '--user', '--collect', f'--unit={service.unit}',
                    f'--property=WorkingDirectory={service.directory}', '--property=UMask=0077',
                    '--property=KillMode=control-group', '--property=TimeoutStopSec=15']
            for key, value in service.environment.items():
                args.append(f'--setenv={key}={value}')
            # No credentials are passed to systemd; the command fetches its own.
            attempted = True
            run(args + service.command)
        deadline = time.monotonic() + 60
        while time.monotonic() < deadline:
            if ready(service):
                print(f'{service.unit} ready' + (f': http://127.0.0.1:{service.port}' if service.port else ''))
                return 0
            if properties(service.unit).get('ActiveState') in ('failed', 'inactive'):
                break
            time.sleep(0.25)
        raise RuntimeError(f'{service.unit} failed readiness; inspect its logs.')
    except BaseException as failure:
        if attempted:
            try:
                # A timed-out launcher may already have started this selected unit.
                run(['systemctl', '--user', 'stop', service.unit])
            except Exception:
                diagnostic = f'{service.unit} cleanup also failed; output withheld.'
                if callable(getattr(failure, 'add_note', None)):
                    failure.add_note(diagnostic)
                else:
                    try:
                        print(diagnostic, file=sys.stderr)
                    except (OSError, ValueError):
                        pass
        raise
