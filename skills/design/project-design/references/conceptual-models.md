# Conceptual modelling

Develop only the meaning needed for the current decision. Start with the questions
this model must answer and its owning part of the design. Keep storage schemas,
record formats and implementation choices separate until the decision needs them.

## Establish meaning from evidence

Use concrete source material or workflow observations to distinguish identities
and lifecycles. Ask what must be named, changed, reviewed or used independently,
and what remains the same through a change. A file, label or directory alone does
not establish a separate domain identity; equal bytes do not establish one shared
lifecycle. Record observed facts separately from proposed meanings and assumptions.
Name missing evidence when it affects the decision.

Describe relationships, their roles and constraints, including cardinality where
it matters. State rules a diagram cannot express clearly in prose: exclusive
alternatives, contextual validity, ordering or prohibited cycles, for example.
Use lifecycle or workflow detail only where change affects the model's meaning.
If a visual helps, use the project's diagram guidance (diagrams-and-tables when available)
for its representation; the model's owning document defines the meaning.

## Exercise the model

Trace one concrete example through the questions, then a relevant change or
failure. Distinguish observed examples from synthetic ones. Check whether the
same identity remains valid, which relationships change and which decisions or
surrounding owners need reconsideration.

For example, in a synthetic lending model, two physical copies of the same book
can be borrowed separately. The title and each copy answer different questions;
a loan connects one copy to a borrower for a period. Returning a damaged copy ends
the loan without necessarily making the copy available again. This separates loan
completion from copy condition and exposes a rule that a relationship line alone
cannot establish. It does not require a history framework or a storage design.

## Stop at sufficient evidence

The slice is sufficient when its current questions have consistent answers across
the example and change case, consequential assumptions are visible and affected
owners can use the result. Record unresolved questions with what they affect and
when they need answers, using the existing planning owner. Defer additional
entities, histories and infrastructure until a concrete decision needs them.
