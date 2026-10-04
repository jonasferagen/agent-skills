"""Shared health envelope and named-instance verification for local services."""
import os
from pathlib import Path


class ServiceHealth:
    SCHEMA = 'service-health/v1'

    @staticmethod
    def response(service: str, checkout: Path, *, ready: bool, details: dict) -> tuple[int, dict]:
        return (200 if ready else 503, {
            'schema': ServiceHealth.SCHEMA,
            'service': service,
            'pid': os.getpid(),
            'checkout': str(checkout.resolve()),
            'status': 'ready' if ready else 'degraded',
            'details': details,
        })

    @staticmethod
    def verify(health: dict, state: dict, memberships: str, *, service: str, checkout: Path) -> None:
        if not isinstance(health, dict) or health.get('schema') != ServiceHealth.SCHEMA:
            raise ValueError('Unsupported service health response')
        if health.get('service') != service:
            raise ValueError('Health responder is a different service')
        if state.get('ActiveState') != 'active' or health.get('status') != 'ready':
            raise ValueError('The named service is not ready')
        pid = health.get('pid')
        if type(pid) is not int or pid <= 0 or str(pid) != state.get('MainPID'):
            raise ValueError('Health responder is not the named service MainPID')
        group = state.get('ControlGroup')
        if not group or not any(line.split(':', 2)[-1] == group for line in memberships.splitlines()):
            raise ValueError('Health responder is outside the named service cgroup')
        expected = str(checkout.resolve())
        if health.get('checkout') != expected or state.get('WorkingDirectory') != expected:
            raise ValueError('Health responder or unit uses a different checkout')
        if not isinstance(health.get('details'), dict):
            raise ValueError('Invalid service health details')
