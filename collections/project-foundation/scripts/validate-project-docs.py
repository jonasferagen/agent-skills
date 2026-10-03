#!/usr/bin/env python3
"""Check the reserved project-document layout, not its semantic ownership."""
import argparse
from pathlib import Path
import re

ROOT_FILES = {'foundation.md', 'working-agreements.md'}
TOPIC_DIRS = {'planning', 'decisions', 'records'}
TOPIC_NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md\Z')


def validate(root: Path) -> list[str]:
    if root.is_symlink():
        return [f'{root}: managed document root must not be a symlink']
    if not root.is_dir():
        return [f'{root}: managed document directory is missing']
    errors = []
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        parts = relative.parts
        if path.is_symlink():
            errors.append(f'{relative}: managed documents must live in this directory, not behind symlinks')
        elif path.is_dir():
            if len(parts) != 1 or parts[0] not in TOPIC_DIRS:
                errors.append(f'{relative}: unrecognized managed document directory')
        elif len(parts) == 1 and parts[0] in ROOT_FILES:
            continue
        elif len(parts) == 2 and parts[0] in TOPIC_DIRS:
            if parts == ('planning', 'README.md') or TOPIC_NAME.fullmatch(parts[1]):
                continue
            errors.append(f'{relative}: expected a lowercase hyphenated Markdown topic name')
        else:
            errors.append(f'{relative}: no managed document type owns this path')
    planning = root / 'planning'
    if planning.is_dir() and any(p.is_file() for p in planning.iterdir()):
        if not (planning / 'README.md').is_file():
            errors.append('planning/README.md: detailed plans need an active plan index')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(error)
    if not errors:
        print(f'Validated managed document paths: {args.root}')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
