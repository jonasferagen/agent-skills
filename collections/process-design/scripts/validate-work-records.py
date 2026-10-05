#!/usr/bin/env python3
"""Check explicitly selected work records; unselected Markdown is skipped, never rewritten."""
import argparse
from pathlib import Path
import runpy
import sys

_format = runpy.run_path(str(Path(__file__).with_name('work_record_format.py')))
RecordError, parse_record, selects = _format['RecordError'], _format['parse_record'], _format['selects']


def documents(path: Path) -> list[Path]:
    """Return the Markdown files a selected path offers, without following symlinks."""
    if path.is_symlink():
        raise ValueError(f'{path}: selected paths must not be symlinks')
    if path.is_file():
        return [path]
    if not path.is_dir():
        raise ValueError(f'{path}: not a file or directory')
    found = []
    for child in sorted(path.rglob('*.md')):
        if child.is_symlink() or any(part.startswith('.') for part in child.relative_to(path).parts):
            continue
        if child.is_file():
            found.append(child)
    return found


def validate(paths: list[Path]) -> tuple[list[str], int, int]:
    errors: list[str] = []
    seen: dict[str, Path] = {}
    selected = skipped = 0
    for path in paths:
        try:
            found = documents(path)
        except ValueError as error:
            errors.append(str(error))
            continue
        for document in found:
            try:
                text = document.read_text(encoding='utf-8')
            except (OSError, UnicodeDecodeError) as error:
                errors.append(f'{document}: unreadable: {error}')
                continue
            if not selects(text):
                skipped += 1
                continue
            selected += 1
            try:
                record = parse_record(text)
            except RecordError as error:
                errors.append(f'{document}: {error}')
                continue
            identifier = record['identifier']
            if identifier in seen:
                errors.append(f'{document}: duplicate record identifier {identifier!r}, '
                              f'already used by {seen[identifier]}')
                continue
            seen[identifier] = document
    return errors, selected, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='+', type=Path, help='Markdown files or directories to check')
    arguments = parser.parse_args()
    errors, selected, skipped = validate(arguments.paths)
    for error in errors:
        print(error, file=sys.stderr)
    print(f'Checked {selected} selected work record(s); skipped {skipped} unselected document(s); '
          f'{len(errors)} problem(s)')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
