"""Offline tests for scripts/copiedValues.py. Every value here is made up."""
import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import copiedValues  # noqa: E402

PRIVATE_MAIL = "Ring 55501000 om faktura 1000007, kode 300007.\nSvar til someone@example.test\nNavn: Example Person\n"


class CopiedValues(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.private = self.root / "data"
        self.private.mkdir()
        (self.private / "mail.txt").write_text(PRIVATE_MAIL, encoding="utf-8")

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def check(self, *arguments):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = copiedValues.main(["--private", str(self.private), *map(str, arguments)])
        return status, out.getvalue(), err.getvalue()

    def test_copied_number_is_reported_by_file_and_line_without_the_value(self):
        test_file = self.write("tests/test_a.py", "first line\nassert parse('tlf 55501000') == []\n")
        status, out, _ = self.check(test_file)
        self.assertEqual(1, status)
        self.assertIn(f"{test_file}:2: copied number of 8 digits\n", out)
        self.assertNotIn("55501000", out)

    def test_file_inside_the_current_directory_is_reported_by_its_relative_path(self):
        self.write("tests/test_a.py", "tlf 55501000\n")
        script = Path(copiedValues.__file__)
        result = subprocess.run([sys.executable, str(script), "--private", "data", "tests/test_a.py"],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual("tests/test_a.py:1: copied number of 8 digits", result.stdout.splitlines()[0])

    def test_six_digit_number_is_reported_when_copied_whole(self):
        notes = self.write("notes.md", "kode 300007\n")
        status, out, _ = self.check(notes)
        self.assertEqual(1, status)
        self.assertIn(f"{notes}:1: copied number of 6 digits\n", out)

    def test_made_up_number_of_the_same_shape_passes(self):
        status, out, _ = self.check(self.write("tests/test_a.py", "assert parse('tlf 00000000') == []\n"))
        self.assertEqual(0, status)
        self.assertIn("0 copied value(s) in 1 file(s) checked", out)

    def test_number_cut_from_a_private_one_is_reported_as_partly_copied(self):
        status, out, _ = self.check(self.write("notes.md", "tlf 5550100\n"))
        self.assertEqual(1, status)
        self.assertIn("number of 7 digits, part of a private number or containing one", out)

    def test_number_padded_around_a_private_one_is_reported_as_partly_copied(self):
        status, out, _ = self.check(self.write("notes.md", "order 9555010009\n"))
        self.assertEqual(1, status)
        self.assertIn("number of 10 digits, part of a private number or containing one", out)

    def test_short_overlap_with_a_private_number_is_not_reported(self):
        status, _, _ = self.check(self.write("notes.md", "count 555010\n"))
        self.assertEqual(0, status)

    def test_copied_mail_address_is_reported_whatever_its_case(self):
        status, out, _ = self.check(self.write("notes.md", "contact Someone@Example.TEST\n"))
        self.assertEqual(1, status)
        self.assertIn("copied mail address", out)
        self.assertNotIn("omeone@", out)

    def test_listed_term_is_reported(self):
        status, out, _ = self.check("--term", "Example Person", self.write("notes.md", "written for example person\n"))
        self.assertEqual(1, status)
        self.assertIn("copied listed term", out)

    def test_allowed_value_is_not_reported(self):
        allow = self.write("allowed.txt", "1000007  # the invoice number the plan uses as an anchor\n")
        status, _, _ = self.check("--allow-file", allow, self.write("plan.md", "resolves invoice 1000007\n"))
        self.assertEqual(0, status)

    def test_absent_private_data_cannot_run_and_is_not_a_pass(self):
        shutil.rmtree(self.private)
        status, out, err = self.check(self.write("notes.md", "anything\n"))
        self.assertEqual(2, status)
        self.assertIn("cannot run", err)
        self.assertEqual("", out)

    def test_files_inside_the_private_data_are_not_checked(self):
        status, _, err = self.check(self.private / "mail.txt")
        self.assertEqual(2, status)
        self.assertIn("no readable files to check", err)

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_without_file_arguments_git_decides_what_is_checked(self):
        self.write(".gitignore", "data/\nignored.txt\n")
        self.write("tracked.md", "tlf 55501000\n")
        self.write("new.md", "faktura 1000007\n")
        self.write("ignored.txt", "tlf 55501000\n")
        for command in (["init", "-q"], ["add", "tracked.md", ".gitignore"]):
            subprocess.run(["git", "-C", str(self.root), *command], check=True)
        script = Path(copiedValues.__file__)
        result = subprocess.run([sys.executable, str(script), "--private", "data"], cwd=self.root,
                                capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertIn("tracked.md:1: copied number of 8 digits\n", result.stdout)
        self.assertIn("new.md:1: copied number of 7 digits\n", result.stdout)
        self.assertNotIn("ignored.txt", result.stdout)


if __name__ == "__main__":
    unittest.main()
