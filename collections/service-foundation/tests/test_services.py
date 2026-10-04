"""Check real filesystem defects without starting a service."""
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate-services.py"
validate = runpy.run_path(str(SCRIPT))["validate"]


class ServiceTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.home = self.root / "services"
        service = self.home / "preview"
        service.mkdir(parents=True)
        (self.home / "README.md").write_text("[Preview](preview/README.md)\n")
        (service / "README.md").write_text("Preview operating guide.\n")
        for path in (self.home / "control", service / "control"):
            path.write_text("#!/bin/sh\ntouch " + str(self.root / "executed") + "\n")
            path.chmod(0o755)

    def test_declared_format_is_checked_without_requiring_migration(self):
        self.assertEqual(validate(self.home), [])
        guide = self.home / 'preview/README.md'
        guide.write_text('# Preview\nService format: service-definition/v99\n')
        self.assertTrue(any('supported Service format' in e for e in validate(self.home)))

    def test_duplicate_structured_identities_fail(self):
        fixture = runpy.run_path(str(Path(__file__).with_name('test_service_format.py')))['example']()
        (self.home / 'preview/README.md').write_text(fixture)
        other = self.home / 'reader'
        other.mkdir()
        (other / 'README.md').write_text(fixture)
        (other / 'control').write_text('#!/bin/sh\nexit 1\n')
        (other / 'control').chmod(0o755)
        (self.home / 'README.md').write_text('[Preview](preview/README.md)\n[Reader](reader/README.md)\n')
        self.assertTrue(any('duplicate service Identity' in e for e in validate(self.home)))

    def test_valid_structure_never_executes_controls(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.home)],
                                cwd="/", capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("unverified", result.stdout)
        self.assertFalse((self.root / "executed").exists())

    def test_missing_and_nonexecutable_controls(self):
        (self.home / "control").unlink()
        (self.home / "preview/control").chmod(0o644)
        self.assertEqual(len(validate(self.home)), 2)

    def test_missing_guide_and_index_link(self):
        (self.home / "preview/README.md").unlink()
        (self.home / "README.md").write_text("[Old](retired/README.md)\n")
        errors = validate(self.home)
        self.assertEqual(len(errors), 3, errors)

    def test_invalid_name(self):
        (self.home / "preview").rename(self.home / "Bad_Name")
        self.assertTrue(any("service name" in e for e in validate(self.home)))

    def test_missing_explicit_home_is_failure(self):
        self.assertTrue(validate(self.root / "missing"))

    def test_empty_home_is_failure(self):
        empty = self.root / "empty"
        empty.mkdir()
        self.assertTrue(any("no service definitions" in e for e in validate(empty)))

    def test_symlinks_are_not_followed(self):
        (self.home / "alias").symlink_to(self.home / "preview", target_is_directory=True)
        (self.home / "preview/control").unlink()
        (self.home / "preview/control").symlink_to(self.home / "control")
        self.assertEqual(len(validate(self.home)), 2)
        alias = self.root / "alias"
        alias.symlink_to(self.home, target_is_directory=True)
        self.assertTrue(validate(alias))

    def test_unreadable_text_reported(self):
        (self.home / "README.md").write_bytes(b"\xff")
        self.assertTrue(any("cannot read index" in e for e in validate(self.home)))

    def test_external_links_do_not_expand_scope(self):
        with (self.home / "README.md").open("a") as f:
            f.write("[Other](../missing.md) [Web](https://example.invalid/README.md)\n")
        self.assertEqual(validate(self.home), [])

    def test_missing_index_and_guide(self):
        (self.home / "README.md").unlink()
        (self.home / "preview/README.md").unlink()
        self.assertEqual(len(validate(self.home)), 2)

    def test_malformed_link_is_a_finding(self):
        with (self.home / "README.md").open("a") as f:
            f.write("[Broken](https://[broken)\n")
        self.assertTrue(any("malformed link" in e for e in validate(self.home)))
