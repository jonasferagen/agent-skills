#!/usr/bin/env python3
"""Find values copied from private data into files that are tracked or about to be.

    copiedValues.py --private PATH [--private PATH ...] [--allow VALUE] [--allow-file FILE]
                    [--term TEXT] [--term-file FILE] [--min-digits N] [FILE ...]

Numbers of six or more digits and mail addresses are collected from every file
under each private path. A number made of one repeated digit identifies nothing
and is left out. Each checked file is then searched for them, for numbers that
share seven or more digits in a row with a private number because one contains
the other, and for each listed term, such as a name. An allowed value is never
reported.

Without FILE arguments the check covers every file Git tracks in the current
repository, from its top, plus untracked files that are not ignored. Files are
read as UTF-8, or byte for byte where they are not UTF-8, so text in another
encoding or inside a database file is seen. A number stored in binary, such as
a SQLite integer, is not.

A finding names the file, the line and the kind of value. The value itself is
never printed.

Exit status:
  0  no copied value found
  1  copied values found
  2  the private data is absent: none of the --private paths exists
  3  the check cannot run: a bad argument, a --private path missing while
     another exists, nothing to look for, nothing to check, an unreadable file,
     a Git error or any other failure

Only status 0 is a pass. A test that runs this check should find the private
data absent itself before it skips, and fail on any other non-zero status.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

EMAIL = re.compile(r"(?<![A-Za-z0-9._%+-])[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
REPEATED_DIGIT = re.compile(r"([0-9])\1*")
ABSENT, CANNOT_RUN = 2, 3


class CannotRun(Exception):
    """The check cannot give a verdict. The message says why and holds no private value."""


class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        raise CannotRun(message)


def number_pattern(min_digits):
    return re.compile(r"(?<![0-9])[0-9]{%d,}(?![0-9])" % min_digits)


def read_text(path):
    """The file as UTF-8, or byte for byte where its bytes are not UTF-8."""
    data = Path(path).read_bytes()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1")


def raise_error(error):
    raise error


def files_under(path):
    """Every file under path, following links to directories and visiting each directory once."""
    if not path.is_dir():
        yield path
        return
    seen = set()
    for directory, subdirectories, names in os.walk(path, followlinks=True, onerror=raise_error):
        status = os.stat(directory)
        if (status.st_dev, status.st_ino) in seen:
            subdirectories[:] = []
            continue
        seen.add((status.st_dev, status.st_ino))
        subdirectories.sort()
        for name in sorted(names):
            yield Path(directory, name)


def collect(roots, numbers):
    """Return (numbers, mail addresses, files read) found under the private roots."""
    found_numbers, found_addresses, read, unreadable = set(), set(), 0, 0
    for root in roots:
        try:
            for path in files_under(root):
                if not path.is_file():
                    continue  # a broken link, a pipe or a socket holds no data to read
                try:
                    text = read_text(path)
                except OSError:
                    unreadable += 1
                    continue
                read += 1
                found_numbers.update(n for n in numbers.findall(text) if not REPEATED_DIGIT.fullmatch(n))
                found_addresses.update(a.casefold() for a in EMAIL.findall(text))
        except OSError:
            raise CannotRun(f"a directory under {root} cannot be read") from None
    if unreadable:
        raise CannotRun(f"{unreadable} private file(s) cannot be read")
    if not read:
        raise CannotRun(f"no file under {', '.join(map(str, roots))} can be read")
    return found_numbers, found_addresses, read


def git(arguments, directory):
    try:
        result = subprocess.run(["git", *arguments], cwd=directory, capture_output=True)
    except FileNotFoundError:
        raise CannotRun("git is not installed; name the files to check") from None
    if result.returncode:
        reason = result.stderr.decode("utf-8", "replace").strip().splitlines()
        raise CannotRun(f"git {arguments[0]} failed: {reason[0] if reason else result.returncode}")
    return result.stdout


def git_files(directory):
    """The repository's top, and the files Git tracks there plus untracked files that are not ignored."""
    root = Path(os.fsdecode(git(["rev-parse", "--show-toplevel"], directory).strip()))
    listing = git(["ls-files", "-co", "--exclude-standard", "-z"], root)
    return root, [root / os.fsdecode(name) for name in listing.split(b"\0") if name]


def shown(path, root=None):
    """The path relative to root, or to the current directory when it lies inside it."""
    try:
        return Path(os.path.abspath(path)).relative_to(os.path.abspath(root or Path.cwd()))
    except ValueError:
        return path


def inside(path, parents):
    resolved = path.resolve()
    return any(resolved == parent or parent in resolved.parents for parent in parents)


def partly_copied(value, private_numbers, shared=7):
    """True when value and a private number overlap by containment over at least `shared` digits."""
    return any(min(len(value), len(private)) >= shared and (value in private or private in value)
               for private in private_numbers)


def term_pattern(term):
    return re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)


