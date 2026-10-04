#!/usr/bin/env python3
"""Check the reserved project-document layout, not its semantic ownership."""
import argparse
from pathlib import Path
import re

HOMES = Path(__file__).resolve().parents[1] / 'references/document-homes.md'
HOME = re.compile(r'^\|[^|\n]+\| `project-docs/([^`]+)` \|', re.MULTILINE)
TOPIC_NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md\Z')
PROCESS_NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def managed_homes():
    """Read file and topic-directory patterns from the document-homes map."""
    files, topic_dirs = set(), set()
    for home in HOME.findall(HOMES.read_text(encoding='utf-8')):
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
    # Only the explicitly mapped <process>/README.md family permits named
    # directories. Expand one direct level, never an arbitrary directory glob.
    process_patterns = {Path(name).parent.as_posix() for name in files
                        if Path(name).name == 'README.md' and Path(name).parent.name == '<process>'}
    process_parents = {Path(pattern).parent.as_posix() for pattern in process_patterns}
    process_dirs = set()
    for parent in sorted(process_parents):
        directory = root / parent
        if not directory.is_dir() or directory.is_symlink():
            continue
        for child in directory.iterdir():
            if child.is_dir() and not child.is_symlink() and PROCESS_NAME.fullmatch(child.name):
                process_dirs.add(child.relative_to(root).as_posix())
    for pattern in process_patterns:
        files.remove(f'{pattern}/README.md')
        has_topics = pattern in topic_dirs
        topic_dirs.discard(pattern)
        for directory in process_dirs:
            if Path(directory).parent == Path(pattern).parent:
                files.add(f'{directory}/README.md')
                if has_topics:
                    topic_dirs.add(directory)
    directories = (topic_dirs | process_parents | process_dirs
                   | {Path(name).parent.as_posix() for name in files}) - {'.'}
    errors = []
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f'{relative}: managed documents must live in this directory, not behind symlinks')
        elif path.is_dir():
            if relative.as_posix() not in directories:
                if relative.parent.as_posix() in process_parents:
                    errors.append(f'{relative}: expected a lowercase hyphenated process directory name')
                else:
                    errors.append(f'{relative}: unrecognized managed document directory')
        elif relative.as_posix() in files:
            continue
        elif relative.parent.as_posix() in topic_dirs:
            if TOPIC_NAME.fullmatch(relative.name):
                continue
            errors.append(f'{relative}: expected a lowercase hyphenated Markdown topic name')
        else:
            errors.append(f'{relative}: no managed document type owns this path')
    for directory in sorted(process_dirs):
        if not (root / directory / 'README.md').is_file():
            errors.append(f'{directory}/README.md: named process directory needs this entry')
        legacy = root / f'{directory}.md'
        if legacy.is_file():
            errors.append(f'{directory}.md: ambiguous process owner; keep either this flat page or {directory}/README.md')
    # Mapped parent indexes cover descendant topics and named processes, even
    # when there are no direct topics. A process entry is required even if empty.
    for index in sorted(files):
        directory = root / Path(index).parent
        parent = Path(index).parent.as_posix()
        if parent in process_dirs:
            continue
        if parent in topic_dirs | process_parents and directory.is_dir() and not (root / index).is_file():
            if any(p.is_file() or p.relative_to(root).as_posix() in process_dirs for p in directory.rglob('*')):
                errors.append(f'{index}: documents in {directory.name}/ need this index')
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
