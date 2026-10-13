# Repository guidance

These maintenance instructions govern changes to this authoring repository.
When only using an installed skill for another project, start at that
installation's entry point and the consuming project's instructions. Source
provenance is not a required reading list for ordinary consumption.

## Git

Use the acting agent's own managed worktree support for task worktrees when it
provides one; otherwise they belong under that agent's own home, as
`~/.claude/worktrees/agent-skills/<task>` or
`~/.codex/worktrees/agent-skills/<task>`. Either way each agent owns and sweeps
what it created and the checkout holds only the repository. Worktrees already
under `.worktrees/` stay there until their work finishes.

## Package maintenance

[README](README.md) owns the catalog, package format, naming and release rules.
Every skill is a standalone package that must work alone: its references,
templates, scripts and tests live inside its directory, and it names another
skill rather than linking to it. This repository ships no bundles; a downstream
distribution that bundles skills owns its own manifest and checks.

Standalone installation does not require independent authorship. Source
maintenance can derive or compare package-local copies of a shared rule; the
committed package must remain complete. Do not replace its local resources with
links or runtime imports into another skill.

For a named skill, start at that package. Use the catalog when selecting additional
guidance. Read the relevant maintenance section directly: [package use](README.md#using-a-skill),
[routing quality](README.md#routing-quality), [releases](README.md#skill-releases)
or [adding a skill](README.md#adding-a-skill). A focused edit needs no full README
or provenance-history read.

Apply the [authoring principle](README.md#authoring-skills) to this repository's
own changes: select relevant guidance from the catalog, then read only what
the task needs.

## Writing

Use [Clear Writing](skills/authoring/clear-writing/SKILL.md) when authoring or revising
prose here. For skill instructions, also read its [instruction
guidance](skills/authoring/clear-writing/references/instructions.md). Use [Diagrams and
tables](skills/authoring/diagrams-and-tables/SKILL.md) when adding or changing a diagram
or table, or when a passage might explain better as one. These skills own their
reusable rules; keep repository-specific package and release rules in the
README.

Shipped content names no consumer: no project, distribution or framework that
installs these skills. Say "the consuming project" or "the project's framework".

## Verification

- For trigger, entrypoint, shared-guidance or packaging changes, meet the
  [routing acceptance requirement](README.md#routing-quality) with the practical
  trials of its [routing trial method](README.md#routing-trial-method). Repeat
  applicable trials before a release; prose-only edits need no automatic
  discovery trial.
- Run `python3 scripts/check.py` and `git diff --check`; the README's
  [verification](README.md#verification) section owns prerequisites and says
  [where a package keeps its checks](README.md#where-a-package-keeps-its-checks).
- Before tagging a release of a skill that bundles scripts, templates or an
  extension declaration, complete the README's
  [release review](README.md#release-review).
- Review the affected cases in the package's `scenarios/README.md` when
  evaluating a skill, by the README's
  [evaluation guidance](README.md#evaluating-a-skill-against-its-scenarios).
  Record observed results with the change that ran them, not in the package.
  Add a demonstrated failure as a regression case and state a current limit
  beside the behavior it qualifies. For a narrow edit, read only the applicable
  cases.
- Keep scenarios free of observed outputs, timestamps and run reports, and keep
  entrypoints and references from routing ordinary use into them.
- Run bundled tests when the behavior they check changes. Render changed
  diagrams and inspect them at their intended reading width.
- On a rename, update the directory, manifest, UI metadata, scenarios,
  invocation examples and references. Preserve source names in provenance when
  they identify material under its original name.
