# Read record

All paths below are relative to this fixture. Word counts use `wc -w`.

| Actual content read | Words | Purpose |
| --- | ---: | --- |
| AGENTS.md | 41 | Initial instructions and document ownership |
| context.md | 50 | Assessment request and observed condition |
| .agents/collections/project-foundation/COLLECTION.md | 344 | Select relevant route |
| .agents/collections/project-foundation/skills/project-policy/SKILL.md | 683 | Assessment and observed-change routing |
| .agents/collections/project-foundation/references/foundation-authority.md | 440 | Authority under changed circumstances |
| policy.md | 82 | Adopted obligations |
| evidence.md | 18 | Supplied recovery evidence |
| .agents/collections/project-foundation/skills/project-policy/references/policy-changes.md | 1102 | Containment, consequences, owners and acceptance evidence |
| .agents/collections/project-foundation/skills/project-policy/references/requirements.md | 217 | Missing decisions for any future public use |
| **Total distinct source content** | **2977** | |

## Other reads and repetition

- Ran `rg --files --hidden` excluding installed guidance and Git internals to inventory project paths. It returned AGENTS.md, context.md, policy.md, evidence.md and UPSTREAM.md. UPSTREAM.md was not opened: provenance was not relevant to the assessment.
- Ran a targeted `rg -n` search over AGENTS.md, context.md, policy.md and evidence.md for exposure, archive, recovery and ownership terms. This repeated matching lines from already-read sources to check affected consumers. No full source file was reread and no output was truncated.
- Ran `wc -w` for the nine source files listed above. This counted source text without presenting a second content read.

## Guidance assessment

No consequential missing instruction or routing defect was found. The observed-change branch correctly requires immediate treatment of an existing breach, separately from adoption and readiness. Authority guidance overlapped with the policy skill on preserving adopted obligations, but its read was explicitly relevant to changed circumstances. Requirement discovery was short and relevant to unresolved future-use decisions. No establishment, policy-writing, shared-authoring, installation or source-maintenance guidance was needed.

Absent deployment evidence, restore results, detailed authority, operational runbooks and downstream consumers are project/evidence gaps, not missing skill instructions. No friction record was warranted.

## Checks performed

- Compared reported public document serving with offline/no-transfer and private-use commitments.
- Checked consequences across the seven areas required by change guidance.
- Distinguished current contradiction, unverified protection/recovery claims and unadopted future decisions.
- Kept concrete follow-ups outside execution authorization; performed no external action or network access.
- Created only answer.md and reads.md; preserved installed guidance and project inputs.
