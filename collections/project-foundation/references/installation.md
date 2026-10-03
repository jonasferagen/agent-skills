# Install or update project-foundation

Use this reference for adoption, upgrades or installation-location decisions.
Install the complete collection directory as one dependency and preserve its
layout so internal references work. A project spanning repositories uses
[multi-repository foundations](multi-repository.md) to choose shared owners and
installation locations before copying files.

The collection contains bootstrap, design and contracts,
documentation and policy, source-of-truth, authoring skills and shared templates.
The [foundation template](../templates/project-docs/foundation.md) has five fixed tables:
References, Inheritance, Boundaries, Overview and Policy. Their meaning belongs to
[foundation format](foundation-format.md); foundation files contain data only.
The [README template](../templates/README.md) links the foundation. Members declare
inheritance and retain local differences. Use the templates through bootstrap.

For a project-local adoption, copy the complete `project-foundation/` directory to
`.agents/collections/project-foundation/`, record the source and full commit in
`.agents/collections/UPSTREAM.md`, and have bootstrap add explicit routes to the
entry points from the project's `AGENTS.md`, through its local foundation when
using a shared installation. If using an uncommitted draft, identify
it as a draft and record its base revision and local changes. Do not claim it
matches a committed release.

This layout supports explicit file routing from project instructions; it does not
claim that a client automatically discovers nested skills. A user-wide adoption
can use its chosen location and equivalent routing. Global installation requires
that scope to be part of the user's request.

When upgrading from a version containing `git-worktrees`, remove routes to that
retired skill. Preserve adopted project working agreements; retiring the skill
does not revoke them. Personal worktree preferences belong in global agent
instructions and need no collection route.
