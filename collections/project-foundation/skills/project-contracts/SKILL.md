---
name: project-contracts
description: "Define or review obligations at an established handoff: inputs, outputs, acceptance, failure behavior and compatibility. Use for file, document, human/agent or service exchanges; legal agreements and choosing the overall architecture are separate tasks."
metadata:
  version: "0.1.0"
---

# Project contracts

Make explicit what each side of a handoff can rely on. Start with the existing
architecture, participating owners and an actual exchange or labelled example.
Use [foundation authority](../../references/foundation-authority.md) for adopted
constraints; reuse current readings. For authored output follow
[authoring guidance](../../references/authoring.md).

If the open question is which responsibilities or components should exist, use
[project-design](../project-design/SKILL.md). A focused contract change need not
reopen settled architecture. A contract can govern a document review or file
handoff; it does not require an API, service or machine-readable schema.

## Define the agreement

Identify the producing and consuming owners, the contract's authoritative home
and whether it is proposed or adopted. Link existing definitions. If several
copies disagree, use [source-of-truth](../source-of-truth/SKILL.md) to reconcile
them. Keep local implementation steps in their procedures.

Specify the obligations that matter for this exchange:

- Preconditions: required inputs, identity/revision, permitted effects and
  existing authority to act. Unresolved prerequisites remain visible.
- Result: what is returned or retained, who owns it, and the evidence linking it
  to the exact request and inputs.
- Acceptance: who checks which conditions, and what makes rejection or completion
  observable. Execution success, acceptance and downstream adoption may have
  different owners and criteria.
- Failure: incomplete output, interruption or invalid input; what remains valid,
  who diagnoses the issue and which action can follow.

Choose enough precision for each side to act without guessing. A short table may
suffice. Define fields, formats or status values only when participants need them;
do not impose a universal record template or turn every internal step into a
separate contract. Refer to policy for retention and authority. Changed obligations
or operating circumstances use [project-policy](../project-policy/SKILL.md).

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
Show what each side observes and which obligation the case checks. Synthetic
records establish design consistency; implementation and actual runs supply
separate evidence that participants honor the contract.

Keep the agreement in its existing document owner and link it from the architecture.
Report unresolved terms and the work they block. A schema, successful operation
or diagram alone does not demonstrate fulfillment of all obligations.
