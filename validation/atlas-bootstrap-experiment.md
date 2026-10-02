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
