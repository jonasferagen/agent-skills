---
name: relational-modeling
description: "Turn known entities and retrieval questions into a relational model, or revise a relationship when its meaning changes. Use for identity, roles, cardinalities and model scenarios before implementation; routine prose edits, database provisioning and migration execution are separate tasks."
metadata:
  version: "0.2.0"
---

# Relational modeling

Produce a coherent model for the questions the project needs to answer, or make
the missing decisions explicit. Start from the supplied brief and project policy,
existing model and terminology. Preserve established document homes and distinguish
supplied facts, provisional assumptions and adopted decisions.

## Select the task

For a question about an existing model, read its owning document and only the
terms or scenarios needed to answer. Cite the source and preserve unresolved
meaning; do not start a modeling or authoring pass merely to read database docs.

For a model review, compare the requested relationships and retrieval paths with
the supplied requirements. Report findings and blockers. Load ER guidance for
notation or relationship interpretation; visual verification applies when the
review includes appearance. A review alone does not require rewritten documents.

For a new model or relationship change, follow the workflow below. Its canonical
relationship view is ER: use the available visual skill’s ER route directly.
PostgreSQL representation, migration planning and rendering tools serve different
tasks; select them when the requested work reaches those decisions.

## Establish or revise the model

For a new model, identify the retrieval questions and the facts needed to answer
them. For a correction, start with the changed meaning and trace only its affected
relationships, constraints, glossary entries, scenarios and representations.

For each relationship that matters, examine:

- Identity: what remains the same when a name or external reference changes?
- Roles and scope: who participates, in what capacity, and in which context?
- Cardinality and absence: can there be none, one or several at each end, and
  which possibilities are known rather than guessed?
- Ownership and lifecycle: which facts belong together, and what must survive a
  correction, withdrawal or deletion when those operations are in scope?

Do not turn an example into a universal constraint. When a missing decision blocks
implementation, ask or record the decision needed. A bounded experiment may use
an explicitly provisional assumption; keep that status visible in the ER view and
related scenarios. An unspecified relationship is not automatically many-to-many.

Keep domain meanings separate from table names, keys and data types. A glossary
defines terms; the model explains relationships and invariants. Use the project's
existing glossary or add one when the resolved meanings need a shared home.
For PostgreSQL representation, use postgres-design when available and relevant;
do not load transaction or runtime guidance just to draw a conceptual relationship.

## Exercise the questions

Use [scenario guidance](references/scenarios.md) to challenge the model with small
synthetic examples. State the expected retrieval result and follow the relationship
path that would produce it. This is reasoning about the model, not evidence that
SQL, permissions or runtime behavior works.

Reconcile the model, scenarios and affected glossary entries after a correction.
Retain useful counterexamples and open questions. Avoid regenerating unrelated
documents or adding features merely because the representation permits them.

## Document and hand off

Use project-docs and authoring guidance when available. Suitable starting homes are
`docs/database/model.md`, `docs/database/scenarios.md` and
`docs/project/glossary.md`; honor existing paths. Add a directory README when routes
help. Defer migration and seed-loading documents until those subjects are addressed.

Keep one canonical ER view with the model. Use ER guidance
when available; do not invent cardinalities to complete the drawing. Distinguish
conceptual relationships, proposed database representation and implemented schema.
Report any missing rendering or visual verification instead of claiming it passed.

Report what the model can answer, assumptions and unresolved implementation
decisions, scenarios reviewed, checks actually performed and the next bounded task.
An implementation-ready claim requires resolved decisions for that implementation
scope; a successful design review does not establish migration or runtime readiness.
Provisioning, migration execution, seed loading, UI and application code are outside
this workflow unless separately requested.
