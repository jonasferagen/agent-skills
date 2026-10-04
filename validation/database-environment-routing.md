# Database guidance practical routing trial — 2026-10-04

## Method and limits

Read-only design/behavior walkthrough with actual reads of a disposable complete installed collection and standalone specialist copies. Source provenance is in fixture/PROVENANCE.md. No source edits, live databases, runtime tests, or releases. No repository code implementation was requested. The fixture includes an instruction hook and adopted catalog scope.

This evaluator was a fresh child agent with no inherited conversation history. Parent supplied routes and scenarios; the hook was persisted/read AFTER initial skill reads. This is therefore a guided practical routing trial, NOT a blind cold-entry trial. Cases ran in one context, reusing reads; case 3 cannot establish independent non-activation. These limitations need a later fresh hook-first trial if cold-entry acceptance is required.

## Case 1 — fresh-checkout SQLite catalog, dev only

Entry: supplied project-instruction routing to project-design, then scope/policy context. Useful deeper path: project-design → database-environments → database-migrations. No PostgreSQL design skill or source-maintenance README was read.

Concrete result (proposed implementation): Keep SQLite in a repository-owned isolated local path; no staging server is needed. Provide checked-in setup/migrate/seed commands using the project's selected migration tool, plus a DISTINCT reset command limited to explicitly disposable fixture storage. Normal dev storage is not made disposable by its label. Show the resolved target; reject unknown/shared/retained targets for reset. Setup creates storage and applies one canonical migration history. Required reference records have their own lifecycle; optional synthetic authors and assets have stable identities and repeat-safe insertion. Include local synthetic asset payloads and demonstrate a useful author-to-assets read without live services. Preserve existing records on ordinary setup or seed replay.

Operating guide must state prerequisites, exact selected command syntax, paths, target selection, seed repeat behavior and reset scope. Command names remain illustrative until implementation picks a framework/tool. Before reporting setup ready, exercise empty setup, seeded retrieval, repeat behavior, disposable reset, and refusal of an unintended target without changing it. Deferring full application tests does not defer these smoke checks. If introducing/changing the runner, additionally verify checksum/history, ordering, atomic ledger success, failure stop and concurrency guarantees appropriate to SQLite. No custom runner is implied. Current architecture and policy owners must reflect adopted work; readiness remains unverified.

Preserved: SQLite choice; dev-only scope; synthetic useful data; fresh setup before full tests; separation of reset and upgrade; explicit evidence gaps. Missed task requirements: none identified in this proposed result; executable commands and observations intentionally absent because the trial is read-only and has no app/tool implementation.

## Case 2 — proposed staging, valuable dev records

Entry: operating-change hook → project-policy → policy-changes → database-environments, reusing project-design/database-migrations and foundation/status guidance. Project-planning used for required implementation work. Staging remains a proposal; retained development data is a current fact.

Concrete result: Required work before shared staging use:

| Owner | Work and dependency | Completion evidence / gate |
| --- | --- | --- |
| Project owner | Decide staging users, access boundary, host/path, retained vs disposable data, recovery objective, external effects and reset authority. Review changed exposure, lifetime and compatibility obligations. | Recorded decisions before enabling shared access; unresolved facts block only their dependent use. |
| Database maintainer | Inventory retained dev records AND payloads; select backup/restore path. Keep normal migration an upgrade, never a reset. | Disposable retained-state copy survives upgrade with relationships/payload references intact; restore rehearsal before migration of valuable records. |
| Application/operations maintainer | Implement distinct owned SQLite targets and payload/output paths, target display/validation, scoped permissions/configuration and isolated external effects. Shared file access strategy must match actual host/users. | Wrong-target refusal without mutation and cross-environment isolation checks before staging enablement. |
| Database maintainer | Deliver identical canonical migration revision to fresh dev and staging; declare SQLite/version/tool prerequisites. Add staging deployment procedure with failure/recovery behavior. | Empty bootstrap plus upgrade of supported retained state; failed migration leaves recoverable state and no false success; observed revision parity. |
| Database maintainer | Define staging reference-data updates and explicitly allowed synthetic seed behavior; prohibit dev reset against staging. Separately authorize/design staging rebuild only if chosen disposable. | Replay preserves retained rows; reset target guard rejects staging; approved staging seeds affect only intended records. |
| Project maintainer | Reconcile current overview, architecture, affected policy facts, operating guide, linked work queue and evidence owner after adoption. Keep proposed/implemented/verified states distinct. | Review affected consumers and links; gate shared use on above evidence. |

This is a substantive implementation/recovery transition even if schema is unchanged. A renamed environment variable alone is insufficient. No live migration, host provisioning or policy adoption occurred. Unknown ownership uses project roles as allowed by guidance. Missed task requirements: none identified at proposal depth; host-specific security/deployment and actual recovery requirements remain deliberately unresolved.

## Case 3 — conceptual author-to-asset explanation only

