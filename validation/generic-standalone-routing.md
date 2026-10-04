# Generic fixture: routing review and draft answers

This trial used one fresh agent context for all three cases. It did not reset context between cases. It began with the fixture's `AGENTS.md` and followed that hook to the three local skills. The skill bodies were loaded together before the case sources; the cases therefore shared the hook and available guidance. No authoring source or provenance contents were inspected.

Fixture root: `/home/ladejarlen/Documents/Codex/2026-10-04/so-in-agent-skills-the-project/work/migration-trials/generic`.

## Draft answers

### 1. README paragraph

> The worker uses the cached lookup to avoid another lookup. It is unclear whether refreshing the cache during a request is safe.

The revision preserves the worker as the actor, the reason for using the cached lookup, and the uncertainty about refreshing it during a request. It makes no recommendation to refresh the cache and does not claim that doing so is safe or unsafe. This is a draft only; `README.md` was not edited.

### 2. MAX_TRIES drift and proposed authoritative home

`limits.py` and `worker.py` each define `MAX_TRIES = 4`. They agree now, but the assignments are independent. `tries_remaining()` reads the definition in `worker.py`, so changing the value in `limits.py` alone would leave the worker using its previous limit. Nothing in the inspected files connects or checks the two definitions.

The smallest adequate proposal is to keep the existing definition in `limits.py` as the authoritative home and replace the assignment in `worker.py` with an import from that module. A package-qualified import may be needed in an actual packaged application; the fixture supplies no package structure. This stops at rung 1 of the source-of-truth guidance: remove the restatement and have the consumer read its home. The value remains 4. No new configuration module, generator, or comparison gate is justified by the visible same-language arrangement.

The concept is the maximum number of tries. `limits.py` is a proposed home based on its current role, not a historically established owner verified by this review. The proposal removes the separately editable worker value; merely documenting that both assignments should change together would leave the drift risk in place. No implementation or test was performed.

### 3. Meaning of flow.md against policy

The diagram says to read a draft, ask “Terms known?”, and go to “Accept” on both the `yes` and `no` branches. The `no` branch therefore reaches acceptance despite unresolved terms.

The prose directly below the diagram requires unresolved terms to be referred back to the owner. The drawn `no` path conflicts with that requirement because it goes straight to “Accept” and shows no referral. A reader following the diagram could accept a draft without the required owner referral.

The smallest proposed semantic correction is for the `no` branch to lead to a step that refers the unresolved terms back to the owner. The supplied policy does not establish what happens after referral, who the owner is, or what permits later acceptance; those remain unknown. This review makes no claim about implemented or deployed behavior. It reviewed source meaning only, with no diagram change, rendering, redraw, or visual-readability assessment.

## Routing evidence

The ordinary hook explicitly selects clear-writing for prose and instructions, source-of-truth for repeated definitions, and diagrams-and-tables for diagrams. It also says to preserve facts and uncertainty and declares no project-foundation installation.

| Case | Guidance selected through the hook | Additional route taken | Guidance intentionally not loaded |
| --- | --- | --- | --- |
| README rewrite | `clear-writing/SKILL.md` | Compared the revision with the supplied explanatory paragraph, especially its uncertainty | Instruction-writing and short-text references: this is explanatory prose, not an edited procedure, rule, or label |
| MAX_TRIES review | `source-of-truth/SKILL.md` | `references/definitions.md` for the home and rung decision; focused source search for retry expressions | Boundaries and check-design: direct reuse is the adequate proposal, and no boundary or retained check was identified |
| Flow meaning review | `diagrams-and-tables/SKILL.md` | `references/review.md` for semantic review and `references/flowchart/read.md` for the relevant flowchart notation | Form selection, construction, Mermaid syntax, examples, and visual verification: no selection, editing, redraw, or visual review was requested |

### Actual content reads

Paths in this table are relative to the fixture root. Counts are whitespace-separated words, including headings, front matter, and code, rather than model tokens. Each complete body was returned once. “Required” means directly requested source or guidance selected by the hook and task route; “useful” means focused supporting guidance beyond the minimum needed to understand this simple notation.

