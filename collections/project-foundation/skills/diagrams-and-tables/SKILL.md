---
name: diagrams-and-tables
description: "Choose prose, tables or diagram types for an explanation, and route construction or review to the relevant visual guidance. Use when selecting a form or creating or reviewing a visual."
metadata:
  version: "0.4.0"
---

# Diagrams and tables

Choose the smallest useful form for the reader's question. Reuse an existing
explanation when it answers that question; link its owner instead of maintaining
another copy. Document ownership and navigation belong to project-docs.

## When to use what

| Reader needs to understand | Start with |
| --- | --- |
| A fact, reason, decision, caveat or convention | Brief prose |
| Cases sharing fields, options, obligations or changes | A table; shared fields matter more than item count |
| Steps, branches or a lifecycle | A flowchart |
| Ordered interactions between participants | A sequence diagram |
| Components and their connections or ownership | A component or relationship view |
| Entities and their relationships | An ER diagram; add a field table only when field details matter |

Use a diagram when the relationships are the explanation. Do not add one merely
because the document describes a system. Keep each form on one reader question
and distinguish established facts, proposals and unknowns.

## Load construction guidance only when needed

Filling an existing scaffold table or making an ordinary wording edit needs no
construction references. Preserve its columns, meaning and uncertainty. Stop here
when the task is only form selection.

- To design or restructure a table, read [tables](references/tables.md).
- To create or restructure a diagram, read [composition](references/composition.md)
  and [verification](references/verification.md) for detail, grounding and visual checks.
- If implementing that diagram in Mermaid, also read [drawing](references/drawing.md).
- To review an existing diagram, read verification; add composition when its
  structure needs work and drawing when Mermaid syntax or layout is involved.
- Use [worked examples](references/worked-examples.md) only when the chosen form
  needs an example.

A diagram must be grounded in its source and visually inspected in the target
renderer. A successful parse alone does not establish readability. Report any
rendering limitation rather than claiming visual verification.
