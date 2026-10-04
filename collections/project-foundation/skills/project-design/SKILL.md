---
name: project-design
description: "Shape system architecture, responsibilities, conceptual models, workflows and integration choices before or during implementation. Use for operating design across people, agents, tools or services; literal edits, provider setup and runtime implementation have separate workflows."
metadata:
  version: "0.10.0"
---

# Project design

If execution exposes a consequential guidance or routing problem, use
[friction capture and repair](../../references/friction.md). Successful work needs
no capture pass.

Develop a design that supports a concrete workflow and makes the next decision
clear. Start from the project's existing foundation, architecture and relevant
implementation. Use [foundation authority](../../references/foundation-authority.md)
for adopted decisions and conflicts; reuse current readings.

## Bound the decision

Identify what the user wants to decide, what is already adopted and what remains
explicitly deferred. A focused boundary change needs only its affected owners and
consumers. Preserve established repository choices unless changing them is in scope.
Use retained implementations as evidence; distinguish useful behavior from the
infrastructure that happened to accompany it.

Read the current phase and delivery scope in policy before choosing design depth.
If they are missing, changing or contradicted by the proposed work, use
[project-policy](../project-policy/SKILL.md) to reconcile them. Applying an already
clear scope does not need a new policy review. Architecture can describe future
relationships without committing to their implementation in the current phase.

Keep responsibility, repository, process and deployment boundaries distinct.
Designing for a possible environment does not select or provision that environment.
A document-only coordinator need not acquire a runtime, and a repository does not
imply a service, container or separate database. State any necessary mapping and
why the workflow requires it.

When defining a named runtime that needs predictable discovery and controls, use
[repository services](../../references/repository-services.md). It owns the
default `services/` home and routes to the project's service/runtime guidance.
Reading an existing service guide or changing an ordinary command needs no new
scaffold.

## Place the slice in its surrounding design

For a modelling or design slice, identify which part of the overall design it
opens, where its detailed model belongs and which surrounding owners could change
because of what it reveals. Use existing overview and document routes; if they
are missing, add only enough context to locate the slice. Work may start inside
an owner and reshape the design around it. A complete top-down model is not a
prerequisite. Reconcile affected owners as findings become decisions, or leave
an explicit question with the work that depends on it.

When establishing how this slice's views connect to their explanations and
surrounding detail, use project-docs'
[connected-view guidance](../project-docs/references/view-structure.md). Ordinary
model reading or a focused boundary change needs no browsing-format adoption.

For a new design, model or process page without an adequate existing structure,
use the [document-home map](../../references/document-homes.md) and its default
templates. Existing pages retain their homes until deliberately migrated.

## Select the design question

These questions also apply to process-oriented repositories whose main outputs
are decisions, procedures and artifacts. A workflow step need not become code.

- For ownership and boundaries, trace the representative case below.
- For internal domain meaning, identities, relationships and lifecycles, read
  [conceptual modelling](references/conceptual-models.md).
- For triggers, human/agent responsibilities, state transitions and handoffs, read
  [workflow design](references/workflows.md).
- For selecting a service capability or its integration mechanism, read
  [integration choices](references/integrations.md). Provider-specific setup and
  execution stay with their owning procedures.
- For obligations at an established handoff, use
  [project-contracts](../project-contracts/SKILL.md).
- For sequencing design, experiments and implementation, use
  [project planning](../project-planning/SKILL.md).

Load only the reference needed by the current decision. A boundary review does
not require a service-selection pass.

## Trace work through owners

Choose a concrete representative case. Follow its inputs, transformations,
acceptance decisions and outputs through the responsible parts. Identify who may
change durable state, who accepts results and who consumes them. Separate an
operation's successful execution from acceptance of its result when those belong
to different owners.

Inspect the source and state that make the case possible. Distinguish authored or
irreplaceable material, accepted revisions, execution records, generated caches
and disposable scratch where relevant. Identify external dependencies, required
reads and writes, configuration and hidden assumptions about paths or host tools.
Describe needed capabilities before selecting their packaging.

When a workflow should reuse an execution environment across authored content
sets, identify runtime code, content, configuration and derived preparation state
separately. State who authors each, what selects a content revision, what the
consumer needs to load it and where preparation may write. Content can include
executable scripts or native project resources; placing it in a file volume does
not make it passive data or define its compatibility contract. Repository ownership,
delivery format and runtime packaging are separate decisions. Co-location during
exploration can be deliberate; identify which coupling a later split must remove.

Identify the consequential handoffs and what each side must be able to rely on.
Use project-contracts when those obligations need definition or review. Architecture
chooses the parts and their relationships; contracts make a selected exchange
precise. A drawing-board review can leave contracts as named open work. Mark
examples explicitly; they do not prove real assets, successful jobs or approvals.

## Challenge the boundary

Exercise a relevant failure or change: rejected output, missing input, a repeated
request, a revised dependency or an unavailable owner. Ask who diagnoses it, which
state remains valid and how work continues without overwriting another owner's work.
Choose cases from actual risks rather than running a fixed exhaustive checklist.

For a proposed runtime/content split, trace a content-only revision and a change
that needs new runtime behavior. Identify which code, configuration, prepared
resources and retained records change in each case. Compare direct use of authored
files with an assembled or prepared delivery where relevant, including missing or
incompatible dependencies and an edit to shared source. Choose the smallest
experiment that could distinguish the options; a generic runtime, extra repository
or container is justified by the workflow rather than by the split alone.

Look for competing writers, ambiguous acceptance, accidental dependency cycles and
changes that force unrelated owners to move together. Compare a simpler arrangement
when it resolves an observed problem. Preserve legitimate differences; shared
vocabulary or similar code alone does not require shared implementation.

## Reconcile the design

Record adopted responsibilities and interfaces in their existing architecture
owner, local implementation choices with their repository and unresolved decisions
with the work that depends on them. Use [project-docs](../project-docs/SKILL.md)
when document placement needs a decision, and
[project-policy](../project-policy/SKILL.md) when responsibilities or operating
circumstances change obligations. Use
[source-of-truth](../source-of-truth/SKILL.md) when competing definitions need
reconciliation. For authored output follow
[authoring guidance](../../references/authoring.md).

When selecting the next task or staging implementation, read
[project planning](../project-planning/SKILL.md). Design readiness means the important
cases have clear owners and remaining unknowns have explicit consequences. Report
which cases were traced and which behavior still needs implementation evidence.
A document walkthrough establishes only the consistency of the traced cases; see
[what evidence establishes](../../references/status-and-evidence.md#what-evidence-establishes).
