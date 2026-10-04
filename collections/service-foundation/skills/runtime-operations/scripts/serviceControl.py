"""Control named user-systemd services; never kill a listener by port."""
from dataclasses import dataclass, field
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Callable
import urllib.error
import urllib.request

from serviceHealth import ServiceHealth


@dataclass
class Service:
    unit: str
    command: list[str] = field(default_factory=list)
    directory: Path | None = None
    environment: dict[str, str] = field(default_factory=dict)
    port: int | None = None
    health_service: str | None = None
    ready_seconds: float = 60
    before_start: Callable[[], None] | None = None


def run(args, *, check=True, timeout=45):
    return subprocess.run(args, check=check, stdin=subprocess.DEVNULL,
                          timeout=timeout, text=True, capture_output=True)


def properties(unit):
    result = run(['systemctl', '--user', 'show', unit,
                  '--property=LoadState,ActiveState,MainPID,ControlGroup,WorkingDirectory'], check=False)
    if result.returncode:
        raise RuntimeError('Cannot inspect the user service manager')
    return dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)


def check(service):
    """Verify readiness of this exact instance, raising a bounded diagnostic."""
    state = properties(service.unit)
    if state.get('ActiveState') != 'active':
        raise ValueError('The named service is not ready')
    if service.port is None:
        return
    # Ignore HTTP proxy configuration for loopback probes.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(f'http://127.0.0.1:{service.port}/health', timeout=3) as response:
        payload = response.read(65537)
    if len(payload) > 65536:
        raise ValueError('Oversized service health response')
    if service.health_service is not None:
        if service.directory is None:
            raise ValueError('Structured health requires an expected checkout')
        health = json.loads(payload)
        pid = health.get('pid') if isinstance(health, dict) else None
        if type(pid) is not int or pid <= 0:
            raise ValueError('Health response has no valid process identity')
        memberships = Path(f'/proc/{pid}/cgroup').read_text()
        ServiceHealth.verify(health, state, memberships, service=service.health_service,
                             checkout=service.directory)
    else:
        # Compatibility for bindings not yet migrated to the structured contract.
        pid = payload.decode().strip()
        if not pid.isdigit():
            raise ValueError('Invalid legacy health PID')
        group = state.get('ControlGroup', '')
        memberships = Path(f'/proc/{pid}/cgroup').read_text().splitlines()
        if not group or not any(line.split(':', 2)[-1] == group for line in memberships):
            raise ValueError('Health responder is outside the named service cgroup')


def ready(service):
    try:
        check(service)
        return True
    except (OSError, ValueError, urllib.error.URLError):
        return False


def _checkout(service, state):
    if service.directory is None or state.get('LoadState') == 'not-found':
        return
    configured = state.get('WorkingDirectory')
    # Legacy bindings may omit checkout; a structured binding requires it.
    if configured is None and service.health_service is None:
        return
    if not configured or Path(configured).resolve() != service.directory.resolve():
        raise ValueError('Named unit uses a different checkout')


def _wait(service):
    deadline = time.monotonic() + service.ready_seconds
    while True:
        if ready(service):
            return
        if properties(service.unit).get('ActiveState') in ('failed', 'inactive'):
            break
        if time.monotonic() >= deadline:
            break
        time.sleep(0.25)
    raise RuntimeError(f'{service.unit} failed readiness; inspect its logs.')


def _report(service):
    print(f'{service.unit} ready' + (f': http://127.0.0.1:{service.port}/' if service.port else ''))


def control(service, action):
    if action not in ('start', 'stop', 'restart', 'status', 'logs'):
        raise ValueError('Action must be start, stop, restart, status or logs')
    if not math.isfinite(service.ready_seconds) or service.ready_seconds <= 0:
        raise ValueError('Readiness timeout must be positive and finite')
    state = properties(service.unit)
    _checkout(service, state)
    if action == 'logs':
        return subprocess.call(['journalctl', '--user', '-u', service.unit, '-n', '50', '--no-pager'],
                               stdin=subprocess.DEVNULL, timeout=45)
    if action == 'status':
        print(f"{service.unit}: {state.get('ActiveState', 'unknown')}; checkout: {state.get('WorkingDirectory', '')}")
        is_ready = ready(service)
        if service.port is not None:
            print('HTTP readiness: ' + ('ready' if is_ready else 'unavailable'))
        return 0 if is_ready else 1
    if action == 'stop':
        if state.get('LoadState') == 'not-found':
            return 0
        run(['systemctl', '--user', 'stop', service.unit])
        return 0
    if action == 'start' and state.get('ActiveState') == 'active':
        # This invocation owns no attempt: failed readiness must preserve it.
        _wait(service)
        _report(service)
        return 0
    if service.health_service is not None and not service.command and state.get('LoadState') == 'not-found':
        raise ValueError('The selected service is not installed')
    if service.command and (service.port is None or not 1024 <= service.port <= 65535):
        raise ValueError('A transient preview needs a port between 1024 and 65535')
    if service.before_start is not None:
        service.before_start()
    attempted = False
    try:
        if not service.command:
            # The installed unit owns release, startup and restart policy.
            attempted = True
            run(['systemctl', '--user', action, service.unit])
        else:
            if state.get('LoadState') != 'not-found':
                run(['systemctl', '--user', 'stop', service.unit])
            run(['systemctl', '--user', 'reset-failed', service.unit], check=False)
            args = ['systemd-run', '--user', '--collect', f'--unit={service.unit}',
                    f'--property=WorkingDirectory={service.directory}', '--property=UMask=0077',
                    '--property=NoNewPrivileges=yes', '--property=KillMode=control-group',
                    '--property=TimeoutStopSec=15']
            for key, value in service.environment.items():
                args.append(f'--setenv={key}={value}')
            # No credentials are passed to systemd; the command fetches its own.
            attempted = True
            run(args + service.command)
        _wait(service)
        _report(service)
        return 0
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
                    print(diagnostic, file=sys.stderr)
        raise
