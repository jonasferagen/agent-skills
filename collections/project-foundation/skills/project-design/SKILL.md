---
name: project-design
description: "Shape or review project responsibilities, repository boundaries and handoffs before or during implementation. Use when deciding how parts work together or what design uncertainty to resolve next; literal document edits and container builds have separate workflows."
metadata:
  version: "0.1.0"
---

# Project design

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

Keep responsibility, repository, process and deployment boundaries distinct.
Designing for a possible environment does not select or provision that environment.
A document-only coordinator need not acquire a runtime, and a repository does not
imply a service, container or separate database. State any necessary mapping and
why the workflow requires it.

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

For each handoff that matters, establish enough input/output identity, revision,
failure and retry behavior to make the case unambiguous. Do not invent a universal
schema or API when a file or human review already serves the workflow. Mark example
records as examples; they do not prove real assets, successful jobs or approvals.

## Challenge the boundary

Exercise a relevant failure or change: rejected output, missing input, a repeated
request, a revised dependency or an unavailable owner. Ask who diagnoses it, which
state remains valid and how work continues without overwriting another owner's work.
Choose cases from actual risks rather than running a fixed exhaustive checklist.

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
[next-step planning](references/next-step.md). Design readiness means the important
cases have clear owners and remaining unknowns have explicit consequences. Report
which cases were traced and which behavior still needs implementation evidence.
A document walkthrough cannot establish working commands, recovery or isolation.
