# Skill decisions

Keep structural decisions and unresolved ideas here. Detailed trial evidence
belongs in `validation/`. A follow-up idea is not an adopted requirement.

## 9 October 2026

### Split containerization into CLI packages and a convention — completed

Retire containerization at 1.1.0 and divide its material by what selects it.
Everyday Docker and Compose usage is a consumer skill; the outcomes a project's
containers must meet are framework convention; PostgreSQL and verification
material belonged to neither.

| Owner | Scope |
| --- | --- |
| [docker-cli](skills/operations/docker-cli/SKILL.md) | One container or image command: naming, identity, secrets, ports, owned mounts, teardown, daemon reads |
| [docker-compose-cli](skills/operations/docker-compose-cli/SKILL.md) | Project-scoped commands: selection and inherited environment, borrowed definitions, closed name sets, project teardown |
| [docker-cleanup](skills/operations/docker-cleanup/SKILL.md) | Host-wide attribution and reclaim of accumulated state |
| Consuming framework's local-containers convention | Lifecycle, label scheme, state custody, isolation, image pinning and provenance, composed sets and variants, containerized tools |
| [database-migrations](skills/operations/database-migrations/SKILL.md) | Disposable PostgreSQL instances: tmpfs data directory and readiness over TCP |
| [verification-design](skills/verification/verification-design/SKILL.md) | Build evidence against runtime evidence for a packaged service |

Three Docker packages for one tool is a routing cost, accepted because the three
triggers do not overlap: assembling a command, driving a project, and accounting
for a host. Cleanup stayed separate rather than becoming a reference inside
docker-cli, because its substance is an authorization about destructive action
and a reader loading flag guidance should not acquire one.

Four rules apply to both CLI packages and are duplicated with reciprocal copy
records, since a package may not link into another: resource naming, run
identity with label-over-pattern selection, cleanup registered before creation,
and the prune refusal. The borrowed-definition rule is the one seam the cut does
not separate: compose-triggered, fixed with a docker run bind, so stated in
both.

Preserve the [containerization validation history](validation/containerization.md)
and Git history. The convention-shaped sections leave this repository entirely;
moving them into the framework's convention and re-pinning its import are
separate work in that repository. Routing acceptance is outstanding and must
separate four near-neighbours, so no release tag is created.

### Prefer the acting agent's managed worktree support — adopted

Use the acting agent's own managed worktree support when it provides one, and
name a concrete fallback home for when it does not. Both hand-named homes stay
correct as that fallback, and no existing worktree moves.

Naming one assistant's directory first makes every other agent's correct
behavior look like a deviation. The 6 October decision below named
`~/.claude/worktrees/agent-skills/<task>` and then the Codex equivalent, so it
read as a primary choice rather than one of two equals. project-bootstrap's
project-instructions convention describes that defect; this repository installs
no documentation collection, so the wording is adopted on its merits and not to
satisfy an installed rule.

### State the reporting checkpoint once — adopted

The 8 October decision below gives consequential guidance and routing problems
one route, declared by the installer in the consuming project's instructions. Three
entrypoints (clear-writing, diagrams-and-tables, source-of-truth) still opened
with their own restatement of that trigger, and godot-gdscript closed with an
older wording of it, while the other 24 skills carried none. A reader could not
tell whether the four had a stronger duty or had merely been written earlier.
The restatements are removed; the obligation is unchanged and lives where the
checkpoint record says it does. project-contracts keeps its one sentence, which
draws a boundary (a missing project term is not a skill defect) rather than
restating the trigger. The four take patch versions because the consumer's
requirement did not move; only its restatement did.

### Validation pages follow skill names — adopted

The catalog asks for `validation/<name>.md`. After the 7 October flattening,
work-records and repository-services were the only skills whose intended
behaviour lived under a collection's name. `process-design.md` is renamed to
`work-records.md`, since work-records was its only member and its dated sections
keep the collection name. `repository-services.md` is new and links the service
foundation history and trials that exercised its templates, validator and
dispatcher. `service-foundation.md` stays, because it also records
service-boundaries and runtime-operations decisions.

The README defines the `(draft)` marker, which eight catalog rows carried without
a stated meaning. Package validation now checks link fragments inside a package,
and a source test checks that the README, repository instructions and this log
resolve their local links, since history under `validation/` may cite moved
paths but the live maintenance pages may not. The
[sweep record](validation/standalone-sweep-2026-10-09.md) holds the findings
and checks.

