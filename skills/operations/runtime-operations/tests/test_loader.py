"""Check the copy-deployed loader against the interface consumers rely on."""
import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
LOADER = SKILL / "templates/service_runtime.py"
SCRIPTS = "scripts"


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
        source = (SKILL / SCRIPTS / "runtimeApi.py").read_text(encoding="utf-8")
        source, major_count = re.subn(r"^MAJOR = \d+$", f"MAJOR = {major}", source, flags=re.M)
        source, minor_count = re.subn(r"^MINOR = \d+$", f"MINOR = {minor}", source, flags=re.M)
        assert major_count == 1 and minor_count == 1, "the declaration states two numbers"
        (self.scripts / "runtimeApi.py").write_text(source, encoding="utf-8")

    def test_accepts_the_skill_root_or_the_scripts_directory(self):
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
            "runtime_api_shipped", SKILL / SCRIPTS / "runtimeApi.py")
        module = importlib.util.module_from_spec(declaration)
        declaration.loader.exec_module(module)
        self.assertEqual(loader().load(SKILL, major=1),
                         f"runtime-operations/{module.MAJOR}.{module.MINOR}")


class DeclaredInterfaceTests(unittest.TestCase):
    """The reference states the offered interface; it must not outlive the file."""

    def test_the_reference_states_the_interface_the_helpers_offer(self):
        declaration = importlib.util.spec_from_file_location(
            "runtime_api_under_test", SKILL / SCRIPTS / "runtimeApi.py")
        module = importlib.util.module_from_spec(declaration)
        declaration.loader.exec_module(module)
        offered = f"`{module.NAME}/{module.MAJOR}.{module.MINOR}`"
        reference = (SKILL / "references/runtime-helpers.md").read_text(encoding="utf-8")
        self.assertIn(f"This installation offers {offered}", reference)
        self.assertIn(f"calls `load(runtime_operations, major={module.MAJOR})`", reference)



if __name__ == "__main__":
    unittest.main()
