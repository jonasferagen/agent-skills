"""Collection metadata and staged-copy checks use synthetic, isolated inputs."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts/collection_installation.py'
spec = importlib.util.spec_from_file_location('collection_installation', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class VersionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        member = self.root / 'skills/example-member'
        member.mkdir(parents=True)
        (member / 'SKILL.md').write_text('# Synthetic member\n', encoding='utf-8')

    def declare(self, version):
        (self.root / 'COLLECTION.md').write_text(
            f'Version: {version}\n[Member](skills/example-member/SKILL.md)\n', encoding='utf-8')
        (self.root / 'collection.json').write_text(json.dumps({
            'name': 'example-collection', 'version': version,
            'members': ['example-member'], 'files': {},
        }), encoding='utf-8')

    def test_invalid_versions_cannot_be_published_as_an_inventory(self):
        for version in (123, None, [], '1', '1.0', '01.0.0', '1.0.0\n',
                        '1.0.0-01', '1.0.0-alpha..1', '1.0.0+build..1'):
            with self.subTest(version=version):
                self.declare(version)
                with self.assertRaisesRegex(ValueError, 'semantic-version string'):
                    checker.write(self.root)

    def test_valid_versions_survive_a_staged_copy(self):
        for version in ('0.1.0', '1.0.0', '1.2.3-rc.1+build.7', '1.2.3+01'):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as directory:
                self.declare(version)
                checker.write(self.root)
                target = Path(directory) / 'installed'
                shutil.copytree(self.root, target)
                self.assertEqual(checker.check(target, self.root), 2)


class StagedCollectionTests(unittest.TestCase):
    def test_each_inventory_checks_a_copy_from_an_unrelated_working_directory(self):
        manifests = sorted((ROOT / 'collections').glob('*/collection.json'))
        self.assertTrue(manifests, 'No collection inventories were exercised')
        for manifest in manifests:
            with self.subTest(collection=manifest.parent.name), tempfile.TemporaryDirectory() as directory:
                source = manifest.parent
                target = Path(directory) / 'installed'
                shutil.copytree(source, target)
                command = [sys.executable, str(source / 'scripts/check_installation.py'), str(target)]
                result = subprocess.run(command, cwd=directory, stdin=subprocess.DEVNULL,
                                        capture_output=True, text=True, timeout=20)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(str(target.resolve()), result.stdout)
                entry = target / 'COLLECTION.md'
                entry.write_bytes(entry.read_bytes() + b'\nSynthetic local edit.\n')
                result = subprocess.run(command, cwd=directory, stdin=subprocess.DEVNULL,
                                        capture_output=True, text=True, timeout=20)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('changed=', result.stderr)


class PackageInventoryTests(unittest.TestCase):
    def test_member_versions_follow_the_same_semantic_version_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / 'scripts'
            scripts.mkdir()
            shutil.copy2(ROOT / 'scripts/validate-packages.py', scripts)
            shutil.copy2(SCRIPT, scripts)
            package = root / 'skills/example-standalone'
            package.mkdir(parents=True)
            command = [sys.executable, str(scripts / 'validate-packages.py')]
            for version, valid in (('1.2.3-rc.1+build.7', True), ('1.2.3+01', True),
                                   ('1.2.3-alpha---1', True),
                                   ('1.2.3-01', False), ('1.2.3-alpha..1', False),
                                   ('1.2.3+build..1', False), ('01.2.3', False)):
                with self.subTest(version=version):
                    (package / 'SKILL.md').write_text(
                        '---\nname: example-standalone\ndescription: Synthetic package\n'
                        f'metadata:\n  version: "{version}"\n---\n\n# Example\n', encoding='utf-8')
                    result = subprocess.run(command, cwd=directory, stdin=subprocess.DEVNULL,
                                            capture_output=True, text=True, timeout=20)
                    self.assertEqual(result.returncode == 0, valid, result.stderr)
                    if not valid:
                        self.assertIn('invalid string metadata.version', result.stderr)

    def test_repository_rejects_a_collection_without_its_inventory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / 'scripts'
            scripts.mkdir()
            shutil.copy2(ROOT / 'scripts/validate-packages.py', scripts)
            shutil.copy2(SCRIPT, scripts)
            for package in (root / 'skills/example-standalone',
                            root / 'collections/example-collection/skills/example-member'):
                package.mkdir(parents=True)
                (package / 'SKILL.md').write_text(
                    f'---\nname: {package.name}\ndescription: Synthetic package\n'
                    'metadata:\n  version: "0.1.0"\n---\n\n# Example\n', encoding='utf-8')
            collection = root / 'collections/example-collection'
            (collection / 'COLLECTION.md').write_text(
                'Version: 0.1.0\n[Member](skills/example-member/SKILL.md)\n', encoding='utf-8')
            command = [sys.executable, str(scripts / 'validate-packages.py')]
            result = subprocess.run(command, cwd=directory, stdin=subprocess.DEVNULL,
                                    capture_output=True, text=True, timeout=20)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('missing collection.json', result.stderr)
            (collection / 'scripts').mkdir()
            shutil.copy2(SCRIPT, collection / 'scripts/check_installation.py')
            (collection / 'collection.json').write_text(json.dumps({
                'name': 'example-collection', 'version': '0.1.0',
                'members': ['example-member'], 'files': {},
            }), encoding='utf-8')
            checker.write(collection)
            result = subprocess.run(command, cwd=directory, stdin=subprocess.DEVNULL,
                                    capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
