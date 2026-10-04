"""Exercise the inventory CLI against isolated synthetic Git repositories."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'prepare-project-foundation-migration.py'


class MigrationInventoryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name) / 'source'
        self.repo.mkdir()
        self.git('init', '--quiet')
        self.git('config', 'user.name', 'Example Author')
        self.git('config', 'user.email', 'author@example.test')
        self.root = self.repo / 'collections/example-collection'
        self.root.mkdir(parents=True)
        self.write('collections/example-collection/COLLECTION.md',
                   'Version: 0.1.0\n[Project](skills/example-project/SKILL.md)\n'
                   '[Authoring](skills/example-authoring/SKILL.md)\n')
        self.write('collections/example-collection/skills/example-project/SKILL.md',
                   '# Project\n[Write](../example-authoring/SKILL.md)\n')
        self.write('collections/example-collection/skills/example-authoring/SKILL.md', '# Authoring\n')
        self.write('collections/example-collection/skills/example-project/references/rule.md',
                   '<!-- Package-boundary copy: example-peer/SKILL.md states this rule. -->\n')
        self.write('skills/example-peer/SKILL.md',
                   '<!-- Package-boundary copy: example-project/references/rule.md states this rule. -->\n')
        self.write('README.md', '[Collection](collections/example-collection/COLLECTION.md)\n')
        self.manifest()
        self.commit = self.commit_all()

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, check=True, timeout=20).stdout.strip()

    def write(self, name, content):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def manifest(self):
        files = {path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                 for path in self.root.rglob('*') if path.is_file() and path.name != 'collection.json'}
        (self.root / 'collection.json').write_text(json.dumps({
            'name': 'example-collection', 'version': '0.1.0',
            'members': ['example-project', 'example-authoring'], 'files': files,
        }), encoding='utf-8')

    def commit_all(self):
        self.git('add', '.')
        self.git('commit', '--quiet', '-m', 'Synthetic inventory')
        return self.git('rev-parse', 'HEAD')

    def run_inventory(self, revision=None):
        return subprocess.run([
            sys.executable, str(SCRIPT), '--repo', str(self.repo),
            '--ref', revision or self.commit, '--collection', 'example-collection',
            '--retain-member', 'example-authoring',
        ], cwd=self.repo.parent, stdin=subprocess.DEVNULL, capture_output=True,
            text=True, encoding='utf-8', timeout=30)

    def test_commit_pin_ignores_dirty_payload_and_preserves_source(self):
        path = 'collections/example-collection/skills/example-project/SKILL.md'
        self.write(path, '# Uncommitted replacement\n')
        self.write('untracked.txt', 'Synthetic scratch\n')
        before = {file.relative_to(self.repo).as_posix(): file.read_bytes()
                  for file in self.repo.rglob('*') if file.is_file()}
        result = self.run_inventory()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report['source_commit'], self.commit)
        expected = hashlib.sha256(b'# Project\n[Write](../example-authoring/SKILL.md)\n').hexdigest()
        self.assertEqual(next(item['sha256'] for item in report['payload']
                              if item['source_path'] == path), expected)
        self.assertTrue(report['worktree_status'])
        after = {file.relative_to(self.repo).as_posix(): file.read_bytes()
                 for file in self.repo.rglob('*') if file.is_file()}
        self.assertEqual(before, after)

    def test_resolves_updated_ref_and_reports_import_links_and_paired_rules(self):
        self.write('collections/example-collection/skills/example-authoring/SKILL.md', '# New authoring revision\n')
        self.manifest()
        latest = self.commit_all()
        result = self.run_inventory('HEAD')
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report['source_commit'], latest)
        self.assertEqual(report['proposed_ownership']['retained_in_agent_skills'], ['example-authoring'])
        self.assertEqual(report['proposed_ownership']['native_project_members'], ['example-project'])
        self.assertEqual({item['direction'] for item in report['cross_boundary_paired_rules']}, {'inbound', 'outbound'})
        self.assertTrue(all(item['target_exists_at_commit'] for item in report['cross_boundary_paired_rules']))
        self.assertTrue(any(item['from_owner'] == 'example-collection' and item['to_owner'] == 'agent-skills'
                            for item in report['proposed_cross_owner_links']))

    def test_committed_drift_fails_without_success_report(self):
        self.write('collections/example-collection/skills/example-project/SKILL.md', '# Stale manifest\n')
        latest = self.commit_all()
        result = self.run_inventory(latest)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, '')
        self.assertIn('Committed inventory drift', result.stderr)

    def test_symlink_payload_is_rejected(self):
        (self.root / 'external-link').symlink_to('../../README.md')
        latest = self.commit_all()
        result = self.run_inventory(latest)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, '')
        self.assertIn('symlink or unsupported entry', result.stderr)

    def test_invalid_revision_fails_without_success_report(self):
        result = self.run_inventory('missing-example-ref')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, '')
        self.assertIn('Git failed', result.stderr)


if __name__ == '__main__':
    unittest.main()
