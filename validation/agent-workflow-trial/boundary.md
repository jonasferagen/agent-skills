# Consumer routing trial: interaction-order boundary

## Answer

Use a sequence diagram. The reader needs the exact order of calls, messages and replies between participants whose ownership is already known. Give the agent client, job API and worker separate lifelines and read time from top to bottom. This follows the form-selection guidance for ordered interactions and its specific advice to use a sequence diagram when exact agent-related calls, messages and replies matter (installed/project-foundation/skills/diagrams-and-tables/references/select.md, “Choose a form”).

The proposed view should trace a single job: the client's submit request, the API's reply carrying the job ID, repeated polling requests using that ID and their status replies, the timeout at the participant that actually enforces it, and the subsequent completion and any late messages. Show the worker's receipt of work and its completion report at their established positions relative to the other exchanges. Mark polling as repetition, identify each sender and receiver, and label what each reply conveys. Make the timeout and late-completion path explicit, including whether polling has stopped and what the client actually receives or observes afterward. If completion can occur before or after the timeout, show those as conditional alternatives, not as two events that must both occur in every run.

The prompt does not establish the full protocol order. Before anyone draws an exact trace, they should resolve whether worker dispatch precedes or follows the job-ID reply, what the timeout measures and where it occurs, whether it cancels work, and how late completion becomes visible. Keep those points marked as unknown until supported by the existing protocol; do not invent cancellation, callbacks, retries or delivery paths. The outline describes what to explain, not a service redesign.

## Routing evidence

This was a fresh consumer read of the installed fixture. The route was AGENTS.md → installed/project-foundation/skills/diagrams-and-tables/SKILL.md → references/select.md. The specific diagram-only route in AGENTS.md applied to this form-selection question. The selection reference explicitly covers exact agent calls, messages and replies, so responsibility-oriented swimlane guidance was unnecessary despite the agent/client/API/worker nouns.

| File read | Approximate whitespace words | Instruction-read classification |
| --- | ---: | --- |
| AGENTS.md | 54 | Required: project entry point and direct diagram-only route |
| installed/project-foundation/skills/diagrams-and-tables/SKILL.md | 587 | Required and useful: choose-form/prose-outline route and scope boundaries |
| installed/project-foundation/skills/diagrams-and-tables/references/select.md | 331 | Required and useful: selects a sequence diagram for exact interactions |
| **Total** | **972** | **No irrelevant instruction files loaded** |

Counts were measured with `wc -w`. Each file was read once in full with `cat`; the word-count command accessed those same files only to count words and did not repeat their instruction contents. No tool output was truncated. No prior trial findings, earlier consumer reads or authoring context were reused; the task assignment and inherited execution constraints were available. Shell startup emitted stream-fd warnings, but all three content reads and the word-count command succeeded.

No source authoring repository, collection overview, family construction manual, renderer guide, verification guide or unrelated family reading notes were read. The project entry point's narrower diagram-only route made a collection-wide read unnecessary. No consequential routing problem or missed applicable guidance was identified, so no capture or repair pass was triggered.

Constraints preserved: recommendation and outline are prose only; no diagram was drawn, no service behavior was redesigned, no documentation was changed, and no live system was touched. Only this requested trial result was written. Git inspection reported that the fixture is outside a repository, so the outside-Git instruction allowed writing directly without a worktree. The existing protocol remains unverified and unspecified details remain unknown.
