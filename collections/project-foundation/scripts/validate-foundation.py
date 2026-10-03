#!/usr/bin/env python3
"""Validate foundation structure against the bundled template; perform no I/O to targets."""

import argparse
from datetime import date
from pathlib import Path
import re

TEMPLATE = Path(__file__).resolve().parents[1] / 'templates/project-docs/foundation.md'


def cells(line):
    if not (line.startswith('|') and line.endswith('|')):
        raise ValueError('expected a table row')
    return [cell.strip() for cell in re.split(r'(?<!\\)\|', line[1:-1])]


def blocks(text):
    preamble, *sections = re.split(r'^## ', text, flags=re.MULTILINE)
    return preamble.strip(), [section.strip().splitlines() for section in sections]


def validate(text):
    errors = []
    preamble, sections = blocks(text)
    template_preamble, template_sections = blocks(TEMPLATE.read_text())
    title = template_preamble.splitlines()[0]
    match = re.fullmatch(re.escape(title) + r'\n\nDate: (\d{4}-\d{2}-\d{2}) · Revision: ([1-9]\d*)', preamble)
    if not match:
        errors.append('expected template title and Date: YYYY-MM-DD · Revision: N')
    else:
        try:
            date.fromisoformat(match[1])
        except ValueError:
            errors.append('invalid calendar date')
    expected = [section[0] for section in template_sections]
    if [section[0] if section else '' for section in sections] != expected:
        errors.append('expected sections in order: ' + ', '.join(expected))
        return errors
    for section, template in zip(sections, template_sections):
        name = section[0]
        lines = [line.strip() for line in section[1:] if line.strip()]
        shape = [line.strip() for line in template[1:] if line.strip()]
        try:
            header = cells(shape[0])
            if len(lines) < 2 or cells(lines[0]) != header:
                raise ValueError('expected columns: ' + ' | '.join(header))
            separator = cells(lines[1])
            if len(separator) != len(header) or any(not re.fullmatch(r':?-{3,}:?', cell) for cell in separator):
                raise ValueError('invalid table separator')
            seen = set()
            for line in lines[2:]:
                row = cells(line)
                if len(row) != len(header) or any(not cell for cell in row):
                    raise ValueError('wrong column count or empty cell; use Unknown or None')
                if all(re.fullmatch(r':?-{3,}:?', cell) for cell in row):
                    raise ValueError('extra table separator')
                if row[0] in seen:
                    raise ValueError('duplicate row key: ' + row[0])
                seen.add(row[0])
                if name == 'References' and not re.fullmatch(r'[a-z][a-z0-9_-]*', row[0]):
                    raise ValueError('invalid reference key: ' + row[0])
                if name == 'Inheritance' and row[0] not in expected[2:]:
                    raise ValueError('unknown inherited section: ' + row[0])
        except ValueError as error:
            errors.append(f'{name}: {error}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.files:
        try:
            errors = validate(path.read_text())
        except (OSError, UnicodeError) as error:
            errors = [str(error)]
        if errors:
            failed = True
            for error in errors:
                print(f'{path}: {error}')
        else:
            print(f'{path}: format valid')
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
