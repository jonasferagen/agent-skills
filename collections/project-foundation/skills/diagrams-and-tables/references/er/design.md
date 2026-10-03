# Construct or change an ER diagram

Use [reading notes](read.md) for notation; reuse a current reading. Keep one
canonical view focused on the reader's question, using established terms. Use
[verification](../verification.md) to ground and visually inspect changed diagrams.
General flowchart drawing guidance is unnecessary for an ER-only task.

A field table helps only when attributes answer another needed question. Avoid
repeating the same inventory in prose. A conceptual view can omit attributes;
it must not imply implemented foreign keys or invented types. Unknown
cardinalities stay explicit in the model and diagram framing; an illustrative
assumption is not an adopted constraint.

When the view exceeds roughly 10–12 entities or relationship edges, or becomes
hard to trace during construction, read [large ER views](large-models.md) for decomposition and
shared targets. Small views need no decomposition inventory.

Give every relationship a meaning label after `:`. Quote labels containing
spaces or reserved words to avoid parsing ambiguity. Use identifiers without spaces, such as `MESH_DEFINITION`, so one
entity cannot be interpreted as two. When showing schema attributes, use the
schema’s actual types and key markers. Omit them for a conceptual view when they
are undecided.

For a focused change, show affected entities and relevant neighbours and link the
canonical model for the rest. Preserve relationships that matter to the question.
Use layout features supported by the project’s renderer; check compatibility
before relying on optional ER direction or grouping features. Verification owns
renderer discovery and reporting limits.

Read [examples](examples.md) only when a worked model would help. This collection's
decomposition thresholds and document placement are authoring conventions, not ER
standards.
