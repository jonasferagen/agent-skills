# Validation scenarios — Project policy

These cases describe observable outcomes. Recorded executions below distinguish
actual trials from author review.

| Request and context | Expected outcome |
| --- | --- |
| Bootstrap a short-lived CLI with synthetic inputs | A small profile and concrete requirements; no production operating machinery inferred from the template. |
| An experiment processes real customer data | Data and authority assessed separately from lifetime; “experiment” does not waive protection or retained-state obligations. |
| A local prototype is moving to an internal pilot with real notes | Separate current scope from planned use; identify downstream work, decision gaps and readiness gates; do not deploy. |
| A tool with retained records and dependent clients is relabelled a prototype | Retain existing guarantees unless deliberately changed; inspect effects on consumers and state. |
| Correct one typo in a policy | Make the correction and record no obligation change; no full test run or operational audit. |
| An exposure change was already made before the policy caught up | Record the observed condition, unmet requirements and authorized containment/remediation; do not call it only a future risk. |
| A stricter recovery policy is adopted without a restore test | Separate adoption from verified compliance; track restore evidence and the use it gates. |
| A policy is relaxed | Identify guarantees removed and dependencies; do not silently delete tests, history or data. |
| Recovery expectations are unknown | Keep them unknown and identify the use they block; do not invent numerical loss/downtime targets. |
| Production and local tests have different data/lifetime profiles | Keep scopes distinct and preserve shared obligations; local disposability does not propagate to production. |
| A copied package has no other foundation skills installed | The policy skill works using its own template and reference; optional companions do not become dependencies. |
| Existing architecture and tests exceed the required minimum | Consider simpler mechanisms, distinguish choices from explicit commitments, and preserve required outcomes with evidence; do not freeze every mechanism into policy. |
| Synthetic local testing will start using a local copy of production data | Review sensitivity, permitted copying, access, logs, retention/deletion and source isolation; local deployment does not make the data synthetic or authorize import. |
| The owner specifies a one-time frozen-source import and explicitly defers backups and restore rehearsal | Preserve that scoped decision and verify import integrity; do not add cloud connectivity or a backup/rehearsal gate. Record that the freeze does not prove ongoing recovery coverage. |
| Broad policy impact suggests work beyond the current authorization | Complete authorized in-scope work and record concrete follow-ups; do not acquire implied permission to deploy or contact users. |

## Initial application — 2026-09-30

Applied to the existing local Atlas/Work development project. Its current
milestone plan, synthetic-data scope, retained development state, immutable
migrations and separate source installations informed the policy. Adoption adds
manual impact review and queue routing; it does not weaken the existing test
gates or expand operational scope. The project's HANDOFF records its checks.

## Independent trials — 2026-09-30

A separate agent received the skill and three synthetic requests, without this
validation file, expected outcomes or the Atlas/Work policy. It created isolated
temporary repositories and applied the skill:

| Trial | Observed artifacts and behavior |
| --- | --- |
| Local experiment moving to a five-person internal pilot with real project notes | Revised policy, seven-area impact review and five owned tasks with dependencies, evidence and pilot gates. Sensitivity and recovery targets remained unknown; retained state and immutable migrations stayed protected. |
| Existing internal tool with real records, nightly backups and two clients relabelled a prototype | Updated label and impact review; preserved backup, data, migration and client obligations. No application or queue change. |
| Policy spelling correction | Exact typo replacement and a short no-obligation-change record; no expanded audit or task queue. |

The author inspected the generated policies and pilot tasks. Local link checks
passed (16, 13 and 4 links respectively); the typo replacement was checked for an
exact one-word change. The evaluator noted that the general axis-verification
bullet could invite excess work on a typo; it now explicitly scopes full profile
verification to establishment or substantive revision.

These are synthetic document trials. They do not verify production transitions,
runtime protections, live recovery or every scenario above. Temporary artifacts
were under `/tmp/project-policy-trial-cTDJSE`; the outcomes here are the durable
record. The final wording clarification was author-reviewed, not independently
re-executed.

## Package checks — 2026-09-30

`python3 scripts/validate-packages.py` passed for all 13 packages. The skill-creator
manifest validator passed for all five foundation skills. A local Markdown
link/heading-anchor scan passed for 201 links across 61 Markdown files in this
repository. `git diff --check` passed. External URLs were not revalidated; no
runtime helpers or diagram sources changed.

The owner's follow-up clarified that policy is a minimum and that the next
Atlas/Work transition is a local production-data copy. The minimum-guarantee
guidance and two scenarios above were added and author-reviewed. The three
independent trials predate this clarification; they were not rerun because it
does not change their required outcomes.

## Discovery routing — 2026-09-30

The description was shortened. See [the discovery review](discovery.md) for the measured sizes, scope and verification. Earlier behavioral results do not establish the new discovery behavior.
