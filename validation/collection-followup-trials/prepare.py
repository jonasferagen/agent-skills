#!/usr/bin/env python3
"""Prepare fresh consumer inputs with complete installations in a new directory."""

import argparse
from pathlib import Path
import shutil


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path, help='new directory outside the source repository')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[2]
    destination = args.destination.resolve()
    if destination.is_relative_to(source):
        parser.error('Consumer trials must be outside the authoring repository')
    destination.mkdir(parents=True, exist_ok=False)
    for fixture in sorted((Path(__file__).parent / 'fixtures').iterdir()):
        target = destination / fixture.name
        shutil.copytree(fixture, target)
        shutil.copytree(source / 'collections', target / '.agents/collections',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '*.pyo'))
    print(destination)


if __name__ == '__main__':
    main()
