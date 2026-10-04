#!/usr/bin/env python3
"""Report a committed collection's inventory and extraction dependencies as JSON.

Reads Git objects, never working-copy payloads. Writes only stdout; does not
export files, execute source helpers, change repositories, or select adoption.
"""

import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


LINK = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
COPY_RECORD = re.compile(r'<!-- Package-boundary copy: (.*?)-->')
COPY_TARGET = re.compile(r'\b([a-z][a-z0-9-]*)/((?:[\w.-]+/)*[\w.-]+\.md)\b')


class GitSnapshot:
    """One immutable commit, with the invoking worktree's state reported separately."""

    def __init__(self, repository: Path, revision: str):
        self.repository = repository.resolve()
        self.commit = self.git('rev-parse', '--verify', '--end-of-options',
                               f'{revision}^{{commit}}').decode('ascii').strip()
        self.entries = {}
        for entry in self.git('ls-tree', '-r', '-z', self.commit).split(b'\0'):
            if entry:
                metadata, name = entry.split(b'\t', 1)
                mode, kind, object_id = metadata.decode('ascii').split()
                self.entries[name.decode('utf-8')] = (mode, kind, object_id)
        self._content: dict[str, bytes] = {}

    def git(self, *arguments: str) -> bytes:
        result = subprocess.run(
            ['git', '--no-optional-locks', '-C', str(self.repository), *arguments],
            stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=30,
        )
        return result.stdout

    def content(self, name: str) -> bytes:
        if name not in self._content:
            _, kind, object_id = self.entries[name]
            if kind != 'blob':
                raise ValueError(f'Unsupported Git entry: {name} ({kind})')
            self._content[name] = self.git('cat-file', 'blob', object_id)
        return self._content[name]


