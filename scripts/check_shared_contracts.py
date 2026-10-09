#!/usr/bin/env python3
"""Compare the few shared contracts whose package-local copies must agree."""

import argparse
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TS_OWNER = Path('skills/languages/typescript-patterns/references/imports.md')
TS_COPY = Path('skills/languages/typescript-design/references/imports-and-barrels.md')


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
