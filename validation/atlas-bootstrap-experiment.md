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

## Selection-only routing trial — 2 October 2026

A fresh subagent bootstrapped against `948796ac75fd72bce0a0952c26a3f63bc1ba6fe4`.
It skipped table construction, diagram placement, composition, drawing and visual
verification references. It produced the intended scoped foundation with stack,
interface and storage open; the proposed slice remained unadopted. Parent review
covered README, AGENTS, policy and overview. The agent reported 86 valid links,
34 exact imported files, no placeholders and clean whitespace. Artifacts remain
at `/tmp/atlas-bootstrap-three-3vpxyse7/Atlas`, local commit `bd2b00c`.

Its instruction/template subtotal was 6,262 words across 16 files, including a
new 365-word short-text read. This is below the preceding 6,908-word subtotal,
but not evidence of lower total reading: the agent also read 2,485 counted words
of repository catalog and an earlier truncated full catalog of unknown delivered
length. Total exact accounting was 9,011 words including 264 words of target
instructions on the routine edit, plus that unknown truncated read. Repository
catalog loading is now an observed source of overhead. The routine wording edit
reused existing skill/foundation context; target README inspection was excluded
from its reread subtotal, so do not compare it directly with earlier edit counts.

### Diagram countercheck at the same revision

A second agent created a proposed import flow at
`/tmp/import-flow-countercheck-6gib_hjo/docs/import-flow.md`. It loaded project-docs,
visual selection, authority, authoring, diagram placement, composition,
verification, Mermaid drawing and clear-writing: nine guidance files. The parent
inspected the output. All seven edges match the supplied validation/review/approval
flow; invalid and cancelled paths perform no writes. Whitespace checks passed.

The conditional route reached construction guidance when needed. No local Mermaid
renderer was found, so syntax/render and visual readability remain unverified.
No renderer was installed and no network was used. The agent noted irrelevant ER
material in composition and drawing. That prompted the later ER reference
extraction; this trial predates it and does not validate its selection behavior.

## Continue into first-slice design — 2 October 2026

Continuation exposed an installation gap: Atlas still had the initial draft, and
friction capture had no route in the collection. Added a small conditional
`references/friction.md` and bootstrap hook at `63be469`, then updated the complete
Atlas installation and provenance. No new discoverable skill was introduced.

A fresh agent in `/tmp/atlas-next-slice-askn6vka/atlas` produced an informal
agreement record/retrieve/correct proposal. Parent review preserved its proposed
status and transferred it to real Atlas with an overview link. It identified
persistence across restart and retention of corrected values as decisions before
stack selection. No implementation, policy transition or environment validation
was performed. The real project's experiment note records the actual reads and
limits. The agent stayed inside project and installed collection guidance.

Reported friction was untracked fixture files limiting Git diff checks; explicit
file checks supplied coverage. Treat this as fixture setup, not a reusable skill
rule. Future rerun fixtures should establish a tracked baseline before editing.
The task explicitly requested reporting friction, so it does not prove unsolicited
capture from the new project hook. Ordinary no-friction behavior was not separately
retested. Package validation and source/installed-copy link checks passed.
