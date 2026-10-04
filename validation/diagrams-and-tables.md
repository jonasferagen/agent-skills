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
| A subgraph is added without an inner direction declaration | Add `direction TB` to express the intended layout, then inspect the target render. Links from internal nodes to outside nodes can cause the subgraph to inherit its parent's direction; the declaration does not guarantee placement or readability. |
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
| ER subgraphs are proposed to keep a crowded model in one block | Check the target renderer's Mermaid version; subgraphs are not a substitute for splitting: past roughly 10–12 entities or a comparable edge count, the model is split whether or not the renderer supports ER subgraphs (Mermaid 11.17.0 or newer). |
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

## Resolutions — 2026-09-30

The owner accepted every recommendation from the contradiction review. Mermaid
behavior was checked by rendering scratch diagrams with Mermaid 12.0.0 (CLI
12.0.0), 11.17.2 and 11.16.1 (both through CLI 11.17.0).

- `erDiagram` layout controls: the ER family example said the type "has no
  layout controls" and the family map said a flowchart gains rank control
  "the `erDiagram` never had", against the manifest and `drawing.md`. The
  example now says direction or subgraphs would arrange the same edges without
  reducing them, and the rank-control clause is gone. Mermaid 12.0.0 and
  11.17.2 render ER `direction` and subgraphs; 11.16.1 has direction only.
- ER-subgraph scenario: it split a model only if its relationships remained
  hard to trace. It now matches the manifest and `drawing.md`: split past the
  threshold, with or without subgraphs.
- Decision matrix: no option was marked as chosen, and reversibility ruled out
  only one of three. **bake at publish** is marked chosen, matching the
  before/after example's target, and the prose names reversibility and the cost
  of being wrong as what outranks effort.
- Family map: the dotted edges had no stated meaning, and the text said both
  hubs stayed out of the graph although game-core is drawn. The dotted edges
  now mark families holding a `blob` foreign key, and the text says neither hub
  is drawn as a table-level node; the map carries them only as family edges.
- ER cardinality: one sentence mixed left- and right-end symbols and omitted
  `o{` and `|{`. `drawing.md` now says each end's symbol describes the entity
  beside it and tabulates both ends; checked against Mermaid 12.0.0 markers.
- ER labels: `drawing.md` now says to quote a label that is a cardinality word;
  unquoted `: one` and `: many` failed to parse on 12.0.0 and 11.17.2.
- ER subgraphs on older renderers: `drawing.md` now says Mermaid 11.16.1 draws
  `subgraph` and `end` as entities instead of failing, and that the renderer's
  Mermaid package version, not its CLI version, decides support.
- Blank cells: the manifest's "blank cell" and "empty cell" read against
  "Fill every cell". The manifest now names the gap, and the cell nobody can
  fill written as `unknown` or `none`.
- Before/after layout: `drawing.md` said a before/after pair's reading order
  "belongs in a vertical stack", against the side-by-side lanes elsewhere. It
  now says the layered pattern does not apply to such a pair: use side-by-side
  lanes, or stack them when reading order must be guaranteed.
- Model list: the manifest named five of the ten worked examples as if
  complete; it now names all ten, grouped.
- Subgraph split: "it should be a separate diagram" had two possible subjects.
  The manifest now gives each case its own sentence.

No Mermaid block changed, so none was rerendered for the package; the family
map and ER example were rendered in light and dark themes to check the new
prose against them.

## Discovery routing — 2026-09-30

The description was shortened and conditional entrypoint guidance moved to references. See [the discovery review](discovery.md) for the measured sizes, scope and verification. Earlier behavioral results do not establish the new discovery behavior.

## Table reading route — 2 October 2026

Version 0.3.0 addresses observed bootstrap reading overhead. The entrypoint now
contains the form-choice table and routes simple tables to `references/tables.md`.
The existing table guidance moved there without changing its rules. Diagram
composition, relationship verification, Mermaid drawing and worked examples remain
conditional on the selected task. No diagram sources or rendering mechanics changed.

Package validation and whitespace checks passed. The follow-up bootstrap trial
is recorded in `validation/atlas-bootstrap-experiment.md`; no reading reduction
is claimed from the reference split alone.

## Selection and conditional construction — 2 October 2026

