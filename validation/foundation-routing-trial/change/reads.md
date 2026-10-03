# Read and check log

All work was confined to `/tmp/foundation-routing-round3/change`. Counts use `wc -w`.

## Actual content reads, in order

1. `AGENTS.md` — 41 words.
2. `context.md` — 89 words.
3. `.agents/collections/project-foundation/COLLECTION.md` — 344 words.
4. `.agents/collections/project-foundation/skills/project-policy/SKILL.md` — 683 words.
5. `.agents/collections/project-foundation/references/foundation-authority.md` — 440 words.
6. `.agents/collections/project-foundation/references/authoring.md` — 248 words.
7. `policy.md` — 82 words.
8. `evidence.md` — 18 words.
9. `.agents/collections/project-foundation/skills/project-policy/references/policy-changes.md` — 1,102 words.
10. `.agents/collections/project-foundation/skills/project-policy/references/requirements.md` — 217 words.

Total unique source content read: 3,264 words. Instruction content: 3,075 words; task and project facts: 189 words. `answer.md` contains 1,123 words.

## Routing and instruction assessment

Selected project-policy because the request assesses changed users, responsibility and lifetime. Its change workflow led to requirement discovery because successor access and ownership need decisions. Foundation authority was relevant to changed circumstances. No contract was supplied or being authored, so the word “handoff” alone did not justify loading project-contracts. Policy-writing guidance was unnecessary because adoption and policy edits were explicitly excluded.

The authoring reference was an unnecessary 248-word read: it confirms that a focused answer from existing policy requires no further authoring references. No clear-writing or visual-construction route was loaded. Some high-level authority and proposal/evidence distinctions repeat across the collection, policy skill, authority and change guidance, but no consequential ambiguity or omission resulted. No missing reusable instruction was identified. Missing owners, procedures and operational evidence are project gaps, not established guidance defects.

## Repeated or truncated reads

No source content was redisplayed or truncated. Final assertions reread `policy.md` (82 words) and `evidence.md` (18 words) programmatically for preservation checks, and read generated `answer.md` (1,123 words) for topic checks. This log was reread once to clarify those validation reads. `wc -w` scanned the same files to measure counts without returning their content. A filename-only `rg --files` inventory excluded installed guidance, known project inputs and generated outputs; its only additional result was `UPSTREAM.md`, which was not opened. No source repository, other fixture or external resource was inspected.

## Checks and execution

Compared every policy axis with the proposed use; traced all seven consequence areas in policy-changes; checked whether the backup observation supports restoration or the loss limit; identified decision owners, dependent work, acceptance evidence and handoff milestones. The filename inventory found no additional foundation declaration, boundaries, overview, runbook or queue. No live or operational checks were authorized or performed.

An initial attempt to write `answer.md` using `python` failed because that executable was unavailable; it made no file changes. The answer was then written with a shell heredoc. Only `answer.md` and `reads.md` were created. Installed guidance and project inputs were preserved. Final local assertions checked the answer's required topics and exact unchanged adopted policy and evidence text.