class MigrationInventory:
    def __init__(self, snapshot: GitSnapshot, collection: str, retained_members: list[str]):
        if not re.fullmatch(r'[a-z][a-z0-9-]*', collection):
            raise ValueError('Collection must be a lowercase package name')
        self.snapshot = snapshot
        self.collection = collection
        self.root = f'collections/{collection}'
        self.prefix = self.root + '/'
        self.retained_members = set(retained_members)

    def source_owner(self, name: str) -> str:
        if not name.startswith(self.prefix):
            return 'agent-skills'
        relative = name[len(self.prefix):].split('/')
        if len(relative) > 1 and relative[0] == 'skills' and relative[1] in self.retained_members:
            return 'agent-skills'
        return self.collection

    def report(self) -> dict:
        snapshot = self.snapshot
        payload = {name: entry for name, entry in snapshot.entries.items()
                   if name.startswith(self.prefix)}
        if not payload:
            raise ValueError(f'{self.root} is absent at {snapshot.commit}')
        for name, (mode, kind, _) in payload.items():
            if mode not in ('100644', '100755') or kind != 'blob':
                raise ValueError(f'Collection contains a symlink or unsupported entry: {name}')
        manifest_path = self.prefix + 'collection.json'
        if manifest_path not in payload:
            raise ValueError('Collection manifest is absent')
        manifest = json.loads(snapshot.content(manifest_path))
        if (not isinstance(manifest, dict)
                or set(manifest) != {'name', 'version', 'members', 'files'}
                or manifest['name'] != self.collection
                or not isinstance(manifest['version'], str)
                or not isinstance(manifest['files'], dict)
                or not isinstance(manifest['members'], list)
                or not manifest['members']
                or any(not isinstance(member, str) for member in manifest['members'])
                or len(set(manifest['members'])) != len(manifest['members'])):
            raise ValueError('Unsupported or inconsistent collection manifest')
        hashes = {name[len(self.prefix):]: hashlib.sha256(snapshot.content(name)).hexdigest()
                  for name in payload
                  if name != manifest_path and '__pycache__' not in name.split('/')
                  and not name.endswith(('.pyc', '.pyo'))}
        if hashes != manifest['files']:
            missing = sorted(set(manifest['files']) - set(hashes))
            extra = sorted(set(hashes) - set(manifest['files']))
            changed = sorted(name for name in hashes.keys() & manifest['files'].keys()
                             if hashes[name] != manifest['files'][name])
            raise ValueError(f'Committed inventory drift: missing={missing}, extra={extra}, changed={changed}')
        members = {name[len(self.prefix):].split('/')[1]
                   for name in payload if re.fullmatch(re.escape(self.prefix) + r'skills/[^/]+/SKILL\.md', name)}
        if members != set(manifest['members']):
            raise ValueError('Declared membership differs from committed skill entrypoints')
        if self.retained_members - members:
            raise ValueError(f'Retained members are absent: {sorted(self.retained_members - members)}')
        entrypoint = snapshot.content(self.prefix + 'COLLECTION.md').decode('utf-8')
        if (f"Version: {manifest['version']}\n" not in entrypoint
                or any(f'skills/{member}/SKILL.md' not in entrypoint for member in members)):
            raise ValueError('Collection entrypoint version or member routes differ from manifest')

        packages = {name.rsplit('/', 2)[-2]: name.rsplit('/', 1)[0]
                    for name in snapshot.entries if name.endswith('/SKILL.md')}
        own_packages = {member for member in members}
        links = []
        ownership_links = []
        paired_rules = []
        mentions = []
        terms = (self.collection, 'clear-writing', 'diagrams-and-tables', 'source-of-truth')
        for name in sorted(snapshot.entries):
            if snapshot.entries[name][1] != 'blob' or not name.endswith(('.md', '.py', '.yaml', '.yml', '.json')):
                continue
            text = snapshot.content(name).decode('utf-8')
            inside = name.startswith(self.prefix)
            for number, line in enumerate(text.splitlines(), 1):
                if not inside and any(term in line for term in terms):
                    mentions.append({'file': name, 'line': number, 'text': line.strip()})
                if name.endswith('.md'):
                    for match in LINK.finditer(line):
                        parts = match.group(1).strip().split()
                        if not parts:
                            continue
                        destination = parts[0].strip('<>')
                        parsed = urlsplit(destination)
                        if parsed.scheme or parsed.netloc or not parsed.path:
                            continue
                        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parsed.path)))
                        target_inside = target == self.root or target.startswith(self.prefix)
                        if inside != target_inside:
                            links.append({'file': name, 'line': number, 'target': target,
                                          'direction': 'outbound' if inside else 'inbound',
                                          'target_exists_at_commit': target in snapshot.entries})
                        if self.source_owner(name) != self.source_owner(target):
                            ownership_links.append({'file': name, 'line': number, 'target': target,
                                                    'from_owner': self.source_owner(name),
                                                    'to_owner': self.source_owner(target)})
                    for record in COPY_RECORD.finditer(line):
                        for package, path in COPY_TARGET.findall(record.group(1)):
                            if inside != (package in own_packages):
                                target_root = packages.get(package)
                                target = f'{target_root}/{path}' if target_root else None
                                paired_rules.append({'file': name, 'line': number,
                                                     'counterpart_package': package,
                                                     'counterpart_path': path,
                                                     'counterpart_source_file': target,
                                                     'target_exists_at_commit': target in snapshot.entries,
                                                     'direction': 'outbound' if inside else 'inbound'})
        canonical = 'scripts/collection_installation.py'
        shipped = self.prefix + 'scripts/check_installation.py'
        checker_matches = (canonical in snapshot.entries and shipped in snapshot.entries
                           and snapshot.content(canonical) == snapshot.content(shipped))
        return {
            'schema_version': 1,
            'scope': 'committed inventory and literal references; no extraction or adoption performed',
            'source_repository': str(snapshot.repository),
            'source_commit': snapshot.commit,
            'worktree_status': snapshot.git('status', '--porcelain=v1', '--untracked-files=normal').decode('utf-8').splitlines(),
            'collection': {'name': self.collection, 'version': manifest['version'],
                           'members': sorted(members), 'committed_file_count': len(payload),
                           'inventory_matches': True},
            'proposed_ownership': {'retained_in_agent_skills': sorted(self.retained_members),
                                   'native_project_members': sorted(members - self.retained_members),
                                   'shared_references': 'Project-owned by default; generic needs require explicit disentangling.'},
            'payload': [{'source_path': name, 'destination_path': name,
                         'git_mode': payload[name][0], 'git_blob': payload[name][2],
                         'proposed_source_owner': self.source_owner(name),
                         'sha256': hashlib.sha256(snapshot.content(name)).hexdigest()}
                        for name in sorted(payload)],
            'shared_checker_matches_canonical': checker_matches,
            'cross_boundary_markdown_links': links,
            'proposed_cross_owner_links': ownership_links,
            'cross_boundary_paired_rules': paired_rules,
            'proposed_cross_owner_paired_rules': [item for item in paired_rules
                                                 if item['counterpart_source_file'] is None
                                                 or self.source_owner(item['file']) != self.source_owner(item['counterpart_source_file'])],
            'source_reference_mentions': mentions,
            'supporting_file_candidates': sorted({item['file'] for item in mentions
                                                if item['file'].startswith(('docs/', 'validation/'))}),
            'existing_release_tags': snapshot.git('tag', '--list', f'{self.collection}/*').decode('utf-8').splitlines(),
            'limits': [
                'Literal references and simple inline Markdown links only; symbolic paths, anchors, and dynamic lookups need review.',
                'Supporting file candidates need an ownership decision; mentioning a collection does not make a file movable.',
                'Existing release tags are listed, without asserting that they identify the selected commit.',
                'Working-copy changes are reported and excluded from payloads; a commit pin does not establish that an iteration has finished.',
                'Inventory consistency does not establish routing quality, semantic conformance, or migration readiness.',
            ],
        }


def main() -> int:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--ref', required=True, help='Explicit commit or ref; resolved once to a full commit SHA')
    parser.add_argument('--collection', default='project-foundation')
    parser.add_argument('--retain-member', action='append', default=None,
                        help='Canonical source stays in agent-skills; default: clear-writing, diagrams-and-tables, source-of-truth')
    args = parser.parse_args()
    try:
        retained = args.retain_member if args.retain_member is not None else ['clear-writing', 'diagrams-and-tables', 'source-of-truth']
        report = MigrationInventory(GitSnapshot(args.repo, args.ref), args.collection, retained).report()
    except subprocess.CalledProcessError as error:
        print(f'Git failed with exit {error.returncode}: {error.stderr.decode("utf-8", errors="replace").strip()}', file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, subprocess.TimeoutExpired) as error:
        print(f'Migration inventory failed: {error}', file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
