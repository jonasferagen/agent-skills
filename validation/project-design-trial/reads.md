# Consumer routing trial log

## Content reads and whitespace word counts

All paths below are relative to this fixture. Each content file was displayed once, in full, with no truncated output. Counts come from `wc -w`.

- AGENTS.md: 17 instruction words.
- README.md: 123 project words.
- .agents/collections/project-foundation/COLLECTION.md: 535 instruction words.
- .agents/collections/project-foundation/references/multi-repository.md: 710 instruction words.
- .agents/collections/project-foundation/references/foundation-authority.md: 440 instruction words.
- .agents/collections/project-foundation/skills/project-design/SKILL.md: 544 instruction words.
- .agents/collections/project-foundation/references/authoring.md: 248 instruction words.
- .agents/collections/project-foundation/skills/project-design/references/next-step.md: 221 instruction words.
- .agents/collections/project-foundation/skills/clear-writing/SKILL.md: 549 instruction words.
- .agents/collections/project-foundation/skills/diagrams-and-tables/SKILL.md: 431 instruction words.
- result.md: 665 output words, read once after writing for verification.

Instruction content totaled 3,695 words. Project input totaled 123 words. Verified output totaled 665 words. Combined displayed file content totaled 4,483 words. This log itself is additional generated output and is excluded from those reading totals. The counting command accessed previously read files again but did not redisplay their content. There were no repeated model-facing content reads.

## Routing and usefulness

AGENTS routed through README and COLLECTION to project-design. Multi-repository guidance applied before assigning proposed document or state owners. Foundation authority preserved existing roles and scoped choices. Project-design supplied the concrete normal/rejection walkthrough, identity and retry questions. Next-step guidance produced an owner, inputs, expected result and acceptance evidence for the next design task. Authoring and clear-writing governed the new explanation. Diagrams-and-tables was used for form selection; concise prose was sufficient, so no construction or rendering references were loaded.

Every selected file had applicable guidance. The multi-repository file included installation, symlink and runtime access material irrelevant to this local design request; its ownership guidance was useful. COLLECTION included unused installation and template material. No source-authoring catalog, release rules, implementation scripts, template files, policy audit, rendering guidance or external sources were read. No definite missed applicable guidance was identified; absence of foundation, architecture and planning owners is a fixture limitation, explicitly reported in the result.

The unrelated typo request needed no additional skill content: COLLECTION's literal-edit exception was sufficient. No typo edit was performed.

## Execution and limits

The first shell call failed before execution because the inherited default process environment could not launch. Retrying with explicit /bin/bash and /tmp succeeded. A file-name inventory found the fixture files; this did not load their contents. A Git root check reported that the fixture was outside Git, so the collection's task-worktree rule did not apply.

Only result.md and this log were written, both inside the fixture. No external calls, source authoring repository reads, software implementation, infrastructure selection or real data operations occurred. The output is a reviewed design proposal, not proof of implementation, runtime recovery or automatic client skill discovery. The trial used a fresh child task with the consumer fixture supplied by the parent; platform instructions and the general available-skill catalog remained in inherited context.
