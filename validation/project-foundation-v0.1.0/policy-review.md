# Release review: policy, design, contracts and planning

Date: 2026-10-03. Fresh delegated reviewer context. Read-only review of the integrated working tree, committed during review as `fdbbb43bfde7c761c3c985bda44a2883a718acb1`. Independently compared assigned changed passages against both `ca00fc7` and `14086af`. No repository files edited.

## Findings

- Release gate failure: `collections/project-foundation/skills/project-policy/references/phase-and-scope.md:21` contains an extra blank line at EOF. The required whole-collection committed whitespace check fails on `fdbbb43`. Remove that blank line, commit the correction, and repeat the gate. This is a mechanical release blocker, not a semantic defect.
- No material semantic, authority, scope-preservation or document-home defect found in the assigned files. No exception proposed.

## Meaning and routing review

Applied self-conformance owners for source of truth, clear writing and instructional strength, status/evidence, table semantics, document ownership and links, and routing inspection. Read their linked review guidance. Checked the canonical document-home owner and foundation template, and inspected the foundation validator's relevant behavior claims.

The policy split preserves main's phase/delivery-scope treatment in `phase-and-scope.md`, the establishment axis and change consequences. It preserves existing guarantees, unknowns, assessment outside policy tables, authorized-work boundaries and proportional verification. The task-routing branch's read/application/design-review distinctions survive integration. A focused question can stop after relevant terms; changed circumstances still reach consequence review.

The canonical `project-docs/` homes remain current. Existing-layout transitions remain explicit. Planning retains one status/next-action owner and the old design next-step path routes to its new owner without duplicating the workflow. Design's phase and conceptual-model additions remain consistent with main. Adopted requirements, implementation and verified claims remain distinct; shared status guidance owns those meanings. Inheritance and local exceptions preserve shared authority; unavailable owners defer only dependent work.

Reviewed all tables semantically: policy axes, consequence prompts, synthetic shared plan, and shared status/evidence tables. The examples state their synthetic status. No diagram occurs in the assigned files.

## Complete file coverage

All paths below are relative to `collections/project-foundation/`; every assigned file was read fully.

- `skills/project-policy/SKILL.md`, `agents/openai.yaml`, and `references/establish.md`, `phase-and-scope.md`, `policy-changes.md`, `requirements.md`, `writing-policy.md`.
- `skills/project-design/SKILL.md`, `agents/openai.yaml`, and `references/conceptual-models.md`, `integrations.md`, `next-step.md`, `workflows.md`.
- `skills/project-contracts/SKILL.md`, `agents/openai.yaml`, and `references/design.md`, `review.md`.
- `skills/project-planning/SKILL.md`, `agents/openai.yaml`, and `references/example.md`, `next-step.md`.
- `references/foundation-authority.md`, `foundation-format.md`, `status-and-evidence.md`, `multi-repository.md`.

Total: 25 files. Fully inspected both baseline diffs for assigned changes; moved next-step and policy passages were compared in their new homes.

## Checks and limits

- `python3 scripts/validate-packages.py`: passed, 25 skill entries and one collection.
- `python3 -m unittest discover -s collections/project-foundation/tests`: passed, 14 tests.
- Local path and heading-anchor inspection: all 76 links from assigned files resolved.
- Whole committed collection whitespace: initially passed against the pre-integration HEAD `ca00fc7`; rerun after integration commit `fdbbb43` failed as reported above. The first result does not establish the integrated release gate.
- No live systems, installed-client discovery, new consumer routing trials, rendered-table inspection or operational compliance checks. Source inspection establishes reachable task routes and preserved obligations, not runtime routing reliability or visual readability. Other collection/catalog files are outside this delegated coverage.
