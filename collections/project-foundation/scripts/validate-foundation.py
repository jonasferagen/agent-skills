#!/usr/bin/env python3
"""Validate foundation structure against the bundled template; perform no I/O to targets."""

import argparse
from datetime import date
import os
from pathlib import Path
import re
from urllib.parse import urlsplit

TEMPLATE = Path(__file__).resolve().parents[1] / 'templates/project-docs/foundation.md'
SYMBOL = re.compile(r'`\$([^/#`\s]*)')
AUTHORITY = re.compile(r'`\$([a-z][a-z0-9_-]*)/([^`#\s]+)#([^`\s]+)`')


def cells(line):
    if not (line.startswith('|') and line.endswith('|')):
        raise ValueError('expected a table row')
    return [cell.strip() for cell in re.split(r'(?<!\\)\|', line[1:-1])]


def blocks(text):
    preamble, *sections = re.split(r'^## ', text, flags=re.MULTILINE)
    return preamble.strip(), [section.strip().splitlines() for section in sections]


def validate(text, path=None):
    errors = []
    tables = {}
    preamble, sections = blocks(text)
    template_preamble, template_sections = blocks(TEMPLATE.read_text(encoding='utf-8'))
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
            rows = []
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
                rows.append(row)
            tables[name] = rows
        except ValueError as error:
            errors.append(f'{name}: {error}')
    if 'References' in tables:
        errors.extend(check_references(tables, path))
    return errors


def check_references(tables, path):
    """Check symbolic references against this file's own bindings, without reading targets."""
    errors = []
    targets = dict(tables['References'])
    for name, rows in tables.items():
        for key in sorted({key for row in rows for key in SYMBOL.findall(' | '.join(row[1:]))}):
            if key not in targets:
                errors.append(f'{name}: undeclared reference key: ${key}')
    for section, authority in tables.get('Inheritance', []):
        match = AUTHORITY.fullmatch(authority)
        if authority == 'Unknown':
            continue
        if not match:
            errors.append(f'Inheritance: {section} authority must be one `$key/path#anchor` reference or Unknown')
        elif path is not None and match[1] in targets and inherits_from_itself(path, targets[match[1]], match[2]):
            errors.append(f'Inheritance: {section} inherits from its own foundation')
    return errors


def inherits_from_itself(path, target, suffix):
    """Compare paths lexically; a target is resolved against the declaring file's directory."""
    if urlsplit(target).scheme:
        return False
    own = os.path.normpath(Path(path).absolute())
    return own == os.path.normpath((Path(path).parent / target / suffix).absolute())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.files:
        try:
            errors = validate(path.read_text(encoding='utf-8'), path)
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