| File actually read | Words | Classification and purpose | Repeated or reused context |
| --- | ---: | --- | --- |
| `AGENTS.md` | 48 | Required: starting hook and scope | Shared across all cases; later reopened only for word-count metadata |
| `.agents/skills/clear-writing/SKILL.md` | 593 | Required: prose route and certainty preservation | Shared while writing all draft answers; later reopened only for word-count metadata |
| `.agents/skills/source-of-truth/SKILL.md` | 653 | Required: repeated-definition route | Available throughout this one context; later reopened only for word-count metadata |
| `.agents/skills/diagrams-and-tables/SKILL.md` | 571 | Required: diagram route and task selection | Available throughout this one context; later reopened only for word-count metadata |
| `README.md` | 30 | Required: paragraph to rewrite | Subsequently scanned by a focused `rg`; no matching text was returned |
| `limits.py` | 3 | Required: first MAX_TRIES definition | Matching definition returned again by focused `rg` |
| `worker.py` | 9 | Required: second definition and consumer | Its three substantive lines returned again by focused `rg` |
| `flow.md` | 31 | Required: diagram and stated policy | Subsequently scanned by focused `rg`; no matching text was returned |
| `.agents/skills/source-of-truth/references/definitions.md` | 1,393 | Required: selecting a home and the smallest adequate rung | Retained in the same context; no repeated body read |
| `.agents/skills/diagrams-and-tables/references/review.md` | 216 | Required: semantic-review route | Retained in the same context; no repeated body read |
| `.agents/skills/diagrams-and-tables/references/flowchart/read.md` | 234 | Useful: confirms the meaning of the relevant action, decision, and branch notation | Retained in the same context; no repeated body read |

Unique content: 11 files and approximately 3,781 whitespace words, comprising 3,708 words of hook/guidance and 73 words of task source. Of these, 3,547 words are classified required and 234 useful. No irrelevant file body was read.

The accounting distinguishes file I/O from context repetition:

- A later count-only metadata pass reopened `AGENTS.md` and the three skill bodies, totaling 1,865 words scanned. It returned their counts, not their bodies; this was repeated file I/O without a second full-text context load.
- A focused `rg` searched `README.md`, `limits.py`, `worker.py`, and `flow.md`, totaling 73 source words scanned. It returned about 12 words of already-seen source lines from the two Python files. This is actual partial context repetition.
- `rg --files --hidden -g '!.git/**'` listed the fixture paths to find its available source files and references. That inventory exposed filenames, including `PROVENANCE.md`, but did not read their contents. `PROVENANCE.md`, all `agents/openai.yaml` files, and the unselected references were not opened.
- An attempted read of `findings.md` failed because the file does not exist. It yielded zero source words. This was an avoidable, zero-content probe of the capture destination, not a missing required prerequisite: the hook describes where consequential guidance findings are recorded, and the skills say successful work needs no capture pass.

The case-specific content groups are 671 words for the hook/writing/README group, 2,058 newly loaded words for the source-of-truth/Python group, and 1,052 newly loaded words for the diagram group. These groups partition the unique reads; they are not three independent fresh-context measurements. All three skill bodies were actually loaded in the same initial batch, so later cases could reuse earlier context without another file read.

### Missed guidance, constraints, and limits

No known task-relevant skill route was missed. The definitions reference recommends history evidence when establishing ownership or prior drift. That evidence was not inspected here: this review proposes an owner from the current visible modules and establishes a possible drift mechanism, not a claim about historical ownership or a past shipped incident. No fixture provenance or surrounding repository history was needed for that bounded proposal.

No consequential guidance or routing defect was found during execution, so no finding was added and no guidance repair was attempted. The missing `findings.md` did not prevent any case from using its declared route.

Preserved output constraints:

- The README revision retains uncertainty and changes no substantive fact.
- MAX_TRIES is reviewed and a small authoritative home is proposed without implementation.
- The diagram is reviewed against its stated policy without rendering, editing, redraw, or inferred owner/resolution rules.
- Fixture source and skill files remain untouched; only this requested evidence artifact was written outside the fixture.
- No authoring source or provenance content was inspected, and no messages were sent to other chats.

The review is bounded to the visible fixture sources. It does not establish package import behavior, broader application policy, Git history, runtime behavior, or rendered readability. Shell calls emitted “Failed to create stream fd: Operation not permitted” notices, but the requested file content and searches completed successfully; the intentional `findings.md` probe was the only failed read.
