"""Check structural failures that would reintroduce instructions or ambiguous rows."""

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('foundation_format', ROOT / 'scripts/validate-foundation.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
REFERENCES = '| Key | Target |\n| --- | --- |'
INHERITANCE = '| Section | Authority |\n| --- | --- |'
BOUND = '| orchard | /workspaces/orchard |'


class FoundationFormatTests(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / 'templates/project-docs/foundation.md').read_text(encoding='utf-8').replace('{{date}}', '2026-10-03').replace('{{revision}}', '1')

    def declare(self, reference, inheritance):
        text = self.text.replace(REFERENCES, REFERENCES + '\n' + reference) if reference else self.text
        return text.replace(INHERITANCE, INHERITANCE + '\n' + inheritance) if inheritance else text

    def test_owner_and_sparse_member(self):
        self.assertEqual(checker.validate(self.text), [])
        member = self.text.replace('| Key | Target |\n| --- | --- |', '| Key | Target |\n| --- | --- |\n| orchard | /workspaces/orchard |')
        member = member.replace('| Section | Authority |\n| --- | --- |', '| Section | Authority |\n| --- | --- |\n| Policy | `$orchard/docs/foundation.md#policy` |')
        member = '\n'.join(line for line in member.splitlines() if 'Unknown' not in line)
        self.assertEqual(checker.validate(member), [])

    def test_instructions_and_extra_structure_rejected(self):
        for extra in ('Read the parent before work.', '<!-- Read the parent. -->', '```yaml\ninherits: parent\n```', '## Routes\n\n| Key | Target |\n| --- | --- |', '| Other | Value |\n| --- | --- |\n| Extra | None |'):
            with self.subTest(extra=extra):
                self.assertTrue(checker.validate(self.text + '\n' + extra))

    def test_ambiguous_tables_rejected(self):
        for old, new in (
            ('## Overview', '## Summary'),
            ('| Axis | Current fact or decision |', '| Axis | Value |'),
            ('| Recovery | Unknown |', '| Recovery | |'),
            ('| Recovery | Unknown |', '| Recovery | Unknown |\n| Recovery | None |'),
            ('| Recovery | Unknown |', '| Recovery | Unknown | extra |'),
            ('Revision: 1', 'Revision: 0'),
            ('2026-10-03', '2026-02-30'),
        ):
            with self.subTest(new=new):
                self.assertTrue(checker.validate(self.text.replace(old, new)))

    def test_invalid_declarations_rejected(self):
        for old, new in (
            ('| Key | Target |\n| --- | --- |', '| Key | Target |\n| --- | --- |\n| $bad | /tmp/owner |'),
            ('| Section | Authority |\n| --- | --- |', '| Section | Authority |\n| --- | --- |\n| Routes | Unknown |'),
        ):
            with self.subTest(new=new):
                self.assertTrue(checker.validate(self.text.replace(old, new)))

    def test_symbolic_references_need_declared_keys(self):
        typo = '| Policy | `$orhcard/docs/foundation.md#policy` |'
        self.assertIn('Inheritance: undeclared reference key: $orhcard', checker.validate(self.declare(BOUND, typo)))
        self.assertIn('Inheritance: undeclared reference key: $orchard', checker.validate(self.declare('', typo.replace('orhcard', 'orchard'))))
        cell = self.declare(BOUND, '').replace('| Purpose | Unknown |', '| Purpose | Roles: `$orhcard/docs/architecture.md#roles` |')
        self.assertIn('Boundaries: undeclared reference key: $orhcard', checker.validate(cell))

    def test_authority_is_one_anchored_reference_or_unknown(self):
        self.assertEqual(checker.validate(self.declare(BOUND, '| Policy | Unknown |')), [])
        for authority in (
            'None',
            '`$orchard/docs/foundation.md`',
            '/workspaces/orchard/docs/foundation.md#policy',
            '[Policy](../orchard/docs/foundation.md#policy)',
            '`$orchard/docs/foundation.md#policy` or `$orchard/docs/other.md#policy`',
        ):
            with self.subTest(authority=authority):
                self.assertTrue(checker.validate(self.declare(BOUND, f'| Policy | {authority} |')))

    def test_inheritance_from_own_file_rejected(self):
        # Paths are compared lexically, so this fixture needs no files.
        path = Path('/repo/project-docs/foundation.md')
        authority = '| Policy | `$own/project-docs/foundation.md#policy` |'
        for target in ('..', '/repo', '../../repo'):
            with self.subTest(target=target):
                errors = checker.validate(self.declare(f'| own | {target} |', authority), path)
                self.assertIn('Inheritance: Policy inherits from its own foundation', errors)
        for target in ('../../orchard', 'https://example.test/repo/raw/main'):
            with self.subTest(target=target):
                self.assertEqual(checker.validate(self.declare(f'| own | {target} |', authority), path), [])

    def test_literal_reference_and_escaped_pipe(self):
        # A target is never opened, fetched or executed by the checker.
        text = self.text.replace('| Key | Target |\n| --- | --- |', '| Key | Target |\n| --- | --- |\n| orchard | /nonexistent/root |')
        text = text.replace('| Purpose | Unknown |', r'| Purpose | Compare A \| B |')
        self.assertEqual(checker.validate(text), [])


if __name__ == '__main__':
    unittest.main()
