#!/usr/bin/env python3
"""Compare the few shared contracts whose package-local copies must agree."""

import argparse
import ast
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TS_OWNER = Path('skills/languages/typescript-patterns/references/imports.md')
TS_COPY = Path('skills/languages/typescript-design/references/imports-and-barrels.md')
REPORT_OWNER = Path('skills/operations/runtime-operations/scripts/serviceReport.py')
REPORT_COPY = Path('skills/operations/repository-services/templates/services/control')
REPORT_GUIDE = Path('skills/operations/repository-services/references/convention.md')


class SharedContracts:
    @staticmethod
    def section(text: str, heading: str) -> str:
        matches = list(re.finditer(r'^## ' + re.escape(heading) + r'\s*$', text, re.M))
        if len(matches) != 1:
            raise ValueError(f'expected one section named {heading!r}')
        body = re.split(r'^## ', text[matches[0].end():], maxsplit=1, flags=re.M)[0].strip()
        if not body:
            raise ValueError(f'empty section {heading!r}')
        return body


    @staticmethod
    def constants(text: str, names: tuple[str, ...], owner: str | None = None) -> dict:
        tree = ast.parse(text)
        body = tree.body
        if owner:
            classes = [node for node in body if isinstance(node, ast.ClassDef) and node.name == owner]
            if len(classes) != 1:
                raise ValueError(f'expected one class named {owner}')
            body = classes[0].body
        result = {}
        for node in body:
            if not isinstance(node, ast.Assign):
                continue
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in names:
                    if target.id in result:
                        raise ValueError(f'duplicate declaration {target.id}')
                    result[target.id] = ast.literal_eval(node.value)
        if set(result) != set(names):
            raise ValueError(f'missing declarations: {sorted(set(names) - set(result))}')
        for name, value in result.items():
            if name == 'SCHEMA':
                if not isinstance(value, str) or not value:
                    raise ValueError('SCHEMA must be a nonempty string')
            elif (not isinstance(value, tuple) or not value
                  or any(not isinstance(item, str) or not item for item in value)
                  or len(set(value)) != len(value)):
                raise ValueError(f'{name} must be a nonempty tuple of unique strings')
        return result


    @staticmethod
    def table_vocabulary(text: str, heading: str) -> tuple[str, ...]:
        lines = text.splitlines()
        starts = [index for index, line in enumerate(lines) if line == heading]
        if len(starts) != 1:
            raise ValueError(f'expected one vocabulary table {heading!r}')
        values = []
        for line in lines[starts[0] + 2:]:
            if not line.startswith('|'):
                break
            match = re.match(r'^\| `([^`]+)` \|', line)
            if not match:
                raise ValueError(f'malformed vocabulary row: {line}')
            values.append(match[1])
        if not values or len(set(values)) != len(values):
            raise ValueError('vocabulary table must contain unique values')
        return tuple(values)


    @staticmethod
    def check(root: Path) -> tuple[int, list[str]]:
        errors = []
        compared = 0

        def read(path):
            return (root / path).read_text(encoding='utf-8')

        def compare(label, owner, copy):
            nonlocal compared
            compared += 1
            if owner != copy:
                errors.append(f'{label}: copy disagrees with its authoritative owner')

        try:
            compare(f'{TS_COPY} (module syntax; owner {TS_OWNER})',
                    SharedContracts.section(read(TS_OWNER), 'Module And Path Syntax'),
                    SharedContracts.section(read(TS_COPY), 'Module And Path Syntax'))
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f'TypeScript module syntax could not be compared: {error}')

        try:
            owner = SharedContracts.constants(read(REPORT_OWNER), ('SCHEMA', 'STATES', 'LIFECYCLES'), 'ServiceReport')
            copy = SharedContracts.constants(read(REPORT_COPY), ('SCHEMA', 'STATES'))
            compare(f'{REPORT_COPY} (SCHEMA; owner {REPORT_OWNER})', owner['SCHEMA'], copy['SCHEMA'])
            compare(f'{REPORT_COPY} (STATES; owner {REPORT_OWNER})', set(owner['STATES']), set(copy['STATES']))
            guide = read(REPORT_GUIDE)
            schemas = set(re.findall(r'`(service-report/v[0-9]+)`', guide))
            compare(f'{REPORT_GUIDE} (schema)', {owner['SCHEMA']}, schemas)
            compare(f'{REPORT_GUIDE} (states)', set(owner['STATES']),
                    set(SharedContracts.table_vocabulary(guide, '| State | Meaning |')))
            compare(f'{REPORT_GUIDE} (lifecycles)', set(owner['LIFECYCLES']),
                    set(SharedContracts.table_vocabulary(guide, '| `lifecycle` | What it is | A project-wide launch |')))
        except (OSError, UnicodeError, ValueError, SyntaxError) as error:
            errors.append(f'Service report contract could not be compared: {error}')
        return compared, errors


def main() -> int:
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT,
                        help='authoring checkout to compare; defaults to this script\'s checkout')
    args = parser.parse_args()
    root = args.root.resolve()
    compared, errors = SharedContracts.check(root)
    for error in errors:
        print(error, file=sys.stderr)
    print(f'{compared} shared-contract comparisons at {root}; {len(errors)} findings')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
