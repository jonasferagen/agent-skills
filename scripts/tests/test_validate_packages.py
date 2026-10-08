"""Package links resolve to files and anchors; the live maintenance pages do too."""

from pathlib import Path
import runpy
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = runpy.run_path(str(ROOT / 'scripts/validate-packages.py'))
MAINTENANCE_PAGES = ('README.md', 'AGENTS.md', 'DECISIONS.md')


class LinkCheckTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.unit = Path(scratch.name) / 'example'
        (self.unit / 'references').mkdir(parents=True)
        (self.unit / 'references/guide.md').write_text(
            '# Guide\n\n## Choose a form\n\nText.\n\n```md\n## Not a heading\n```\n\n'
            '## Choose a form\n\n<a id="explicit"></a>\n\n### Review — 2026-10-09\n', encoding='utf-8')

    def errors_for(self, body: str) -> list[str]:
        page = self.unit / 'SKILL.md'
        page.write_text(body, encoding='utf-8')
        return VALIDATOR['check_page_links'](page, self.unit)

    def test_present_file_anchors_pass_including_repeats_and_html_anchors(self):
        self.assertEqual(self.errors_for(
            '[a](references/guide.md#choose-a-form) [b](references/guide.md#choose-a-form-1) '
            '[c](references/guide.md#explicit) [d](references/guide.md#review--2026-10-09) '
            '[e](references/guide.md) [f](https://example.invalid/x#y)\n'), [])

    def test_missing_anchor_is_reported_with_its_location(self):
        errors = self.errors_for('Intro.\n\nSee [the rule](references/guide.md#not-a-heading).\n')
        self.assertEqual(len(errors), 1)
        self.assertIn('SKILL.md:3: missing link anchor: references/guide.md#not-a-heading', errors[0])

    def test_missing_file_and_escaping_link_are_still_reported(self):
        errors = self.errors_for('[x](references/absent.md#any) [y](../outside.md)\n')
        self.assertEqual(len(errors), 2)
        self.assertTrue(any('missing link target' in error for error in errors))
        self.assertTrue(any('leaves installation unit' in error for error in errors))

    def test_same_page_fragment_is_checked(self):
        self.assertEqual(self.errors_for('# Top\n\n## Section\n\n[s](#section)\n'), [])
        self.assertEqual(len(self.errors_for('# Top\n\n[s](#absent)\n')), 1)


class MaintenancePageTests(unittest.TestCase):
    def test_readme_instructions_and_decision_log_resolve_their_local_links(self):
        errors = [error for name in MAINTENANCE_PAGES
                  for error in VALIDATOR['check_page_links'](ROOT / name, ROOT)]
        self.assertEqual(errors, [], '\n'.join(errors))
