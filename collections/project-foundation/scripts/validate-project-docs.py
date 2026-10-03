#!/usr/bin/env python3
"""Check the reserved project-document layout, not its semantic ownership."""
import argparse
from pathlib import Path
import re

HOMES = Path(__file__).resolve().parents[1] / 'references/document-homes.md'
HOME = re.compile(r'^\|[^|\n]+\| `project-docs/([^`]+)` \|', re.MULTILINE)
TOPIC_NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md\Z')


def managed_homes():
    """Read fixed files and topic directories from the document-homes map."""
    files, topic_dirs = set(), set()
    for home in HOME.findall(HOMES.read_text()):
        directory, _, name = home.rpartition('/')
        if name == '<topic>.md':
            topic_dirs.add(directory)
        else:
            files.add(home)
    return files, topic_dirs


def validate(root: Path) -> list[str]:
    if root.is_symlink():
        return [f'{root}: managed document root must not be a symlink']
    if not root.is_dir():
        return [f'{root}: managed document directory is missing']
    files, topic_dirs = managed_homes()
    if not files and not topic_dirs:
        return [f'{HOMES}: no managed homes found in its document type table']
    directories = topic_dirs | {str(Path(name).parent) for name in files} - {'.'}
    errors = []
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f'{relative}: managed documents must live in this directory, not behind symlinks')
        elif path.is_dir():
            if relative.as_posix() not in directories:
                errors.append(f'{relative}: unrecognized managed document directory')
        elif relative.as_posix() in files:
            continue
        elif relative.parent.as_posix() in topic_dirs:
            if TOPIC_NAME.fullmatch(relative.name):
                continue
            errors.append(f'{relative}: expected a lowercase hyphenated Markdown topic name')
        else:
            errors.append(f'{relative}: no managed document type owns this path')
    # A mapped file inside a topic directory is that directory's index; its topics link from it.
    for index in sorted(files):
        directory = root / Path(index).parent
        if Path(index).parent.as_posix() in topic_dirs and directory.is_dir() and not (root / index).is_file():
            if any(p.is_file() for p in directory.iterdir()):
                errors.append(f'{index}: topic documents in {directory.name}/ need this index')
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
