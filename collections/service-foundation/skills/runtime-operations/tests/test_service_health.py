"""The health contract refuses a different identity, checkout or degraded instance."""
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from serviceHealth import ServiceHealth
import serviceControl as services


class HealthTests(unittest.TestCase):
    def setUp(self):
        self.root = Path('/example/checkout')
        self.state = dict(LoadState='loaded', ActiveState='active', MainPID='1234',
                          ControlGroup='/example/unit', WorkingDirectory=str(self.root))
        self.body = dict(schema='service-health/v1', service='example-reader', pid=1234,
                         checkout=str(self.root), status='ready', details={'source': 'ready'})

    def test_verifier_accepts_only_the_named_ready_instance(self):
        ServiceHealth.verify(self.body, self.state, '0::/example/unit', service='example-reader', checkout=self.root)
        cases = [({'schema': 'unknown'}, {}, '0::/example/unit', 'Unsupported'),
                 ({'service': 'other'}, {}, '0::/example/unit', 'different service'),
                 ({'status': 'degraded'}, {}, '0::/example/unit', 'not ready'),
                 ({'pid': True}, {}, '0::/example/unit', 'MainPID'),
                 ({'pid': 5678}, {}, '0::/example/unit', 'MainPID'),
                 ({}, {}, '0::/example/other', 'cgroup'),
                 ({'checkout': '/example/other'}, {}, '0::/example/unit', 'checkout'),
                 ({}, {'WorkingDirectory': '/example/other'}, '0::/example/unit', 'checkout'),
                 ({'details': []}, {}, '0::/example/unit', 'details')]
        for body, state, groups, message in cases:
            with self.subTest(body=body, state=state), self.assertRaisesRegex(ValueError, message):
                ServiceHealth.verify(self.body | body, self.state | state, groups,
                                     service='example-reader', checkout=self.root)

    def test_structured_probe_verifies_the_response_identity(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = json.dumps(self.body).encode()
        opener = MagicMock(); opener.open.return_value = response
        service = services.Service('example.service', directory=self.root, port=3199, health_service='example-reader')
        with patch.object(services, 'properties', return_value=self.state), \
             patch.object(services.urllib.request, 'build_opener', return_value=opener), \
             patch.object(Path, 'read_text', return_value='0::/example/unit'):
            self.assertTrue(services.ready(service))
            response.__enter__.return_value.read.return_value = json.dumps(self.body | {'checkout': '/example/other'}).encode()
            self.assertFalse(services.ready(service))

    def test_control_refuses_checkout_mismatch_before_dependency_or_mutation(self):
        service = services.Service('example.service', directory=self.root, port=3199,
            health_service='example-reader', before_start=MagicMock())
        with patch.object(services, 'properties', return_value=self.state | {'WorkingDirectory': '/example/other'}), \
             patch.object(services, 'run') as run:
            for action in ('start', 'stop', 'restart'):
                with self.subTest(action=action), self.assertRaisesRegex(ValueError, 'checkout'):
                    services.control(service, action)
        run.assert_not_called()
        service.before_start.assert_not_called()

    def test_active_start_checks_readiness_without_replacing_or_stopping(self):
        service = services.Service('example.service', directory=self.root, port=3199, health_service='example-reader')
        with patch.object(services, 'properties', return_value=self.state), patch.object(services, 'run') as run, \
             patch.object(services, 'ready', return_value=False), patch.object(services.time, 'monotonic', side_effect=[0, 61]):
            with self.assertRaisesRegex(RuntimeError, 'readiness'):
                services.control(service, 'start')
        run.assert_not_called()

    def test_status_fails_for_an_active_but_degraded_http_service(self):
        with patch.object(services, 'properties', return_value=self.state), patch.object(services, 'ready', return_value=False), \
             patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(services.control(services.Service('example.service', port=3199), 'status'), 1)
