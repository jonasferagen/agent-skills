# Skill decisions

Keep structural decisions and unresolved ideas here. Detailed trial evidence
belongs in `validation/`. A follow-up idea is not an adopted requirement.

## 2 October 2026

### Group packages by the task that selects them — adopted

Use `projects/`, `authoring/`, `design/`, `verification/`, `operations/`,
`workflow/` and `languages/` under `skills/`. This initially preserved independent packages. The collection decision below
supersedes that requirement for project-foundation members. Categories organize browsing; they do not
require loading every skill in the group.

### Retire shared-code-design — completed

Remove the standalone package from the active catalog. Its useful context is
aligning repositories while discovering architecture and patterns, but the skill
mostly addressed distribution after an abstraction had already stabilized.
Preserve its [validation history](validation/shared-code-design.md) and Git history.

Ideas to revisit, without transferring the rules yet:

- Pattern-capture could cover comparing implementations and distinguishing useful
  differences from accidental drift before extracting an established pattern.
- Source-of-truth already covers authoritative rules and derived or checked copies.
- A conditional reference could compare copying, generation and versioned
  dependencies if future work needs it.
- Independent build guarantees remain in containerization where they are relevant.

Downstream installations are mostly inactive. The owner has excluded downstream
installation migration from this cleanup.

### Extract migrations and service boundaries from containerization — completed

| Owner | Scope |
| --- | --- |
| [Containerization](skills/operations/containerization/SKILL.md) | Images, stack configuration, startup and container resource cleanup |
| [Database migrations](skills/operations/database-migrations/SKILL.md) | History, runners, baselines, bootstrap, upgrades and migration verification |
| [Service boundaries](skills/design/service-boundaries/SKILL.md) | Service ownership, caller identities and shared application behavior across HTTP/MCP |

These tasks can arise independently of containers. The database-testing reference
moves with migrations; container cleanup mechanics stay with containerization.
Startup still invokes the project's migration procedure. Each package works alone.
Containerization's narrowed scope is version 1.0.0; the two new packages start at
0.1.0. These versions are unreleased; no tags or installations are changed.

### Remaining ideas — proposed

- Split runtime-operations into credential handling, local service control and
  database backup/recovery. Distinguish general guidance from its 1Password and
  systemd implementations.
- Consider separating consistency-check design from source-of-truth, with a home
  under verification.
- Review general completion and handoff guidance inside change-workflow separately
  from its adopted Git worktree workflow.
- Clarify documentation ownership versus domain modeling in project-docs.
- Decide user-wide installation after the responsibilities settle.

Keep verification-design, test-writing and test-audit separate: they select
evidence, write tests and assess an existing suite respectively.

### Project foundation as one collection — adopted

Move bootstrap, policy, project-docs, clear-writing and diagrams-and-tables into
`collections/project-foundation/`. Install and update the complete collection,
with internal references preserved. The remaining skills keep their standalone
format for now. This replaces the earlier requirement that every skill must work
when copied alone; further specialization is deferred until useful.

Keep one set of sparse templates at the collection root. Policy starts with
`Axis` and `Current fact or decision`; boundaries and glossary also use compact
tables. Dates and revisions identify document decisions. Empty cells mean unknown.
Remove the duplicate policy template. Shared authoring instructions live in the
collection and project instructions route to them and the task entry points.

Project-policy interprets the foundation and reviews its consequences during
project work. A small document can govern a large transition: spike to maintained
use or local development to cloud hosting requires an impact assessment, selected
reviews/audits, implementation work and evidence before claiming readiness.
Document adoption, implementation and verified readiness remain distinct.
Relaxing a policy also prompts consideration of simpler implementations and
removal of machinery that only served the removed guarantee. Preserve remaining
obligations and assess the value of cleanup before undertaking it.
This adds no background monitoring or automatic deployment. Global installation
and adoption into Atlas are separate from authoring this collection.

### Foundation authority and source-of-truth — adopted

Include source-of-truth in the project-foundation collection. Boundaries, policy
and glossary are authoritative for their adopted decisions and should be consulted
before substantive project work, when affected decisions change, and before
claiming completion. Bootstrap writes these routes into project instructions.

Project-policy assesses changed obligations and their consequences; source-of-truth
traces authoritative definitions, consumers and drift checks. Shared authority
guidance distinguishes adopted decisions, proposals and observed implementation.
The source-of-truth version becomes 2.0.0 for the collection dependency; no release
or downstream installation is performed.

### Minimal overview and Atlas bootstrap trial — adopted

Replace the default glossary with a project overview covering environment,
resources, application/interface, stack, patterns, packaging and a proposed first
slice. Use it for spikes as well as maintained projects. Add a glossary when
ambiguous terminology warrants one.

Replace mandatory reading of every foundation document with a short operating
summary in project instructions and task-specific routes. Link summary statements
to their owners and update them with changed decisions. Authority remains with
the foundation; reading frequency depends on the task.

Applied this draft to `personal/atlas` on 2 October 2026. See the
[experiment record](validation/atlas-bootstrap-experiment.md). The application
slice, language, storage and interface remain unchosen. The trial produced project
documents and installed one collection locally; no application or environment
validation was performed.

### Triage friction and consolidate ideas — completed

Address concrete instruction conflicts now; keep unmeasured improvements as
proposals. The excessive foundation-reading rule and mandatory-glossary assumption
were already corrected during the Atlas trial. Bootstrap now explicitly separates
policy constraints from overview mechanisms, so future scaffolds retain the
ownership distinction used in Atlas. No new friction-capture skill is needed yet.
The loopback/dependency-network question remains an Atlas decision to resolve when
an implementation choice depends on it. Context savings remain unmeasured.

Preserve the candidate from `ideas.md` under
[source-of-truth validation](validation/source-of-truth.md#candidate-record-meaning-versus-storage-origin):
consumers can silently change behavior when they infer record meaning from storage
origin. It has one recorded reproduction; a second case and the legitimate
provenance-based counterexample still need evaluation. No reusable rule is adopted
yet. The candidate belongs with definition consumers even if check-design guidance
later moves. Delete `ideas.md` after preserving its evidence and open work there.
