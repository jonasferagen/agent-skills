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
the task needs. This includes Pattern capture for a reusable finding or an
explicit `/pattern-capture [idea]` request; its source home is this repository.
Use it also when skill use exposes repeated friction, an undocumented workaround
or a correction that suggests missing guidance. Load its instructions when that
trigger applies; routine successful use needs no capture pass.

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
History under `validation/` may name what it actually tested.

## Verification

- For trigger, entrypoint, shared-guidance or packaging changes, meet the
  [routing acceptance requirement](README.md#routing-quality) using the practical
  trials in [discovery validation](validation/discovery.md#routing-trial-method).
  Repeat applicable trials before a release; prose-only edits need no
  automatic discovery trial.

- Run `python3 scripts/check.py` and `git diff --check`; the README's
  [verification](README.md#verification) section owns prerequisites.
- Before tagging a release of a skill that bundles scripts, templates or an
  extension declaration, complete its
  [self-conformance review](validation/self-conformance.md).
- Review the affected scenarios under `validation/`; record actual results and
  remaining limits when evaluating a skill. For a narrow edit, read the applicable
  behavior cases; load dated trial history only when revisiting those results.
- Run bundled helper tests when helper behavior changes. Render changed
  diagrams and inspect them at their intended reading width.
- On a rename, update the directory, manifest, UI metadata, validation page,
  invocation examples and references. Preserve source names in provenance when
  they identify material under its original name.
