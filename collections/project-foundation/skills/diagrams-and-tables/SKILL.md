---
name: diagrams-and-tables
description: "Read or explain diagrams and tables, check their meaning, choose a visual form, or construct and visually review one. Route by the task so interpreting an existing view does not require authoring or renderer guidance."
metadata:
  version: "0.9.0"
---

# Diagrams and tables

Start with the user's question and the existing view, caption, legend and source.
Keep what the view states separate from what the underlying system proves.
Document ownership and navigation belong to project-docs.

## Select the task

| Task | Guidance to load |
| --- | --- |
| Read or explain an existing view | Use the reading guidance below; load family reading notes only for relevant notation |
| Apply a view to a particular case | Trace the case through its stated relationships and report matches, conflicts or unknowns; use reading notes as needed |
| Review meaning or accuracy | Use [semantic review](references/review.md) and relevant reading notes |
| Choose a form or outline a proposed view in prose | Use [form selection](references/select.md); family reading notes supply meanings without drawing rules |
| Create, restructure or change diagram source | Use the family's guide below, or shared construction guidance when no family guide exists |
| Review visual readability | Use [verification](references/verification.md); load construction guidance only if repairing the view |

Infer the route from the request. Reading does not imply an accuracy audit, redraw
or renderer search. A missing relationship stays unresolved when explaining a
view; proposing one belongs to authorized design work. A literal label correction
needs a focused meaning check and, if it changes a diagram, a rendered check of
that change; it does not require redesigning the system.

## Read the relevant meaning

Follow the supplied legend and scope before assuming a notation. For tables, use
row/column headers, units, footnotes and explicit unknowns; a blank does not prove
zero, absence or permission. For diagrams, explain the relevant nodes and edge
ends, direction and labels. Do not infer chronology, ownership, cardinality or
network access from an arrow whose meaning is unspecified.

- Workflow steps and branches: [read a flowchart](references/flowchart/read.md).
- ER notation: [read an ER](references/er/read.md).
- Data movement: [read a data-flow view](references/data-flow/read.md).
- For other forms, use the declared notation and project definitions. Seek an
  authoritative notation reference only if the answer depends on an unfamiliar
  symbol; a routine reading task needs no construction manual.

Cite the portion that supports the answer. Distinguish explicit statements,
interpretation and missing information. Applying a view does not itself authorize
changing data or executing the process it describes.

## Construct only when needed

- Flowcharts: [family guide](references/flowchart/guide.md).
- ER: [family guide](references/er/guide.md).
- Data flow: [family guide](references/data-flow/guide.md).
- Other diagrams: [composition](references/composition.md) and
  [verification](references/verification.md); add [Mermaid](references/mermaid.md)
  when using that renderer syntax.
- Designing or restructuring a table: [tables](references/tables.md). Filling an
  existing scaffold preserves its columns, meaning and uncertainty without loading
  construction references.

Family guides own notation, examples and external source links. Shared layout and
rendering conventions stay at the reference root. Use examples only when useful.
New or changed diagrams require grounding and visual inspection in the target
renderer. Report unavailable checks separately; parsing does not prove readability.
