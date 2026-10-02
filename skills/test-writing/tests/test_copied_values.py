"""Offline tests for scripts/copiedValues.py. Every value here is made up."""
import contextlib
import io
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import copiedValues  # noqa: E402

PRIVATE_MAIL = "Ring 55501000 om faktura 1000007, kode 300007.\nSvar til someone@example.test\nNavn: Example Person\n"
SCRIPT = Path(copiedValues.__file__)
PERMISSIONS_ENFORCED = hasattr(os, "geteuid") and os.geteuid() != 0


class CopiedValues(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.private = self.root / "data"
        self.private.mkdir()
        (self.private / "mail.txt").write_text(PRIVATE_MAIL, encoding="utf-8")

    def write(self, name, text, encoding="utf-8"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode(encoding))
        return path

    def check(self, *arguments, private=None):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = copiedValues.main(["--private", str(private or self.private), *map(str, arguments)])
        return status, out.getvalue(), err.getvalue()

    def run_script(self, *arguments, cwd=None, env=None):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, arguments)], cwd=cwd or self.root,
                              capture_output=True, text=True, env=env)

    def unreadable(self, path):
        path.chmod(0)
        self.addCleanup(path.chmod, 0o700)

    # What counts as copied

    def test_copied_number_is_reported_by_file_and_line_without_the_value(self):
        test_file = self.write("tests/test_a.py", "first line\nassert parse('tlf 55501000') == []\n")
        status, out, _ = self.check(test_file)
        self.assertEqual(1, status)
        self.assertIn(f"{test_file}:2: copied number of 8 digits\n", out)
        self.assertNotIn("55501000", out)

    def test_file_inside_the_current_directory_is_reported_by_its_relative_path(self):
        self.write("tests/test_a.py", "tlf 55501000\n")
        result = self.run_script("--private", "data", "tests/test_a.py")
        self.assertEqual("tests/test_a.py:1: copied number of 8 digits", result.stdout.splitlines()[0])

    def test_six_digit_number_is_reported_when_copied_whole(self):
        notes = self.write("notes.md", "kode 300007\n")
        status, out, _ = self.check(notes)
        self.assertEqual(1, status)
        self.assertIn(f"{notes}:1: copied number of 6 digits\n", out)

    def test_made_up_number_of_the_same_shape_passes(self):
        status, out, _ = self.check(self.write("tests/test_a.py", "assert parse('tlf 12345678') == []\n"))
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

    def test_number_of_one_repeated_digit_is_neither_collected_nor_reported(self):
        self.write("data/headers.txt", "boundary 000000000000\nsent 1696000000000\ncode 777777\n")
        test_file = self.write("tests/test_a.py", "phone 00000000\nid 00000000000\ncode 777777\namount 40000000000005\n")
        status, out, _ = self.check(test_file)
        self.assertEqual(0, status, out)

    def test_min_digits_sets_the_shortest_number_that_counts(self):
        self.write("data/short.txt", "pin 12345\n")
        notes = self.write("notes.md", "pin 12345\n")
        self.assertEqual(0, self.check(notes)[0])
        self.assertEqual(1, self.check("--min-digits", "5", notes)[0])

    def test_copied_mail_address_is_reported_whatever_its_case(self):
        status, out, _ = self.check(self.write("notes.md", "contact Someone@Example.TEST\n"))
        self.assertEqual(1, status)
        self.assertIn("copied mail address", out)
        self.assertNotIn("omeone@", out)

    def test_listed_term_is_reported(self):
        status, out, _ = self.check("--term", "Example Person", self.write("notes.md", "written for example person\n"))
        self.assertEqual(1, status)
        self.assertIn("copied listed term", out)

    def test_listed_term_matches_whole_words_only(self):
        self.assertEqual(0, self.check("--term", "Ola", self.write("notes.md", "Olav drinks cola\n"))[0])
        self.assertEqual(1, self.check("--term", "Ola", self.write("notes.md", "signed, ola.\n"))[0])

    def test_terms_can_be_read_from_a_file_kept_with_the_private_data(self):
        names = self.write("data/names.txt", "# names seen in the mails\nExample Person\n")
        status, out, _ = self.check("--term-file", names, self.write("notes.md", "written for example person\n"))
        self.assertEqual(1, status)
        self.assertIn("notes.md:1: copied listed term", out)

    def test_line_numbers_count_line_feeds_only(self):
        notes = self.write("notes.md", "page one\fpage two\ntlf 55501000\n")
        status, out, _ = self.check(notes)
        self.assertEqual(1, status)
        self.assertIn(f"{notes}:2: copied number of 8 digits", out)

    # Allowed values

    def test_value_in_the_allow_file_is_not_reported(self):
        allow = self.write("allowed.txt", "1000007  # the invoice number the plan uses as an anchor\n")
        status, _, _ = self.check("--allow-file", allow, self.write("plan.md", "resolves invoice 1000007\n"))
        self.assertEqual(0, status)

    def test_value_allowed_on_the_command_line_is_not_reported(self):
        self.assertEqual(0, self.check("--allow", "1000007", self.write("plan.md", "invoice 1000007\n"))[0])

    def test_allowed_mail_address_is_not_reported_whatever_its_case(self):
        notes = self.write("notes.md", "contact someone@example.test\n")
        self.assertEqual(0, self.check("--allow", "Someone@Example.TEST", notes)[0])

    def test_allowed_value_inside_a_longer_private_number_is_not_reported(self):
        self.write("data/ledger.txt", "account 91000007\n")
        allow = self.write("tests/allowed.txt", "1000007\n")
        plan = self.write("plan.md", "resolves invoice 1000007\n")
        status, out, _ = self.check("--allow-file", allow, plan, allow)
        self.assertEqual(0, status, out)
        self.assertEqual(1, self.check("--allow-file", allow, self.write("other.md", "account 91000007\n"))[0])

    # What is read

    def test_every_private_path_is_read(self):
        dumps = self.root / "dumps"
        dumps.mkdir()
        (dumps / "dump.sql").write_text("insert into phones values ('55507777');\n", encoding="utf-8")
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = copiedValues.main(["--private", str(self.private), "--private", str(dumps),
                                        str(self.write("notes.md", "tlf 55507777\n"))])
        self.assertEqual(1, status)

    def test_private_mail_in_another_encoding_is_read(self):
        self.write("data/old.eml", "Tlf 55509876 - Ærlig hilsen\n", encoding="latin-1")
        self.assertEqual(1, self.check(self.write("notes.md", "tlf 55509876\n"))[0])

    def test_text_inside_a_private_database_file_is_read(self):
        database = sqlite3.connect(self.private / "records.sqlite")
        with database:
            database.execute("create table contact (phone text, mail text)")
            database.execute("insert into contact values ('55509876', 'other@example.test')")
        database.close()
        status, out, _ = self.check(self.write("notes.md", "tlf 55509876\nmail other@example.test\n"))
        self.assertEqual(1, status)
        self.assertEqual(2, out.count("copied"))

    def test_checked_file_in_another_encoding_is_checked(self):
        notes = self.write("notes.md", "Ærlig: tlf 55501000\n", encoding="latin-1")
        self.assertEqual(1, self.check(notes)[0])

    def test_private_directory_reached_through_a_link_is_read(self):
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        (elsewhere / "mail.txt").write_text("tlf 55504444\n", encoding="utf-8")
        (self.private / "linked").symlink_to(elsewhere, target_is_directory=True)
        self.assertEqual(1, self.check(self.write("notes.md", "tlf 55504444\n"))[0])

    def test_directory_given_as_a_file_argument_is_walked(self):
        self.write("tests/unit/test_b.py", "tlf 55501000\n")
        status, out, _ = self.check(self.root / "tests")
        self.assertEqual(1, status)
        self.assertIn("test_b.py:1: copied number of 8 digits", out)

    def test_files_inside_the_private_data_are_not_checked(self):
        status, _, err = self.check(self.private / "mail.txt")
        self.assertEqual(3, status)
        self.assertIn("no file to check", err)

    def test_long_line_without_an_address_is_scanned_quickly(self):
        # The address pattern once took quadratic time: a 200 KiB line ran for about a minute.
        notes = self.write("notes.md", "ab12" * 50_000 + "\n")
        started = time.monotonic()
        status, _, _ = self.check(notes)
        self.assertEqual(0, status)
        self.assertLess(time.monotonic() - started, 5)

    # When the check cannot give a verdict

    def test_absent_private_data_exits_2_and_checks_nothing(self):
        shutil.rmtree(self.private)
        status, out, err = self.check(self.write("notes.md", "anything\n"))
        self.assertEqual(2, status)
        self.assertIn("private data absent", err)
        self.assertEqual("", out)

    def test_missing_second_private_path_cannot_run(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = copiedValues.main(["--private", str(self.private), "--private", str(self.root / "dumps"),
                                        str(self.write("notes.md", "tlf 55501000\n"))])
        self.assertEqual(3, status)
        self.assertIn("does not exist", err.getvalue())
        self.assertEqual("", out.getvalue())

    def test_empty_private_directory_cannot_run(self):
        empty = self.root / "empty"
        empty.mkdir()
        status, _, err = self.check(self.write("notes.md", "anything\n"), private=empty)
        self.assertEqual(3, status)
        self.assertIn("can be read", err)

    def test_private_data_with_nothing_to_look_for_cannot_run(self):
        (self.private / "mail.txt").write_text("no numbers or addresses here\n", encoding="utf-8")
        status, _, err = self.check(self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("nothing to look for", err)

    def test_a_listed_term_is_enough_to_look_for(self):
        (self.private / "mail.txt").write_text("written by Example Person\n", encoding="utf-8")
        status, _, _ = self.check("--term", "Example Person", self.write("notes.md", "example person wrote\n"))
        self.assertEqual(1, status)

    def test_misspelled_option_cannot_run(self):
        status, _, err = self.check("--alow-file", "allowed.txt", self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("cannot run", err)

    def test_missing_allow_file_cannot_run(self):
        status, _, err = self.check("--allow-file", self.root / "missing.txt", self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("cannot be read", err)

    def test_empty_term_cannot_run(self):
        self.assertEqual(3, self.check("--term", " ", self.write("notes.md", "anything\n"))[0])

    def test_min_digits_below_one_cannot_run(self):
        self.assertEqual(3, self.check("--min-digits", "0", self.write("notes.md", "anything\n"))[0])

    def test_missing_file_to_check_cannot_run(self):
        status, _, err = self.check(self.root / "missing.md")
        self.assertEqual(3, status)
        self.assertIn("does not exist", err)

    def test_unexpected_failure_cannot_run_and_prints_no_detail(self):
        with mock.patch.object(copiedValues, "collect", side_effect=RuntimeError("tlf 55501000")):
            status, out, err = self.check(self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("unexpected RuntimeError", err)
        self.assertNotIn("55501000", out + err)

    @unittest.skipUnless(PERMISSIONS_ENFORCED, "file permissions do not stop this user from reading")
    def test_unreadable_private_file_cannot_run(self):
        self.unreadable(self.write("data/locked.txt", "tlf 55502222\n"))
        status, _, err = self.check(self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("1 private file(s) cannot be read", err)

    @unittest.skipUnless(PERMISSIONS_ENFORCED, "file permissions do not stop this user from reading")
    def test_unreadable_private_directory_cannot_run(self):
        self.write("data/locked/mail.txt", "tlf 55502222\n")
        self.unreadable(self.private / "locked")
        status, _, err = self.check(self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("cannot be read", err)

    @unittest.skipUnless(PERMISSIONS_ENFORCED, "file permissions do not stop this user from reading")
    def test_unreadable_file_to_check_cannot_run(self):
        locked = self.write("locked.md", "tlf 55501000\n")
        self.unreadable(locked)
        status, _, err = self.check(locked, self.write("notes.md", "anything\n"))
        self.assertEqual(3, status)
        self.assertIn("locked.md: cannot be read", err)

    def test_missing_git_cannot_run(self):
        empty = self.root / "no-tools"
        empty.mkdir()
        with mock.patch.dict(os.environ, {"PATH": str(empty)}):
            status, _, err = self.check()
        self.assertEqual(3, status)
        self.assertIn("git is not installed", err)

    # The default file list

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_without_file_arguments_git_decides_what_is_checked(self):
        self.write(".gitignore", "data/\nignored.txt\n")
        self.write("tracked.md", "tlf 55501000\n")
        self.write("new.md", "faktura 1000007\n")
        self.write("ignored.txt", "tlf 55501000\n")
        for command in (["init", "-q"], ["add", "tracked.md", ".gitignore"]):
            subprocess.run(["git", "-C", str(self.root), *command], check=True)
        result = self.run_script("--private", "data")
        self.assertEqual(1, result.returncode)
        self.assertIn("tracked.md:1: copied number of 8 digits\n", result.stdout)
        self.assertIn("new.md:1: copied number of 7 digits\n", result.stdout)
        self.assertNotIn("ignored.txt", result.stdout)

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_from_a_subdirectory_the_whole_repository_is_checked(self):
        self.write(".gitignore", "data/\n")
        self.write("docs/notes.md", "tlf 55501000\n")
        self.write("tests/test_a.py", "assert True\n")
        subprocess.run(["git", "-C", str(self.root), "init", "-q"], check=True)
        result = self.run_script("--private", "../data", cwd=self.root / "tests")
        self.assertEqual(1, result.returncode)
        self.assertEqual("docs/notes.md:1: copied number of 8 digits", result.stdout.splitlines()[0])
        self.assertIn(f"under {self.root.resolve()}", result.stdout)

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_outside_a_repository_without_file_arguments_cannot_run(self):
        env = dict(os.environ, GIT_CEILING_DIRECTORIES=str(self.root.parent))
        result = self.run_script("--private", "data", env=env)
        self.assertEqual(3, result.returncode)
        self.assertIn("git rev-parse failed", result.stderr)


if __name__ == "__main__":
    unittest.main()
