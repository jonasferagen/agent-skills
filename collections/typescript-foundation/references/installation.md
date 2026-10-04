# Install and maintain typescript-foundation

Copy the complete `typescript-foundation/` directory from one selected source commit into
`.agents/collections/typescript-foundation/`. Record its source repository, source directory,
full SHA, collection version and any release tag in project provenance. This
unreleased draft may be pinned without a tag. TypeScript design, TypeScript patterns and Node patterns are members of
one installation and upgrade unit; preserve their names and conditional routes.

Add a concrete project route to `COLLECTION.md` for the tasks it owns. One shared
installation may serve several repositories under their existing access rules.
This is project file routing, not native client auto-registration. Keep adoption
choices and local constraints outside the imported files.

Before adoption run the selected source's checker against a complete staged copy:

```sh
python3 /selected/source/typescript-foundation/scripts/check_installation.py /staged/typescript-foundation
```

`collection.json` declares member names and a file hash inventory. The check compares
that manifest with the trusted source, then rejects missing members, changed files,
retired overlay files, missing entry routes and symlinks. Generated Python bytecode
is ignored. A consumer self-check detects accidental drift; it does not independently
prove the recorded source pin. Do not use `--write` to accept consumer drift.

For an update, stage the whole new directory, compare membership and guidance with
the old pin, preserve local edits and replace the entire old directory after checks.
Update provenance and task routes together; avoid overlays that retain retired files.
Keep the old pin for rollback. Run repository link and guidance checks after adoption.

When migrating standalone copies, compare them with their old pins before removal.
Preserve local changes and reconcile their rules into project-owned homes. Replace
standalone provenance with the collection pin and rewrite current routes. Remove
old copies only after preservation; history retains its original pins and paths.
There must be one active installed owner per member.

For source authoring, modify members in this collection. The repository owns a
canonical checker at `scripts/collection_installation.py`; synchronize distributed
copies with `python3 scripts/sync-collection-tools.py` from the source repository.
After reviewed edits, regenerate this collection's inventory using its checker
with `--write`, then self-check and run the repository package and routing checks.
Regeneration never selects new membership or grants authorization to accept drift.
The collection supplies no remote resolver, automatic updater or dependency installer.
