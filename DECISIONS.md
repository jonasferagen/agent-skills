# Skill decisions

Keep structural decisions and unresolved ideas here. Detailed trial evidence
belongs in `validation/`. A follow-up idea is not an adopted requirement.

## 3 October 2026

### Retire change-workflow — completed

Remove the standalone package and active catalog entry at the owner's request.
Its broad workflow is not needed. Preserve the [validation and retirement
review](validation/change-workflow.md) and Git history; do not transfer its merge,
publishing, tracker or reporting requirements into another package.

### Make task worktrees a foundation default — adopted

Use a separate task worktree for edits in Git repositories. Only repository-local
instructions can opt out, for example for a deliberately single-agent project.
Work outside Git proceeds directly; a spike needs no repository merely to
satisfy this rule. Small tasks and an agent working alone do not create implicit
exceptions.

The collection's [Git worktrees skill](collections/project-foundation/skills/git-worktrees/SKILL.md)
owns the short shared procedure. Bootstrap installs a visible rule and concrete
skill route in each project's instructions. Repository instructions own exceptions, and
existing installations adopt the rule through an explicit collection and hook
update. The authoring repository uses the same route.

Git worktrees starts at unreleased version 0.1.0. Project bootstrap becomes 2.0.0
because the default for repository edits and generated instructions changes.
No release tag or downstream installation is updated by this source change.

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

### Visual selection before construction — adopted

Keep one visual skill, with a small entrypoint choosing prose, tables and diagram
families by reader question. Existing scaffold tables need no construction guide.
Project-docs owns document placement and freshness, loading diagram-specific
placement only when needed. ER composition and syntax now have a separate
reference; flowchart work need not load them. No extra skill dependency is added.

Remaining observed friction: authoring repository instructions can lead agents to
read much of the catalog during consumption, and Mermaid rendering currently lacks
an available local tool in the trial environment. Address those separately from
form selection. The latest trials do not establish cold-start everyday behavior
or a reduction in total session context.

### Routing quality as an acceptance requirement — adopted

