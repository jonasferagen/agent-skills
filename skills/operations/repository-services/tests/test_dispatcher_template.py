"""Exercise the shipped dispatcher template through its process boundary."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

DISPATCHER = Path(__file__).resolve().parents[1] / "templates/services/control"


class DispatcherTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.home = Path(tmp.name) / "services"
        service = self.home / "preview"
        service.mkdir(parents=True)
        self.dispatcher = self.home / "control"
        self.dispatcher.write_bytes(DISPATCHER.read_bytes())
        self.dispatcher.chmod(0o755)
        controller = service / "control"
        controller.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n')
        controller.chmod(0o755)

    def run_dispatcher(self, *arguments):
        return subprocess.run([sys.executable, str(self.dispatcher), *arguments],
                              capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=30)

    def test_the_action_and_expected_checkout_reach_the_controller(self):
        result = self.run_dispatcher("preview", "status")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.split(), ["status", "--root", str(self.home.parent)])

    def test_options_after_the_action_pass_through(self):
        result = self.run_dispatcher("preview", "start", "--instance", "lobby", "--port", "8791")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.split()[3:], ["--instance", "lobby", "--port", "8791"])

    def test_an_undefined_service_or_action_is_refused(self):
        self.assertNotEqual(self.run_dispatcher("absent", "status").returncode, 0)
        self.assertNotEqual(self.run_dispatcher("preview", "deploy").returncode, 0)

    def test_a_service_without_an_executable_controller_is_not_offered(self):
        (self.home / "preview/control").chmod(0o644)
        self.assertNotEqual(self.run_dispatcher("preview", "status").returncode, 0)



if __name__ == "__main__":
    unittest.main()
