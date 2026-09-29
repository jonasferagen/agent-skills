---
name: diagrams
description: "Apply the smallest useful diagram, table or matrix when authoring or revising docs, skills, plans, issues, comments, design records and review feedback. Use whenever a structured form might beat prose: a paragraph describing what connects to what, a flow or lifecycle across more than about three components, a schema or data-model change, options or tiers that want one row each, a diagram grown too wide to read, a decision or coverage matrix, or a relationship whose cardinality matters. Reach for it before writing the prose, and again when a diagram needs splitting by altitude, grounding in its source, or checking for readability in the renderer its readers use. Owns form choice, drawing and verification; where a form lives is the owning surface's call."
metadata:
  version: "0.1.0"
---

# Diagrams

Apply these conventions wherever a task authors or revises prose, a diagram, or
an overview table — docs, skills, plans, issue bodies, durable comments, design
records, prompts, and review feedback alike. **Before drafting or rewriting a
substantive artifact, ask whether its central facts have a smallest useful
structured form; keep simple claims, why, gotchas, decisions, and conventions as
brief prose.** When the detail would outgrow the artifact, link one canonical
detail owner rather than copying it; in a skill, that owner is normally a
bundled `references/` document.

This skill owns **form choice**: which form carries a subject, at what altitude,
and how it is drawn. Where a form lives is the owning surface's call. For a
documentation set, that owner decides the form's placement, discoverability,
freshness review against its source, catalog entry, and when an index hands its
detail to the owning document; it also decides that a system document opens with
a brief overview. This skill decides only whether that overview wants a diagram
or a table, and which — concise prose is the right overview when there is no
relationship, flow or ownership shape to show. Where a project documentation
skill is available, it owns those placement rules.

- **How to draw it** — direction, subgraphs, `erDiagram`, table mechanics, and
  portable syntax — is in [references/drawing.md](references/drawing.md). Read
  it before writing a Mermaid block.
- **Models to copy** — an overview/detail split, before/after lanes, a
  schema change, a coverage matrix, a decision matrix — are in
  [references/worked-examples.md](references/worked-examples.md). Read it once
  the form is chosen.