def findings(text, private_numbers, private_addresses, allowed, terms, numbers):
    """Yield (line number, kind) for each copied value in text."""
    for line_number, line in enumerate(text.split("\n"), 1):
        for value in numbers.findall(line):
            if value in allowed or REPEATED_DIGIT.fullmatch(value):
                continue
            if value in private_numbers:
                yield line_number, f"number of {len(value)} digits"
            elif partly_copied(value, private_numbers):
                yield line_number, f"number of {len(value)} digits, part of a private number or containing one"
        for value in EMAIL.findall(line):
            if value.casefold() in private_addresses:
                yield line_number, "mail address"
        for term in terms:
            if term.search(line):
                yield line_number, "listed term"


def listed(path, option):
    """The values in a file of one value per line, where # starts a comment."""
    try:
        text = read_text(path)
    except OSError:
        raise CannotRun(f"{option} {path} cannot be read") from None
    return [line.split("#")[0].strip() for line in text.split("\n") if line.split("#")[0].strip()]


def check(argv):
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--private", action="append", required=True, type=Path,
                        help="file or directory that holds the private data; repeatable")
    parser.add_argument("--allow", action="append", default=[],
                        help="a value from the private data that may appear in checked files; repeatable")
    parser.add_argument("--allow-file", type=Path, help="file with one allowed value per line; # starts a comment")
    parser.add_argument("--term", action="append", default=[], help="a name or other text to look for; repeatable")
    parser.add_argument("--term-file", type=Path,
                        help="file with one term per line, # starts a comment; keep it with the private data")
    parser.add_argument("--min-digits", type=int, default=6, help="shortest number that counts (default 6)")
    parser.add_argument("files", nargs="*", type=Path, help="files to check; default: what Git tracks or would track")
    args = parser.parse_args(argv)

    if args.min_digits < 1:
        raise CannotRun("--min-digits must be at least 1")
    allowed = set(args.allow) | set(listed(args.allow_file, "--allow-file") if args.allow_file else [])
    terms = args.term + (listed(args.term_file, "--term-file") if args.term_file else [])
    if any(not term.strip() for term in terms):
        raise CannotRun("a --term is empty")
    patterns = [term_pattern(term.strip()) for term in terms]

    missing = [path for path in args.private if not path.exists()]
    if len(missing) == len(args.private):
        print(f"private data absent: nothing at {', '.join(map(str, missing))}, so nothing was checked",
              file=sys.stderr)
        return ABSENT
    if missing:
        raise CannotRun(f"--private {missing[0]} does not exist, although other private paths do")
    numbers = number_pattern(args.min_digits)
    private_numbers, private_addresses, read = collect(args.private, numbers)
    private_numbers -= allowed
    private_addresses -= {value.casefold() for value in allowed}
    if not (private_numbers or private_addresses or patterns):
        raise CannotRun(f"nothing to look for: the private data holds no number of {args.min_digits} or more "
                        "digits and no mail address that is not allowed, and no term was given")

    if args.files:
        absent = [path for path in args.files if not path.exists()]
        if absent:
            raise CannotRun(f"{absent[0]} does not exist")
        try:
            root, candidates = None, [path for given in args.files for path in files_under(given)]
        except OSError:
            raise CannotRun("a directory among the files to check cannot be read") from None
    else:
        root, candidates = git_files(Path.cwd())
    private_roots = [path.resolve() for path in args.private]
    checked = copied = 0
    unreadable = []
    for path in candidates:
        if inside(path, private_roots):
            continue
        if not path.is_file():
            continue  # deleted from the work tree, a broken link or a link to a directory
        try:
            text = read_text(path)
        except OSError:
            unreadable.append(shown(path, root))
            continue
        checked += 1
        for line_number, kind in findings(text, private_numbers, private_addresses, allowed, patterns, numbers):
            copied += 1
            print(f"{shown(path, root)}:{line_number}: copied {kind}")
    for path in unreadable:
        print(f"{path}: cannot be read", file=sys.stderr)
    if not checked and not unreadable:
        raise CannotRun("no file to check")
    where = f" under {root}" if root else ""
    print(f"{copied} copied value(s) in {checked} file(s) checked{where}, against {len(private_numbers)} numbers, "
          f"{len(private_addresses)} mail addresses and {len(patterns)} terms from {read} private file(s)")
    if copied:
        return 1
    if unreadable:
        raise CannotRun(f"{len(unreadable)} file(s) to check cannot be read")
    return 0


def main(argv=None):
    try:
        return check(argv)
    except CannotRun as error:
        print(f"cannot run: {error}", file=sys.stderr)
    except Exception as error:  # the reporting boundary: no failure may read as a pass or as a finding
        print(f"cannot run: unexpected {type(error).__name__}", file=sys.stderr)
    return CANNOT_RUN


if __name__ == "__main__":
    raise SystemExit(main())
