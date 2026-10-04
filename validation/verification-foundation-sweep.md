# Verification foundation sweep — 2026-10-04

This review inspected all three members for skill quality before reviewing the
collection's consistency. It used Skill Creator, Clear Writing and its
instruction guidance. Diagrams and Tables supplied table guidance for the
collection routing table. No diagram was added or changed.

## Phase 1: skill quality

| Member | Coverage | Finding and change |
| --- | --- | --- |
| `verification-design` | Entrypoint, UI metadata, behavioral scenarios | Evidence selection, preservation of adopted gates and consolidation by failure signal were coherent. The handoffs named activities without linking their now-coinstalled owners; phase 2 made them reachable. |
| `test-audit` | Entrypoint, UI metadata, principles, triage, behavioral scenarios and review limits | Corrected the blanket claim that doubles cannot check requests: a strict double checks its own expectation, whose agreement with the real contract needs separate evidence. Kept runner changes within authorized edit scope, distinguished isolated integration networking from unit dependencies, preserved local coverage thresholds and narrowed the fail-fast caveat to runs that stopped early. Focused audits need only relevant gaps and peers. Existing authorization for test edits suffices to remove a focused marker. |
| `test-writing` | Entrypoint, UI metadata, unit tests, integration tests, fixtures, current behavioral scenarios and recorded trial limits | Aligned the entrypoint with its existing policy-approved real-data exception without permitting private data in tracked artifacts. Clarified isolated project-approved test services and the ban on fallback to developer, shared or production resources. Aligned the double-contract guidance and clarified sanitization of recorded responses, including nested content and metadata. |

The integration-test lifecycle, synthetic fixture construction, contract chain
tests, outcome assertions, private-value handling and copied-value check
properties were retained. Stored private values must be replaced with synthetic
ones; a real-data test reads its policy-approved source from an untracked home.
Required project gates and coverage thresholds remain authoritative.

## Phase 2: collection consistency

The collection has three distinct tasks: select evidence, author tests and audit
a settled suite. Direct sibling links now support those handoffs only when the
requested work reaches the neighboring task. Adding a regression does not start
a suite audit, and choosing evidence can end with a plan.

The test-writing description and collection table now refer to test inputs;
ordinary documentation examples and general probes do not inherit this workflow
merely because they contain input. Installation guidance now places project
routes in the consuming project's agent instructions, avoiding an apparent
instruction to edit the imported collection entrypoint. All three UI blurbs fit
the documented short-description range and retain the existing names, prompts
and invocation policy.

Package-boundary passages were compared with runtime-operations' denominator
rule, source-of-truth's fixture and ledger guidance, and database-migrations'
test lifecycle. These external mirrored rules were unchanged and require no
counterpart edit. The audit and authoring mock passages inside this collection
were revised together.

Collection version: `0.1.1`. Member versions: verification-design `0.1.1`,
test-writing `0.1.1`, test-audit `0.3.1`. These are corrections and clarified
routes within the intended contracts, with no rename, new framework, new gate,
automatic registration or release tag.

## Verification and limits

- The system Skill Creator's `quick_validate.py` passed for all three members.
- `git diff --check -- collections/verification-foundation` passed.
- A local path check resolved all 28 Markdown file links inside the collection's
  installation unit; all three UI short descriptions met the 25–64 character
  range. This check did not validate rendered output or heading anchors.
- The revised passages were compared with their prior text for preserved
  privacy, local authority, gates, permissions and conditional reference reads.
- Member and reference coverage above is static review. It is not a behavioral
  trial, a live-suite audit or evidence that instructions reliably affect agents.
- The root sweep owns final manifest/version synchronization, whole-repository
  package checks and complete-copy integrity verification. This pass deliberately
  did not regenerate the manifest or edit the distributed installation helper.
- Earlier validation rows about universally unfalsifiable double requests and
  all fail-fast runs describe prior wording. The distinctions in this sweep are
  the current expected behavior; old trial outcomes were not reinterpreted.

The changed routing needs practical trials with an installed copy outside the
authoring repository: a regression with synthetic fixtures; active-change
evidence selection; a settled-suite audit containing both a strict fake and an
isolated integration boundary; and a documentation-example near-miss. Record
actual reads, deeper references reached, constraints preserved and irrelevant
activation. Installation-route wording also needs a project-instruction-hook
check when the unified installation tooling is finalized.

## Additional improvements

- Add current-revision pointers from the existing member validation pages to
  this sweep while retaining their dated trial history and explicit limits.
- Run an independent authoring trial with the copied-value guard owned by the
  consuming project. The old sixth-revision limit still applies; instructions
  alone were less reliable than a project-owned check in the recorded trials.
- Use a strict fake and a deliberately guessed contract in an independent audit
  trial to verify that the revised lens distinguishes assertion strength from
  external contract evidence, without treating every mock as a defect.
- Consider a collection-level self-conformance checklist that points to each
  member's maintained scenarios rather than copying expected outcomes into
  another inventory.

## Coordinated completion

The [coordinated sweep](collection-sweep.md) records the final source inventories,
combined checks and retained consumer trials. Earlier pending or partial results
on this page describe the review stage at which they were recorded. No release
or installed Forge pin was changed.