Two steps bracket the drawing itself: [ground every edge in its
source](#ground-every-edge-in-its-source) before drawing, and [verify that it
reads](#verify-that-it-reads) in the renderer its readers use afterwards. A
diagram that parses is not yet a diagram that works.

A repository-specific _diagram catalog_ is different again: it indexes the
diagrams a repository owns and points at their canonical docs. Conventions here;
inventory there.

## When to diagram

When a doc describes flow, structure, or lifecycle across more than about three
components, sketch a Mermaid block **before** writing the prose — the topic is
_what connects to what_, _in what order_, or _what shape_.

**A diagram on its own is usually a puzzle** — pair it with a short framing
paragraph and outbound links to deeper docs.

## The job is the central concepts, not decoration

A diagram earns its place by handing a reader the subject's **central concepts
at a glance** — the pieces that matter, how they relate, and, when something is
changing, how the shape differs afterward. That is the test to apply before
drawing: name the one question the reader arrives with, and draw the answer.

It follows that **a paragraph describing what a structured form would have shown
is a paragraph the reader has to re-derive.** Prefer the structured form
wherever one fits:

| Subject | Form to reach for first |
| --- | --- |
| Flow, sequence, lifecycle, component wiring | Flowchart — before/after when it changes |
| Schema, storage, or data-model change | ER diagram, plus a table-and-column overview of the delta |
| Tables, columns, indexes, or migration steps | Table: name, type, nullability, what changes |
| Options, states, tiers, per-surface obligations | Ordinary table, one row per case |
| Why, gotchas, decisions, trade-offs, conventions | Prose — no diagram carries these |

That holds wherever the text is authored: draw the shape, then write the prose
the shape cannot carry.

**Two forms, never three.** When an ER diagram and a column table both apply,
the diagram carries the relationships and the table carries the field-level
delta. The prose beneath restates neither.

## Draw less: link the diagram that already exists

Preferring the structured form is not licence to fill the page with blocks.
Budget it: a README usually gets one compact thumbnail; a deep doc usually gets
one or two detailed diagrams. That is an attention budget, not a hard block
count. When one canonical overview owns several independently complex black
boxes, the overview and its compact per-box details form **one two-altitude
diagram set**; that set may contain one detail per important box. Do not spend
that exception on boxes whose detail belongs to another canonical owner, or on
extra diagrams that answer unrelated questions. Past that, each new block costs
the reader attention and costs the repository another surface to keep true.

**Before drawing, look for the diagram that already exists** — in the owning
doc, in the design record, in the plan or issue that decided the shape. Link it.
A redrawn copy is a second home for one fact, and the copy is the one that
drifts, silently, because nobody knows it is there to update.

- **In an issue body, a plan, or review feedback, link the canonical diagram and
  draw only the delta.** Those texts are read once and never maintained; a full
  system diagram pasted into one is stale within a sprint and outlives the
  discussion that justified it.
- **Redraw only when the existing diagram answers a different question.** A
  different altitude or a different audience is a reason; wanting the picture
  inline is not.
- **A diagram that would restate the paragraph above it earns nothing.** Cut one
  of them.

**Audit an existing over-threshold diagram before redesigning it.** Those rules
fire while authoring something new; a block that has already outgrown its
threshold needs one mechanical measurement first. For each element it draws, ask
whether a canonical owner below already carries that element — the same fact,
with the same or better fidelity. A low duplicated fraction means the block is
genuinely dense, and the altitude split below is the fix. A high fraction is a
different diagnosis: the block owns nothing, so delete it and draw the altitude
**above** it instead. Take that measurement before choosing the remedy, because
splitting a fully duplicated block yields a correctly-split set that still
duplicates every fact.

## Tables and matrices are underused

A table is the cheapest structured form there is: it renders everywhere, diffs
line by line, needs no syntax discipline, and survives being quoted into an
issue. **Reach for one earlier than feels natural** — most prose that enumerates
anything is a table that was never drawn.

**The test is shared fields, not item count.** Items carrying the same fields
are a table however few of them there are: three items × three fields is one
scan down a column instead of three sentences to parse. Items sharing no
structure stay prose however many there are — ruling a list of unrelated
statements gains the reader nothing. A short parallel set is exactly where a
table pays, so counting rows is the wrong question to ask first.

Five shapes carry most cases:

| Shape | Rows × columns | What it exposes |
| --- | --- | --- |
| **Delta table** | one field or option × before, after, migration | exactly what changes, at field altitude |
| **Decision matrix** | one option × each criterion | why the chosen option wins, and what it costs |
| **Coverage matrix** | one surface × each obligation | the blank cell nobody had noticed |
| **Registry table** | one term × status, canonical meaning | which name is current, and what replaced the rest |
| **Fan-in table** | one referencing entity or group × what it reaches | who depends on a hub, without drawing the hub |

The coverage matrix is the one to reach for deliberately: prose can describe
every surface in turn and never reveal that one of them answers nothing, whereas
an empty cell is visible from across the room.

The fan-in table is the one that rescues a diagram. **A shared target reached by
many entities belongs in a table rather than as a drawn hub** — it is the most
expensive node a graph layout can carry, since its edges cross every other edge
in the block, while a table shows the same dependency with no crossing at all.
Put the target in the heading, one referencing entity or group per row, and keep
the hub out of the drawing.

### What choosing a form buys

A structured form buys **scannability, not brevity**, and the two are easy to
confuse when reporting a restructure. Converting wrapped prose into a table
collapses the line count while barely moving the word count, because the words
were never what made the passage slow to read — one table row holds what four
wrapped lines held. Measure words before claiming a document got shorter. A
line count after a form change describes cell width more than it describes how
much the reader has to take in, and a reviewer told "150 lines to 115" will
believe it.

## Keep it vertical, and keep it at one altitude

**Vertical is the default** — `flowchart TB`, and **`direction TB` as the first
line inside every subgraph**. The inner declaration is the one that decides
readability: without it a subgraph lays its chain out left to right whatever the
parent chart says, and the block overflows the column, shrinking its label text
until the reader is worse off than with no diagram at all. A before/after pair
may sit side by side once each lane is vertical and the pair still fits the
target column; stack it when it does not. Make the two lanes **comparable** —
same granularity, same vocabulary, one node per surviving stage — so the delta
is what differs between them.

**When the delta is per-item rather than per-stage** — fields, options, flags,
permissions — neither lane layout is right. Use a before/after table.

**One diagram, one altitude.** The widest, least readable diagrams come from a
single block trying to show both how the system fits together *and* what happens
inside its most complex part. Split it:

- The **overview** keeps that part as a **single node**, deliberately a black
  box. Its job is what connects to what.
- A **detail diagram** opens that one node, in the doc that owns it, and gives
  it the full column width it needed all along.
- **Name the seam both ways.** The detail's title or entry node repeats the
  black box's exact label, so a reader knows what they just opened; the overview
  links to the detail.

Before calling an overview complete, inventory **every black box** and give it
one explicit disposition:

| Disposition | Use when | What the overview owes |
| --- | --- | --- |
| **Intentionally atomic** | its internals do not change the overview reader's understanding | say why it stays closed |
| **Compact detail here** | this document canonically owns the box and its internals are important | open it at the next altitude and repeat its label exactly |
| **Canonical detail elsewhere** | another document owns the internals | link that owner instead of redrawing it |

This inventory is a construction and review checkpoint, not necessarily a table
that must remain in the finished document. A box is not intentionally atomic
merely because the overview collapsed it. Every box is explicitly classified;
every non-atomic important box is opened or linked.

When several boxes choose **compact detail here**, give each its own diagram at
the same detail altitude. Redraw only the immediate external seams needed to
orient the reader; do not copy the full overview into every detail. Keep a
lifecycle or sequence diagram separate when it answers _in what order_ rather
than _who owns what_ — it is a different question, not another level of the
overview.

An `erDiagram` has its own, lower split threshold: **past roughly 10–12
entities, or a comparable number of relationship edges, split the block**.
Current Mermaid supports ER direction and subgraphs, but subgraphs require
Mermaid 11.17.0 or newer; check the target renderer before using them. Neither
control makes a crowded relationship map easy to read. Trimming attributes to
keys and moving column detail to a companion table makes entities narrower, but
it does not raise this ceiling because it fixes width, not the number of
relationships a reader must trace.

Split a large ER model by **aggregate cluster**, as the ER-specific instance of
the same overview/detail black-box pattern above. The root-only overview names
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
block stops being an `erDiagram`: draw it as a `flowchart` and regain the
`subgraph`, `direction`, and rank control ER layout never had. It answers a
different question from the diagram it replaces — which groups depend on which,
and the layer order that implies — while each group's own page keeps every
individual relationship at full cardinality.

See [the worked ER split](references/worked-examples.md#a-large-er-family-split-by-aggregate-cluster)
for the matching stub-elision rule on an aggregate-sized family, and
[the whole-schema overview](references/worked-examples.md#an-over-threshold-overview-raised-to-its-owning-documents)
for the ownership grouping and the fan-in tables that keep its hubs out of the
graph.

A subgraph is the right tool when the grouping is a handful of nodes the reader
must see in place. **When a subgraph grows past roughly five nodes, or when two
subgraphs in one block are each large enough to stand alone, it wanted to be a
separate diagram.** That local threshold is not the whole complexity test. A
lifecycle is also above the split threshold when the whole block makes the
reader independently understand several stage-level questions, especially a
combination of:

- **multi-input fan-in** whose normalization or precedence matters;
- an **optional or branching middle lane** whose internal order matters; and
- a **long finalization tail** with several meaningful states or handoffs.

All of those nodes may be relevant and still be at the wrong altitude for the
main lifecycle. Relevance asks whether a fact belongs in the subject;
altitude asks whether it belongs in this diagram. When the fan-in, branch, and
tail are each useful on their own, collapse the main lifecycle into stable stage
boxes, then open the stages as focused details. Collapse repeated top-level
inputs and routine finalization states first; preserve ordering only in the
detail whose question depends on it.

Treat those stages with the same black-box disposition inventory as a component
overview: intentionally atomic, compact detail here, or canonical detail
elsewhere. The resulting overview and per-stage details remain one two-altitude
set. Two altitudes are almost always enough; a subject needing a third wants a
doc with sections, not a diagram with nesting.

## Ground every edge in its source

A diagram states facts, and a reader treats a drawn edge as verified. Draw from
evidence, not from memory of how the system probably works.

1. Use terms the project has already defined. A diagram that coins a synonym for
   an existing concept adds a second name for it.
2. Verify each relationship against whatever owns it: the schema for a stored
   link, the implementation for behavior, the configuration for what is deployed,
   and an explicit decision for anything planned.
3. Label each edge with its meaning — *belongs to*, *supports*, *creates after
   approval* — not with a column name. Distinguish owner, payer, actor, identity
   and permission wherever the domain distinguishes them, and never collapse them
   to tidy the picture.
4. Mark optionality, uncertainty and proposed behavior where leaving them out
   would mislead. A conceptual map need not carry every column or cardinality,
   but it must not imply a certainty it lacks.
5. Caption the view with its scope and any interpretation its arrows require,
   especially when one diagram's arrows mean a stored link and another's mean a
   process.

Use one label for one concept across every view in a set. Where several nodes are
instances of one type, name their roles — *parent task* and *subtask* — rather
than repeating the type name. Do not let a layout group read as a domain entity it
is not.

## Verify that it reads

A parse is not a readability check, and neither is your own satisfaction with the
source. Render the diagram with the project's tooling and look at it at the width
a reader gets.

- Check clipped text, colliding edge labels, crossings, runaway width and labels
  shrunk past reading size. Reflow or split the view rather than shrinking it
  further.
- Where the project has a preview or publishing renderer, inspect it there too.
  The source is authoritative, but the reader sees the render.
- Check the themes readers actually use, including dark mode. A diagram type may
  color text, nodes, rows, labels and edges separately, so give text and its
  background compatible colors in each theme, and keep any renderer-specific
  override in the project that needs it.
- Do not rely on color alone to carry meaning.
- Use temporary output for visual checks unless the project's renderer needs a
  committed image. Never add a runtime dependency to an application solely to
  render its documentation.
