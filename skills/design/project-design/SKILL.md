---
name: project-design
description: "Shape system responsibilities, conceptual models, workflows and integration choices before or during implementation. Use for design across people, agents, tools or services; literal edits and provider setup have their own workflows."
metadata:
  version: "0.1.1"
---

# Project design

Develop a design around a concrete workflow and decision. Start with applicable
project policy, existing design owners and relevant implementation. Follow the
project's authority, document homes and selected templates; this skill requires
no particular scaffold or companion installation.

## Bound the decision

Identify what is being decided, what is adopted and what remains open. Read the
current phase and delivery scope before choosing design depth. A focused boundary
change needs only affected owners and consumers. Preserve established choices
unless changing them is in scope; an earlier implementation is evidence of useful
behavior, not automatic adoption of its infrastructure.

Keep responsibility, repository, process and deployment boundaries distinct.
A repository need not be a service; an agent following a document can be a valid
mechanism. Designing for a possible environment does not select or provision it.
State the mapping only where the workflow needs it. Follow adopted engineering
or specialist guidance when a design reaches its capability, without inventing
a new requirement merely because a skill is available.

Locate the slice in its surrounding design: which responsibility it opens,
where its detail belongs and which owners might change because of it. A complete
top-down model is not a prerequisite. Establish a small overview if one is missing,
then reconcile affected owners as findings become decisions.

## Select the design question

- For ownership and boundaries, trace a representative case below.
- For domain meaning, identities, relationships and lifecycle, read
  [conceptual models](references/conceptual-models.md).
- For triggers, actor responsibilities, state changes and handoffs, read
  [workflow design](references/workflows.md).
- For a service capability or integration mechanism, read
  [integration choices](references/integrations.md). Actual provider setup belongs
  to the implementing owner's procedures.
- For obligations at an established handoff, use the project's contract workflow;
  project-contracts is a suitable companion when available.
- For sequencing designs, experiments and implementation, use the project's
  planning workflow.

A boundary review needs no integration-selection pass. Reading an existing model
or correcting a label needs no design reconstruction or document migration.

## Trace work through owners

Follow a concrete case from inputs through transformations and acceptance to
outputs and consumers. Name who changes durable state, accepts a result and
adopts it for downstream use. Execution success and acceptance may belong to
different owners. Label examples; they prove no actual assets, runs or approvals.

Distinguish authored or irreplaceable material, accepted revisions, execution
records, generated caches and disposable scratch where relevant. Identify required
reads and writes, external dependencies and assumptions about configuration or
host tools. Describe needed capabilities before selecting packaging.

For runtime/content separation, identify code, authored content, configuration and
derived preparation state separately. State who owns each, what selects a content
revision, what the consumer needs and where preparation writes. Content can
include executable scripts; a file volume does not make it passive data or define
compatibility. Repository ownership and delivery format are separate decisions.

Identify consequential handoffs and what each side relies on. Define their
obligations through the project's contract route when needed; a drawing-board
review can leave a named exchange as open work with its dependent decisions.

## Challenge and reconcile

Exercise a relevant rejection, missing input, repeated request, revised dependency
or unavailable owner. Name who diagnoses it, what state remains valid and how work
continues without overwriting another owner's work. Choose cases from the actual
decision rather than filling an exhaustive checklist.

For a runtime/content split, trace a content-only revision and a change requiring
new runtime behavior. Compare direct authored files with a prepared delivery when
that choice matters. Include missing or incompatible dependencies and choose the
smallest experiment that distinguishes options. An extra repository, container or
generic runtime needs a workflow reason.

Look for competing writers, ambiguous acceptance, dependency cycles and changes
that force unrelated owners to move together. Compare a simpler arrangement when
it resolves an observed problem. Similar vocabulary alone does not require shared
implementation.

Record proposed decisions, adopted requirements, implemented mechanisms and
verification evidence distinctly. Follow the project's policy workflow when the
design changes responsibility, scope, operating facts or obligations, including
when a proposal is adopted or implemented. An ordinary change within known
constraints needs no fresh policy reconstruction. Reconcile affected definitions
through their authoritative owners; source-of-truth is useful when available.

Keep proposals and unimplemented work outside current-state documentation, using
the project's design and planning homes. Link the active queue rather than adding
another status owner. Use the project's writing guidance for authored output.
Report the cases traced, decisions made, consequential unknowns and implementation
evidence still needed. A walkthrough establishes only consistency of its cases;
the design grants no new execution authority.
