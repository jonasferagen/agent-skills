# Status, evidence and authority

Use this reference when recording, reporting or relying on the status of a
decision or behavior. A claim moves through separate states, and each state needs
its own evidence. Report the state actually reached and what supports it.

## States

| State | Meaning | Recorded in |
| --- | --- | --- |
| Unknown | No fact or decision is recorded. It is not permission, absence, a default guarantee or a waiver. | The owning table or document, with what depends on it when consequential |
| Proposed | A recommended option, draft term, design or sequence awaiting a decision | The owner of the choice, such as a design page or the active plan, marked as a proposal; not the Policy table |
| Adopted | Accepted by the decision's authority | The owning foundation, agreement or decision record |
| Implemented | Code, configuration, provisioning or an operation exists or has run | The implementing repository and its work records |
| Verified | An observation shows that an adopted requirement is met, within a stated scope and date | The evidence record |

A workflow or agreement may need finer states, such as an operation's completion,
review acceptance and consumer adoption. Define them in that owner; each still
needs its own evidence. [Foundation format](foundation-format.md) owns how
`Unknown`, `None` and omitted rows are written in foundation tables.

Implementation does not amend an adopted requirement, and an adopted requirement
does not show that implementation meets it. Use
[foundation authority](foundation-authority.md) when they disagree.

## What evidence establishes

| Evidence | Can establish | Cannot establish alone |
| --- | --- | --- |
| A document, plan or policy edit | That a decision, intent or sequence was recorded | Its adoption, implementation or verification |
| A design walkthrough or synthetic example | Consistency of the traced cases | Working commands, recovery, isolation, real assets or approvals |
| A schema, field list or passing schema check | The declared shape | Compatibility, coverage or behavior |
| A diagram parse | Valid syntax | Correct content or readability |
| A render inspected at reading width | Readability in that renderer and theme | Correct content |
| A successful operation or tool status | That the operation ran | Acceptance of its result or readiness for another use |
| A test or check run | The behavior it observes, in that environment | Behavior outside its scope |
| A local experiment | Feasibility under its conditions | Provider retry safety or production readiness |

Name the scope of each verification: what was observed, where and when. Report
checks that could not run separately from checks that passed. A consistency check
that has never been seen to fail is not yet evidence; see
[make disagreement fail](../skills/source-of-truth/references/boundaries.md#make-disagreement-fail).

## Authority to act

Authority to act comes from the user's instructions and the delegation they have
given. Project documents can record that delegation; they do not expand it.
Recording, reading, reviewing or applying a document does not grant authority. A plan,
design, contract, diagram, finding, template or policy gives no permission to
execute, deploy, spend, contact people, publish, migrate or change data. A
stricter requirement creates work; it does not authorize that work. Discovering
that a condition already holds, such as real personal data in a store, records a
fact; it does not authorize processing that data.

Follow existing delegation. Do not invent approval steps the project has not
adopted.
