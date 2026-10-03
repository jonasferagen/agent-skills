# Repository guidance

These maintenance instructions govern changes to this authoring repository.
When only using an installed skill or collection for another project, start at
that installation's entry point and the consuming project's instructions. Source
provenance is not a required reading list for ordinary consumption.

## Git

This repository keeps task worktrees under `.worktrees/` in the main checkout.

## Package maintenance

[README](README.md) owns the catalog, package format, naming and release rules.
Standalone packages must work alone. Collection members may use shared resources
inside their collection; copy the complete collection as one installation unit.

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

Use [Clear Writing](collections/project-foundation/skills/clear-writing/SKILL.md) when authoring or revising
prose here. For skill instructions, also read its [instruction
guidance](collections/project-foundation/skills/clear-writing/references/instructions.md). Use [Diagrams and
tables](collections/project-foundation/skills/diagrams-and-tables/SKILL.md) when adding or changing a diagram
or table, or when a passage might explain better as one. These skills own their
reusable rules; keep repository-specific package and release rules in the
README.

The project-foundation collection includes these authoring skills and routes its
project skills to shared authoring guidance. Standalone packages outside that
collection use them here as an authoring convention. The
README's [authoring skills](README.md#authoring-skills) section recommends these
passes before a skill release and says what to record.

## Verification

- For trigger, entrypoint, shared-guidance or packaging changes, meet the
  [routing acceptance requirement](README.md#routing-quality) using the practical
  trials in [discovery validation](validation/discovery.md#routing-trial-method).
  Repeat applicable trials before a collection release; prose-only edits need no
  automatic discovery trial.

- Run `python3 scripts/validate-packages.py` and `git diff --check`.
- Before tagging a collection release, complete its
  [self-conformance review](validation/self-conformance.md).
- Review the affected scenarios under `validation/`; record actual results and
  remaining limits when evaluating a skill. For a narrow edit, read the applicable
  behavior cases; load dated trial history only when revisiting those results.
- Run bundled helper tests when helper behavior changes. Render changed
  diagrams and inspect them at their intended reading width.
- On a rename, update the directory, manifest, UI metadata, validation page,
  invocation examples and references. Preserve source names in provenance when
  they identify material under its original name.
