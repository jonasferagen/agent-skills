# Repository guidance

These instructions govern changes to this authoring repository. To use an
installed skill in another project, start at that installation's entry point
and the consuming project's instructions.

[README](README.md) owns the catalog and task routes. Its linked guides own
package authoring, verification, evaluation and releases. For a named skill,
start at its package. For package changes, read [authoring rules](docs/packages.md#adding-a-skill)
and [selection](docs/packages.md#selection); for versions or tags, read
[releases](docs/releases.md). Use the catalog only when choosing a skill.
Read applicable instructions first; in long guides inspect headings and read the
relevant sections, prerequisites and required references. A narrow route does not
waive an applicable rule.

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
diagram or table. Keep repository-specific package and release rules in the linked maintenance guides.

## Verification

- Run `python3 scripts/check.py` and `git diff --check`; see
  [maintenance checks](docs/verification.md#maintenance-checks) for prerequisites.
- Trigger, entrypoint, shared-guidance or packaging changes meet the
  [routing acceptance requirement](docs/verification.md#routing-quality).
- Before tagging a release of a skill that bundles scripts, templates or an
  extension declaration, complete the [release review](docs/releases.md#release-review).
- When evaluating a skill, follow the source
  [scenario guidance](docs/verification.md#evaluating-a-skill-against-its-scenarios).
  Record observed results with the change that ran them, never in the package.
- Run bundled tests when the behaviour they check changes. Render changed
  diagrams and inspect them at their intended reading width.
- On a rename, update the directory, manifest, scenarios,
  invocation examples and references. Keep source names in provenance where they
  identify material under its original name.
