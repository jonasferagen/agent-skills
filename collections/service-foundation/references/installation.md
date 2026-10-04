# Install and maintain service foundation

Copy the complete `service-foundation/` directory from one selected source commit
into `.agents/collections/service-foundation/`, preserving its layout. Record the
source repository, source directory, full SHA, collection version and release tag
(if any) in the project's collection provenance. This draft may be pinned without
a release tag. Its member versions do not select independent upgrade units.

## Route ordinary work

Add a project-instruction route to `COLLECTION.md` for service boundaries, lifecycle
and promotion from an experiment to maintained use. Keep that trigger reachable
from ordinary design work, not only installation instructions. Existing known
member routes may remain direct when they fit the task; a service transition needs
the collection's combined route. This is file-based project routing, not automatic
client registration. In a multi-repository project, one accessible shared owner
can hold the installation; consumer instructions retain their existing access rules.

The authoritative membership list is `collection.json`. It declares both members
and a hash inventory of every shipped file other than itself. Before adoption run:

```sh
python3 /trusted/source/service-foundation/scripts/check_installation.py /staged/service-foundation
```

Use the checker from the selected source revision for a staged install. It compares
the installed manifest to that source manifest, then checks exact membership, file
hashes, missing files and unexpected files. Symlinks are rejected. Python bytecode
caches are ignored as generated state. The default root is the checker's own
collection; that self-check detects accidental drift but is not independent proof
of the selected source revision.

## Update as one unit

Stage the complete new collection beside the existing installation. Compare the
new membership and task routes with the old pin; preserve local edits before
replacement and keep project-specific rules outside the vendored collection.
Check the staged copy against the selected source, review changed guidance and
its project consequences, then replace the whole directory and update provenance
and affected routes together. Never overlay a new version onto an old directory:
retired files would survive. Retain the old pin for rollback. Run project link and
guidance checks after replacement; a hash check does not prove routing behavior.

When migrating standalone `service-boundaries` or `runtime-operations`, compare
both old copies with their recorded pins. Preserve any local changes before
removing them. Replace their provenance entries with the collection pin, rewrite
all current member routes and verify no active route selects an old copy. Historical
records retain their original source paths and pins. Do not leave two active homes
for one member. Other standalone skills remain independently installed.

## Authoring the collection

The repository owns the canonical installation checker at
`scripts/collection_installation.py`. Synchronize distributed copies with
`python3 scripts/sync-collection-tools.py` from the authoring repository.
The two moved member packages retain their existing names and behavior. Change
members in this collection only; do not maintain a second standalone source copy.
After authorized edits, regenerate the inventory with:

```sh
python3 scripts/check_installation.py --write
python3 scripts/check_installation.py
python3 -m unittest discover -s tests -q
```

Run these commands from this collection's directory. `--write` is an authoring
operation, never a way to bless drift in a consumer. It preserves the declared
membership, rejects missing or undeclared members and records current file hashes.
The source repository's package checks, member tests and routing trials still
apply. No automatic updater, remote resolver or global installation is supplied.
