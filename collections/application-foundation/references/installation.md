# Install and maintain application foundation

Copy the complete collection, retaining its relative layout, into the project's
chosen collection location, normally `.agents/collections/application-foundation/`.
Select a source commit and record its repository URL, source directory, full SHA,
collection version and any release tag in the project's provenance file. A draft
can be pinned by commit without a release tag.

Before adoption, run the selected source's checker against a complete staged copy:

```sh
python3 /selected/source/application-foundation/scripts/check_installation.py /staged/application-foundation
```

`collection.json` declares member names and a file hash inventory. The checker
compares the staged manifest and files with that trusted source, rejecting missing
or changed members, extra retired files, missing entry routes and symlinks.
Generated Python bytecode is ignored. An installed self-check can detect accidental
drift, but does not independently prove the recorded source pin. Do not use
`--write` to accept consumer drift.

Route from project instructions to the installed `COLLECTION.md` for
application-design tasks, or directly to `skills/application-design/SKILL.md`
when that owner is known.
The installation does not itself register native client discovery. Use the
client's supported discovery mechanism or an explicit project-instruction route.
For several repositories, one accessible, pinned installation may serve all of
them; each repository retains its own implementation and decision owners.

## Companion guidance

The collection has no required dependency on another collection or skill. All
required references are included. Project instructions can route to separately
installed companions when their tasks apply:

| Task | Companion candidates |
| --- | --- |
| Project responsibilities, handoffs and document ownership | project-foundation |
| Language-specific implementation | typescript-foundation or python-foundation collection |
| Service boundaries, HTTP/MCP behavior, lifecycle or promotion to maintained use | service-foundation collection |
| Evidence selection and writing tests | verification-foundation collection |

Pin each selected installation independently in project provenance. Give it a
concrete local route in project instructions; do not put cross-installation
relative links inside this collection. Missing companions do not block the core
workflow, but project-required guidance remains required by that project. The
project's scope determines whether an unavailable dependency blocks a particular
implementation task.

For an update, stage the complete new collection, compare membership and guidance
with the old pin, and preserve any local modifications before replacement. Check
the staged copy against the selected source, replace the whole old directory,
and update provenance and project routes together. Avoid overlays that retain
retired files; keep the old pin available for rollback. Run the consuming
repository's link and guidance checks after adoption.

This scheme uses explicit installations and project routing; it provides no
automatic dependency resolution, version compatibility solver or tracking of
upstream main.

When installing service-foundation, add its task route to the project instructions
used for ordinary design work. A companion listed only here will not be discovered
by an agent correctly skipping installation guidance during implementation.

## Source maintenance

Author members and shared references inside this collection. The source repository
owns a canonical checker at `scripts/collection_installation.py`; synchronize its
distributed copies with `python3 scripts/sync-collection-tools.py` from that
repository. After reviewed edits, regenerate this collection's inventory with
its checker using `--write`, self-check it, and run the repository's package and
routing checks. Regeneration does not choose membership or authorize accepting
consumer drift.
