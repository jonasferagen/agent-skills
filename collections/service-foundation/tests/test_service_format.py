"""Synthetic service definitions exercise the public Markdown boundary."""
from pathlib import Path
import runpy
import unittest
import tempfile

ServiceDefinition = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/service_format.py'))['ServiceDefinition']


def example():
    return '''# Example reader

Service format: service-definition/v1

## Service definition

| Field | Value |
| --- | --- |
| Identity | example.reader |
| Owner | Example repository |
| Purpose | Read synthetic pages. |
| Status | Proposed; no runtime evidence. |
| Lifetime | Explicit session. |
| Exposure | Local only. |
| Dependencies | None |
| State | [State](#operation) |
| Operations | [Guide](#operation) |
| Readiness | Unknown |
| Recovery | [Recovery](#operation) |
| Evidence | Unknown |

## Operation

No runtime is operated by this fixture.
'''


class ServiceHomeTests(unittest.TestCase):
    def test_discovery_is_bounded_and_rejects_missing_or_symlinked_guides(self):
        Home = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/service_format.py'))["ServiceHome"]
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / 'services'
            (home / 'reader' / 'nested').mkdir(parents=True)
            (home / 'README.md').write_text('# Services')
            guide = home / 'reader/README.md'
            guide.write_text('# Reader')
            (home / 'reader/nested/README.md').write_text('Not a service')
            self.assertEqual(Home.documents(home), [home / 'README.md', guide])
            guide.unlink()
            with self.assertRaisesRegex(ValueError, 'non-symlink guide'):
                Home.documents(home)
            guide.symlink_to(home / 'README.md')
            with self.assertRaisesRegex(ValueError, 'non-symlink guide'):
                Home.documents(home)
            guide.unlink()
            guide.write_text('# Reader')
            (home / 'other').symlink_to(home / 'reader', target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'symlinks'):
                Home.documents(home)


class ServiceFormatTests(unittest.TestCase):
    def test_preserves_scoped_facts_unknowns_and_source_lines(self):
        parsed = ServiceDefinition.parse(example())
        self.assertEqual(parsed['id'], 'example.reader')
        values = {fact['name']: fact['value'] for fact in parsed['facts']}
        self.assertEqual(values['Readiness'], 'Unknown')
        self.assertEqual(values['Status'], 'Proposed; no runtime evidence.')
        for fact in parsed['facts']:
            self.assertIn('| ' + fact['name'] + ' |', example().splitlines()[fact['line'] - 1])
        self.assertEqual([link['field'] for link in parsed['links']], ['State', 'Operations', 'Recovery'])

    def test_unversioned_guides_and_fenced_or_commented_examples_are_not_selected(self):
        for text in ['# Existing guide\n', '```markdown\n' + example() + '\n```', '<!--\n' + example() + '\n-->']:
            with self.subTest(text=text[:20]):
                self.assertIsNone(ServiceDefinition.parse(text))

    def test_unknown_or_duplicate_versions_are_rejected(self):
        for text in [example().replace('/v1', '/v8'), example() + '\nService format: service-definition/v1\n']:
            with self.assertRaisesRegex(ValueError, 'supported Service format'):
                ServiceDefinition.parse(text)

    def test_missing_duplicate_unknown_or_empty_fields_are_rejected(self):
        for text in [example().replace('| Owner | Example repository |\n', ''),
                     example().replace('| Owner | Example repository |', '| Owner | Example repository |\n| Owner | Other |'),
                     example().replace('| Owner |', '| Custodian |'),
                     example().replace('| Owner | Example repository |', '| Owner | |')]:
            with self.assertRaisesRegex(ValueError, 'field'):
                ServiceDefinition.parse(text)

    def test_duplicate_sections_and_broken_tables_are_rejected(self):
        for text in [example() + '\n## Service definition\n', example().replace('| Field | Value |', '| Name | Value |'), example().replace('| --- | --- |', '| - | - |')]:
            with self.assertRaises(ValueError):
                ServiceDefinition.parse(text)

    def test_routes_cannot_claim_missing_detail_or_execute_external_urls(self):
        for value in ['not linked', '[Bad](javascript:alert)', '[Bad](/private/file.md)', '[Bad](https://example.test/page)']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                ServiceDefinition.parse(example().replace('[Guide](#operation)', value))

    def test_identity_is_explicit_and_not_a_path(self):
        with self.assertRaisesRegex(ValueError, 'Identity'):
            ServiceDefinition.parse(example().replace('example.reader', '../reader'))


if __name__ == '__main__':
    unittest.main()
