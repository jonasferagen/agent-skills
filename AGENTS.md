# Repository guidance

These instructions govern changes to this authoring repository. To use an
installed skill in another project, start at that installation's entry point
and the consuming project's instructions.

[README](README.md) owns the catalog, package format, naming, verification,
evaluation and release rules. For a named skill, start at its package and read
only the README section the task needs.

## Git

Use the acting agent's own managed worktree support for task worktrees. Each
agent cleans up the worktrees it created. Worktrees already under `.worktrees/`
stay there until their work finishes.

## Packages

Every skill is a standalone package: its references, templates, scripts and
tests live inside its directory, and it names another skill rather than linking
to it. Source maintenance may derive package-local copies of a shared rule, but
never replaces them with links or runtime imports into another skill. This
repository ships no bundles. Shipped content names no consumer: say
"the consuming project" or "the project's framework".

## Writing

Use [Clear Writing](skills/authoring/clear-writing/SKILL.md) for prose here and,
for skill instructions, its [instruction guidance](skills/authoring/clear-writing/references/instructions.md).
Use [Diagrams and Tables](skills/authoring/diagrams-and-tables/SKILL.md) for a
diagram or table. Keep repository-specific package and release rules in the README.

## Verification

- Run `python3 scripts/check.py` and `git diff --check`; see
  [maintenance checks](README.md#maintenance-checks) for prerequisites.
- Trigger, entrypoint, shared-guidance or packaging changes meet the
  [routing acceptance requirement](README.md#routing-quality).
- Before tagging a release of a skill that bundles scripts, templates or an
  extension declaration, complete the [release review](README.md#release-review).
- When evaluating a skill, follow the README's
  [scenario guidance](README.md#evaluating-a-skill-against-its-scenarios).
  Record observed results with the change that ran them, never in the package.
- Run bundled tests when the behaviour they check changes. Render changed
  diagrams and inspect them at their intended reading width.
- On a rename, update the directory, manifest, scenarios,
  invocation examples and references. Keep source names in provenance where they
  identify material under its original name.
