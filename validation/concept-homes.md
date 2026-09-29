# Validation and alignment — Concept Homes

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation.

| Request and context | Expected outcome |
| --- | --- |
| A vocabulary is enforced by a database constraint and restated in application code | The constraint is authoritative; the application derives the vocabulary or a gate check compares the two. |
| A list in code holds every value the constraint admits | Treated as a copy that will fall behind, not as a policy. |
| A list in code holds some of the values the constraint admits | Treated as a policy over the vocabulary; left in place with its reason stated. |
| An input boundary validates more strictly than the column that stores the value | The stricter check is identified as able only to reject stored values; narrowing needs its own stated reason. |
| A lookup returns a default for an unknown code | Named as the mechanism that makes drift silent; exhaustiveness or explicit failure proposed where the concept must be complete. |
| A consumer states a fixed label and ignores the stored value | Treated as worse than a missing label, because the stated fact becomes false; a derived vague answer preferred. |
| The same rule exists in two languages with different spellings | Copying rejected; the spelling difference is attributed to each language's parsing, and a normalising home-to-home check is proposed. |
| A proposed fix would import a server module into a client bundle | Unification refused; request-time delivery or a dependency-free shared module proposed instead. |
| Only a type is shared across a bundle boundary | Type-only declarations are erased, so the boundary does not block it. |
| Paired processes each hardcode the other's address | The hardcoded value is removed from shared code and supplied at the edge by whichever process owns it. |
| A vocabulary would need to become rows a check constraint reads | Identified as impossible for a check constraint and as a schema decision; the project's migration rules govern. |
| A test restates the expected values as the check | Rejected as a third home; the check must compare one home to the other. |
| A relevant test exists but runs only behind an environment variable | Reported as unprotected in the gate rather than as covered. |
| A proposed check has never been observed to fail | Disagreement is introduced deliberately to confirm the check fails, then reverted. |
| Two similar lists answer different questions | Not a second home; the questions are compared rather than the contents. |
| One constant is used several times inside one module | Not a duplication. |
| A document and a constraint both list a vocabulary and the document is stale | The document is a home; it is reconciled in the present tense. |
| A duplication can be neither derived nor checked | Recorded where the concept lives, naming what must change together and what goes wrong when one is missed. |
| Ranking a stable constant copied many times against one growing cross-medium vocabulary | The growing cross-medium concept ranks higher; copy count alone does not decide. |
| Adopting the skill into an existing project | No renaming, code movement or schema change is implied; existing project conventions take precedence. |

## Sources inspected

Derived from an audit of Personal Atlas at
`a70229a79009ae6bce9fde56f26c5db6b30bc183`, comparing application source,
migrations, tests, build configuration and documentation. The audit ran as six
parallel searches — validation rules, domain vocabularies, logic expressed in
more than one medium, configuration constants, types and shapes, and
documentation — with each candidate independently challenged before being
accepted. Twenty-seven duplications survived that challenge; several claims were
corrected or rejected by it, and those corrections are the source of the
false-positive guidance above.

The distinction between a complete copy and a deliberate subset, the observation
that silent drift is nearly always a fallback, the objection that a test stating
its expectations is a third home rather than a check, and the point that an
opt-in test does not constitute gate coverage all came from that challenge step
rather than from the initial findings.

## Extraction decisions

Retained the diagnostic sequence — name the concept as a question, find its
appearances across media, identify the appearance that decides, then derive,
check or record — together with the escalation rungs, the boundary analysis, the
fallback mechanism and the false-positive tests.

Removed every project-specific instance: schema, table, column, role, port and
project identifiers, the domain vocabularies themselves, and the source project's
migration approval, backup and merge policy. Those remain in their owning
documentation. The package names no language, framework, database or toolchain as
a requirement, and no scenario depends on the source project's structure.

This skill deliberately does not cover code shape, naming or module layout, which
belong to a TypeScript or language-specific canon, nor schema design, which
belongs to a database canon. Its subject is only the seam between media and what
keeps a restatement honest across it.

## Verification limits

The author reviewed the extracted instructions against the scenarios above and
against the audit findings and their challenges. No independent agent evaluation
was performed. The skill has been applied in one project only; it needs
experience in a second before its scope boundaries can be considered settled. In
particular, the rung list has not been exercised on a build-time generation case
(rung 2), and the language-boundary guidance rests on a single observed instance.
