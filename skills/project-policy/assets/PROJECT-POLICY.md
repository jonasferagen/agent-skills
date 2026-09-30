# Project policy

<!-- Adapt this template to the project. Replace prompts with facts and decisions;
keep unknowns explicit. Reuse existing canonical homes and remove authoring notes.
The template itself chooses no risk level, recovery target or permission. -->

## Scope and authority

State the project and environments covered, policy owner, effective date and
review date. Separate the current operating scope from any intended expansion.
Name the existing authorization boundaries. Link the active plan, implementation
status and detailed engineering conventions.

## Project profile

| Axis | Current fact or decision | Evidence or unresolved question |
| --- | --- | --- |
| Intended lifetime | State the expected lifespan and maintenance intent | Cite the decision, or mark unknown |
| Users and reliance | Name users and consequences of failure | Cite the decision, or mark unknown |
| Data | Describe sensitivity, ownership and replaceability | Cite the decision, or mark unknown |
| Exposure and authority | Describe reach, identities and allowed effects | Cite the decision, or mark unknown |
| Compatibility | Identify consumers and state that must survive changes | Cite the decision, or mark unknown |
| Recovery | State acceptable loss/downtime and recovery responsibility | Cite the decision, or mark unknown |

## Requirements and their owners

For each consequential profile choice, state an observable requirement, where
its procedure lives, and what evidence establishes it. Preserve existing
commitments. Keep commands and implementation details in their owning guides.

| Requirement and reason | Canonical procedure or contract | Evidence or open work |
| --- | --- | --- |
| Replace with a concrete obligation derived from this project's profile | Link its owner | Link current evidence or the active work item |

Document deliberate exclusions and their boundaries. “No backup requirement for
disposable synthetic test data” does not make a retained development volume
disposable. Record exceptions with their scope, rationale, owner and review or
expiry condition; do not silently mark an unmet requirement complete.

## Policy changes

Every edit includes an impact assessment; wording-only changes can record that
obligations are unchanged. Changes in users, data, exposure, lifetime,
compatibility or recovery also trigger review, even without a policy-file edit.

For substantive changes, record the old and new requirements and assess code,
stored data/migrations, interfaces, identity/permissions, tests/release checks,
operations/recovery, documentation and agent/skill guidance. Include affected
external consumers when known; mark uninspected areas explicitly.

Put follow-up work in the active queue with an owner, dependencies, acceptance
evidence and a gate for the changed use. Tightening requires evidence before
claiming compliance; relaxing requires an explicit account of the guarantees
removed and affected consumers. Do authorized in-scope work and keep other gaps
visible. Policy changes do not themselves authorize external operations.

Start with a manual review. Maintain a short dated change record linking the
impact review, active work and evidence. Automate repeated transitions when
experience justifies it; no automatic full-project audit is implied by a typo.

## Open decisions and transition work

Link the project's active queue and identify which unresolved decisions block
which future uses. Keep implementation status and detailed task lists at their
existing canonical locations rather than duplicating them here.
