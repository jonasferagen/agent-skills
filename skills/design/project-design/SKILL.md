---
name: project-design
description: "Shape system responsibilities, conceptual models, workflows and integration choices before or during implementation. Use for design across people, agents, tools or services; not for literal code edits or provider account setup."
metadata:
  version: "0.2.0"
---

# Project design

Develop a design around a concrete workflow and decision. Start with the
project's existing design documents, conventions and relevant implementation.
Follow the project's conventions for where designs are written and how they are
reviewed; if none are documented, infer them from the repository's existing
documents and state the assumption, or ask the user.

Terms used throughout: the **owner** of something is the person, team,
component or repository responsible for changing it and answering for it. A
**role** is a named responsibility in a workflow (reviewer, deployer); the
**actor** is whoever fills it in a given run (a person, an agent, a service). A
**handoff agreement** is the written terms of one exchange between a producing
and a consuming side: what is handed over and how it is identified, what the
receiver checks before accepting it, and what each side does on failure. The
references use this term for every such agreement.

## Procedure

1. Read the request and the existing design material. Bound the decision
   (next section): what is settled, what is open, how deep to go.
2. Select the design question and read the matching reference.
3. Trace one concrete case through its owners, then challenge it with the
   failure cases that matter (sections below).
4. Decide: record options, the choice and its reasons; write the handoff
   agreements the case needed; leave the rest as open points.
5. Write the design note (deliverable below) and report to the user the cases
   traced, decisions made, open points and evidence still needed.

## Deliverable

A design note, written where the project keeps designs; when it has no such
place, at `docs/design/<topic>.md`, and tell the user. When the project has no
form of its own, use these headings:

1. Decision and scope
2. Evidence read
3. Cases traced
4. Options and choice, with reasons
5. Owners and handoffs, with their handoff agreements
6. Open points (linked to the project's issue tracker when one exists;
   otherwise kept here and told to the user)

Mark each item's **design status** with a bracketed label: `[proposed]`
suggested, `[decided]` agreed by whoever decides it, `[implemented]` built,
`[verified]` shown working with evidence. These describe the design; the
candidate/accepted/adopted terms below describe outputs moving through the
workflow. Label examples; they prove no actual outputs, runs or approvals. A
walkthrough establishes only consistency of its cases; writing the design does
not by itself permit anyone to run, spend or change anything.

A handoff agreement is a few lines, for example:

> Build → Deploy. Hands over: `app-<git sha>.tar.gz` and its checksum. Deploy
> accepts when the checksum matches and the sha is on `main`; otherwise it
> rejects and keeps the previous release. A resubmitted sha is the same
> handoff; Build re-runs only for a new sha.

## Bound the decision

Identify what is being decided, what is already settled and what remains open.
Read how far along the project is (prototype, in production, mid-migration) and
what it must deliver before choosing design depth. A focused boundary change
needs only the affected owners and consumers. Preserve established choices
unless changing them is in scope; an earlier implementation is evidence of
useful behavior, not automatic adoption of its infrastructure.

Keep responsibility, repository, process and deployment boundaries distinct.
A repository need not be a service; an agent following a document can be a valid
mechanism. Designing for a possible environment does not select or provision it.
Follow the project's existing engineering or specialist guidance when a design
reaches its subject, without inventing a new requirement merely because guidance
exists. A complete top-down model is not a prerequisite: establish a small
overview if one is missing, then reconcile affected owners as findings become
decisions.

## Select the design question

- For ownership and boundaries, trace a representative case below.
- For domain meaning, identities, relationships and lifecycle, read
  [conceptual models](references/conceptual-models.md).
- For triggers, actor responsibilities, state changes and handoffs, read
  [workflow design](references/workflows.md).
- For a service capability or integration mechanism, read
  [integration choices](references/integrations.md). Actual provider setup belongs
  to whoever implements the integration.
- For obligations at an established handoff (a build handing a package to
  deployment, a review returning a verdict to the author), write its handoff
  agreement beside the design that needs it.
- For sequencing designs, experiments and implementation, use the project's
  planning documents or issue tracker.

A boundary review needs no integration-selection pass. Reading an existing model
or correcting a label needs no design reconstruction or document migration.

## Trace work through owners

Follow a concrete case from inputs through transformations and acceptance to
outputs and consumers. Name who changes durable state, accepts a result and
adopts it for downstream use: a **candidate** is output awaiting judgment,
**accepted** means its receiver approved it, **adopted** means a downstream
consumer now relies on it. Execution success and acceptance may belong to
different owners.

Distinguish, where relevant, inputs that cannot be regenerated, accepted
outputs, run records, regenerable caches and disposable scratch. Identify required
reads and writes, external dependencies and assumptions about configuration or
host tools. Describe needed capabilities before selecting packaging.

When the system separates runtime code from authored content (a site generator
and its pages, a rules engine and its rule files), identify code, authored
content, configuration and **derived preparation state** (what a build or import
step produces from the content, such as compiled pages or an index; regenerable)
separately. State who owns each, which content revision the runtime uses and who
chooses it, what the consumer needs and where preparation writes. Content can
include executable scripts; a file volume does not make it passive data or define
compatibility. Repository ownership and delivery format are separate decisions.

## Challenge and reconcile

Exercise a relevant rejection, missing input, repeated request, revised dependency
or unavailable owner. Name who diagnoses it, what state remains valid and how work
continues without overwriting another owner's work. Choose cases from the actual
decision rather than filling an exhaustive checklist.

For a runtime/content split, trace a content-only revision and a change requiring
new runtime behavior. Compare shipping the authored files directly with shipping
a prepared build of them when that choice matters. Include missing or
incompatible dependencies and choose the smallest experiment that distinguishes
options. An extra repository, container or generic runtime needs a workflow
reason.

Look for competing writers, ambiguous acceptance, dependency cycles and changes
that force unrelated owners to move together. Compare a simpler arrangement when
it resolves an observed problem. Similar vocabulary alone does not require shared
implementation.

When the design changes a responsibility, a scope, an **operating fact** (who
runs what, where, with which access) or a handoff agreement, follow the
project's process for agreeing such changes, or ask the user when there is
none. An ordinary change within known constraints needs no fresh design
document. When the design changes a definition that appears in several places,
update the place that decides it and derive or correct the other appearances.
