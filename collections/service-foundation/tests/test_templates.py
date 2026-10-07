"""Check the copy-deployed templates against the interfaces consumers rely on."""
import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

COLLECTION = Path(__file__).resolve().parents[1]
LOADER = COLLECTION / "templates/repository-docs/tools/service_runtime.py"
DISPATCHER = COLLECTION / "templates/repository-docs/services/control"
SCRIPTS = "skills/runtime-operations/scripts"


def loader():
    specification = importlib.util.spec_from_file_location("service_runtime_under_test", LOADER)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


class LoaderTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.scripts = self.root / SCRIPTS
        self.scripts.mkdir(parents=True)
        self.declare(major=1, minor=2)
        self.load = loader().load
        self.addCleanup(self.restore, list(sys.path))

    def restore(self, path):
        sys.path[:] = path

    def declare(self, *, major, minor):
        """A synthetic installation declaring exactly these two numbers.

        Rewritten by assignment rather than by the literals the shipped file
        happens to hold: matching those made raising the shipped minor silently
        stop building the version this fixture is about.
        """
        source = (COLLECTION / SCRIPTS / "runtimeApi.py").read_text(encoding="utf-8")
        source, major_count = re.subn(r"^MAJOR = \d+$", f"MAJOR = {major}", source, flags=re.M)
        source, minor_count = re.subn(r"^MINOR = \d+$", f"MINOR = {minor}", source, flags=re.M)
        assert major_count == 1 and minor_count == 1, "the declaration states two numbers"
        (self.scripts / "runtimeApi.py").write_text(source, encoding="utf-8")

    def test_accepts_the_collection_root_or_the_scripts_directory(self):
        self.assertEqual(self.load(self.root, major=1), "runtime-operations/1.2")
        self.assertEqual(self.load(self.scripts, major=1), "runtime-operations/1.2")
        self.assertIn(str(self.scripts), sys.path)

    def test_an_earlier_consumer_runs_on_added_surface(self):
        self.assertEqual(self.load(self.root, major=1, minor=0), "runtime-operations/1.2")

    def test_a_consumer_needing_absent_surface_is_refused(self):
        with self.assertRaises(RuntimeError) as refusal:
            self.load(self.root, major=1, minor=3)
        self.assertIn("1.2", str(refusal.exception))
        self.assertIn("1.3", str(refusal.exception))

    def test_an_incompatible_major_version_is_refused(self):
        with self.assertRaises(RuntimeError):
            self.load(self.root, major=2)

    def test_a_refusal_leaves_no_import_path_behind(self):
        before = list(sys.path)
        with self.assertRaises(RuntimeError):
            self.load(self.root, major=2)
        self.assertEqual(sys.path, before)

    def test_an_installation_predating_the_declaration_is_named(self):
        (self.scripts / "runtimeApi.py").unlink()
        with self.assertRaises(RuntimeError) as refusal:
            self.load(self.root, major=1)
        self.assertIn("re-pinned", str(refusal.exception))
        self.assertNotIn(str(self.scripts), sys.path)

    def test_a_missing_or_symlinked_installation_is_refused(self):
        with self.assertRaises(RuntimeError):
            self.load(self.root / "absent", major=1)
        link = self.root / "linked"
        link.symlink_to(self.scripts, target_is_directory=True)
        with self.assertRaises(RuntimeError):
            self.load(link, major=1)

    def test_a_version_that_is_not_two_integers_is_refused(self):
        with self.assertRaises(TypeError):
            self.load(self.root, major="1")

    def test_the_shipped_declaration_matches_the_shipped_helpers(self):
        declaration = importlib.util.spec_from_file_location(
            "runtime_api_shipped", COLLECTION / SCRIPTS / "runtimeApi.py")
        module = importlib.util.module_from_spec(declaration)
        declaration.loader.exec_module(module)
        self.assertEqual(loader().load(COLLECTION, major=1),
                         f"runtime-operations/{module.MAJOR}.{module.MINOR}")


class DeclaredInterfaceTests(unittest.TestCase):
    """The reference states the offered interface; it must not outlive the file."""

    def test_the_reference_states_the_interface_the_helpers_offer(self):
        declaration = importlib.util.spec_from_file_location(
            "runtime_api_under_test", COLLECTION / SCRIPTS / "runtimeApi.py")
        module = importlib.util.module_from_spec(declaration)
        declaration.loader.exec_module(module)
        offered = f"`{module.NAME}/{module.MAJOR}.{module.MINOR}`"
        reference = (COLLECTION / "references/runtime-helpers.md").read_text(encoding="utf-8")
        self.assertIn(f"This installation offers {offered}", reference)
        self.assertIn(f"calls `load(collection, major={module.MAJOR})`", reference)


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
