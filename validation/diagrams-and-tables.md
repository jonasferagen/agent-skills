# Validation and alignment — Diagrams and tables

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation or a live render.

| Request and context | Expected outcome |
| --- | --- |
| A paragraph describes what connects to what across five components | A diagram is drafted before the prose; the paragraph then carries only what the shape cannot. |
| A subject is a decision, a trade-off, a gotcha or a convention | Stays prose; no diagram is drawn for it. |
| A change alters fields, options, flags or permissions per item | A before/after table, not before/after lanes; neither lane layout suits a per-item delta. |
| A change alters stages in a flow | Before/after lanes, made comparable: same granularity, same vocabulary, one node per surviving stage. |
| A subgraph is added without an inner direction declaration | Flagged: without `direction TB` the subgraph lays out left to right whatever the parent says, overflowing the column and shrinking labels. |
| One block tries to show both how a system fits together and what happens inside its most complex part | Split by altitude: the overview keeps that part as a deliberate black box; the detail opens it. |
| A subject appears to need a third altitude | Redirected to a document with sections rather than a diagram with deeper nesting. |
| A form change is reported as a line-count reduction | Rejected as a measure: a line count after a form change describes cell width more than reader load. Words are measured instead. |
| A diagram already exists elsewhere for the same question | Linked rather than redrawn, so a correction lands once. |
| An edge is drawn from memory of how the system probably works | Flagged: each relationship is verified against whatever owns it — schema for a stored link, implementation for behavior, configuration for what is deployed, an explicit decision for anything planned. |
| An edge is labelled with a column name | Relabelled with its meaning; *belongs to* or *creates after approval*, not a foreign key's name. |
| Owner, payer, actor, identity and permission are collapsed into one node to simplify | Refused where the domain distinguishes them. |
| A conceptual map omits cardinality | Accepted, provided it does not imply a certainty it lacks; optionality, uncertainty and proposed behavior are marked where omission would mislead. |
| A layout group is added for spacing | Checked that it does not read as a domain entity it is not. |
| Several nodes are instances of one type | Their roles are named — *parent task*, *subtask* — rather than the type name repeated. |
| A diagram parses successfully | Not accepted as a readability check; it is rendered and inspected at the width a reader gets. |
| A diagram is readable in light mode | Dark mode and any other theme readers use are checked too, because a diagram type may color text, nodes, rows, labels and edges separately. |
| Meaning is carried by color | Flagged; color alone is not sufficient. |
| A diagram is too wide at reading width | Reflowed or split, rather than shrunk further. |
| ER subgraphs are proposed to keep a crowded model in one block | Check the target renderer's Mermaid version (ER subgraphs need 11.17.0 or newer), then split the model if its relationships remain hard to trace. |
| Rendering documentation would need a new application dependency | Refused; temporary output is used for visual checks unless the project's renderer needs a committed image. |
| Deciding where a diagram lives in a document set | Deferred: this skill owns form choice, drawing and verification; the owning surface decides placement, discoverability and catalog entry. |
| Adopting the skill into an existing project | No redrawing of existing diagrams is implied, and an established visual format the project already follows takes precedence. |

## Scope boundaries

Owns **form choice** (which form carries a subject, at what altitude), **drawing**
(direction, subgraphs, `erDiagram`, table mechanics, portable syntax) and
**verification** (evidence grounding before, readability after). It applies wherever
text is authored — docs, skills, plans, issue bodies, durable comments, design
records, review feedback.

It does not decide where a form lives. Placement, discoverability, freshness review
against a source, and catalog entry belong to the owning surface; for a documentation
set, `project-docs` owns those and its own diagrams reference covers them.

Mermaid is the assumed text format. The layout and altitude rules generalize; the
specific syntax and the renderer caveats do not.

## Sources inspected

Merged on 2026-09-29 from two sources.

The bulk is the owner's Forge Agent Kit `diagrams` skill at
`c98147a115a30f36b952df5faf1c869b54480c59` (2026-09-18): form choice, the
underused-tables argument, draw-less-link-more, vertical-and-one-altitude, the
drawing reference and ten worked examples.

Two sections are newly written from `project-docs`' own diagram conventions, which
upstream did not cover: grounding every edge in the source that owns it, and
verifying that a diagram reads in the renderer and themes its readers use. The
sharpest line in the second — a successful parse is not a readability check — came
from that local reference, which had recently gained the theme-checking rule.

