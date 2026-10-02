#!/usr/bin/env python3
"""Find values copied from private data into files that are tracked or about to be.

    copiedValues.py --private PATH [--private PATH ...] [FILE ...]

Numbers of six or more digits and mail addresses are collected from the private
data. Each checked file is then searched for them, and for numbers that share
seven or more digits in a row with a private number because one contains the
other. Without FILE arguments the check covers the files Git tracks plus
untracked files that are not ignored.
A finding names the file, the line and the kind of value. The value itself is
never printed.

Exit status: 0 nothing copied; 1 copied values found; 2 the check could not
run, for example because the private data is absent. Status 2 is not a pass.

Names and free text are not detected. Pass known ones with --term.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

EMAIL = re.compile(r"[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")


def number_pattern(min_digits):
    return re.compile(r"(?<!\d)\d{%d,}(?!\d)" % min_digits)


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def files_under(paths):
    for path in paths:
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from sorted(p for p in path.rglob("*") if p.is_file())


def collect(private, numbers, allowed):
    """Return ({number: kind}, {address: kind}, files read) for the private data."""
    found_numbers, found_addresses, read = set(), set(), 0
    for path in files_under(private):
        text = read_text(path)
        if text is None:
            continue
        read += 1
        found_numbers.update(numbers.findall(text))
        found_addresses.update(a.casefold() for a in EMAIL.findall(text))
    return found_numbers - allowed, found_addresses - {a.casefold() for a in allowed}, read


def git_files(root):
    result = subprocess.run(["git", "-C", str(root), "ls-files", "-co", "--exclude-standard", "-z"],
                            capture_output=True)
    if result.returncode:
        return None
    return [root / name for name in result.stdout.decode("utf-8", "surrogateescape").split("\0") if name]


def shown(path):
    """The path as given, or relative to the current directory when it lies inside it."""
    try:
        return path.resolve().relative_to(Path.cwd().resolve())
    except ValueError:
        return path


def inside(path, parents):
    resolved = path.resolve()
    return any(resolved == parent or parent in resolved.parents for parent in parents)


def partly_copied(value, private_numbers, shared=7):
    """True when value and a private number overlap by containment over at least `shared` digits."""
    return any(min(len(value), len(private)) >= shared and (value in private or private in value)
               for private in private_numbers)


def findings(path, text, private_numbers, private_addresses, terms, numbers):
    for line_number, line in enumerate(text.splitlines(), 1):
        for value in numbers.findall(line):
            if value in private_numbers:
                yield line_number, f"number of {len(value)} digits"
            elif partly_copied(value, private_numbers):
                yield line_number, f"number of {len(value)} digits, part of a private number or containing one"
        for value in EMAIL.findall(line):
            if value.casefold() in private_addresses:
                yield line_number, "mail address"
        for term in terms:
            if re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", line, re.IGNORECASE):
                yield line_number, "listed term"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--private", action="append", required=True, type=Path,
                        help="file or directory that holds the private data; repeatable")
    parser.add_argument("--min-digits", type=int, default=6, help="shortest number that counts (default 6)")
    parser.add_argument("--term", action="append", default=[], help="a name or other text to look for; repeatable")
    parser.add_argument("--allow", action="append", default=[],
                        help="a value from the private data that may appear in checked files; repeatable")
    parser.add_argument("--allow-file", type=Path, help="file with one allowed value per line; # starts a comment")
    parser.add_argument("files", nargs="*", type=Path, help="files to check; default: what Git tracks or would track")
    args = parser.parse_args(argv)

    allowed = set(args.allow)
    if args.allow_file:
        text = read_text(args.allow_file)
        if text is None:
            print(f"cannot run: allow file {args.allow_file} is not readable", file=sys.stderr)
            return 2
        allowed.update(line.split("#")[0].strip() for line in text.splitlines() if line.split("#")[0].strip())

    numbers = number_pattern(args.min_digits)
    private_numbers, private_addresses, read = collect(args.private, numbers, allowed)
    if not read:
        print(f"cannot run: no readable private data at {', '.join(map(str, args.private))}", file=sys.stderr)
        return 2

    if args.files:
        candidates = list(files_under(args.files))
    else:
        candidates = git_files(Path.cwd())
        if candidates is None:
            print("cannot run: not a Git repository; name the files to check", file=sys.stderr)
            return 2
    private_roots = [p.resolve() for p in args.private]
    checked = copied = 0
    for path in candidates:
        if inside(path, private_roots):
            continue
        text = read_text(path)
        if text is None:
            continue
        checked += 1
        for line_number, kind in findings(path, text, private_numbers, private_addresses, args.term, numbers):
            copied += 1
            print(f"{shown(path)}:{line_number}: copied {kind}")
    if not checked:
        print("cannot run: no readable files to check", file=sys.stderr)
        return 2
    print(f"{copied} copied value(s) in {checked} file(s) checked, against "
          f"{len(private_numbers)} numbers and {len(private_addresses)} mail addresses from {read} private file(s)")
    return 1 if copied else 0


if __name__ == "__main__":
    raise SystemExit(main())
