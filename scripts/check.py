#!/usr/bin/env python3
"""Run package checks and every maintained helper/example suite without silent skips."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


def test_directories(root: Path) -> list[Path]:
    return sorted({file.parent for owner in ('scripts', 'collections')
                   for file in (root / owner).rglob('test_*.py')
                   if not {'.worktrees', '__pycache__'} & set(file.relative_to(root).parts)})


def run_suite(directory: Path) -> int:
    suite = unittest.defaultTestLoader.discover(str(directory), pattern='test_*.py')
    if not suite.countTestCases():
        print(f'No tests found in {directory}', file=sys.stderr)
        return 1
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return int(not result.wasSuccessful() or bool(result.skipped))


def prerequisites(root: Path) -> list[str]:
    errors = []
    if sys.version_info < (3, 11):
        errors.append('Python 3.11 or later is required for source checks')
    for executable in ('node', 'gpg'):
        if not shutil.which(executable):
            errors.append(f'{executable} is required; install it before running checks')
    compiler = root / 'node_modules/typescript/bin/tsc'
    if not compiler.is_file():
        errors.append('TypeScript is required; run npm ci in the source repository')
    else:
        expected = json.loads((root / 'package.json').read_text(encoding='utf-8'))['devDependencies']['typescript']
        actual = json.loads((compiler.parents[1] / 'package.json').read_text(encoding='utf-8'))['version']
        if actual != expected:
            errors.append(f'TypeScript {expected} is required; found {actual}; run npm ci')
    if shutil.which('node'):
        version = subprocess.run(['node', '--version'], stdin=subprocess.DEVNULL,
                                 capture_output=True, text=True, encoding='utf-8', check=True, timeout=10)
        if int(version.stdout.strip().removeprefix('v').split('.')[0]) != 24:
            errors.append(f'Node 24 is required for the retained example checks; found {version.stdout.strip()}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.suite is not None:
        return run_suite(args.suite)
    errors = prerequisites(ROOT)
    directories = test_directories(ROOT)
    if not directories:
        errors.append('No maintained test suites found')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    commands = [[sys.executable, str(ROOT / 'scripts/validate-packages.py')]]
    commands.extend([sys.executable, str(Path(__file__).resolve()), '--suite', str(directory)]
                    for directory in directories)
    failures = 0
    for command in commands:
        print(f'Checking {command[-1]}', flush=True)
        try:
            result = subprocess.run(command, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=180,
                                    env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONIOENCODING': 'utf-8'})
            failures += result.returncode != 0
        except (OSError, subprocess.TimeoutExpired) as error:
            print(f'Check did not complete: {error}', file=sys.stderr)
            failures += 1
    print(f'{len(commands)} checks completed; {failures} failed')
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
