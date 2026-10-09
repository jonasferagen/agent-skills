"""A package-local copy of a shared contract fails when it disagrees with its owner."""

from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / 'scripts/check_shared_contracts.py'
CONTRACTS = runpy.run_path(str(CHECKER))


class SharedContractCheckTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.write('TS_OWNER', '# Imports\n\n## Module And Path Syntax\n\nUse the local module policy.\n')
        self.write('TS_COPY', '# Design\n\n## Module And Path Syntax\n\nUse the local module policy.\n\n## Other rules\n\nUnrelated guidance.\n')

    def write(self, name, text):
        target = self.root / CONTRACTS[name]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8')

    def replace(self, name, old, new):
        path = self.root / CONTRACTS[name]
        path.write_text(path.read_text(encoding='utf-8').replace(old, new), encoding='utf-8')

    def test_compares_from_any_working_directory(self):
        result = subprocess.run([sys.executable, str(CHECKER), '--root', str(self.root)],
                                cwd=self.root.parent, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f'1 shared-contract comparisons at {self.root}', result.stdout)

    def test_a_prose_copy_that_changes_the_rule_fails(self):
        self.replace('TS_COPY', 'Use the local module policy.', 'Ignore the local module policy.')
        compared, errors = CONTRACTS['SharedContracts'].check(self.root)
        self.assertEqual(compared, 1)
        self.assertEqual(len(errors), 1)
        self.assertIn('module syntax', errors[0])

    def test_help_names_the_invoked_path(self):
        result = subprocess.run([sys.executable, str(CHECKER), '--help'],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertIn(str(CHECKER), result.stdout)

    def test_a_changed_prose_owner_requires_updating_its_copy(self):
        self.replace('TS_OWNER', 'local module', 'adopted module')
        self.assertIn('module syntax', CONTRACTS['SharedContracts'].check(self.root)[1][0])

    def test_a_missing_home_fails_as_unavailable_comparison(self):
        (self.root / CONTRACTS['TS_OWNER']).unlink()
        compared, errors = CONTRACTS['SharedContracts'].check(self.root)
        self.assertEqual(compared, 0)
        self.assertIn('could not be compared', errors[0])

    def test_missing_empty_and_ambiguous_sections_do_not_pass(self):
        for body in ('# No section\n', '## Module And Path Syntax\n',
                     '## Module And Path Syntax\nOne\n## Module And Path Syntax\nTwo\n'):
            with self.subTest(body=body):
                self.write('TS_COPY', body)
                self.assertIn('could not be compared', CONTRACTS['SharedContracts'].check(self.root)[1][0])


if __name__ == '__main__':
    unittest.main()