### Checkpoint text and placement belong to the installer — adopted

The reporting checkpoint is stated in two homes. This README's
[selection and capture](README.md#selection-and-capture) section dictates the
instruction's text, that it goes in the consuming project's instructions, the
local-link rule and the `/pattern-capture` shortcut; the 8 October entry below
names the README as owner of that proposed instruction. The project-bootstrap
distribution's project-instructions convention states the same checkpoint,
placement and link rules in its own wording, and already lets a member route to
a shared owner's statement. The two texts have begun to differ.

Where a consuming project's instruction lives, and what it says, is a claim
about that project's documentation. This repository owns pattern-capture and
the need it has: a reporting trigger available before any skill is selected. It
does not own the installer's instruction. The proposed change keeps the need in
the README and hands the text, placement and shortcut rules to the installing
distribution or project; the 8 October ownership sentence and the "state the
reporting checkpoint once" entry above would be reworded to "one route, declared
by the installer". pattern-capture's own sentence about mapping
`/pattern-capture [idea]` would say "the installer may map", at a patch version
the distribution picks up when it next re-pins.

Held on 9 October 2026 while a separate task was live in the distribution's
`task/alignment-register` worktree, then adopted the same day once that task
landed as project-bootstrap `be125fc`. The README's selection-and-capture
section now states the need and hands text, placement, link, capture home and
shortcut to the installer; pattern-capture 0.3.1 says the installer may map the
shortcut. relational-modeling 0.2.2 drops its suggested document homes for the
same reason: where a consumer's model, scenarios and glossary live is the
installing distribution's claim. The discovery trials that exercised the
checkpoint remain valid evidence about the instruction, whichever repository
states it. The distribution picks up both patch versions when it next re-pins.

## 6 October 2026

### Task worktrees belong to the acting agent — superseded by 9 October above

Task worktrees go under the acting agent's own home, as
`~/.claude/worktrees/agent-skills/<task>` or the Codex equivalent, so each agent
owns and sweeps what it created and this checkout holds only the repository. AGENTS
previously stated `.worktrees/` in the main checkout, which is why agents kept
placing them there.

Worktrees already under `.worktrees/` stay until their work finishes. Moving a
checkout another session is using breaks that session, and the ignored files inside
one — installed packages, run output, scratch evidence — are the easiest thing to
lose in a move. Both locations are task worktrees; tooling that resolves them
through `git worktree list` needs no change.

### Landed branches are retired, not kept — adopted

Landing never retired a branch, so eleven worktrees had accumulated, every one
merged into main and clean. A branch is swept only when it is merged, carries no
uncommitted change and holds no ignored file beyond build output; anything else is
reported and kept, because age and merge status alone do not establish abandonment.
The sweep used Forge Primary's `tools/worktrees`, which implements that rule. This
repository had nothing outside the removable class, and `python3 scripts/check.py`
passes with one worktree and one branch remaining.

### Settle the named-process owner — adopted

Project-foundation owns the named-process document type and its
`project-process/v1` reference, parser and template. Process-design owns work
records. Process-design 0.2.0 recorded taking the process type and the
`review-feedback-section` template over as its next step; that intention is
withdrawn and the boundary is now stated as a settled division of document
types in the [extension boundary](skills/workflow/work-records/references/extension.md#owned-by-the-project-framework).

The reason is that a recorded future transfer is a second source of truth while
it is pending. A consumer reading either collection had to know which release it
held and what was planned before it could tell who owned a process page. The
division itself was never in doubt in practice: the reference, parser, template,
checker and tests all live in project-foundation and nothing here duplicates
them.

The division follows the document's home and subject rather than the collection
name. A named process is a standing explanation of recurring work inside the
framework's governed document root. A work record is a dated document about one
assignment, kept with the work. `review-feedback-section` stays core's as a
section pattern for an assessment inside the document that already owns the
subject; this collection's report and worklog stay standalone records that
return findings to a commissioning owner. Both remain defined and neither
deprecates the other.

Process-design becomes 0.3.0: the scope statement changes meaning, though no
guidance, template, script or check changes behavior. Reopening the transfer
would be a new decision in both collections.

## 3 October 2026

### Retire change-workflow — completed

Remove the standalone package and active catalog entry at the owner's request.
Its broad workflow is not needed. Preserve the [validation and retirement
review](validation/change-workflow.md) and Git history; do not transfer its merge,
publishing, tracker or reporting requirements into another package.

### Make task worktrees a foundation default — superseded by retirement below

Use a separate task worktree for edits in Git repositories. Only repository-local
instructions can opt out, for example for a deliberately single-agent project.
Work outside Git proceeds directly; a spike needs no repository merely to
satisfy this rule. Small tasks and an agent working alone do not create implicit
exceptions.

The collection's former `git-worktrees` skill (preserved in Git history)
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
| Containerization (retired 9 October 2026) | Images, stack configuration, startup and container resource cleanup |
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
- Clarify documentation ownership versus domain modeling in project-docs. (That
  skill left this repository with project-foundation on 4 October 2026; the idea
  went with it.)
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
[experiment record](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/atlas-bootstrap-experiment.md). The application
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

The data-foundations proposal (`docs/data-foundations.md`, removed 7 October 2026 once relational-modeling landed) mapped tasks to guidance.
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
See [validation](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/multi-repository-foundation.md). No release tag created.

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
See [validation](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/multi-repository-foundation.md).

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
Behavioral trials and limitations belong in [validation](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/project-design.md).
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
Validation belongs in [project-contracts](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/project-contracts.md).
No release or downstream adoption is implied.


## 2026-10-03 — Foundation task routing and family growth

Adopt the [collection authoring convention](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/docs/project-foundation-authoring.md)
for project-foundation maintenance. Task distinctions follow each skill's work;
project, evidence and guidance gaps have different owners. Design and adequacy
review discover necessary decisions beyond listed examples. Keep this convention
in source maintenance and each consumer's useful behavior in its skill.

Project-policy 3.1.0 applies the convention next. Interpretation and compliance
assessment stay in the entrypoint; establishment, adequacy discovery and changes
use conditional guidance. Existing six axes, format rules, impact assessment,
policy relaxation and observed-transition requirements are preserved. No other
member receives a mandatory mode taxonomy.

Keep diagrams-and-tables together for this iteration. Both forms answer visual
explanation questions, share semantic reading/review and need a common form-choice
route. The current family directories allow diagram growth without loading all
construction guidance for tables. Splitting now would require another selection
owner and new caller routes without evidence that it improves the tasks.

Reconsider separate diagram and table skills if realistic trials expose persistent
misrouting or unnecessary reads that internal routing cannot solve, or independent
adoption becomes useful. The present decision does not claim those possibilities
have been ruled out. More diagram types alone are insufficient evidence.

Use a directory per diagram family as substantial guidance is added, keeping
shared rendering/layout rules outside the families. Contracts can use the same
structure for distinct exchange semantics; cross-cutting properties may require
several references and keep shared owners. Do not duplicate concurrency or retry
rules into every type, introduce empty family directories, or prescribe a fixed
set of files per family. No diagrams or contract families are added in this round.

## 2026-10-03 — Narrow collection entry and policy task references

Continue the foundation coherence work on the existing task branch. The collection
entrypoint selects work; installation, provenance and template setup move to a
conditional reference reached by bootstrap and adoption tasks. Preserve the visible
Git worktree default and the distinction between unknowns, proposals, adopted
obligations and evidence. Known terms can be read or applied through their owners.

Foundation-authority remains the owner of consultation and reconciliation guidance.
Load it for establishing/reconciling decisions, conflicting authority or changed
scope/circumstances. Narrow known-scope work need not load it. Inherited scope still
routes through foundation format and shared-owner resolution when the answer needs
it; unknowns or missing authority grant no permission. Policy, contracts and docs
entrypoints make those task conditions explicit.

Project-policy 3.2.0 separates establishment, requirement discovery, policy-change
assessment and document-writing references. The existing policy-change consequence
workflow is preserved, including already-observed changes, relaxation, readiness
and authorized work. Adequacy review can discover omissions without reconstructing
a new policy. Assessments that preserve policy need no document-format workflow.

Bootstrap 4.2.1 follows the relocated installation route; contracts 0.2.1 and docs
3.0.1 clarify conditional authority reads. No client discovery behavior, automatic
installation or authorization changes are claimed. No new skill is introduced.

A direct-contract trial exposed an additional authority-to-format read for projects
with established separate document owners. Authority now loads format guidance
when resolving declarations or inherited values. Its rules for consulting affected
owners, handling conflicts and preserving adopted obligations remain unchanged.

## 2026-10-03 — Retire git-worktrees from project-foundation

Remove `git-worktrees` and its active catalog, collection and bootstrap routes.
The owner has moved personal worktree preferences into global agent instructions.
Keep repository placement conventions in repository instructions. The collection
continues to preserve project working agreements without imposing a worktree
policy or reproducing personal preferences in generated instructions.

This supersedes the earlier collection worktree default. Project-bootstrap becomes
5.0.0 because its mandatory startup and generated-instruction behavior changes.
Upgrades remove retired skill links while preserving adopted working agreements.
Historical validation remains available; this change does not establish a measured
comparison with native worktree support. No downstream installation or release tag
is changed.

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

[Status and evidence](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/collections/project-foundation/references/status-and-evidence.md)
is the shared home for the unknown, proposed, adopted, implemented and verified
states, what common kinds of evidence can establish, and where authority to act
comes from. Skills link to it where they restated the general rule and keep
domain-specific cautions, such as what a flowchart arrow does not prove, and
their existing state terms. The catalog no longer restates the
collection's rules. Edited members take patch versions; no release tag is created.

## 2026-10-03 — Application foundation first package

Create application-foundation (its design record `docs/application-foundation.md` was removed with the collections on 7 October 2026) with one
application-design member and a conditional external-integration reference. The
user approved drafting this workflow, exercising it on Tools and a different
application case, and packaging the useful guidance. Keep project-design's system
and workflow authority and service-boundaries' HTTP/MCP scope intact.

The core is self-contained. Existing language, runtime and verification skills
remain independently installable companions selected through project instructions.
This avoids requiring cross-collection dependency resolution for the first package;
it does not implement that mechanism for other collections. No consumer adoption,
provider runtime or release tag is part of this source change. Bounded trial
evidence belongs in [application-design validation](validation/application-design.md).

## 2026-10-04 — Service foundation pilot

Move `service-boundaries` and `runtime-operations` into one complete
[service-foundation collection](https://github.com/jonasferagen/agent-skills/blob/914aa01b1915d190ee0429d18a570e72c179fd5d/collections/service-foundation/COLLECTION.md),
version 0.1.0. Member names, versions, helper APIs and behavior are unchanged;
there is one source home per member. Earlier standalone pins remain historical
identities, not alternate current sources. Application-foundation 0.1.1 adds a
normal-work route to project-selected service guidance and flags its absence.

The pilot addresses a demonstrated consumer omission: the application collection
was installed while service companions remained separately selected in an
installation-only table. A maintained-service transition now selects both members
through the ordinary project hook. Narrow work still selects only what it needs.
An explicit manifest and source-based installation checker detect missing members,
local changes and stale overlay files; adoption and upgrades replace the whole
collection and reconcile provenance and project routes.

[Validation](validation/service-foundation.md) owns the synthetic routing trials,
package tests, preservation comparisons and limitations. No release tag, universal
dependency resolver or automatic host registration is selected. Python, TypeScript
and verification grouping remain candidates after the pilot; containerization is
not moved without an exercised consumer need. Forge adoption is a separate consumer
commit after this source change lands.

## 2026-10-04 — Python, TypeScript and verification collections

Group the remaining selected companions as complete collections:
`python-foundation` 0.1.0 (python-design, python-patterns),
`typescript-foundation` 0.1.0 (typescript-design, typescript-patterns, node-patterns),
and `verification-foundation` 0.1.0 (verification-design, test-writing, test-audit).
Each member keeps its name, version, resources and existing behavior. There is
one source home per member, with current catalog and validation routes reconciled.

Node belongs in the TypeScript tooling group conditionally: its process-wrapper
and CLI guidance also serves JavaScript tooling. Browser JavaScript alone selects
neither Node process guidance nor TypeScript type/design conventions. Verification
routes distinguish active evidence selection, test authoring and settled-suite
review; installing the group does not make audits mandatory for regression work.
Python language-boundary fixes need not trigger class reorganization.

The pilot's installation checker is now maintained once at
`scripts/collection_installation.py` and distributed into the four inventoried
collections by `scripts/sync-collection-tools.py`. The package validator rejects
unsynchronized copies as well as inventory drift. Service-foundation 0.1.1 retains
its member behavior and updates only this tooling/maintenance mechanism.
Application-foundation 0.1.2 routes ordinary work to project language and verification
owners as well as its existing service route. No remote resolver or global client
registration is selected. The [validation record](validation/companion-collections.md)
owns checks and task-routing evidence. Source landing and project-local adoption
remain separate commits; no release tag is implied.

## 2026-10-04 — Consistent collection integrity and quality sweep

Review the five new foundation collections and project-foundation in two passes:
individual skill quality, then collection consistency. Keep their distinct task
owners and conditional loading; repairs belong in the existing owner rather than
adding another workflow for the same decision.

Application-foundation and project-foundation now use the same declared membership,
file inventory and source-based installation checker as the four companion
collections. Package validation requires an inventory for every collection and
checks the distributed checker against its canonical source. Shared tests exercise
staged copies without a fixed catalog list, reject missing inventories and malformed
versions, and name the measured root in verdicts. Artifact identity remains distinct
from behavioral evidence and live parity between current authoritative owners.

The [sweep record](validation/collection-sweep.md) links per-collection findings,
consumer trials, helper verification and further improvements. Version updates
describe source revisions; this sweep creates no release tag or consumer pin update.


## 4 October 2026 — Extract project-foundation

Project-foundation is maintained in [its own repository](https://github.com/jonasferagen/project-foundation). Its project
conventions and workflows remain one complete installation. Clear-writing,
diagrams-and-tables and source-of-truth remain owned here as standalone packages;
the framework imports selected committed revisions. Old installed collections
retain their historical source pins until deliberately replaced.

Keep the shared collection installation checker owned here. The framework
imports its selected implementation and records that dependency with its skills.

## 7 October 2026 — Flatten the catalog and drop collections

Every skill is a standalone package at `skills/<area>/<name>/`; there are no
collections, manifests, bundled checkers or collection releases here. The six
collections' members moved into the areas authoring, design, operations,
verification, workflow and languages under their existing names. Collection-level
resources followed the skill that uses them: process-design's references,
templates and checker into `work-records`; the service loader and runtime-helpers
contract into `runtime-operations`; the service convention, structured
definition, templates, validator, parser and dispatcher into a new
`repository-services` skill. Sibling links became skill names, because the
consumer decides which skills are installed and where.

A downstream distribution bundles skills from here as pinned directory imports
and owns its own membership, lock, installation checker and releases. This
repository no longer names any consumer in shipped content; a test under
`scripts/tests/` fails on such a name. The finished extraction tooling and plan
left with the migration they served; `validation/framework-extraction.md`
records the result. Old collection tags and pins remain history and are not
reused.


## 8 October 2026 — Shared reporting and independent acceptance

Capture consequential guidance and routing problems through one checkpoint in
consumer project instructions, available before any individual skill is selected.
Route reusable findings to the existing Pattern capture workflow and keep repair
within the task's authorization. The installing distribution or project owns
that instruction, and the [consumer checkpoint](README.md#selection-and-capture)
states the need (reworded 9 October); [discovery validation](validation/discovery.md#reporting-acceptance-trials)
owns acceptance. Fresh conversation context, actual startup metadata and retained
behavioral evidence are separate requirements. Informed reviews using inherited
or reused context do not establish independent activation.

The [finding record](validation/pattern-capture.md#shared-reporting-checkpoint--2026-10-08)
records current coverage and the positive and successful-control trial results.
The reporting and repair mechanism already has a home; no new skill is proposed.

### Distribution scope — proposed

Engineering-conventions currently bundles five native conventions and 18 pinned
agent-skills imports. Pattern capture, clear-writing, diagrams-and-tables,
source-of-truth and work-records are absent from its imported membership. Its
entrypoint says governance, document homes and document-maintenance workflows
ship separately in the documents collection. This is already the requested
agent-skills -> package -> project structure, but it does not provide the shared
reporting checkpoint or Pattern capture in the engineering installation.

Assess whether to broaden that distribution's scope and include Pattern capture
with an installation checkpoint, or provide a package that assembles engineering
and document guidance. Decide the membership, checkpoint owner and consumer
migration before choosing a new name. Preserve standalone ownership in
agent-skills and pinned imports in the distribution. No distribution rename,
import update or consumer adoption is made by this source change.
