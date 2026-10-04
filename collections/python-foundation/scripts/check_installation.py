#!/usr/bin/env python3
"""Check a complete collection against its selected source inventory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

SOURCE = Path(__file__).resolve().parents[1]


def inventory(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if '__pycache__' in relative.parts or path.suffix in ('.pyc', '.pyo'):
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink is not a collection file: {relative}')
        if path.is_file() and relative.as_posix() != 'collection.json':
            result[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def metadata(root: Path) -> dict:
    data = json.loads((root / 'collection.json').read_text())
    if not isinstance(data, dict) or set(data) != {'name', 'version', 'members', 'files'}:
        raise ValueError('Invalid collection manifest fields')
    members = data['members']
    if (not isinstance(data['name'], str) or not re.fullmatch(r'[a-z][a-z0-9-]*', data['name']) or not isinstance(members, list)
            or not members or any(not isinstance(name, str) or not re.fullmatch(r'[a-z][a-z0-9-]*', name) for name in members)
            or len(set(members)) != len(members)):
        raise ValueError('Invalid or empty collection membership')
    if not isinstance(data['files'], dict):
        raise ValueError('Invalid file inventory')
    entry = (root / 'COLLECTION.md').read_text()
    if f"Version: {data['version']}\n" not in entry:
        raise ValueError('Collection version differs from entrypoint')
    actual = {p.parent.name for p in (root / 'skills').glob('*/SKILL.md')}
    if actual != set(members):
        raise ValueError(f'Membership mismatch: expected {sorted(members)}, found {sorted(actual)}')
    for name in members:
        if f'skills/{name}/SKILL.md' not in entry:
            raise ValueError(f'Entrypoint does not route to {name}')
    return data


def check(root: Path, source: Path = SOURCE) -> int:
    expected = metadata(source)
    actual = metadata(root)
    if actual != expected:
        raise ValueError('Installed manifest differs from the selected source')
    if not expected['files']:
        raise ValueError('Empty file inventory cannot establish an installation')
    files = inventory(root)
    missing = set(expected['files']) - set(files)
    extra = set(files) - set(expected['files'])
    changed = {name for name in files.keys() & expected['files'].keys()
               if files[name] != expected['files'][name]}
    if missing or extra or changed:
        raise ValueError(f'Installation drift: missing={sorted(missing)}, extra={sorted(extra)}, changed={sorted(changed)}')
    return len(files)


def write(root: Path) -> None:
    data = metadata(root)
    data['files'] = inventory(root)
    if not data['files']:
        raise ValueError('Refusing an empty inventory')
    (root / 'collection.json').write_text(json.dumps(data, indent=2) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=SOURCE)
    parser.add_argument('--write', action='store_true', help='regenerate source inventory after reviewed authoring edits')
    args = parser.parse_args()
    try:
        if args.write:
            if args.root.resolve() != SOURCE:
                raise ValueError('--write only operates on this checker\'s source collection')
            write(SOURCE)
        count = check(args.root)
        print(f'Validated {metadata(args.root)["name"]}: {count} files and {len(metadata(args.root)["members"])} declared members')
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
