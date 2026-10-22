"""Every skill is a standalone package directory."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / 'skills'


class PackageLayoutTests(unittest.TestCase):
    def test_every_skill_is_a_complete_standalone_directory(self):
        packages = sorted(path.parent for path in SKILLS.rglob('SKILL.md'))
        self.assertGreater(len(packages), 0)
        for package in packages:
            with self.subTest(package=package.name):
                self.assertEqual(len(package.relative_to(SKILLS).parts), 2,
                                 'a skill sits directly under one area')
        self.assertFalse((ROOT / 'collections').exists(), 'the catalog ships no bundles')