Entry: architecture hook → project-design → conceptual-models; shared authority and owner information reused. Database lifecycle and PostgreSQL skills are unnecessary for this case.

Concrete result: An Author identifies a person or organization credited with creating an Asset. An Asset has its own identity: correcting its title or replacing a representation need not change which asset it is. Authorship expresses credit, not necessarily ownership, upload responsibility or access rights. Pending domain confirmation, a useful proposal allows an author to have zero or more assets and an asset to have one or more authors; allow zero authors only if unknown attribution is valid. Example: Ada and Bo jointly authored “Harbor study”; both point to the same asset. Correcting Ada's display name leaves that authorship intact. Removing an author profile must not silently erase asset identity or historical credit; deletion semantics remain an explicit model question. These are synthetic examples and proposed cardinalities, not observed project facts. No schema, setup tooling or new environment is required to answer this.

Preserved: conceptual scope, identity/relationship separation, assumptions, synthetic example and change case. Missed requirements: none identified. Because lifecycle references were already in context, this is evidence of restrained output, not proof of clean cold routing.

## Actual reads and classification

Every listed file was read once, without tool truncation; no repeated reads. Cases shared context. Counts below are approximate whitespace words of instruction/project-context file content, not total model context or token use. Copied files not listed were not read as instructions. A file-name catalog (`rg --files`, 106 paths) was read separately; generated evidence authoring is not included. The validation method was read separately (actual count recorded below).

| File relative to fixture | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 34 | Required: declared entry routes and read-only authority (read late; limitation above). |
| `catalog-context.md` | 82 | Required: adopted SQLite/dev scope and retained-data delta. |
| `skills/project-foundation/skills/project-design/SKILL.md` | 1211 | Required: architecture and conceptual entry. |
| `skills/project-foundation/skills/project-policy/SKILL.md` | 717 | Required: operating transition entry. |
| `skills/project-foundation/references/database-environments.md` | 610 | Required: reproducible dev and staging transition obligations. |
| `skills/project-foundation/skills/project-policy/references/policy-changes.md` | 1399 | Required: changed use, owners, work and evidence gates. |
| `skills/project-foundation/references/foundation-authority.md` | 442 | Required: adopted vs proposed scope/authority. |
| `skills/project-foundation/references/status-and-evidence.md` | 590 | Required: distinguish walkthrough from execution evidence. |
| `skills/database-migrations/SKILL.md` | 806 | Useful: setup, seed, reset and migration guarantees. |
| `skills/project-foundation/skills/project-design/references/conceptual-models.md` | 357 | Required: conceptual case identity and change example. |
| `skills/project-foundation/references/document-homes.md` | 2254 | Useful: current owner and proposal rules; much of full file unnecessary for these small proposals. |
| `skills/project-foundation/skills/project-planning/SKILL.md` | 822 | Required by project-design when sequencing implementation; useful owners/dependencies/evidence. |
| `skills/database-migrations/references/database-tests.md` | 878 | Mixed: generic provenance/lifecycle useful, PostgreSQL/PGlite/platform sections irrelevant to SQLite. |

Instruction/project-context subtotal: 10202 whitespace words. Method read: 413 words. This excludes inherited context, catalog listing, tool scaffolding and result text.

## Findings and smallest supported fix

1. Core deeper routes preserved the important requirements: dev-only does not mean no setup; full tests can wait while smoke checks cannot be claimed; valuable dev state survives; staging requires concrete work and evidence; conceptual output stays conceptual.
2. `database-migrations` routes “selecting an embedded engine ... or checking migration behavior” to `references/database-tests.md`, whose title and significant content are PostgreSQL-specific. SQLite case reaches unnecessary PostgreSQL/PGlite advice. Smallest fix: qualify the reference route for PostgreSQL-specific testing, keeping generic smoke/runner requirements in SKILL.md, or split generic lifecycle from PostgreSQL details. This is a routing cost finding, not observed erroneous engine selection.
3. No required database guidance was missed in resulting proposals. No source maintenance guidance or postgres-design activation occurred. Reading broad document-homes introduces extra unrelated placement detail, but no new regression is established without a comparable baseline.
4. Remaining validation gaps: blind hook-first cold entry, independent conceptual-only context, runtime behavior, existing application integration, source-authoring route and comparison with previous revision. Single walkthrough does not demonstrate routing reliability.

## Focused fix verification

After the original copied-fixture walkthrough, the parent updated the source route. A read-only `rg` excerpt of source database-migrations/SKILL.md lines 75–86 confirms that database-tests.md now applies explicitly “For PostgreSQL”; other engines use their own disposable instances and project verification guidance. The fixture intentionally preserves the original evaluated snapshot. This textual check resolves finding 2's overbroad link condition, without claiming a fresh consumer rerun or runtime tests. This additional source excerpt is separate from the 10,202-word copied-fixture instruction subtotal above.
