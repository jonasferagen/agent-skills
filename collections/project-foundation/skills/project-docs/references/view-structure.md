# Connected documentation views

Use this reference when establishing or reviewing how architecture and design
views connect to their explanations and detail owners, or when preparing them
for a generated documentation browser. Reading an existing view or correcting
a label does not require adopting a new format.

The model's owner defines its meaning through
[project-design](../../project-design/SKILL.md). Form, notation, layout and visual
checks belong to [diagrams and tables](../../diagrams-and-tables/SKILL.md).
This reference owns the associations that let readers move between views and
their sources. Preserve existing document homes and apply changes to the slice
being worked on; a complete documentation migration is not a prerequisite.

## Start from a shared template

For a new view-owning page, use the collection's
[view template](../../../templates/views/view.md); for a process-owning page, use
the [process template](../../../templates/views/process.md). They provide a
default structure for purpose, scope, ownership, the view and its explanation,
constraints or decisions, and evidence and open questions. Preserve an existing
structure that supplies those associations; omit irrelevant sections and do not
invent content to complete a template. Several views can remain in one document
when their questions and explanations stay identifiable.

Collection ownership of these templates is independent of where project pages
live. Keep the current [document homes](../../../references/document-homes.md):
technical views and processes remain in their declared repository homes.
Managing them under `project-docs/` would require an explicit collection change
to document types, ownership, templates and validation, followed by deliberate
consumer migration. Using these templates does not adopt that relocation.

## Locate the view and its explanation

Give each view one reader question, a stated scope and a canonical document
section. A document can own several views answering different questions.
Declare what its nodes and relationships mean beside the diagram; a rendering
keyword such as Mermaid `flowchart` does not identify that meaning.

Connect drawn elements to their explanation using consistent names and explicit
references. A nearby table can explain boxes or stages, but state its mapping
when it groups elements or includes supporting material outside the view. Do
not assume every table on the page describes the diagram. Keep relationship
labels concise; link the owning explanation, process or contract when a label
cannot carry the meaning or constraints.

Follow the diagram guidance's
[overview and detail dispositions](../../diagrams-and-tables/references/composition.md#keep-it-vertical-and-keep-it-at-one-altitude).
For navigation alone, read its disposition inventory; the wider construction
guidance applies when drawing or restructuring a diagram.
Make the chosen detail destination or reason for keeping a box closed available
to the reader. A destination may be prose, a section or another view; it need
not contain another diagram. Link back to the surrounding view where that helps
orientation. Distinguish opening a box's internals from moving to another
viewpoint or a governing contract; these links answer different questions.

## Preserve scope, status and uncertainty

Use [status and evidence](../../../references/status-and-evidence.md) for the
claims the view makes. A page-level summary does not replace the state of a
particular section, element or relationship. Keep proposed detail distinguishable
from an adopted boundary, and keep implementation and scoped verification
evidence identifiable alongside the decision they concern. Mark synthetic cases
as examples rather than actual events.

A scoped adopted or implemented trial can use a proposed general process without
adopting that whole process. Navigation between them does not transfer status.

An intentionally closed box, detail outside the view's scope, an unresolved
modelling question and an unavailable source have different meanings. Record the
applicable case when it affects navigation or interpretation. A missing diagram
or contract link alone establishes neither missing functionality nor a missing
obligation. Necessary new decisions belong with their owner and dependent work,
as [project-design](../../project-design/SKILL.md) describes.

## Add machine browsing only when selected

When a project selects extraction or generated browsing, define one documented,
versioned input convention for the selected sources. It may use structured
Markdown, explicit metadata or an associated manifest. Choose its syntax and
supported forms with a small representative slice before migrating other pages.
The collection establishes the meanings below; a project's adopted input
convention establishes their concrete representation.

- **Identity:** distinguish the stable identity of a view, a shared concept and
  that concept's occurrence within a view. Keep file/section locations and display
  labels separate from those identities. Diagram-local node names are local;
  equal names across views do not prove equal concepts. Identify relationships
  separately where repeated endpoints would make references ambiguous.
- **Source association:** bind each participating view and its displayed element
  or relationship details to their owning source sections. Derive summaries,
  status and model relationships from those owners. A metadata binding should
  reference the explanation rather than maintain a second copy of it.
- **Meaning:** retain the declared view kind, node roles, relationship meaning
  and direction. Collaboration, information flow, dependency, process progression,
  sequence and navigation are distinct. Preserve applicable prose constraints;
  extracting arrows does not recover the whole model.
- **Navigation:** represent detail destinations and related viewpoints explicitly.
  Keep declared unknowns and excluded scope distinct from broken references or
  unsupported input. Resolve symbolic cross-repository routes using the declaring
  foundation's bindings, following
  [foundation format](../../../references/foundation-format.md#references).
- **Presentation:** let the browser own layout, styling, selection and tour order.
  A presentation grouping or parent link does not establish model containment,
  execution order, responsibility or access authority.

For example, a synthetic overview and data-flow view may both display a node
labelled `Library`. They can refer to the same owned concept while giving their
node occurrences different roles and their arrows different meanings. Moving
the concept's explanation changes its location, not its identity. A proposed
relationship in either view keeps its own status.

## Verify the selected slice

Trace the reader from an overview element to its explanation and relevant detail,
then back to its context. Check a relationship's meaning and governing source.
Exercise a relevant change or unknown, such as a moved source, repeated local
node name, mixed status or deliberately unopened box. Diagram meaning and rendered
readability retain their own checks; navigation does not establish either.

For a generated browser, record the source set, repository revisions and any
uncommitted input used to build it. Validate declared identities and references
against that set; report collisions, broken targets and unsupported forms rather
than silently inventing or dropping content. A deliberately unresolved detail
can remain visible without making it a broken reference. Detect unavailable
owners and defer only the affected claims, preserving known context.

For choosing how a browser uses its sources, start with the source-of-truth
[derivation options](../../source-of-truth/references/definitions.md#derive-instead-of-restate).
Use its [full workflow](../../source-of-truth/SKILL.md) when reconciling competing
definitions or designing a consistency check. A generated projection may
display the owning view without becoming a separately edited definition. Until
an extractor is implemented and exercised, these conventions establish source
structure and intent; they do not establish automatic parseability or freshness
of a manually authored browser.
