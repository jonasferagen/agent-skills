# Project contracts scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Route | Expected behavior |
| --- | --- | --- |
| Explain whether receipt means acceptance | Read | Answer from the terms; silence remains unresolved without redesigning the agreement. |
| Assess a generated output against its specification | Apply | Check exact input and specification identity and the relevant criteria; tool success alone does not establish acceptance. |
| Define a design-to-implementation handoff | Design | State scope, who decides acceptance, input revision, result and open terms without turning every internal step into an API. |
| Retry an operation after a timeout | Design, failure and change section | An unknown outcome differs from a confirmed failure; reconciliation precedes a submission that could duplicate. No provider capability is assumed. |
| Review an added field for compatibility | Review, then the failure and change section when needed | Compare actual consumer expectations and retained records; schema success alone is insufficient. |
| Correct a sentence without changing terms | Ordinary editing | No full contract review or format migration. |
| Ask for a legal agreement | Outside the skill | The description excludes legal agreements; this skill covers operational handoffs. |
| No written agreement exists for the handoff in question | Read | The absence is stated; expectations are inferred from code, tests and records on each side, labelled as inferred, and the user is asked before they are treated as adopted. |

## Worked case: a review against the wrong revision

A sender supplies candidate C for brief B, revision 2. A review of C against
revision 1 is evidence for that earlier basis, not acceptance against revision 2.
If the agreement has no rule for changed briefs, applying it reports the gap;
a design task may establish the rule. Neither task silently rewrites the
historical review. A timeout while transferring C does not establish that
the receiver failed to retain it.

The reusable point: successful execution, acceptance and downstream adoption are
separate claims. The agreement needs only the distinctions that affect its
participants, with missing terms left visible during interpretation.

## Limits

- No runtime helper, schema or live exchange is part of the skill, so a manual
  review cannot establish runtime compliance.
