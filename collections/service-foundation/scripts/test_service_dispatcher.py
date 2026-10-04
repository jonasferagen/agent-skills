"""Exercise the shipped dispatcher across its executable/process boundary."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "templates/repository-docs/services/control"


class DispatcherTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        home = self.root / "services"
        home.mkdir()
        self.entry = home / "control"
        shutil.copy2(SOURCE, self.entry)
        controller = home / "example-preview/control"
        controller.parent.mkdir()
        controller.write_text('#!/usr/bin/env python3\nimport json, sys\n'
                              'print(json.dumps(sys.argv[1:]))\nsys.exit(7)\n', encoding="utf-8")
        controller.chmod(0o755)

    def run_control(self, *arguments):
        return subprocess.run([str(self.entry), *arguments], cwd=self.root.parent,
                              stdin=subprocess.DEVNULL, capture_output=True, text=True,
                              encoding="utf-8", timeout=5)

    def test_dispatches_action_and_checkout_from_another_directory(self):
        result = self.run_control("example-preview", "status")
        self.assertEqual(result.returncode, 7)
        self.assertEqual(json.loads(result.stdout), ["status", "--root", str(self.root)])

    def test_forwards_explicit_checkout(self):
        selected = self.root / "other-checkout"
        result = self.run_control("example-preview", "start", "--root", str(selected))
        self.assertEqual(result.returncode, 7)
        self.assertEqual(json.loads(result.stdout), ["start", "--root", str(selected)])

    def test_rejects_unknown_service_and_path_traversal(self):
        for name in ("absent", "../example-preview"):
            with self.subTest(name=name):
                result = self.run_control(name, "start")
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("invalid choice", result.stderr)

    def test_rejects_unknown_action(self):
        result = self.run_control("example-preview", "install")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("invalid choice", result.stderr)

    def test_discovers_only_executable_regular_controllers(self):
        home = self.entry.parent
        (home / "unfinished").mkdir()
        (home / "unfinished/control").write_text("unfinished", encoding="utf-8")
        (home / "alias").symlink_to(home / "example-preview", target_is_directory=True)
        result = self.run_control("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("example-preview", result.stdout)
        self.assertNotIn("unfinished", result.stdout)
        self.assertNotIn("alias", result.stdout)
