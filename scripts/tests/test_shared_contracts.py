"""Copies fail on disagreement; the two service-report consumers stay compatible."""

import json
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / 'scripts/check_shared_contracts.py'
CONTRACTS = runpy.run_path(str(CHECKER))
REPORT = runpy.run_path(str(ROOT / CONTRACTS['REPORT_OWNER']))['ServiceReport']
DISPATCHER = runpy.run_path(str(ROOT / CONTRACTS['REPORT_COPY']))


class SharedContractCheckTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.write('TS_OWNER', '# Imports\n\n## Module And Path Syntax\n\nUse the local module policy.\n')
        self.write('TS_COPY', '# Design\n\n## Module And Path Syntax\n\nUse the local module policy.\n\n## Other rules\n\nUnrelated guidance.\n')
        self.write('REPORT_OWNER', "class ServiceReport:\n    SCHEMA = 'service-report/v9'\n"
                   "    STATES = ('up', 'down')\n    LIFECYCLES = ('manual',)\n")
        self.write('REPORT_COPY', "SCHEMA = 'service-report/v9'\nSTATES = ('up', 'down')\n")
        self.write('REPORT_GUIDE', '# Reports\n\nUse `service-report/v9`.\n\n'
                   '| State | Meaning |\n| --- | --- |\n| `up` | available |\n| `down` | unavailable |\n\n'
                   '| `lifecycle` | What it is | A project-wide launch |\n| --- | --- | --- |\n'
                   '| `manual` | explicit | leaves it alone |\n')

    def write(self, name, text):
        target = self.root / CONTRACTS[name]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8')

    def replace(self, name, old, new):
        path = self.root / CONTRACTS[name]
        path.write_text(path.read_text(encoding='utf-8').replace(old, new), encoding='utf-8')

    def test_compares_declared_contracts_without_a_fixed_vocabulary_or_working_directory(self):
        result = subprocess.run([sys.executable, str(CHECKER), '--root', str(self.root)],
                                cwd=self.root.parent, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f'6 shared-contract comparisons at {self.root}', result.stdout)

    def test_a_prose_copy_that_changes_the_rule_fails(self):
        self.replace('TS_COPY', 'Use the local module policy.', 'Ignore the local module policy.')
        compared, errors = CONTRACTS['SharedContracts'].check(self.root)
        self.assertEqual(compared, 6)
        self.assertEqual(len(errors), 1)
        self.assertIn('module syntax', errors[0])

    def test_help_names_the_invoked_path(self):
        result = subprocess.run([sys.executable, str(CHECKER), '--help'],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertIn(str(CHECKER), result.stdout)

    def test_vocabulary_order_is_not_a_protocol_requirement(self):
        self.replace('REPORT_COPY', "('up', 'down')", "('down', 'up')")
        self.replace('REPORT_GUIDE', '| `up` | available |\n| `down` | unavailable |',
                     '| `down` | unavailable |\n| `up` | available |')
        self.assertEqual(CONTRACTS['SharedContracts'].check(self.root), (6, []))

    def test_a_changed_prose_owner_requires_updating_its_copy(self):
        self.replace('TS_OWNER', 'local module', 'adopted module')
        self.assertIn('module syntax', CONTRACTS['SharedContracts'].check(self.root)[1][0])

    def test_a_changed_wire_vocabulary_rejects_the_stale_dispatcher_and_guide(self):
        self.replace('REPORT_OWNER', "('up', 'down')", "('up', 'down', 'waiting')")
        errors = CONTRACTS['SharedContracts'].check(self.root)[1]
        self.assertEqual(len(errors), 2)
        self.assertTrue(any('(STATES;' in error for error in errors))
        self.assertTrue(any('(states)' in error for error in errors))

    def test_a_changed_dispatcher_schema_is_detected(self):
        self.replace('REPORT_COPY', 'service-report/v9', 'service-report/v10')
        errors = CONTRACTS['SharedContracts'].check(self.root)[1]
        self.assertEqual(len(errors), 1)
        self.assertIn('(SCHEMA;', errors[0])

    def test_documented_lifecycles_must_match_their_owner(self):
        self.replace('REPORT_GUIDE', '| `manual` |', '| `automatic` |')
        errors = CONTRACTS['SharedContracts'].check(self.root)[1]
        self.assertEqual(len(errors), 1)
        self.assertIn('(lifecycles)', errors[0])

    def test_a_missing_home_fails_as_unavailable_comparison(self):
        (self.root / CONTRACTS['REPORT_OWNER']).unlink()
        compared, errors = CONTRACTS['SharedContracts'].check(self.root)
        self.assertEqual(compared, 1)
        self.assertIn('could not be compared', errors[0])

    def test_missing_empty_and_ambiguous_sections_do_not_pass(self):
        for body in ('# No section\n', '## Module And Path Syntax\n',
                     '## Module And Path Syntax\nOne\n## Module And Path Syntax\nTwo\n'):
            with self.subTest(body=body):
                self.write('TS_COPY', body)
                self.assertIn('could not be compared', CONTRACTS['SharedContracts'].check(self.root)[1][0])

    def test_an_empty_wire_vocabulary_is_not_a_successful_comparison(self):
        self.replace('REPORT_OWNER', "('up', 'down')", '()')
        errors = CONTRACTS['SharedContracts'].check(self.root)[1]
        self.assertIn('nonempty tuple', errors[0])

    def test_malformed_owner_code_is_reported_as_unavailable_comparison(self):
        self.write('REPORT_OWNER', 'class ServiceReport:\n    broken syntax!\n')
        compared, errors = CONTRACTS['SharedContracts'].check(self.root)
        self.assertEqual(compared, 1)
        self.assertIn('could not be compared', errors[0])


class ServiceReportCompatibilityTests(unittest.TestCase):
    def test_dispatcher_accepts_every_state_and_lifecycle_the_producer_emits(self):
        for state in REPORT.STATES:
            for lifecycle in (*REPORT.LIFECYCLES, None):
                with self.subTest(state=state, lifecycle=lifecycle):
                    line = REPORT.line('example:one', '/synthetic-checkout', state,
                                       lifecycle=lifecycle, detail='synthetic status')
                    self.assertEqual(DISPATCHER['reports'](line), [json.loads(line)])
                    self.assertEqual(REPORT.reports(line), [json.loads(line)])

    def test_both_consumers_ignore_malformed_or_incompatible_records(self):
        valid = {'schema': REPORT.SCHEMA, 'service': 'example', 'state': 'ready'}
        invalid = ['not json', '{', '{}', json.dumps([]),
                   json.dumps({**valid, 'schema': 'unrelated/v1'}),
                   json.dumps({**valid, 'state': 'undeclared-state'}),
                   json.dumps({**valid, 'service': None}),
                   json.dumps({key: value for key, value in valid.items() if key != 'state'})]
        for text in invalid:
            with self.subTest(text=text):
                self.assertEqual(DISPATCHER['reports'](text), [])
                self.assertEqual(REPORT.reports(text), [])

    def test_read_only_dispatcher_preserves_unknown_lifecycle_while_runtime_normalizes_it(self):
        original = {'schema': REPORT.SCHEMA, 'service': 'example', 'state': 'ready',
                    'lifecycle': 'future-class', 'future-field': 'retained'}
        line = json.dumps(original)
        self.assertEqual(DISPATCHER['reports'](line), [original])
        self.assertEqual(REPORT.reports(line), [{**original, 'lifecycle': None}])

    def test_old_reports_keep_the_row_without_inventing_a_lifecycle(self):
        original = {'schema': REPORT.SCHEMA, 'service': 'example', 'state': 'stopped'}
        line = json.dumps(original)
        self.assertEqual(DISPATCHER['reports'](line), [original])
        self.assertEqual(REPORT.reports(line), [{**original, 'lifecycle': None}])

    def test_isolated_dispatcher_reports_producer_messages_without_runtime_installation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            services = root / 'services'
            controller = services / 'example' / 'control'
            controller.parent.mkdir(parents=True)
            entry = services / 'control'
            shutil.copyfile(ROOT / CONTRACTS['REPORT_COPY'], entry)
            lines = [REPORT.line('example:' + state, '/synthetic-checkout', state)
                     for state in REPORT.STATES]
            controller.write_text(f'#!{sys.executable}\nprint({chr(10).join(lines)!r})\n', encoding='utf-8')
            controller.chmod(0o755)
            result = subprocess.run([sys.executable, '-I', str(entry), 'status', '--scope', 'checkout',
                                     '--root', str(root), '--report'], cwd=root.parent,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual([json.loads(line) for line in result.stdout.splitlines()],
                             [json.loads(line) for line in lines])


if __name__ == '__main__':
    unittest.main()
