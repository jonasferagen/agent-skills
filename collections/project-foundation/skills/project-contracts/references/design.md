# Design or change a contract

Start with the participating owners, the purpose of the exchange and an actual
case or labelled example. Identify the agreement's authoritative home and whether
terms are proposed or adopted. Link existing definitions; use
[source-of-truth](../../source-of-truth/SKILL.md) when competing copies disagree.
Keep local implementation steps in their procedures.

## Discover the obligations

Trace the exchange from each participant's perspective. At each action, decision
or recovery step, determine what that participant must know or be able to rely on.
Look for plausible cases in which participants could follow the written terms
and still disagree about the valid outcome. The subjects below are starting
points, not an exhaustive definition of a complete contract.

- Preconditions: required inputs, identity/revision, permitted effects and
  existing authority to act. Unresolved prerequisites remain visible.
- Result: what is returned or retained, who owns it, and the evidence linking it
  to the exact request and inputs.
- Acceptance: who checks which conditions, and what makes rejection or completion
  observable. Execution success, acceptance and downstream adoption may have
  different owners and criteria.
- Failure: incomplete output, interruption or invalid input; what remains valid,
  who diagnoses the issue and which action can follow.

Challenge assumptions using the actual exchange: participants' independent actions,
changing inputs, unavailable information or dependencies may expose further terms.
Select cases because they could change a participant's decision, not to fill a
fixed checklist. Existing guidance need not name a subject for it to matter.

For each consequential gap, identify the missing decision, affected participant,
consequence, responsible owner and work that depends on resolving it. Propose or
establish terms where evidence and authorization permit; distinguish recommendations
from adopted decisions. Preserve unresolved choices when the answer is not known.

Choose enough precision for each side to act without guessing. A short table may
suffice. Define fields, formats or status values only when participants need them;
do not impose a universal record template or turn every internal step into a
separate contract. Refer to policy for retention and authority. Changed obligations
or operating circumstances use [project-policy](../../project-policy/SKILL.md).

## Preserve identity through failure and change

For repeatable operations, distinguish a request from its attempts. State whether
repetition returns an existing result, creates a new attempt or refuses, and how
participants detect conflicting content under the same identity.

A timeout may leave an operation running or complete. Separate an unknown outcome
from confirmed failure; establish how it can be reconciled before resubmission
that may duplicate writes or spending. Withdrawing interest does not prove actual
cancellation. Preserve required evidence and earlier accepted state. Provider
lookup, retry and cancellation guarantees need evidence from that provider.

When a brief or input changes, assess whether an earlier result still satisfies
it. When the contract changes, name affected consumers and compare their actual
expectations: can they still use old and new records? State any transition or
version distinction needed. Adding a field alone does not prove compatibility.
Do not silently rewrite historical decisions to fit a new contract.

## Exercise and record

Trace one valid exchange and a consequential rejection, interruption or revision.
Show what each side observes and which obligation the case checks. Revisit gaps
found during the exercise; a completed list of fields does not establish coverage.
Synthetic records establish design consistency; implementation and actual runs
supply separate evidence that participants honor the contract.

Keep the agreement in its existing document owner and link it from the architecture.
Report unresolved terms and the work they block. A schema, successful operation
or diagram alone does not demonstrate fulfillment of all obligations.
