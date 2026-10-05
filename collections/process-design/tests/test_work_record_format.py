"""Synthetic records exercise selection, field rules and bounded directory checking."""
from pathlib import Path
import runpy
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
_format = runpy.run_path(str(SCRIPTS / 'work_record_format.py'))
RecordError, parse_record, selects = _format['RecordError'], _format['parse_record'], _format['selects']
validate = runpy.run_path(str(SCRIPTS / 'validate-work-records.py'))['validate']

VALID = """# Portrait card rendering

Record format: work-record/v1

Record ID: `portrait-card` · Revision: 2 · Date: 2026-10-05
Kind: concept
Workflow: ready
Owner: Primary and the acting UI artist.
Status: The layout basis is selected; finished art is open.
Worklog: [Selection](../studies/selection.md)

## Intent

Render the selected card.
"""

MINIMAL = """# Scale calibration

Record format: work-record/v1

Record ID: `scale-calibration` · Revision: 1 · Date: 2026-10-01
Owner: Game.
Status: Measurements are pending.
"""


def altered(original: str, old: str, new: str) -> str:
    assert old in original
    return original.replace(old, new)


class SelectionTests(unittest.TestCase):
    def test_unselected_document_is_not_a_record(self):
        self.assertFalse(selects('# A brief\n\nBrief ID: `x`\n'))
        with self.assertRaisesRegex(RecordError, 'not a selected work record'):
            parse_record('# A brief\n\nBrief ID: `x`\n')

    def test_unsupported_version_fails_rather_than_falling_back(self):
        with self.assertRaisesRegex(RecordError, 'unsupported record format version'):
            parse_record(altered(VALID, 'work-record/v1', 'work-record/v9'))

    def test_brief_id_remains_an_accepted_alias(self):
        record = parse_record(altered(VALID, 'Record ID:', 'Brief ID:'))
        self.assertEqual(record['identity_field'], 'Brief')
        self.assertEqual(record['identifier'], 'portrait-card')


class FieldTests(unittest.TestCase):
    def test_valid_record_parses_every_field(self):
        record = parse_record(VALID)
        self.assertEqual(record['identifier'], 'portrait-card')
        self.assertEqual((record['revision'], record['date']), (2, '2026-10-05'))
        self.assertEqual((record['Kind'], record['Workflow']), ('concept', 'ready'))

    def test_optional_fields_may_be_absent_and_stay_unrecorded(self):
        record = parse_record(MINIMAL)
        self.assertNotIn('Kind', record)
        self.assertNotIn('Workflow', record)

    def test_required_fields_are_enforced(self):
        with self.assertRaisesRegex(RecordError, 'missing required field'):
            parse_record(altered(MINIMAL, 'Owner: Game.\n', ''))

    def test_out_of_order_fields_are_rejected(self):
        swapped = altered(VALID, 'Kind: concept\nWorkflow: ready\n', 'Workflow: ready\nKind: concept\n')
        with self.assertRaisesRegex(RecordError, 'out of order'):
            parse_record(swapped)

    def test_duplicate_field_is_rejected(self):
        with self.assertRaisesRegex(RecordError, 'duplicate metadata field'):
            parse_record(altered(VALID, 'Workflow: ready\n', 'Workflow: ready\nWorkflow: done\n'))

    def test_empty_field_is_rejected(self):
        with self.assertRaisesRegex(RecordError, 'empty metadata field'):
            parse_record(altered(VALID, 'Status: The layout basis is selected; finished art is open.',
                                 'Status:  '))

    def test_unknown_field_is_rejected(self):
        with self.assertRaisesRegex(RecordError, 'unexpected metadata line'):
            parse_record(altered(VALID, 'Workflow: ready\n', 'Workflow: ready\nPriority: high\n'))

    def test_vocabularies_are_closed(self):
        with self.assertRaisesRegex(RecordError, 'Kind must be one of'):
            parse_record(altered(VALID, 'Kind: concept', 'Kind: artwork'))
        with self.assertRaisesRegex(RecordError, 'Workflow must be one of'):
            parse_record(altered(VALID, 'Workflow: ready', 'Workflow: shipped'))

    def test_identity_line_must_be_complete_and_real(self):
        with self.assertRaisesRegex(RecordError, 'malformed identity line'):
            parse_record(altered(VALID, ' · Revision: 2', ''))
        with self.assertRaisesRegex(RecordError, 'malformed identity line'):
            parse_record(altered(VALID, 'Revision: 2', 'Revision: 0'))
        with self.assertRaisesRegex(RecordError, 'not a real calendar date'):
            parse_record(altered(VALID, 'Date: 2026-10-05', 'Date: 2026-02-30'))

    def test_identifier_must_be_lowercase_hyphenated(self):
        with self.assertRaisesRegex(RecordError, 'malformed identity line'):
            parse_record(altered(VALID, '`portrait-card`', '`Portrait Card`'))

    def test_worklog_must_be_a_single_link(self):
        with self.assertRaisesRegex(RecordError, 'Worklog must be a single Markdown link'):
            parse_record(altered(VALID, 'Worklog: [Selection](../studies/selection.md)',
                                 'Worklog: see the studies directory'))

    def test_unfilled_template_is_named_as_such(self):
        with self.assertRaisesRegex(RecordError, 'unfilled template placeholder'):
            parse_record(altered(VALID, '`portrait-card`', '`{{stable-id}}`'))

    def test_block_must_follow_the_title_and_format_line(self):
        with self.assertRaisesRegex(RecordError, 'format line must follow the title'):
            parse_record(altered(VALID, '# Portrait card rendering\n\nRecord format',
                                 '# Portrait card rendering\n\nSome prose.\n\nRecord format'))
        with self.assertRaisesRegex(RecordError, 'metadata block must follow the format line'):
            parse_record(altered(VALID, 'work-record/v1\n\nRecord ID:', 'work-record/v1\nRecord ID:'))


class DirectoryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def write(self, name: str, text: str) -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def test_unselected_documents_are_skipped_not_failed(self):
        self.write('legacy.md', '# Legacy brief\n\nBrief ID: `legacy`\n\nNo format line.\n')
        self.write('current.md', VALID)
        errors, selected, skipped = validate([self.root])
        self.assertEqual((errors, selected, skipped), ([], 1, 1))

    def test_duplicate_identifier_within_one_run_is_rejected(self):
        self.write('one.md', VALID)
        self.write('nested/two.md', VALID)
        errors, selected, _ = validate([self.root])
        self.assertEqual(selected, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn('duplicate record identifier', errors[0])

    def test_hidden_directories_are_not_scanned(self):
        self.write('.git/objects/stray.md', altered(VALID, '`portrait-card`', '`stray`'))
        errors, selected, skipped = validate([self.root])
        self.assertEqual((errors, selected, skipped), ([], 0, 0))

    def test_symlinked_selection_is_refused(self):
        target = self.write('real.md', VALID)
        link = self.root / 'alias.md'
        link.symlink_to(target)
        errors, _, _ = validate([link])
        self.assertEqual(len(errors), 1)
        self.assertIn('must not be symlinks', errors[0])

    def test_missing_path_is_reported_without_crashing(self):
        errors, selected, skipped = validate([self.root / 'absent'])
        self.assertEqual((selected, skipped), (0, 0))
        self.assertIn('not a file or directory', errors[0])

    def test_shipped_templates_are_not_valid_instances(self):
        templates = Path(__file__).resolve().parents[1] / 'templates'
        errors, selected, _ = validate([templates])
        self.assertEqual(selected, 5)
        self.assertEqual(len(errors), 5)
        self.assertTrue(all('unfilled template placeholder' in error for error in errors))


class DocumentedVocabularyTests(unittest.TestCase):
    """The reference explains what the checker enforces; silent drift between them is a defect."""

    @classmethod
    def setUpClass(cls):
        cls.reference = (Path(__file__).resolve().parents[1]
                         / 'references/record-format.md').read_text(encoding='utf-8')
        cls.module = _format

    def documented(self, field: str) -> list[str]:
        import re
        row = re.search(rf'^\| `{field}` \| (?:Yes|No) \| One of (.+?) \|$',
                        self.reference, re.MULTILINE)
        self.assertIsNotNone(row, f'{field} has no documented value row')
        return re.findall(r'`([^`]+)`', row.group(1))

    def test_documented_kinds_match_the_checker(self):
        self.assertEqual(self.documented('Kind'), list(self.module['KIND']))

    def test_documented_workflows_match_the_checker(self):
        self.assertEqual(self.documented('Workflow'), list(self.module['WORKFLOW']))

    def test_documented_field_order_matches_the_checker(self):
        import re
        rows = re.findall(r'^\| `([A-Za-z ]+)` \| (?:Yes|No) \|', self.reference, re.MULTILINE)
        identity = ['Record ID', 'Revision', 'Date']
        self.assertEqual(rows[:len(identity)], identity, 'identity fields changed in the reference')
        self.assertEqual(rows[len(identity):], list(self.module['ORDER']))

    def test_the_example_in_the_reference_is_a_valid_record(self):
        import re
        block = re.search(r'```text\n(# .+?)\n```', self.reference, re.DOTALL)
        self.assertIsNotNone(block, 'the reference no longer shows an example record')
        record = parse_record(block.group(1))
        self.assertEqual(record['identifier'], 'hud-portrait-card-graphics')
