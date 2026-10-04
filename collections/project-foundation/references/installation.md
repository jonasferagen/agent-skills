# Install or update project-foundation

Use this reference for adoption, upgrades or installation-location decisions.
Install the complete collection directory as one dependency and preserve its
layout so internal references work. A project spanning repositories uses
[multi-repository foundations](multi-repository.md) to choose shared owners and
installation locations before copying files.

The collection supplies project workflows, authoring guidance and shared templates.
The [foundation template](../templates/project-docs/foundation.md) has five fixed tables:
References, Inheritance, Boundaries, Overview and Policy. Their meaning belongs to
[foundation format](foundation-format.md); foundation files contain data only.
The [README template](../templates/README.md) links the foundation. Members declare
inheritance and retain local differences. Use the templates through bootstrap.

For a project-local adoption, stage the complete `project-foundation/` directory
from one selected source commit for `.agents/collections/project-foundation/`.
Record source repository, source directory, full commit SHA, collection version
and any selected release tag in `.agents/collections/UPSTREAM.md`. The SHA is the
authoritative pin. If using an uncommitted draft, identify it as a draft and
record its base revision and local changes; it does not match a committed release.

Before adoption, run the checker from the selected source against the staged copy:

```sh
python3 /selected/source/project-foundation/scripts/check_installation.py /staged/project-foundation
```

`collection.json` declares members, collection version and shipped file hashes.
The checker compares that manifest with the selected source and rejects missing,
extra or changed files, undeclared members, absent member routes and symlinks.
Generated Python bytecode is ignored. An installed checker's self-check detects
accidental drift; comparison against the selected source also verifies the manifest.
Neither proves correct behavior, the source pin by itself or native client discovery.
Do not use `--write` to accept consumer drift; inventory regeneration belongs to
reviewed source authoring.

Have bootstrap merge explicit routes from the project's `AGENTS.md` to the
installed entry points, through its local foundation when using a shared
installation. Keep project choices outside the imported directory. Document
necessary local modifications in provenance instead of claiming an exact import.

This layout supports explicit file routing from project instructions; it does not
claim that a client automatically discovers nested skills. A user-wide adoption
can use its chosen location and equivalent routing. Global installation requires
that scope to be part of the user's request.

For an update, review changed guidance, membership and local modifications before
replacing the complete old directory with the checked staged copy. Preserve local
changes and retain the old pin for rollback; an overlay can leave retired files
active. Update provenance and affected project routes together. Run the project's
link and guidance checks after adoption. An upgrade alone does not migrate project
document homes or change inherited decisions.

When upgrading from a version containing `git-worktrees`, remove routes to that
retired skill. Preserve adopted project working agreements; retiring the skill
does not revoke them. Personal worktree preferences belong in global agent
instructions and need no collection route.
