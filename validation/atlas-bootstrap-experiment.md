# Atlas bootstrap experiment — 2 October 2026

## What was tried

Applied the collection to the existing fresh local repository at
`personal/atlas`. Used the owner's current decisions: maintained project,
local operation, no application network access, synthetic non-sensitive data,
no initial containers, and no environment validation at this stage. Planning
for later needs does not adopt their requirements now.

Created overview, boundaries and policy, linked them from the existing README,
and added a short operating summary with task routes in AGENTS.md. Copied the
complete 33-file collection into `.agents/collections/project-foundation/` and
recorded its uncommitted source revision, changes and snapshot digest in provenance.
No glossary, application code, dependencies, database or service was created.

The earlier agreement example remains a proposed slice. Product purpose,
language, interface and storage remain open. Network restrictions for loopback
and dependency acquisition must be clarified before introducing either.

## Observations

| Observation | Consequence and disposition |
| --- | --- |
| The prior instructions required all three foundation documents before substantive work. | Revised the experiment to use a small operating summary and task-specific reading; its effectiveness still needs real follow-up tasks. |
| Policy and overview both invite environment facts. | Policy owns operating constraints; overview links to those and records implementation choices. Future changes must preserve this distinction. |
| A generic documentation reference assumed a glossary existed. | Updated it to use established terminology and add a glossary only when ambiguity warrants one. |
| The no-network decision leaves loopback and dependency downloads unspecified. | Recorded the open distinction rather than choosing a storage engine or setup workflow that silently settles it. |

The AGENTS.md is 198 whitespace-delimited words. The three project documents
contain 532 words combined. The installed collection has six entry points and
33 files; those are installation counts, not a requirement to load them all.
No model context usage or task-time savings were measured. This was author-led
application, not an independent behavioral trial.

## Checks and limits

Repository package validation passed for 22 skill entries. All 82 local Markdown
link targets in Atlas resolved; the collection copy matched the source files.
No default glossary was created. Whitespace checks passed in both repositories.
These checks cover document integrity only. No runtime, container, database,
network or deployment behavior was exercised.

Next evidence should come from an actual everyday task, an implementation decision
within the current constraints, and a policy transition. Record unnecessary reading
and missed obligations. These observations do not yet justify a separate
friction-capture skill or a claim that the consultation model is effective.

## Friction follow-up — 2 October 2026

The source bootstrap now states the ownership distinction used in this trial:
policy holds operating constraints and required guarantees; overview holds chosen
mechanisms and open implementation options. A no-network constraint versus a
local database choice illustrates the boundary. This is a clarification of the
trial's result, not a measured reduction in context or document churn.

The reading and glossary issues were already corrected. The network question
remains local and open until needed. No additional skill was created. The Atlas
collection remains its recorded draft snapshot; this source-only clarification
was not installed downstream.

## Independent rerun — 2 October 2026

After committing the source as `13771b91ef0c6634aee23455032ec157ab36ac4b`
and the original Atlas foundation as `7ee11d3`, a subagent without conversation
history received the collection and the original project intent. It used a fresh
temporary repository and did not read the earlier Atlas documents or trial report.

It produced seven project files, including provenance, plus the complete 33-file
collection matching the committed source. The parent inspected README, AGENTS,
overview, policy, boundaries and provenance. Stack, interface, storage and product
scope remained open; the agreement slice stayed proposed. No glossary, network
calls, application dependencies or environment validation were introduced.

The subagent reported 83 valid local links/anchors, no unresolved template prompts
and clean whitespace. The source repository and real Atlas were left unchanged.
Artifacts remain at `/tmp/atlas-bootstrap-trial-tpJIPJ/`; this record preserves
the results if the temporary directory is later removed.

### Reading and friction

The subagent reported 8,496 whitespace-delimited words across 17 instruction and
template files emitted to its context. This excludes metadata, authored drafts,
mechanical verification reads and generated-file review; it is not a token or
whole-session context measurement.

