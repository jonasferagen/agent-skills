# Synthetic model scenarios

Start with a retrieval question. Construct the smallest made-up case that reveals
which relationships and distinctions its answer needs. Use fabricated names and
identifiers, never copied private records.

Record inputs, expected answer, relationship path and the rule or assumption being
exercised. Include an ordinary case and a counterexample relevant to the proposed
constraint: a missing relationship, a second participant, multiple roles or several
targets. Choose cases because they could expose a wrong answer, not to fill a
checklist. Keep an unanswered expectation explicit when it depends on an open rule.

Names alone do not establish identity. Two similar labels can denote distinct
entities; one entity can have several roles. A fact at one scope need not apply at
another. Make these distinctions visible when they matter to the retrieval.

On a relationship correction, revisit affected expected answers and add one case
that distinguishes the old interpretation from the new one. State whether the
change invalidates a former assumption or confirms an existing model. Preserve
unaffected answers; do not silently rewrite every expectation to match the model.

These examples can later inform seeds and tests. They are not a seed loader,
an executable test suite or a reason to select a fixture framework. Defer loading,
reset semantics and database lifecycle until that work is actually in scope.
