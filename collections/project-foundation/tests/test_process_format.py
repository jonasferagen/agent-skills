import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('process_format', Path(__file__).resolve().parents[1] / 'scripts/process_format.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

DOCUMENT = '''# Synthetic intake

Status: Proposed synthetic example, 2026-10-04.

Process format: project-process/v1

<!-- process-section: purpose -->
## Existing purpose anchor

| Fact | Value |
| --- | --- |
| Reader question | How is the synthetic request assessed? |
| Trigger | An identified request |
| Owner | Example owner |
| Inputs | Saved input and existing delegation |
| Completion | Retained finding or unresolved question with next owner |

<!-- process-section: stages -->
## Existing work anchor

| Step | Action | Owner | Input | Result / condition | Detail |
| --- | --- | --- | --- | --- | --- |
| assess-request | Assess the request | Example owner | Identified request | A scoped finding | [Purpose](#existing-purpose-anchor) |

<!-- process-section: handoffs -->
## Return findings

| Handoff | From | To | Result | Kind | Detail |
| --- | --- | --- | --- | --- | --- |
| return-findings | Reviewer | Example owner | Scoped findings | feedback | [Purpose](#existing-purpose-anchor) |
'''


class ProcessFormatTests(unittest.TestCase):
    def test_source_locations_and_explicit_relations_are_retained(self):
        value = module.parse_process(DOCUMENT)
        self.assertEqual(value['version'], 'project-process/v1')
        self.assertEqual(value['roles']['purpose']['title'], 'Existing purpose anchor')
        self.assertEqual(value['facts'][0]['cells'][0], 'Reader question')
        self.assertEqual(DOCUMENT.splitlines()[value['steps'][0]['line'] - 1].split('|')[1].strip(), 'assess-request')
        self.assertEqual(value['handoffs'][0]['cells'][4], 'feedback')
        self.assertEqual(value['steps'][0]['detail'], '#existing-purpose-anchor')

    def test_legacy_and_fenced_format_examples_are_not_opted_in(self):
        self.assertIsNone(module.parse_process('# Legacy\n\nProse only.'))
        for fence in ('```', '~~~~'):
            self.assertIsNone(module.parse_process(f'# Legacy\n{fence}markdown\n{DOCUMENT}\n{fence}'))
        self.assertIsNone(module.parse_process('# Legacy\n<!-- example\nProcess format: project-process/v1\n-->'))

    def test_bad_versions_and_unversioned_markers_are_rejected(self):
        for text in (DOCUMENT.replace('/v1', '/v9'), DOCUMENT.replace('Process format: project-process/v1', ''), DOCUMENT + '\nProcess format: project-process/v1\n'):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, 'Process format'):
                    module.parse_process(text)

    def test_facts_must_have_exact_keys_order_and_values(self):
        for text in (DOCUMENT.replace('| Trigger |', '| Start |'), DOCUMENT.replace('| Inputs |', '| Owner |'), DOCUMENT.replace('An identified request', ''), DOCUMENT.replace('An identified request', '{{trigger}}')):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    module.parse_process(text)

    def test_missing_duplicate_and_unattached_roles_fail(self):
        for text in (DOCUMENT.replace('process-section: stages', 'process-section: evidence'), DOCUMENT.replace('process-section: handoffs', 'process-section: purpose'), DOCUMENT.replace('## Existing work anchor', 'No heading'), DOCUMENT.replace('process-section: stages', 'process-section: invented')):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    module.parse_process(text)

    def test_duplicate_and_display_label_keys_fail(self):
        row = next(line for line in DOCUMENT.splitlines() if line.startswith('| assess-request'))
        for text in (DOCUMENT.replace(row, row + '\n' + row), DOCUMENT.replace('| assess-request |', '| Assess request |')):
            with self.assertRaisesRegex(ValueError, 'stable lowercase'):
                module.parse_process(text)

    def test_incomplete_steps_bad_details_and_inferred_relations_fail(self):
        for before, after in [('Example owner | Identified request', ' | Identified request'), ('[Purpose](#existing-purpose-anchor)', 'Purpose'), ('| feedback |', '| relates-to |'), ('| Action | Owner |', '| Activity | Owner |')]:
            with self.subTest(before=before):
                with self.assertRaises(ValueError):
                    module.parse_process(DOCUMENT.replace(before, after))

    def test_unknown_and_no_handoffs_are_explicit(self):
        before = DOCUMENT.split('| Handoff |')[0]
        for value in ('Handoffs: None.', 'Handoffs: Unknown — Example owner must select exchange terms before delivery.'):
            self.assertEqual(module.parse_process(before + value)['handoffs'], [])

    def test_duplicate_table_is_rejected(self):
        start = DOCUMENT.index('| Fact |')
        stop = DOCUMENT.index('<!-- process-section: stages')
        with self.assertRaisesRegex(ValueError, 'exactly one table'):
            module.parse_process(DOCUMENT[:stop] + DOCUMENT[start:stop] + DOCUMENT[stop:])

    def test_schema_marker_in_longer_fence_does_not_end_example(self):
        self.assertIsNone(module.parse_process('````markdown\n```\n' + DOCUMENT + '\n````'))


if __name__ == '__main__':
    unittest.main()
