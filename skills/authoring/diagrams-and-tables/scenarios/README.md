# Diagrams and tables scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Routing by task

| Request and context | Expected behavior |
| --- | --- |
| Explain the cardinality at one end of an existing ER view | Read the view through the ER reading notes; report zero-or-more as stated, infer no database constraint, and load no construction, review or renderer guidance. |
| Outline a proposed data-flow view in prose | Use form selection and family meanings only; composition and verification are for creating or changing diagram source. |
| Create a diagram from a described workflow | Reach the family guide, design notes, notation and verification; leave large-model and unrelated family guidance unread. |
| Correct a literal label in an existing diagram | A focused meaning check and a rendered check of that change; no system redesign. |
| Interpret a repository map drawn in flowchart syntax as handoff responsibilities | Read it as the responsibilities it states, without loading construction or renderer guidance. |
| Explain an agent-led workflow's swimlane view | Retain proposed status and delegated authority; invent no APIs or services. |
| A question needs the exact order of calls and replies | A sequence diagram, not a swimlane; missing protocol ordering stays explicit. |
| Fill cells in an existing table | Table reading and authoring notes; no diagram construction references. |

## Form choice

| Request and context | Expected behavior |
| --- | --- |
| A paragraph describes what connects to what across five components | A diagram is drafted before the prose; the paragraph then carries only what the shape cannot. |
| A subject is a decision, a trade-off, a gotcha or a convention | Stays prose; no diagram is drawn for it. |
| A validation pipeline, a request/reply exchange, one object's allowed transitions, or stored entity relationships | Flowchart, sequence, state and ER respectively, chosen by the reader's question rather than the nouns. |
| Responsibility and method explain a handoff | A swimlane activity view; it does not select orchestration or turn every process into an API. |
| A change alters fields, options, flags or permissions per item | A before/after table, not before/after lanes; neither lane layout suits a per-item delta. |
| A change alters stages in a flow | Before/after lanes, made comparable: same granularity, same vocabulary, one node per surviving stage. |
| One block tries to show both how a system fits together and what happens inside its most complex part | Split by altitude: the overview keeps that part as a deliberate black box; the detail opens it. |
| A subject appears to need a third altitude | Redirected to a document with sections rather than a diagram with deeper nesting. |
| A form change is reported as a line-count reduction | Rejected as a measure: a line count after a form change describes cell width more than reader load. Words are measured instead. |
| A diagram already exists elsewhere for the same question | Linked rather than redrawn, so a correction lands once. |

## Grounding and meaning

| Request and context | Expected behavior |
| --- | --- |
| An edge is drawn from memory of how the system probably works | Flagged: each relationship is verified against whatever owns it — schema for a stored link, implementation for behavior, configuration for what is deployed, an explicit decision for anything planned. |
| An edge is labelled with a column name | Relabelled with its meaning; *belongs to* or *creates after approval*, not a foreign key's name. |
| Owner, payer, actor, identity and permission are collapsed into one node to simplify | Refused where the domain distinguishes them. |
| A conceptual map omits cardinality | Accepted, provided it does not imply a certainty it lacks; optionality, uncertainty and proposed behavior are marked where omission would mislead. |
| A layout group is added for spacing | Checked that it does not read as a domain entity it is not. |
| Several nodes are instances of one type | Their roles are named — *parent task*, *subtask* — rather than the type name repeated. |
| A table has a cell nobody can fill | Written as `unknown` or `none` on purpose; a blank is not left to read as "not applicable". |
| A decision matrix compares options | The chosen option is marked and the deciding criterion named; a matrix that rules out only one option has not decided. |

## Drawing and verification

| Request and context | Expected behavior |
| --- | --- |
| A subgraph is added without an inner direction declaration | Add `direction TB` to express the intended layout, then inspect the target render. Links from internal nodes to outside nodes can make the subgraph inherit its parent's direction; the declaration does not guarantee placement or readability. |
| An ER relationship label is a cardinality word such as `one` or `many` | Quoted; unquoted it fails to parse on the tested Mermaid versions. |
| ER subgraphs are proposed to keep a crowded model in one block | Check the target renderer's Mermaid version; subgraphs are not a substitute for splitting. Past roughly 10–12 entities or a comparable edge count, the model is split whether or not the renderer supports ER subgraphs (Mermaid 11.17.0 or newer; 11.16.1 draws `subgraph` and `end` as entities). |
| A diagram parses successfully | Not accepted as a readability check; it is rendered and inspected at the width a reader gets. |
| A diagram is readable in light mode | Dark mode and any other theme readers use are checked too, because a diagram type may color text, nodes, rows, labels and edges separately. |
| Meaning is carried by color | Flagged; color alone is not sufficient. |
| A diagram is too wide at reading width | Reflowed or split, rather than shrunk further. |
| Rendering documentation would need a new application dependency | Refused; temporary output is used for visual checks unless the project's renderer needs a committed image. |
| No renderer is available | Source review is reported separately from the parse and visual checks that did not run. |
| Deciding where a diagram lives in a document set | Deferred: this skill owns form choice, drawing and verification; the owning surface decides placement, discoverability and catalog entry. |
| Adopting the skill into an existing project | No redrawing of existing diagrams is implied, and an established visual format the project already follows takes precedence. |

## Limits

- Mermaid behavior claims were checked with Mermaid 12.0.0, 11.17.2 and 11.16.1
  through the CLI and Chrome in light and dark themes; the bundled examples have
  not been checked in every consuming project's publishing renderer, so
  cross-renderer parity is unverified.
- Swimlane syntax is documented from Mermaid 11.16.0 as an evolving beta;
  actor-labelled flowcharts are the compatible alternative.
- Mermaid is the assumed text format. The layout and altitude rules generalize;
  the syntax and renderer caveats do not.
- Table application, semantic review, visual-review-only and data-flow reading
  routes were source-reviewed, not independently trialled.
