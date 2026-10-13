"""Shipped packages name no consumer: the project or distribution that installs them."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / 'skills'
# Word-bounded so that "forgetting" in prose does not match; a hyphenated
# compound such as a service or repository name does.
CONSUMER_NAMES = re.compile(r'project-foundation|\bforge\b|\bforge-', re.IGNORECASE)
# Skills that left this catalog. A shipped package names only skills a consumer
# can still install from here; history under validation/ may keep these names.
RETIRED_SKILL_NAMES = re.compile(
    r'\b(containerization|repository-services|project-docs|shared-code-design|change-workflow|git-worktrees|jonas-email-style|selfcheck-guard|work-records|project-planning|project-bootstrap|pattern-capture|project-policy|typescript-patterns|typescript-design)\b')
TEXT = {'.md', '.py', '.yaml', '.yml', '.json', '.txt', '.sh', ''}


class ShippedContentTests(unittest.TestCase):
    def test_no_consumer_name_appears_in_a_shipped_package(self):
        hits = []
        for file in sorted(SKILLS.rglob('*')):
            if not file.is_file() or '__pycache__' in file.parts or file.suffix not in TEXT:
                continue
            for number, line in enumerate(file.read_text(encoding='utf-8').splitlines(), 1):
                if CONSUMER_NAMES.search(line):
                    hits.append(f'{file.relative_to(ROOT)}:{number}: {line.strip()}')
        self.assertEqual(hits, [], '\n'.join(hits))

    def test_no_retired_skill_is_named_in_a_shipped_package(self):
        hits = []
        for file in sorted(SKILLS.rglob('*')):
            if not file.is_file() or '__pycache__' in file.parts or file.suffix not in TEXT:
                continue
            for number, line in enumerate(file.read_text(encoding='utf-8').splitlines(), 1):
                if RETIRED_SKILL_NAMES.search(line):
                    hits.append(f'{file.relative_to(ROOT)}:{number}: {line.strip()}')
        self.assertEqual(hits, [], '\n'.join(hits))

    def test_every_skill_is_a_complete_standalone_directory(self):
        packages = sorted(path.parent for path in SKILLS.rglob('SKILL.md'))
        self.assertGreater(len(packages), 0)
        for package in packages:
            with self.subTest(package=package.name):
                self.assertEqual(len(package.relative_to(SKILLS).parts), 2,
                                 'a skill sits directly under one area')
                self.assertTrue((package / 'agents/openai.yaml').is_file())
        self.assertFalse((ROOT / 'collections').exists(), 'the catalog ships no bundles')
