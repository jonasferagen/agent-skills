"""Exercise the shipped dispatcher across its executable/process boundary."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "templates/repository-docs/services/control"


def controller(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('#!/usr/bin/env python3\nimport json, sys\n' + body, encoding="utf-8")
    path.chmod(0o755)


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

    def test_bare_status_reports_every_service_and_shows_each_exit_without_judging_it(self):
        """A service that exits nonzero is a row; only an unrunnable controller is a fault."""
        controller(self.entry.parent / "docs/control", 'print("docs up", sys.argv[1:3])\n')
        result = self.run_control("status", "--scope", "checkout")
        self.assertEqual(result.returncode, 0)
        self.assertIn("docs: reports ready", result.stdout)
        self.assertIn("  docs up ['status', '--root']", result.stdout)
        self.assertIn("example-preview: reports exit 7", result.stdout)

    def reporter(self, name, **fields):
        """A controller that reports when asked and prints an essay when not."""
        record = {"schema": "service-report/v1", "service": name, "checkout": "/checkout",
                  "state": "ready", "endpoint": None, "unit": None, "detail": None,
                  "attention": None, **fields}
        controller(self.entry.parent / name / "control",
                   'if "--report" in sys.argv:\n'
                   f'    print(json.dumps({record!r}))\n'
                   '    sys.exit(0)\n'
                   'print("line one")\nprint("line two")\nsys.exit(3)\n')

    def test_a_reporting_controller_becomes_one_row_and_its_essay_is_not_printed(self):
        """One timer's own status was forty-one lines of a forty-six line report."""
        self.reporter("docs", endpoint="http://127.0.0.1:8765/", unit="docs.service")
        result = self.run_control("status", "--scope", "checkout")
        self.assertIn("docs             ready      http://127.0.0.1:8765/", result.stdout)
        self.assertNotIn("line one", result.stdout)
        # The unadopted controller beside it still prints the way it printed itself.
        self.assertIn("example-preview: reports exit 7", result.stdout)

    def test_attention_is_shown_and_detail_only_without_it(self):
        self.reporter("one", state="scheduled", detail="next run Thursday")
        self.reporter("two", state="failed", detail="exit 1", attention="no successful run recorded")
        result = self.run_control("status", "--scope", "checkout")
        self.assertIn("(next run Thursday)", result.stdout)
        self.assertIn("** no successful run recorded", result.stdout)
        self.assertNotIn("(exit 1)", result.stdout)

    def test_a_row_without_an_endpoint_keeps_the_state_column(self):
        self.reporter("one", state="absent", detail="nothing is provisioned here")
        self.reporter("two", state="ready", unit="two.service")
        result = self.run_control("status", "--scope", "checkout")
        rows = {line.split()[0]: line for line in result.stdout.splitlines() if line[:1].isalpha()}
        # The state column keeps its width even with nothing to point at, so the
        # detail does not slide left into the space a missing endpoint left behind.
        self.assertRegex(rows["one"], r"absent\s{4,}\(nothing is provisioned here\)")
        self.assertRegex(rows["two"], r"ready\s+two\.service")

    def test_several_instances_of_one_service_are_several_rows(self):
        controller(self.entry.parent / "preview/control",
                   'if "--report" in sys.argv:\n'
                   '    for name in ("preview:water", "preview:lamplighter"):\n'
                   '        print(json.dumps({"schema": "service-report/v1", "service": name,\n'
                   '                          "checkout": "/checkout", "state": "stopped"}))\n'
                   '    sys.exit(1)\n'
                   'sys.exit(1)\n')
        result = self.run_control("status", "--scope", "checkout")
        self.assertIn("preview:water", result.stdout)
        self.assertIn("preview:lamplighter", result.stdout)

    def test_report_emits_the_lines_for_a_consumer_that_is_not_a_person(self):
        self.reporter("docs", unit="docs.service")
        result = self.run_control("status", "--scope", "checkout", "--report")
        lines = [json.loads(line) for line in result.stdout.splitlines() if line.startswith("{")]
        by_service = {record["service"]: record for record in lines}
        self.assertEqual(by_service["docs"]["state"], "ready")
        # A service that does not report is still a row, and says that about itself.
        self.assertEqual(by_service["example-preview"]["state"], "unknown")
        self.assertIn("has not adopted", by_service["example-preview"]["attention"])

    def test_report_applies_only_to_bare_status(self):
        result = self.run_control("example-preview", "status", "--report")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--report applies only to bare status", result.stderr)

    def test_an_unrunnable_controller_is_the_only_fault_bare_status_reports(self):
        broken = self.entry.parent / "broken/control"
        broken.parent.mkdir()
        broken.write_text("#!/nonexistent/interpreter\n", encoding="utf-8")
        broken.chmod(0o755)
        result = self.run_control("status", "--scope", "checkout")
        self.assertEqual(result.returncode, 1)
        self.assertIn("broken: controller would not run", result.stdout)

    def test_other_actions_still_need_a_service_and_scope_needs_bare_status(self):
        for arguments in (("start",), ("example-preview", "status", "--scope", "checkout")):
            with self.subTest(arguments=arguments):
                result = self.run_control(*arguments)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")

    def test_bare_status_is_workspace_wide_and_follows_references_once(self):
        """Workspace is the default shape, so a bare status answers for the project."""
        (self.entry.parent / "example-preview/control").unlink()
        controller(self.entry.parent / "docs/control", 'print("primary")\n')
        member = self.root.parent / (self.root.name + "-member")
        self.addCleanup(shutil.rmtree, member, True)
        shutil.copy2(SOURCE, (member / "services").mkdir(parents=True) or member / "services/control")
        controller(member / "services/db/control", 'print("member db")\nsys.exit(1)\n')
        quiet = self.root.parent / (self.root.name + "-quiet")
        self.addCleanup(shutil.rmtree, quiet, True)
        (quiet / "project-docs").mkdir(parents=True)
        (quiet / "project-docs/foundation.md").write_text("# Foundation\n", encoding="utf-8")
        (self.root / "project-docs").mkdir()
        (self.root / "project-docs/foundation.md").write_text(
            "# Foundation\n\n## References\n\n| Key | Target |\n| --- | --- |\n"
            f"| member | {member} |\n| quiet | {quiet} |\n| self | .. |\n"
            "| files | /nonexistent |\n\n## Inheritance\n",
            encoding="utf-8")
        result = self.run_control("status")
        self.assertEqual(result.returncode, 0)
        self.assertIn("docs: reports ready", result.stdout)
        self.assertIn(f"== member ({member})", result.stdout)
        self.assertIn("db: reports exit 1", result.stdout)
        # A declared member with no service home is stated; a non-repository is not.
        self.assertIn(f"== quiet ({quiet})", result.stdout)
        self.assertIn("no service home", result.stdout)
        self.assertEqual(result.stdout.count("== "), 2)

    def test_a_worktree_reports_the_installed_checkout_not_itself(self):
        """A task worktree has no units of its own, so it must not answer for them."""
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=T",
                        "-c", "user.email=t@example.test", "commit", "-qm", "base"], check=True)
        worktree = self.root.parent / (self.root.name + "-wt")
        self.addCleanup(shutil.rmtree, worktree, True)
        subprocess.run(["git", "-C", str(self.root), "worktree", "add", "-q",
                        str(worktree), "-b", "task"], check=True)
        self.addCleanup(subprocess.run, ["git", "-C", str(self.root), "worktree", "prune"])
        result = subprocess.run([str(worktree / "services/control"), "status", "--scope", "checkout"],
                                cwd=worktree, stdin=subprocess.DEVNULL, capture_output=True,
                                text=True, encoding="utf-8", timeout=10)
        self.assertEqual(result.returncode, 0)
        # The controller is asked about the installed checkout, never the worktree.
        self.assertIn(f'"--root", "{self.root}"'.replace('"', '"'), result.stdout.replace("'", '"'))
