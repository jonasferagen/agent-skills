# Repository guidance

[README](README.md) owns the catalog, package format, naming and release rules.
Each skill directory must remain usable when copied on its own.

Apply the [authoring principle](README.md#authoring-skills) to this repository's
own changes: select relevant guidance from the catalog, then read only what
the task needs. This includes Capture Pattern for a reusable finding or an
explicit `/capture-pattern [idea]` request; its source home is this repository.

## Writing

Use [Clear Writing](skills/clear-writing/SKILL.md) when authoring or revising
prose here. For skill instructions, also read its [instruction
guidance](skills/clear-writing/references/instructions.md). Use [Diagrams and
tables](skills/diagrams-and-tables/SKILL.md) when adding or changing a diagram
or table, or when a passage might explain better as one. These skills own their
reusable rules; keep repository-specific package and release rules in the
README.

This is an authoring convention. Other skill packages do not require
`clear-writing` or `diagrams-and-tables` to be installed beside them. The
README's [authoring skills](README.md#authoring-skills) section recommends these
passes before a skill release and says what to record.

## Verification

- Run `python3 scripts/validate-packages.py` and `git diff --check`.
- Review the affected scenarios under `validation/`; record actual results and
  remaining limits when evaluating a skill.
- Run bundled helper tests when helper behavior changes. Render changed
  diagrams and inspect them at their intended reading width.
- On a rename, update the directory, manifest, UI metadata, validation page,
  invocation examples and references. Preserve source names in provenance when
  they identify material under its original name.