| File read | Words |
| --- | ---: |
| `AGENTS.md` | 286 |
| `collections/project-foundation/skills/project-bootstrap/SKILL.md` | 847 |
| `collections/project-foundation/COLLECTION.md` | 288 |
| `collections/project-foundation/references/authoring.md` | 162 |
| `collections/project-foundation/references/foundation-authority.md` | 339 |
| `collections/project-foundation/skills/project-policy/SKILL.md` | 1,012 |
| `collections/project-foundation/skills/project-docs/SKILL.md` | 783 |
| `collections/project-foundation/skills/clear-writing/SKILL.md` | 549 |
| `collections/project-foundation/skills/clear-writing/references/instructions.md` | 506 |
| `collections/project-foundation/skills/diagrams-and-tables/SKILL.md` | 364 |
| `collections/project-foundation/skills/project-docs/references/structure.md` | 600 |
| `collections/project-foundation/skills/project-docs/references/diagrams.md` | 371 |
| `collections/project-foundation/templates/README.md` | 7 |
| `collections/project-foundation/templates/docs/project/boundaries.md` | 39 |
| `collections/project-foundation/templates/docs/project/policy.md` | 49 |
| `collections/project-foundation/templates/docs/project/overview.md` | 73 |
| `collections/project-foundation/skills/diagrams-and-tables/references/composition.md` | 2,221 |

The clearest friction was table authoring routing through the 2,221-word visual
composition reference, including substantial diagram detail unrelated to the
output. The next candidate is a smaller form-selection/table route with diagram
composition loaded only when a diagram is selected. This is a proposed follow-up;
no guidance was changed during the rerun.

For a routine follow-up, the subagent shortened “A personal project, currently at
the planning stage” to “A personal project in the planning stage.” It reread only
AGENTS and README: 254 words. It reused authoring guidance already in context and
made no policy review or revision change. This supports the warm-context route;
a cold-start everyday task has not yet been tested. No substantive instruction
conflict was reported. The parent did not independently reproduce each behavioral
check, and one trial does not establish reliable discovery or general savings.

## Table-route rerun — 2 October 2026

A fresh subagent repeated the same bootstrap and routine-edit task against
`de05d8f31ba8fb52dab187a8cb40ed167647c40d`, without the previous reports or real
Atlas documents. The source change moved table guidance to its own reference and
put initial form selection in the visual skill entrypoint. The extracted table
rules were checked against the previous source and preserved unchanged.

Artifacts: `/tmp/atlas-bootstrap-trial-two-iCW2L2/atlas`; local trial commit
`7c42345`. The parent reviewed the generated README, AGENTS, foundation documents
and provenance. The subagent reported 88 valid links/anchors, 34 collection files
matching the pinned source exactly, no leftover project placeholders and clean
whitespace. Stack, storage, interface and product details remained open; the
agreement slice stayed proposed. No application, runtime validation or network
activity was introduced. Real Atlas was unchanged.

| Reading measure | Previous trial | Table-route trial |
| --- | ---: | ---: |
| Initial instruction/template files | 17 | 17 |
| Initial words | 8,496 | 6,908 |
| Routine-edit reread words | 254 | 296 |

The second trial read the 505-word tables reference instead of the 2,221-word
composition reference. Total initial reading fell by 1,588 words, about 19%.
These are observed whitespace-word counts from two separate runs, not a controlled
estimate of context tokens or execution time. Counts exclude generated-file review
and machine-only scans. Both routine edits reused warm-context guidance and loaded
no new skill files or foundation documents.

Remaining observed friction: project-docs still explicitly routes this table-only
bootstrap to its diagram-placement reference. Consider making that read conditional
on an actual diagram or diagram ownership question. No new operational conflict
was reported. Broader guidance reading remains material; a cold-context ordinary
task and an actual policy transition still need trials. No additional skill change
was made in response to this run.
