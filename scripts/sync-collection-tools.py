#!/usr/bin/env python3
"""Distribute the canonical checker after reviewed source changes; never bless drift."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = (root / 'scripts/collection_installation.py').read_bytes()
for manifest in sorted((root / 'collections').glob('*/collection.json')):
    target = manifest.parent / 'scripts/check_installation.py'
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(source)
    print(f'Synchronized {manifest.parent.name} checker')
