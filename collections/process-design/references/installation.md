# Install and maintain process design

Copy the complete `process-design/` directory from one selected source commit
into `.agents/collections/process-design/`, preserving its layout. Record the
source repository, source directory, full SHA, collection version and release
tag (if any) in the project's collection provenance. This draft may be pinned
without a release tag. Member versions do not select independent upgrade units.

## Route ordinary work

Add a project-instruction route to `COLLECTION.md` for commissioning bounded
work, retaining its evidence and recording a disposition. Declare the selected
repositories, homes and checks through the
[process-design extension](extension.md); installation alone does not adopt the
convention. Keep that trigger reachable from ordinary work, not only from
installation instructions. A known member route may remain direct when it fits
the task. This is file-based project routing, not automatic client registration.

In a multi-repository project, one accessible shared owner can hold the
installation; consumer instructions retain their existing access rules.

The authoritative membership list is `collection.json`. It declares both members
and a hash inventory of every shipped file other than itself. Before adoption run:

```sh
python3 /trusted/source/process-design/scripts/check_installation.py /staged/process-design
```

Use the checker from the selected source revision for a staged install. It
compares the installed manifest to that source manifest, then checks exact
membership, file hashes, missing files and unexpected files. Symlinks are
rejected. Python bytecode caches are ignored as generated state. The default
root is the checker's own collection; that self-check detects accidental drift
but is not independent proof of the selected source revision.

## Update as one unit

Stage the complete new collection beside the existing installation. Compare the
new membership and task routes with the old pin; preserve local edits before
replacement and keep project-specific rules outside the vendored collection.
Check the staged copy against the selected source, review changed guidance and
its project consequences, then replace the whole directory and update provenance
and affected routes together. Never overlay a new version onto an old directory:
retired files would survive. Retain the old pin for rollback. Run project link
and guidance checks after replacement; a hash check does not prove routing
behavior.

A collection upgrade does not re-check, re-date or re-classify existing records,
and it does not opt an unselected record into the structured format.

## One owner per document type

No upgrade of this collection changes who owns the named-process document type:
it stays with the consuming project's framework, as the
[extension boundary](extension.md#owned-by-the-project-framework) states. An
upgrade that appeared to move it would be a framework change, not an available
version, and the project's own instructions would have to select it.

If a project does find two active definitions of one document type or format,
treat that as the defect: select one owner, remove active routes to the other,
and preserve existing pages, their selected format, anchors and inbound links.
Historical records keep their original source paths and pins.

## Authoring the collection

The repository owns the canonical installation checker at
`scripts/collection_installation.py`. Synchronize distributed copies with
`python3 scripts/sync-collection-tools.py` from the authoring repository.
After authorized edits, regenerate the inventory with:

```sh
python3 scripts/check_installation.py --write
python3 scripts/check_installation.py
python3 -m unittest discover -s tests -q
```

Run these commands from this collection's directory. `--write` is an authoring
operation, never a way to bless drift in a consumer. It preserves the declared
membership, rejects missing or undeclared members and records current file
hashes. The source repository's package checks, member tests and routing trials
still apply. No automatic updater, remote resolver or global installation is
supplied.
