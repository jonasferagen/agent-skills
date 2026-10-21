---
name: relational-modeling
description: "Turn known entities and retrieval questions into a relational model, or revise a relationship when its meaning changes. Use for identity, roles, cardinalities and model scenarios before implementation; not for routine prose edits, database provisioning or migration execution."
metadata:
  version: "0.3.0"
---

# Relational modeling

Produce a coherent model for the questions the project needs to answer, or make
the missing decisions explicit. Start from the supplied brief, the project's existing
model, conventions and terminology. Keep documents where the project already
keeps them, and distinguish supplied facts, provisional assumptions and adopted
decisions.

## Select the task

For a question about an existing model, read its owning document and only the
terms or scenarios needed to answer. Cite the source and preserve unresolved
meaning; do not start a modeling or authoring pass merely to read database docs.

For a model review, compare the requested relationships and retrieval paths with
the supplied requirements. Report findings and blockers to the user. A review
alone does not require rewritten documents.

For a new model or relationship change, follow the workflow below. Its canonical
relationship view is an entity-relationship (ER) diagram. Draw it in the diagram
format the project already uses; if there is none, use Mermaid `erDiagram` with
its standard notation and state that choice. This skill ships no notation guide
or renderer. Database representation, migration planning and rendering are
later steps; take them up only when the requested work reaches them.

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
implementation, ask the user if they are available; otherwise record the decision
needed and the assumption you proceed on. A bounded experiment may use
an explicitly provisional assumption; keep that status visible in the ER view and
related scenarios. An unspecified relationship is not automatically many-to-many.

Keep domain meanings separate from table names, keys and data types. A glossary
defines terms; the model explains relationships and invariants. Use the project's
existing glossary or add one when the resolved meanings need a shared home.
Choosing a database representation is a later step; do not take up transaction
or runtime questions just to draw a conceptual relationship.

## Exercise the questions

Use [scenario guidance](references/scenarios.md) to challenge the model with small
synthetic examples. State the expected retrieval result and follow the relationship
path that would produce it. This is reasoning about the model, not evidence that
SQL, permissions or runtime behavior works.

Reconcile the model, scenarios and affected glossary entries after a correction.
Retain useful counterexamples and open questions. Avoid regenerating unrelated
documents or adding features merely because the representation permits them.

## Document and hand off

The model document states the entities, their relationships with cardinalities,
the invariants, and the retrieval questions it answers. Put it, its scenarios
and the glossary where the project keeps its
design documents; if there is no such place, put them together in one directory
beside the code they describe, with a short README naming each file's purpose,
and say which you chose. Honor existing paths. Defer migration and seed-loading
documents until those subjects are addressed.

Keep one canonical ER view with the model. Do not invent cardinalities to
complete the drawing; mark an undecided end as provisional instead. Distinguish
conceptual relationships, proposed database representation and implemented schema.
Report any missing rendering or visual verification instead of claiming it passed.

Report to the user what the model can answer, assumptions and unresolved
implementation decisions, scenarios reviewed, checks actually performed and the
next task (one decision or one representation step, not the rest of the project).
An implementation-ready claim requires resolved decisions for that implementation
scope; a successful design review does not establish migration or runtime readiness.
Provisioning, migration execution, seed loading, UI and application code are outside
this workflow unless separately requested.