Adaptations: upstream's handoff to its sibling documentation skill became a
description of the boundary, because each skill directory is the installable unit
here and a cross-package path would break when this skill is installed alone.
Three provenance citations naming a private repository and commit were replaced
with neutral descriptions, and one worked example's table prefix was renamed, so
the package carries no project identifiers while keeping the real shapes and
counts those examples depend on.

`project-docs` was reduced in the same change to what is particular to a
documentation set — which document owns which view, glossary-led terms, freshness
as part of doc review — so the craft has one home rather than two that drift.

## Review limits

- No independent agent evaluation has run against these scenarios.
- On 2026-09-29, all 19 Mermaid blocks in
  `skills/diagrams/references/worked-examples.md` rendered with Mermaid CLI 12.0.0
  and Chrome in light and dark themes. The two ER detail diagrams were also
  inspected at an 830 px document width in both themes.
- The examples have not been checked in every consuming project's publishing
  renderer. Their shapes come from real repositories; their entity names do not.
- The two new sections have not been reconciled against the consuming projects'
  existing diagrams, which were drawn under the narrower local reference.

## Project foundations naming — 2026-09-30

Version 0.1.1 changes the display name and heading to “Diagrams and tables” and
shortens the UI description. The installation name remains `diagrams`; drawing
instructions and examples are unchanged. Package and skill-creator validation
passed. No diagram was changed or rerendered for this metadata update.

## Clear writing pass — 2026-09-30

Version 0.1.2 revises the prose around the diagrams; see the [package
sweep](clear-writing.md#package-sweep--2026-09-30). Idioms such as "hairball",
"puzzle" and "from across the room" were replaced, and ambiguous references were
resolved. The description's last clause was reworded with its triggers kept. No
diagram source changed, so none was rerendered. Review found the meaning
preserved; six wording corrections restored distinctions such as "cheapest"
crossings and a "lower-altitude" owner.

Left unresolved, because each answer changes behavior:

- `worked-examples.md` says `erDiagram` has no layout controls, while the
  manifest and `drawing.md` describe ER direction and subgraphs in current
  Mermaid. The example may describe an older renderer but reads as current.
- The ER-subgraph scenario above splits a model only if its relationships remain
  hard to trace; the manifest and `drawing.md` split past the threshold.

## Rename — 2026-09-30

Version 0.2.0 renames the installation name from `diagrams` to
`diagrams-and-tables`, so the name shows that the skill covers tables and
matrices as well as diagrams. The display name, instructions and examples are
unchanged. Consumers that copied the package under `.agents/skills/diagrams/`
keep working at their pinned commit; they move the directory and update their
provenance when they next update the pin. Earlier entries on this page use the
old name as it was at the time.

## Package pass — 2026-09-30

The skill was applied to its own package and to the seven other packages revised
in the Clear Writing package sweep. For each package, one agent checked the
existing diagrams and tables and looked for prose that a structured form would
explain better; a second agent reviewed every change. The literal comparison
script, the heading-anchor scan and package validation passed.

| Package | Result |
| --- | --- |
| `diagrams-and-tables` | Three corrections in the worked examples: the set-finalization detail now enters from the two seams its overview draws; the schema-change diagram is captioned as the touched entities after the change; and "the nine that were easy" now reads "seven", matching the coverage matrix. The changed detail was rendered in light and dark themes. |
| `typescript-patterns` | Three passages became tables: shape escalation, type-only files in family and subsystem directories, and the shapes of a closed-union switch. Review corrected one quantifier in the last. |
| `change-workflow`, `test-audit`, `postgres-design`, `project-docs`, `runtime-operations`, `source-of-truth` | No change. Existing tables were complete and grounded; each candidate conversion would have dropped a qualifier, invented a value or settled a question the text leaves open. |

4 of 36 files changed. Most passages in these packages are connected reasoning,
which the skill keeps as prose. Several candidate tables were blocked by
contradictions in the source; each package's validation page records them.

Left unresolved in this package:

- The decision-matrix example does not say which option was chosen; its stated
  reason, reversibility, rules out only one of the three.
- The family map's dotted edges have no stated meaning, and the text says both
  hubs stay out of the graph although game-core is drawn.
- `drawing.md` lists four ER cardinality symbols in one sentence, mixes left-
  and right-side forms, and omits `o{`, which its own examples use, and `|{`.
