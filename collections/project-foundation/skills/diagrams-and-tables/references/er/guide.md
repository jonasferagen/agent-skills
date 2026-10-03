# Entity-relationship diagrams

Use this reference when the task already calls for an ER view of entities and
relationships. State whether it describes a conceptual model, proposed schema or
implemented schema. The model or schema owns meanings and constraints; this
reference owns their representation.

## Read, review or construct

- To answer a question from an existing ER, follow the relevant relationships
  and consult its model or glossary for meaning. Report ambiguity; reading alone
  needs no redraw, renderer discovery or construction references.
- To review semantics, compare entities, role scope and both ends of each relevant
  relationship with its source. Keep proposals and unknowns visible. Use
  [verification](../verification.md) for a visual review or changed diagram.
- To create or change an ER, keep one canonical view focused on the reader’s
  question, using established terms. Read verification and the notation below.
  General flowchart drawing guidance is unnecessary for an ER-only task.

A field table helps only when attributes answer another needed question. Avoid
repeating the same inventory in prose. A conceptual view can omit attributes;
it must not imply implemented foreign keys or invented types. Unknown
cardinalities stay explicit in the model and diagram framing; an illustrative
assumption is not an adopted constraint.

When the view exceeds roughly 10–12 entities or relationship edges, or becomes
hard to trace, read [large ER views](large-models.md) for decomposition and
shared targets. Small views need no decomposition inventory.

## `erDiagram`

Each end’s symbol describes the entity beside it. In
`LEVEL ||--o{ PLACEMENT : contains`, each placement belongs to exactly one level,
and a level contains zero or more placements.

| Meaning | Left end | Right end |
| --- | --- | --- |
| exactly one | `\|\|` | `\|\|` |
| zero or one | `\|o` | `o\|` |
| zero or more | `}o` | `o{` |
| one or more | `}\|` | `\|{` |

Give every relationship a meaning label after `:`; quote labels to avoid keyword
collisions. Use identifiers without spaces, such as `MESH_DEFINITION`, so one
entity cannot be interpreted as two. When showing schema attributes, use the
schema’s actual types and key markers. Omit them for a conceptual view when they
are undecided.

For a focused change, show affected entities and relevant neighbours and link the
canonical model for the rest. Preserve relationships that matter to the question.
Use layout features supported by the project’s renderer; check compatibility
before relying on optional ER direction or grouping features. Verification owns
renderer discovery and reporting limits.

## Sources and conventions

[Mermaid's ER documentation](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)
owns renderer syntax and cardinality notation. This collection's decomposition
thresholds and document placement are authoring conventions, not ER standards.
Read [examples](examples.md) only when a worked model would help.