Consumers must reach relevant guidance without source-maintenance reading unless
their task needs it. Deeper guidance must still be reached when required. Apply
this standard to the repository's own instructions and collections. The
[requirement](README.md#routing-quality) owns acceptance; the
[trial method](validation/discovery.md#routing-trial-method) defines practical
evidence for meaningful routing changes and collection releases. Ordinary wording
edits do not automatically trigger trials.

Measure actual reads and their relevance, missed obligations and preserved task
constraints. Compare equivalent tasks rather than imposing a universal word
budget. Source-authoring and installed-consumer routes need separate checks.

### Friction capture available in the collection — adopted

Include a conditional reference and generated project-instruction trigger for
observed friction. Capture task, obstacle, consequence and disposition in existing
project notes; ordinary successful work needs no report. Reusable guidance still
requires assessment, through pattern-capture when available. The first continuation
trial is recorded with the Atlas experiment and does not yet prove spontaneous
capture without an explicit evaluation request.

### Scope the next data-design stage — proposed

The [data-foundations proposal](docs/data-foundations.md) maps tasks to guidance.
The likely new entry point is relational-modeling: structure known entities around
retrieval questions and iterate toward an implementation-ready model. Reuse
PostgreSQL, migration, authoring and ER guidance; start synthetic scenario/seed
guidance as a reference rather than another discoverable skill.

This pass defines responsibilities only. No Atlas schema, new skill package or
second collection has been implemented. Cross-collection dependency installation
and pinning remain unresolved and must be made concrete before packaging.

## Keep policy as an input table — 2026-10-03

Forge's policy accumulated working rules and bootstrap/import/upgrade reports.
The template was sparse, but project-policy explicitly invited extra requirements
tables. Keep the policy body to Axis and Current fact or decision. Project-policy
interprets those entries alongside boundaries and records consequences in their
affected owners. Worktree exceptions belong in repository instructions. Preserve
obligations when moving them; a document cleanup does not relax requirements.

## Keep boundary templates minimal — 2026-10-03

Forge's boundary document accumulated prior-repository narrative and current
implementation details around its ownership tables. Keep the shared template to
Purpose, Responsibilities, Outside the scope and Ownership. Project-specific
boundary tables may remain local; history, status and procedures stay in their
existing owners. Tighten the common structure as recurring patterns emerge.

## Keep overview as current technical choices — 2026-10-03

Forge's overview accumulated a next-task queue, skill-selection notes and evidence
summaries. Keep its table focused on current choices and unresolved options.
Remove the template's First useful slice row; work notes own proposed slices and
acceptance work. Existing instructions and evidence records own the other material.

## 3 October 2026 — Multi-repository foundations

A project spanning repositories can share one authoritative foundation and one
accessible collection installation. Members retain local facts and explicit
exceptions. Independent projects and deliberately separate pinned installations
remain supported. The Forge bootstrap exposed duplicated policy and installation
copies; this change separates project ownership from Git repository boundaries.
See [validation](validation/multi-repository-foundation.md). No release tag created.

## 3 October 2026 — Unified foundation and named references

Default bootstrap output is one `docs/foundation.md` with Boundaries, Overview
and Policy tables. Existing document homes remain supported. Shared members use
the same sections, declare inheritance and retain only local differences.
The source-of-truth lookup rule already owns indirect external identifiers;
multi-repository guidance now applies it to parent roots and documents resolution,
unknowns, exceptions and missing authority. This is an agent-read convention;
no runtime resolver or automatic Markdown expansion is introduced.

Project-bootstrap becomes unreleased 3.0.0 because its default scaffold changes;
project-policy 2.2.0 and project-docs 2.3.0 support both section and existing-file
owners. The collection is pinned by commit; no release tag is created.
See [validation](validation/multi-repository-foundation.md).

## 3 October 2026 — Foundation declarations only

The user requested a strict format with interpretation owned by the collection.
The template now defines the fixed title, date/revision and five table sections:
References, Inheritance, Boundaries, Overview and Policy. No instructional prose,
comments, YAML or workflow routes belong in populated foundations. The shared
format reference owns resolution and section inheritance; AGENTS provides the
minimal lookup and unavailable-owner hook needed before shared guidance is read.
Project-policy remains responsible for changed facts and obligations.

A format-only checker derives table headings and columns from the template.
It does not fetch targets or implement inheritance. Existing separate document
homes remain valid until deliberately migrated. Bootstrap 4.0.0, project-policy
3.0.0 and project-docs 3.0.0 reflect the changed authoring contract; all remain
unreleased and pinned by collection commit. No tag is published.

## 3 October 2026 — Workspace discovery entry

Bootstrap now checks the agent's entry directory when authorized setup includes
a shared workspace. The workspace hook routes to the shared owner and installed
collection, then target repository instructions; it neither copies the collection
nor grants project membership through filesystem ancestry. Untracked parents can
expose versioned entry files by symlink, with the exposed link base stated and
existing files preserved. Whole-owner absence also removes symlinked hooks; this
dependency is explicit. Bootstrap 4.1.0 is unreleased; no tag is created.

## 3 October 2026 — Project design draft

Add project-design to project-foundation for shaping responsibilities, repository
boundaries and handoffs. Start next-step planning as a conditional reference.
Keep repository, process and deployment choices distinct; future packaging does
not select current infrastructure. Reuse policy, documentation and authority
guidance without restoring retired change-workflow or shared-code-design rules.

Project-design starts at unreleased 0.1.0; bootstrap 4.2.0 adds its discovery hook.
Behavioral trials and limitations belong in [validation](validation/project-design.md).
No release tag is created. Forge adoption is a separately recorded consumer update.

## 3 October 2026 — Workflow and integration design

Extend project-design for projects whose primary work is decisions, procedures
and artifacts. Conditional workflow guidance covers triggers, acting roles,
artifact ownership, acceptance and interruption. Integration guidance starts from
the needed capability and compares manual/local and service mechanisms using
concrete constraints and evidence. Setup, external execution and provider-specific
procedures remain with their owners; design does not expand authorization.

Project-design 0.2.0 is unreleased. The existing Forge wall-texture exercise informs
its application; the real brief, source and operation remain prerequisites. No
new standalone integration skill or runtime framework is introduced.

## 2026-10-03 — Separate architecture questions from contracts

Project-design 0.3.0 remains the entry for system responsibilities, workflows and
integration choices. Project-contracts 0.1.0 owns obligations at an established
exchange, including process and document handoffs. The collection routes directly
to either; project-design also routes existing callers to contracts when needed.
This keeps the design entry compatible while extracting detailed handoff work.
Neither skill forces a service, schema or mandatory phase sequence.

This small round adds one collection member. Diagram construction remains with
diagrams-and-tables; policy consequences remain with project-policy. The standalone
service-boundaries skill retains its narrower HTTP/MCP implementation scope and
is not added as a dependency. A separate architecture rename, provider skill or
contract template needs further use evidence. These revisions are unreleased.

## 2026-10-03 — Diagram reference families

Diagrams-and-tables 0.7.0 groups ER guide, large-model guidance and examples under
references/er, and adds references/data-flow. Shared composition, verification,
tables and mixed layout examples remain at the root. Drawing guidance is named
mermaid.md to distinguish renderer syntax from view semantics. All active internal
callers move together in the complete collection; old reference paths are removed.
Historical validation records retain the paths used in their trials.

Family guides distinguish official source scope, collection conventions and
renderer constraints. Deployment guidance remains a future addition; this round
creates no empty family directories. No release tag is created.

## 2026-10-03 — Route diagrams by task before form

Diagrams-and-tables 0.8.0 applies the task distinction from the project-contracts
0.2.0 worktree: reading/application, semantic review, selection, construction and
visual review have separate routes. Family read.md files retain interpretation;
design.md files own authoring obligations. Family guide paths remain entry points.
No project-contracts draft content is merged by this change. Existing diagrams
remain unchanged.

## 2026-10-03 — Contract tasks and obligation discovery

Project-contracts 0.2.0 separates reading, applying, designing and reviewing an
agreement. The entrypoint keeps interpretation and application short; design and
review load conditional references. Contract type alone does not select a design
workflow. Existing identity, interruption and compatibility obligations remain in
the design reference and are reachable from focused review.

Design discovers obligations by tracing participants' decisions and looking for
cases where they can follow the terms yet disagree about the valid outcome.
Named subjects are starting points, not a completeness checklist. Missing project
terms stay with the contract; observed failures of guidance or routing use friction
capture and, when warranted, pattern-capture. Shared friction guidance now includes
consequential omissions discovered after otherwise smooth work.

This applies the distinction to contracts first. It does not impose four modes
on every skill or add a subject reference for every possible contract type.
Validation belongs in [project-contracts](validation/project-contracts.md).
No release or downstream adoption is implied.

## 2026-10-03 — Self-conformance before collection releases

This repository follows the rules its skills teach. A collection release now
requires a [self-conformance review](validation/self-conformance.md) of the whole
collection against its members' own review steps, recorded on its validation page.
Skill releases keep the lighter recommended pass. The method selects rule owners
and links their checklists rather than restating them; a recurring finding can
become a mechanical check.

Three mechanical checks now apply rules that were previously followed by hand.
Package validation checks that each recorded package-boundary copy names an
existing counterpart that records it back; its first run found test-audit's ledger
record still pointing to source-of-truth's entry point after the report-only rule
moved to check design. The foundation checker checks, without reading targets,
that symbolic references use declared keys, that each authority is one anchored
reference or `Unknown`, and that no section inherits from its own file. The
project-docs checker reads its allowed paths from the
document-homes table instead of a copied list.

## 2026-10-03 — One home for status, evidence and authority

[Status and evidence](collections/project-foundation/references/status-and-evidence.md)
is the shared home for the unknown, proposed, adopted, implemented and verified
states, what common kinds of evidence can establish, and where authority to act
comes from. Skills link to it where they restated the general rule and keep
domain-specific cautions, such as what a flowchart arrow does not prove, and
their existing state terms. The catalog no longer restates the
collection's rules. Edited members take patch versions; no release tag is created.
