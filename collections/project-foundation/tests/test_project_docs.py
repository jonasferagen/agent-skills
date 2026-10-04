import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('project_docs', Path(__file__).resolve().parents[1] / 'scripts/validate-project-docs.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ProjectDocsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('Synthetic fixture\n')

    def test_minimal_foundation_does_not_require_unused_categories(self):
        self.write('foundation.md')
        self.assertEqual(module.validate(self.root), [])

    def test_plan_with_index_and_retained_record(self):
        for name in ['planning/README.md', 'planning/local-import.md', 'records/2026-10-03-import.md']:
            self.write(name)
        self.assertEqual(module.validate(self.root), [])

    def test_detailed_plan_without_active_index(self):
        self.write('planning/import.md')
        self.assertTrue(any(e.startswith('planning/README.md:') and 'index' in e for e in module.validate(self.root)))

    def test_unmanaged_types_and_nested_output_are_rejected(self):
        for name in ['policy.md', 'operations/command.md', 'records/images/render.png']:
            self.write(name)
        errors = module.validate(self.root)
        for name in ['policy.md', 'operations', 'records/images']:
            self.assertTrue(any(name in e for e in errors))

    def test_managed_design_and_indexed_explanations(self):
        for name in ['design.md', 'architecture/README.md', 'architecture/data-flows.md',
                     'architecture/proposals/storage.md', 'architecture/examples/exchange.md',
                     'models/README.md', 'models/identity.md',
                     'processes/README.md', 'processes/review.md',
                     'contracts/README.md', 'contracts/delivery.md']:
            self.write(name)
        self.assertEqual(module.validate(self.root), [])
        (self.root / 'models/README.md').unlink()
        self.assertTrue(any(e.startswith('models/README.md:') and 'index' in e
                            for e in module.validate(self.root)))

    def test_architecture_subtopics_need_their_owning_index(self):
        for category in ('proposals', 'examples'):
            with self.subTest(category=category):
                topic = f'architecture/{category}/sample.md'
                self.write(topic)
                self.assertTrue(any(e.startswith('architecture/README.md:') and 'index' in e
                                    for e in module.validate(self.root)))
                self.write('architecture/README.md')
                self.assertEqual(module.validate(self.root), [])
                (self.root / 'architecture/README.md').unlink()
                (self.root / topic).unlink()

    def test_layout_is_read_from_document_homes(self):
        homes = self.root / 'homes.md'
        homes.write_text('| Type | Home | Workflow |\n| --- | --- | --- |\n| Notes | `project-docs/notes/<topic>.md` | Synthetic |\n')
        original = module.HOMES
        module.HOMES = homes
        self.addCleanup(setattr, module, 'HOMES', original)
        docs = self.root / 'project-docs'
        (docs / 'notes').mkdir(parents=True)
        (docs / 'notes' / 'first-note.md').write_text('Synthetic fixture\n')
        self.assertEqual(module.validate(docs), [])
        (docs / 'foundation.md').write_text('Synthetic fixture\n')
        self.assertTrue(any('foundation.md' in e for e in module.validate(docs)))

    def test_external_symlink_is_rejected(self):
        (self.root / 'foundation.md').symlink_to('/tmp/nonexistent-project-doc-fixture')
        self.assertTrue(any('symlink' in e for e in module.validate(self.root)))

    def test_named_process_needs_only_its_entry_and_parent_index(self):
        for name in ['processes/README.md', 'processes/sample-review/README.md']:
            self.write(name)
        self.assertEqual(module.validate(self.root), [])

    def test_process_supporting_pages_and_distinct_legacy_process_can_coexist(self):
        for name in ['processes/README.md', 'processes/sample-review/README.md',
                     'processes/sample-review/revision-path.md', 'processes/sample-intake.md']:
            self.write(name)
        self.assertEqual(module.validate(self.root), [])

    def test_process_directory_requires_parent_index_without_flat_topics(self):
        self.write('processes/sample-review/README.md')
        self.assertTrue(any(e.startswith('processes/README.md:') and 'index' in e
                            for e in module.validate(self.root)))

    def test_empty_process_directory_requires_entry(self):
        self.write('processes/README.md')
        (self.root / 'processes/sample-review').mkdir()
        self.assertTrue(any(e.startswith('processes/sample-review/README.md:') and 'entry' in e
                            for e in module.validate(self.root)))

    def test_supporting_page_cannot_replace_process_entry(self):
        for name in ['processes/README.md', 'processes/sample-review/decision.md']:
            self.write(name)
        self.assertTrue(any(e.startswith('processes/sample-review/README.md:') and 'entry' in e
                            for e in module.validate(self.root)))

    def test_same_name_flat_and_directory_process_is_ambiguous(self):
        for name in ['processes/README.md', 'processes/sample-review.md',
                     'processes/sample-review/README.md']:
            self.write(name)
        self.assertTrue(any('sample-review.md' in e and 'ambiguous' in e
                            for e in module.validate(self.root)))

    def test_process_directory_and_supporting_names_remain_lowercase_hyphenated(self):
        for name in ['processes/README.md', 'processes/Bad_Name/README.md',
                     'processes/sample-review/README.md', 'processes/sample-review/Bad_Name.md']:
            self.write(name)
        errors = module.validate(self.root)
        for name in ['processes/Bad_Name', 'processes/sample-review/Bad_Name.md']:
            self.assertTrue(any(e.startswith(name + ':') and 'lowercase hyphenated' in e for e in errors))

    def test_process_directory_rejects_nested_pages_and_runtime_artifacts(self):
        for name in ['processes/README.md', 'processes/sample-review/README.md',
                     'processes/sample-review/stages/first.md', 'processes/sample-review/output.json']:
            self.write(name)
        errors = module.validate(self.root)
        for name in ['processes/sample-review/stages', 'processes/sample-review/output.json']:
            self.assertTrue(any(e.startswith(name + ':') for e in errors))

    def test_process_symlink_cannot_import_an_external_process(self):
        self.write('processes/README.md')
        external = tempfile.TemporaryDirectory()
        self.addCleanup(external.cleanup)
        (Path(external.name) / 'README.md').write_text('Synthetic fixture\n')
        (self.root / 'processes/sample-review').symlink_to(external.name, target_is_directory=True)
        self.assertTrue(any(e.startswith('processes/sample-review:') and 'symlink' in e
                            for e in module.validate(self.root)))

    def test_named_directory_patterns_are_read_from_document_homes(self):
        homes = self.root / 'homes.md'
        homes.write_text('| Type | Home | Workflow |\n| --- | --- | --- |\n'
                         '| Index | `project-docs/flows/README.md` | Synthetic |\n'
                         '| Entry | `project-docs/flows/<process>/README.md` | Synthetic |\n'
                         '| Detail | `project-docs/flows/<process>/<topic>.md` | Synthetic |\n')
        original = module.HOMES
        module.HOMES = homes
        self.addCleanup(setattr, module, 'HOMES', original)
        docs = self.root / 'project-docs'
        for name in ['flows/README.md', 'flows/sample-review/README.md',
                     'flows/sample-review/decision.md']:
            path = docs / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Synthetic fixture\n')
        self.assertEqual(module.validate(docs), [])
        (docs / 'flows/README.md').unlink()
        self.assertTrue(any(e.startswith('flows/README.md:') and 'index' in e
                            for e in module.validate(docs)))


if __name__ == '__main__':
    unittest.main()
