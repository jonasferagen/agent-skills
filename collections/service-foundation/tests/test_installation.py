"""Synthetic staged collections exercise installation drift and membership failures."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_installation.py'
spec = importlib.util.spec_from_file_location('collection_check', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.source = Path(temporary.name) / 'source'
        self.source.mkdir()
        self.names = ['example-first', 'example-second']
        for name in self.names:
            package = self.source / 'skills' / name
            package.mkdir(parents=True)
            (package / 'SKILL.md').write_text(f'# {name}\n')
        (self.source / 'COLLECTION.md').write_text('Version: 0.1.0\n' + '\n'.join(
            f'[Member](skills/{name}/SKILL.md)' for name in self.names))
        (self.source / 'collection.json').write_text(json.dumps({
            'name': 'service-foundation', 'version': '0.1.0', 'members': self.names, 'files': {}}))
        checker.write(self.source)
        self.target = Path(temporary.name) / 'installed'
        shutil.copytree(self.source, self.target)

    def test_complete_copy_passes_and_bytecode_is_ignored(self):
        cache = self.target / '__pycache__'
        cache.mkdir()
        (cache / 'example.pyc').write_bytes(b'generated')
        self.assertEqual(checker.check(self.target, self.source), 3)

    def test_missing_member_is_rejected(self):
        shutil.rmtree(self.target / 'skills/example-first')
        with self.assertRaisesRegex(ValueError, 'Membership mismatch'):
            checker.check(self.target, self.source)

    def test_changed_file_is_rejected(self):
        (self.target / 'skills/example-first/SKILL.md').write_text('Edited locally')
        with self.assertRaisesRegex(ValueError, 'changed='):
            checker.check(self.target, self.source)

    def test_retired_file_left_by_overlay_is_rejected(self):
        (self.target / 'retired.md').write_text('Left by overlay')
        with self.assertRaisesRegex(ValueError, 'extra='):
            checker.check(self.target, self.source)

    def test_consumer_cannot_bless_drift_by_regenerating_manifest(self):
        (self.target / 'skills/example-first/SKILL.md').write_text('Edited locally')
        checker.write(self.target)
        with self.assertRaisesRegex(ValueError, 'manifest differs'):
            checker.check(self.target, self.source)

    def test_empty_denominator_is_rejected(self):
        p = self.source / 'collection.json'
        data = json.loads(p.read_text()); data['files'] = {}; p.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Empty file inventory'):
            checker.check(self.source, self.source)

    def test_missing_entry_route_is_rejected(self):
        (self.target / 'COLLECTION.md').write_text('Version: 0.1.0\n')
        with self.assertRaisesRegex(ValueError, 'does not route'):
            checker.check(self.target, self.source)

    def test_source_cannot_write_inventory_with_undeclared_member(self):
        member = self.source / 'skills/example-third'
        member.mkdir(); (member / 'SKILL.md').write_text('# Extra')
        with self.assertRaisesRegex(ValueError, 'Membership mismatch'):
            checker.write(self.source)

    def test_symlink_is_rejected(self):
        (self.target / 'alias').symlink_to(self.source / 'COLLECTION.md')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            checker.check(self.target, self.source)


class CollectionNameTests(unittest.TestCase):
    def test_each_collection_name_has_a_valid_installation(self):
        for name in ('python-foundation', 'typescript-foundation', 'verification-foundation'):
            with self.subTest(collection=name):
                fixture = InstallationTests()
                fixture.setUp()
                try:
                    p = fixture.source / 'collection.json'
                    data = json.loads(p.read_text()); data['name'] = name
                    p.write_text(json.dumps(data)); checker.write(fixture.source)
                    shutil.rmtree(fixture.target); shutil.copytree(fixture.source, fixture.target)
                    self.assertEqual(checker.check(fixture.target, fixture.source), 3)
                finally:
                    fixture.doCleanups()

    def test_different_collection_manifest_is_rejected(self):
        fixture = InstallationTests(); fixture.setUp()
        try:
            p = fixture.target / 'collection.json'
            data = json.loads(p.read_text()); data['name'] = 'example-other'
            p.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'manifest differs'):
                checker.check(fixture.target, fixture.source)
        finally:
            fixture.doCleanups()
