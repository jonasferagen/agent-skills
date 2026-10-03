# Actual reads

Word counts use `wc -w` on the complete files read.

| File | Words | Purpose |
| --- | ---: | --- |
| AGENTS.md | 30 | Task entry, direct contract route and owners |
| context.md | 50 | Requested assessment and reported behavior |
| .agents/collections/project-foundation/skills/project-contracts/SKILL.md | 427 | Applying handoff obligations and changed-scope routing |
| exchange.md | 34 | Adopted handoff obligations |
| policy.md | 49 | Adopted data, exposure and compatibility constraints |
| .agents/collections/project-foundation/references/foundation-authority.md | 458 | Changed operating circumstances and owner authority |
| .agents/collections/project-foundation/skills/project-policy/SKILL.md | 683 | Policy assessment and observed-change route |
| .agents/collections/project-foundation/skills/project-policy/references/policy-changes.md | 1102 | Consequences, owners, evidence and readiness gate |
| UPSTREAM.md | 14 | Checked remaining project file for a relevant owner or consumer; only provenance |
| **Total** | **2847** | |

## Reading efficiency

No whole file was reread and no output was truncated. The scoped `rg` search repeated matching lines from AGENTS.md, context.md, policy.md and exchange.md; this was a consumer search, not an additional whole-file read. Counts above count unique full-file content, not repeated search snippets. A filename listing and word counts added no substantive instructions.

UPSTREAM.md was unnecessary in hindsight (provenance only). The policy change reference contains writing, relaxation and implementation details beyond this assessment, but its observed-change, consequences and follow-up instructions were relevant. No missing routing instruction blocked the task. No foundation-format, contract-design/review, policy-writing or authoring workflow was needed: the separate owners were explicit, and this was a focused application and changed-circumstance assessment. Requirement discovery was unnecessary because the current local boundary is explicit and cloud adoption was not requested.

Project/evidence gaps: candidate identification, actual completion report timing, rejection handling, retained copies and identity preservation, cloud exposure/access history, downstream dependencies, accountable policy/cloud roles and operational records. These are not missing skill instructions. The supplied files contained no task queue, implementation or runbook; follow-up work is captured in answer.md without inventing an adopted project queue.

## Checks performed

- Listed project files outside installed guidance using `rg --files --hidden`.
- Searched project Markdown for local/external, retention, accepted files, bucket, handoff and completion references.
- Compared reported behavior with agreement and policy; traced the changed exposure across consequence areas.
- Counted all read files with `wc -w`.
- Created only answer.md and reads.md; preserved project inputs and installed guidance.
- No external actions, bucket inspection, policy modification or operational execution.