Version 0.4.0 shortened the entrypoint to form selection and task-specific routes.
Filling existing tables needs no construction references; actual diagrams still
require composition, grounding and visual verification. Project-docs 2.1.0 reads
its diagram-placement reference only for diagram tasks. Independent bootstrap and
diagram outcomes, including their limits, are recorded in
[the experiment](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/atlas-bootstrap-experiment.md#selection-only-routing-trial--2-october-2026).

Version 0.5.0 adds the distinction between workflow, participant interactions,
object state transitions and entity relationships. It moves ER composition and
Mermaid ER syntax to `references/er-diagrams.md`, and moves the remaining table
syntax from drawing to tables. Existing ER examples and rules are preserved;
new framing distinguishes conceptual/proposed models from implemented schema.
Author review checked that a validation pipeline selects flowchart, request/reply
ordering selects sequence, one object's allowed transitions select state, and
stored entity relationships select ER. These are author-reviewed selection cases,
not additional agent trials. No changed diagram was rendered.

## ER routing follow-up — 2 October 2026

The [ER routing trial](er-routing.md) tests a direct ER route, conditional
large-model guidance, and reading an existing model without diagram construction.

## Diagram reference families — 2026-10-03

Version 0.7.0 moves ER guidance to references/er/guide.md, decomposition to
er/large-models.md, and ER worked models to er/examples.md. Shared drawing syntax
is renamed mermaid.md. Data-flow has its own guide and context/detail examples.
Deployment remains future work; no empty family is introduced.

All existing example diagram blocks were compared with the prior commit and are
verbatim. The extracted ER example sections preserve their content, with the trailing blank
line removed; guide edits adjust
relative links and add an official syntax source/convention distinction. Old active
reference paths were checked and updated; dated trial records preserve their original
paths. Consumers must update the whole collection when adopting these moved paths.

The data-flow guide distinguishes information movement from timing, control flow,
connectivity and ownership. It labels the compact Mermaid shapes as collection
conventions, links OWASP's system-modeling scope and official Mermaid syntax, and
does not impose threat modeling on ordinary diagram work. Source pages were read
on 2026-10-03. Skill-creator, clear-writing, instruction guidance and diagram/table
guidance were applied to the new text and entry routes.

Package validation (25 skills, one collection), skill quick validation, diff checks
and 135 collection local links/anchors passed. Both new examples were rendered
with Mermaid CLI 12.0.0 using external Google Chrome and visually inspected in
light and dark themes. The tall detail was rechecked at natural dimensions after
an 840px maximum-height export reduced its text size; natural labels are readable
without clipping. Existing diagram source was unchanged and was not rerendered.
Target client rendering remains untested.

A fresh fixture trial selected the data-flow guide from the installed collection
and interpreted both ER endpoints through the moved ER guide. The reviewer read
the complete [result](diagram-family-trial/result.md) and
[report](diagram-family-trial/report.md). It preserved unknown byte retention and
delivery mechanics rather than inventing them. The report records about 4,303
guidance/request words, no repeated content reads and no truncation.

The evaluator unnecessarily read composition and verification for a prose outline.
The guide now explicitly reserves those routes for creating/changing diagram source
and says prose outlines use semantic guidance only. This targeted correction was
author-reviewed after the trial; no reduced-read claim or fresh rerun is made. The
ER question was in the same context; diagram construction and native discovery were
not exercised by the trial.

## Task routing — 2026-10-03

Version 0.8.0 routes reading/application, semantic review, form selection,
construction and visual review separately. ER and data-flow families now have
read.md and design.md behind their existing guide.md entry points. Interpretation
retains cardinalities, role meanings, explicit unknowns and observed/proposed
distinctions. Construction retains grounding, syntax, decomposition and rendering.

Form selection moved to select.md; semantic review has a focused review.md. Table
reading uses headers, units and missing-value meanings without loading table
authoring. Literal label corrections retain a focused meaning/render check; they
do not trigger system redesign. No existing Mermaid example source changed.

The task pattern was read from the separate project-contracts 0.2.0 worktree at
484daf8. The user subsequently authorized landing both branches. Its existing five
mode trials and validation record remain that change's evidence.

Two fresh evaluators used isolated installed fixtures based on 289f852 plus this
draft. Neither received an expected route. [Read answer/log](diagram-task-routing-trial/read/reads.md)
shows direct entry-to-ER-reading routing: correct zero-or-more interpretation and
no inferred database constraint, with no construction, review or renderer reads.
[Construction answer/log](diagram-task-routing-trial/create/reads.md) shows family
guide, design, notation and verification routes while omitting examples, large-model
and flowchart guidance. The author inspected both complete answers and read logs.

No content reads were repeated or truncated. Construction reported about 3,876
input words; foundation-authority and prose guidance included some unnecessary
material for the small fixture. These different tasks are not a before/after
context-cost comparison. One case per route does not establish discovery reliability.
Table application, semantic review, visual-review-only and the new data-flow reading
route were source-reviewed but not independently trialled in this round.

The parent rendered the construction output with Mermaid CLI 12.0.0 and external
Google Chrome, inspecting light/dark output. Cardinalities, labels and unknown
implementation status matched the fixture; no clipping or overlap was observed.
Existing package diagram blocks were mechanically checked unchanged. Package
validation, skill quick validation, 156 collection links/anchors and diff checks
passed before integration. No runtime or client-native discovery claim is made.

## Flowchart family — 2026-10-03

Added conditional reading, construction and example guidance for action flow,
branch conditions, loops, meaningful outcomes and actor responsibility. Form
selection distinguishes Mermaid's flowchart syntax from the semantics of a
component/context view. Existing family routes remain available.

The synthetic review-loop example rendered with Mermaid CLI 11.16.0 at 800px
in light and dark themes and was visually inspected. Labels and outcomes are
readable; ordering the pause branch before the repeat branch removed an edge
crossing in the tested renderer. No target
GitHub/editor preview was available, so cross-renderer parity is unverified.
Mermaid's official flowchart documentation was consulted for syntax; the workflow
semantics are explicitly collection conventions, not formal BPMN/UML compliance.

The planning consumer trial correctly interpreted a flowchart-syntax repository
map as handoff responsibilities without loading construction or renderer guidance.
See project-planning validation for its read log and limitations. Clear Writing
kept branch requirements scoped to depicted behavior; no provider retry guarantee
is implied by the synthetic loop.

A second fresh consumer trial created the proposed review workflow and inspected
light/dark renders at 760px. Its output preserved acceptance, revision and pause,
left unspecified feasibility ownership/resumption visible, and did not add
publishing. It reached the flowchart family and required construction references.
The recorded read log counted 7,259 words across 16 files, with no repeated or
truncated reads; foundation-format was avoidable with the missing foundation.
The trial render retained a visible crossing; the separately verified bundled
example removes it. No source-repository instructions or live systems were used.
The trial used the family before the example's final layout-only adjustment.


## Standalone source after framework extraction — 4 October 2026

Version `0.11.0` is owned at `skills/authoring/diagrams-and-tables`. Package-local references,
examples and UI metadata remain together. The entrypoint now follows declared
project authority and repair routes instead of requiring project-foundation.
Earlier dated records retain their original tested source identities.
Migration routing evidence is recorded in [the extraction review](framework-extraction.md).

## Agent-led work and swimlane activities — 2026-10-04

Version 0.12.0 adds a responsibility-oriented form-selection route, separate
reading and construction references, and a method-labelled synthetic example.
The observed need came from a repository browser whose dependency map was useful
but did not explain agent instructions as a mechanism for doing work. The generic
addition applies when responsibility and method explain the handoff; it does not
select orchestration or turn every process into an API. Exact interaction order
still routes to sequence diagrams. Native project workflow guidance is integrated
in project-foundation; generic notation stays here.

Consulted Mermaid's official swimlane and flowchart documentation and OMG BPMN
2.0.2 for notation boundaries. Swimlanes are documented from Mermaid 11.16.0 with
evolving swimlane-beta syntax. Actor-labelled flowcharts provide a compatible
alternative. Agent instruction-following does not imply BPMN Manual Task semantics.
No custom standard agent symbol, mandatory human gate or fixed method taxonomy is
introduced. Clear Writing and pattern-capture informed the scoped wording.

Both bundled examples rendered using cached Mermaid 11.16.0, in light and dark
themes. The swimlane render was inspected at 1000px, the fallback at document
width (760/900px); labels, lane headers and conditional handoffs were readable
without clipping. An initial back-edge put the review before preparation in the
layout. The retained example separates accepted and revision outcomes, with the
repeat point stated explicitly in the caption. These are detail views, not a
claim that a full process diagram fits a compact landing page. No runtime
renderer dependency was added; Forge's custom renderer remains unverified for
swimlane-beta.

[Three fresh routing trials](agent-workflow-trial/README.md) exercise interpretation,
deeper design and a nearby sequence question. The reading trial retained proposed
status and delegated authority without inventing APIs or services. The sequence
trial avoided swimlane construction and kept missing protocol ordering explicit.
The design artifact and its limits are retained with the trial evidence.

Required source checks passed: package validation and all four maintained helper
suites (92 tests), plus git diff --check. Rendered inspection is separate from
structural validation. This source revision is not a published tag or consumer
installation.
