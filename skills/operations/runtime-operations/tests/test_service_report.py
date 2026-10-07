"""A report is one scannable line per instance, and refuses to become an essay."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from serviceReport import ServiceReport


class ReportLineTests(unittest.TestCase):
    def test_a_line_carries_the_declared_fields_and_nothing_else(self):
        record = json.loads(ServiceReport.line('docs-browser', '/checkout', 'ready',
                                               endpoint='http://127.0.0.1:8765/',
                                               unit='docs-viewer.service',
                                               lifecycle='maintained'))
        self.assertEqual(record, {'schema': 'service-report/v1', 'service': 'docs-browser',
                                  'checkout': '/checkout', 'state': 'ready',
                                  'lifecycle': 'maintained',
                                  'endpoint': 'http://127.0.0.1:8765/',
                                  'unit': 'docs-viewer.service', 'detail': None,
                                  'attention': None})

    def test_a_controller_that_declares_no_class_is_unclassified(self):
        """Absent is a value a consumer can act on; a guess is not."""
        record = json.loads(ServiceReport.line('example', '/checkout', 'ready'))
        self.assertIn('lifecycle', record)
        self.assertIsNone(record['lifecycle'])

    def test_a_class_outside_the_vocabulary_is_refused(self):
        for invalid in ('Maintained', 'daemon', 'on demand', ''):
            with self.subTest(lifecycle=invalid), self.assertRaisesRegex(ValueError, 'lifecycle'):
                ServiceReport.line('example', '/checkout', 'ready', lifecycle=invalid)
        for declared in ServiceReport.LIFECYCLES:
            with self.subTest(lifecycle=declared):
                record = json.loads(ServiceReport.line('example', '/checkout', 'ready',
                                                       lifecycle=declared))
                self.assertEqual(record['lifecycle'], declared)

    def test_a_line_is_one_line(self):
        for state in ServiceReport.STATES:
            self.assertNotIn('\n', ServiceReport.line('example', '/checkout', state))

    def test_an_instance_is_named_on_its_service(self):
        record = json.loads(ServiceReport.line('station-preview:lamplighter', '/checkout', 'stopped'))
        self.assertEqual(record['service'], 'station-preview:lamplighter')
        for invalid in ('Station-Preview', 'station preview', '', 'station:', ':lamplighter'):
            with self.subTest(service=invalid), self.assertRaisesRegex(ValueError, 'names its service'):
                ServiceReport.line(invalid, '/checkout', 'ready')

    def test_a_state_outside_the_vocabulary_is_refused(self):
        with self.assertRaisesRegex(ValueError, 'one of'):
            ServiceReport.line('example', '/checkout', 'degraded')

    def test_detail_cannot_become_the_output_it_replaces(self):
        """The row is the point; a journal belongs to `status <name>`."""
        for field in ('detail', 'attention', 'unit', 'endpoint'):
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'one line'):
                ServiceReport.line('example', '/checkout', 'ready', **{field: 'a\nb'})
            with self.subTest(field=field, case='length'), self.assertRaisesRegex(ValueError, 'one line'):
                ServiceReport.line('example', '/checkout', 'ready',
                                   **{field: 'x' * (ServiceReport.LIMIT + 1)})
            with self.subTest(field=field, case='empty'), self.assertRaisesRegex(ValueError, 'non-empty'):
                ServiceReport.line('example', '/checkout', 'ready', **{field: '  '})


class ReportParsingTests(unittest.TestCase):
    def test_reports_are_read_out_of_whatever_else_a_controller_printed(self):
        output = ('Generating units\n'
                  + ServiceReport.line('one', '/checkout', 'ready') + '\n'
                  + 'a trailing note\n'
                  + '  ' + ServiceReport.line('two', '/checkout', 'absent') + '  \n')
        self.assertEqual([record['service'] for record in ServiceReport.reports(output)],
                         ['one', 'two'])

    def test_an_unreadable_class_loses_the_class_and_not_the_row(self):
        """A reading must survive a value a consumer cannot act on."""
        found = ServiceReport.reports(
            '{"schema": "service-report/v1", "service": "one", "state": "ready",'
            ' "lifecycle": "daemon"}\n'
            '{"schema": "service-report/v1", "service": "two", "state": "ready",'
            ' "lifecycle": "maintained"}\n')
        self.assertEqual([(record['service'], record['lifecycle']) for record in found],
                         [('one', None), ('two', 'maintained')])

    def test_a_report_from_before_the_class_reads_as_unclassified(self):
        found = ServiceReport.reports(
            '{"schema": "service-report/v1", "service": "one", "state": "ready"}')
        self.assertEqual(len(found), 1)
        self.assertIsNone(found[0]['lifecycle'])

    def test_a_partial_adoption_is_not_mistaken_for_a_report(self):
        for text in ('{}', '{"schema": "service-report/v1"}', 'not json at all',
                     '{"schema": "service-health/v1", "service": "one", "state": "ready"}',
                     '{"schema": "service-report/v1", "service": "one", "state": "degraded"}',
                     '{"schema": "service-report/v1", "state": "ready"}',
                     '{"schema": "service-report/v1", "service": "one", "state": "ready"'):
            with self.subTest(text=text):
                self.assertEqual(ServiceReport.reports(text), [])


if __name__ == '__main__':
    unittest.main()
