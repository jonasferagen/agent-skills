"""The source runner finds nested suites and fails incomplete verification."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / 'check.py'
spec = importlib.util.spec_from_file_location('source_check', SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class CheckTests(unittest.TestCase):
    def test_missing_prerequisites_fail_explicitly(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(runner.shutil, 'which', return_value=None):
            errors = runner.prerequisites(Path(directory))
        self.assertEqual(len(errors), 3)
        self.assertTrue(any('node is required' in error for error in errors))
        self.assertTrue(any('gpg is required' in error for error in errors))
        self.assertTrue(any('npm ci' in error for error in errors))

    def test_discovery_includes_nested_helpers_without_duplicate_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('scripts/tests/test_one.py', 'scripts/tests/test_two.py',
                         'skills/example/helper/tests/test_nested.py',
                         'skills/.worktrees/old/test_retired.py'):
                file = root / name
                file.parent.mkdir(parents=True, exist_ok=True)
                file.touch()
            self.assertEqual(runner.test_directories(root), [
                root / 'scripts/tests', root / 'skills/example/helper/tests'])

    def test_empty_failed_and_skipped_suites_cannot_report_success(self):
        for body in ('', 'self.fail("synthetic failure")', 'self.skipTest("synthetic missing prerequisite")'):
            with self.subTest(body=body), tempfile.TemporaryDirectory() as directory:
                if body:
                    (Path(directory) / 'test_example.py').write_text(
                        f'import unittest\nclass Example(unittest.TestCase):\n    def test_result(self):\n        {body}\n',
                        encoding='utf-8')
                result = subprocess.run([sys.executable, str(SCRIPT), '--suite', directory],
                                        stdin=subprocess.DEVNULL, capture_output=True, timeout=15)
                self.assertNotEqual(result.returncode, 0)

    def test_successful_suite_reports_success(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / 'test_example.py').write_text(
                'import unittest\nclass Example(unittest.TestCase):\n    def test_result(self):\n        self.assertEqual(2 + 2, 4)\n',
                encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), '--suite', directory],
                                    stdin=subprocess.DEVNULL, capture_output=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
