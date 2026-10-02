---
name: diagrams-and-tables
description: "Choose prose, tables or diagram types for an explanation, and route construction or review to the relevant visual guidance. Use when selecting a form or creating or reviewing a visual."
metadata:
  version: "0.6.0"
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
| Work steps and conditional branches | A flowchart |
| One object's states and allowed transitions | A state diagram |
| Ordered interactions between participants | A sequence diagram |
| System parts, ownership and dependencies | A component or context view |
| Entities and their relationships | An ER diagram; add a field table only when field details matter |

Choose by the question, not the nouns: a database request can need a sequence
view of callers, an ER view of stored relationships, or a flowchart of validation
steps. A workflow describes work moving; a state diagram describes what one
object may become. Show several views only when they answer distinct questions.

Use a diagram when the relationships are the explanation. Do not add one merely
because the document describes a system. Keep each form on one reader question
and distinguish established facts, proposals and unknowns.

## Load construction guidance only when needed

Filling an existing scaffold table or making an ordinary wording edit needs no
construction references. Preserve its columns, meaning and uncertainty. Stop here
when the task is only form selection.

- To design or restructure a table, read [tables](references/tables.md).
- When the form is already ER, go directly to [ER guidance](references/er-diagrams.md).
  It separates reading, semantic review, construction and large-view work; do not
  also load general composition or Mermaid drawing guidance by default.
- For other diagram construction, read [composition](references/composition.md)
  and [verification](references/verification.md); add
  [drawing](references/drawing.md) when implementing in Mermaid.
- For visual review, read verification; add the relevant construction reference
  only when structure or notation needs work.
- Use [worked examples](references/worked-examples.md) only when the chosen form
  needs an example.

A diagram must be grounded in its source and visually inspected in the target
renderer. A successful parse alone does not establish readability. Report any
rendering limitation rather than claiming visual verification.
