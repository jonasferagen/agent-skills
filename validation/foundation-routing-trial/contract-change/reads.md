# Reading log

Counts use `wc -w` for the actual full files read. All paths are relative to this fixture.

| Order | File | Words | Purpose |
| --- | --- | ---: | --- |
| 1 | AGENTS.md | 30 | Entry route, authoritative owners and scope limits |
| 2 | context.md | 50 | Requested assessment and reported operating change |
| 3 | .agents/collections/project-foundation/skills/project-contracts/SKILL.md | 427 | Apply adopted handoff terms and route changed circumstances |
| 4 | exchange.md | 34 | Adopted handoff agreement |
| 5 | policy.md | 49 | Data, exposure and compatibility obligations |
| 6 | .agents/collections/project-foundation/references/foundation-authority.md | 440 | Preserve policy authority despite changed observed behavior |
| 7 | .agents/collections/project-foundation/references/foundation-format.md | 803 | Follow authority reference; confirm separate existing owners remain valid |
| 8 | .agents/collections/project-foundation/skills/project-policy/SKILL.md | 683 | Assess already-observed change |
| 9 | .agents/collections/project-foundation/skills/project-policy/references/policy-changes.md | 1102 | Consequences, remediation owners and necessary evidence |
| | Total full-file content | 3618 | |

## Repeated or truncated reads

No full file was reread and no output was truncated. A targeted `rg -n` search repeated matching lines from AGENTS.md, context.md, exchange.md and policy.md to check consumers of the affected rule. `wc -w` counted the nine listed files without reprinting contents. A file listing revealed UPSTREAM.md; its contents were not read. No other fixtures or source repositories were inspected.

## Unnecessary or missing instructions

The foundation-format reference was linked by authority guidance, but most of its 803 words concern a foundation layout, symbolic references and inheritance absent from the supplied separate-owner setup. Its statement that existing separate homes remain valid was useful; the other format detail was unnecessary to the conclusion. No missing instruction prevented the assessment. Missing implementation, incident history, operational owners and evidence are project/evidence gaps, not instruction defects. The change guidance supplied a broader consequence checklist than the small fixture can verify; those limits are made explicit in the answer.

## Checks performed

- Compared reported acceptance with the contract's acceptance and reporting conditions.
- Compared reported external delivery with all three policy axes.
- Searched the supplied project inputs/instructions for local/external delivery, public bucket and accepted-file preservation references.
- Assessed changed delivery consequences across architecture, stored data, interfaces, access, checks, recovery and guidance using only supplied evidence.
- Counted actual reading sizes; checked the written deliverables exist and computed final hashes of the nine read files. No pre-write hash baseline was captured; preservation rests on the commands writing only answer.md and reads.md.

No operational checks, bucket access, external activity or remediation was performed.

A log correction initially failed because `python` was unavailable; it succeeded with `python3`. This reread only the generated reads.md, not a source or guidance file.
