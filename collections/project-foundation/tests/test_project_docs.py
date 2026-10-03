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
        self.assertTrue(any('active plan index' in e for e in module.validate(self.root)))

    def test_unmanaged_types_and_nested_output_are_rejected(self):
        for name in ['policy.md', 'architecture/design.md', 'records/images/render.png']:
            self.write(name)
        errors = module.validate(self.root)
        for name in ['policy.md', 'architecture', 'records/images']:
            self.assertTrue(any(name in e for e in errors))

    def test_external_symlink_is_rejected(self):
        (self.root / 'foundation.md').symlink_to('/tmp/nonexistent-project-doc-fixture')
        self.assertTrue(any('symlink' in e for e in module.validate(self.root)))


if __name__ == '__main__':
    unittest.main()
