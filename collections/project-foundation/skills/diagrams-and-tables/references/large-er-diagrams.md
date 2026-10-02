# Large entity-relationship views

Read this when an ER view exceeds roughly 10–12 entities or relationship edges,
or when crowding makes relationships hard to trace. Use
[composition](composition.md) for overview/detail ownership and
[verification](verification.md) for rendered checks.

## Split a large ER view

An `erDiagram` has its own, lower split threshold: **past roughly 10–12
entities, or a comparable number of relationship edges, split the block**.
Current Mermaid supports ER direction and subgraphs, but subgraphs require
Mermaid 11.17.0 or newer; check the target renderer before using them. Neither
control makes a crowded relationship map easy to read. Trimming attributes to
keys and moving column detail to a companion table makes entities narrower, but
it does not raise this ceiling because it fixes width, not the number of
relationships a reader must trace.

Split a large ER model by **aggregate cluster**, as the ER-specific instance of
the overview/detail pattern in [composition](composition.md). The root-only overview names
every aggregate root and draws only relationships directly between roots; it
does not open their children. One compact detail diagram per non-atomic root
then opens that root's owned children and join tables. Apply the black-box
disposition inventory to roots too: a root with no load-bearing internal shape
may stay intentionally atomic, while detail owned elsewhere is linked rather
than redrawn.

**When the root-only overview is itself over threshold, raise the altitude
instead of splitting again.** A schema with dozens of aggregate roots has no
useful ER split left beneath it. Group by ownership — one node per document,
page, or migration family that owns the entities — and label each edge with the
number of references crossing that boundary. The nodes stop being tables, so the
block becomes a `flowchart`, showing ownership groups and their dependencies.
Use layout features supported by the target renderer. The flowchart answers a
different question from the diagram it replaces — which groups depend on which,
and the layer order that implies — while each group's own page keeps every
individual relationship at full cardinality.

See [the worked ER split](worked-examples.md#a-large-er-family-split-by-aggregate-cluster)
for the matching stub-elision rule on an aggregate-sized family, and
[the whole-schema overview](worked-examples.md#an-over-threshold-overview-raised-to-its-owning-documents)
for the ownership grouping and the fan-in tables that keep its hubs from being
drawn as table-level nodes.


## Shared targets

Keep cross-family targets in a detail view when their cardinality matters to its
question. Otherwise link their owner or identify them in the field detail. When
a shared target creates a dense hub, a companion table can list its referencing
entities; preserve each relationship’s meaning and cardinality there. Use
[table guidance](tables.md) when designing that companion.
