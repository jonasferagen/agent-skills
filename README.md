# Jonas’s agent skills

Jonas's reusable, project-agnostic agent skills. Every skill is a standalone
package at `skills/<area>/<name>/`, installed by its name and complete in its
own directory. Areas group skills by their main task for browsing; they do not
require loading every skill in the group, and they are not installation units.
A skill marked (draft) is a first version whose scope is still settling: expect
its contract to change, and read its validation page for what has been exercised.

Dated review and trial records live under `validation/`; the
[collection sweep](validation/collection-sweep.md) and the per-collection pages
there describe the grouped layout this repository used until October 2026.

A downstream distribution may bundle several skills from here into one
installation. It owns its own membership, lock, checker and release rules; this
repository supplies the packages and their versions.

## Authoring

| Skill | Use it for |
| --- | --- |
| [clear-writing](skills/authoring/clear-writing/SKILL.md) | Express facts and instructions clearly without changing their meaning. |
| [diagrams-and-tables](skills/authoring/diagrams-and-tables/SKILL.md) | Choose and verify useful visual explanations of relationships and comparisons. |

## Design

| Skill | Use it for |
| --- | --- |
| [project-design](skills/design/project-design/SKILL.md) (draft) | Shape system responsibilities, conceptual models, workflows and integration choices. |
| [project-contracts](skills/design/project-contracts/SKILL.md) (draft) | Read, apply, design or review obligations at a handoff, including acceptance and failure. |
| [source-of-truth](skills/design/source-of-truth/SKILL.md) | Give each rule a home and derive or check its other appearances. |
| [application-design](skills/design/application-design/SKILL.md) (draft) | Shape operations, state ownership and dependency interfaces inside an application, including external operation boundaries. |
| [service-boundaries](skills/design/service-boundaries/SKILL.md) | Define service ownership and shared behavior across HTTP and MCP adapters. |
| [relational-modeling](skills/design/relational-modeling/SKILL.md) (draft) | Structure known entities around retrieval questions and revise relationships through synthetic scenarios. |
| [postgres-design](skills/design/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, timestamps and integrity boundaries, and transactions on pooled connections. |

## Operations

| Skill | Use it for |
| --- | --- |
| [service-classes](skills/operations/service-classes/SKILL.md) (draft) | Decide whether a capability is a service and whether it is running or scheduled, what evidence each class owes, and what a status report may claim. |
| [runtime-operations](skills/operations/runtime-operations/SKILL.md) | Credential handling, local service controls, child processes and encrypted PostgreSQL backups, as method and an interface contract rather than shipped code. |
| [database-migrations](skills/operations/database-migrations/SKILL.md) | Preserve migration history, review baselines and verify database bootstrap and upgrades. |
| [docker-cli](skills/operations/docker-cli/SKILL.md) | Write or review a single container or image command: ports, secrets, mounts, labels, identity and the cleanup of what it created. |
| [docker-compose-cli](skills/operations/docker-compose-cli/SKILL.md) | Write or review a compose command and the file it reads: project selection, inherited environment, borrowed definitions and project-scoped teardown. |
| [docker-cleanup](skills/operations/docker-cleanup/SKILL.md) | Audit a Docker host's accumulated images, volumes, networks and build cache, and reclaim space by attributed owner and tier. |

Runtime-operations states the
[runtime helpers contract](skills/operations/runtime-operations/references/runtime-helpers.md)
a consumer binds to, without shipping the helpers themselves: a distribution
deploys that code and names the interface version it was written against.
Service homes, document shapes, control commands and their checks are the
installing distribution's convention, and service-classes states only what a
service and its status owe. Promotion from a spike to maintained service use
reads service-boundaries, service-classes and runtime-operations together.

The three Docker packages split one tool by the moment it is used: assembling a
command, driving a project of containers, or accounting for what a host has
accumulated. Each is standalone and carries its own copy of the identity,
label-over-pattern and prune-refusal rules they share. The outcomes a project's
containers must meet — lifecycle, state custody, image pinning, composed sets —
are convention rather than CLI usage and belong to the consuming project's
framework.

## Verification

| Skill | Use it for |
| --- | --- |
| [verification-design](skills/verification/verification-design/SKILL.md) | Choose evidence for a change or milestone and consolidate checks by the failures they detect. |
| [test-writing](skills/verification/test-writing/SKILL.md) | Writing unit tests, integration tests and their fixtures, with made-up data and state each test owns. |
| [test-audit](skills/verification/test-audit/SKILL.md) | Auditing a settled test suite for brittleness, coverage asymmetry, weak assertions, mock drift and non-determinism. |

Choose by the requested task; new regression work does not require a suite audit.

## Workflow

| Skill | Use it for |
| --- | --- |
| [project-bootstrap](skills/workflow/project-bootstrap/SKILL.md) (draft) | Establish actual project context, policy, overview and usable agent routes. |
| [project-planning](skills/workflow/project-planning/SKILL.md) (draft) | Choose next work, sequence prerequisites and keep one coordination owner per item. |
| [project-policy](skills/workflow/project-policy/SKILL.md) (draft) | Establish or interpret policy, assess compliance and review changed operating facts or obligations. |
| [work-records](skills/workflow/work-records/SKILL.md) | Commission bounded work as a brief, retain its evidence and close it with a scoped disposition; supplies assignment and evidence methods plus the opt-in `work-record/v1` checker; concrete shapes belong to the consuming project. |
| [pattern-capture](skills/workflow/pattern-capture/SKILL.md) | Decide whether an engineering discovery generalizes and improve its existing skill home when authorized. |

Work records are an extension a project adopts through their
[extension declaration](skills/workflow/work-records/references/extension.md).
Named processes and their page format belong to the consuming project's framework.

## Languages and runtimes

| Skill | Use it for |
| --- | --- |
| [typescript-patterns](skills/languages/typescript-patterns/SKILL.md) | TypeScript types, narrowing, generics, absence, module syntax and enforcement. |
| [typescript-design](skills/languages/typescript-design/SKILL.md) | Class-based TypeScript house style: operations, naming, ownership, ports, barrels and directory layout. |
| [node-patterns](skills/languages/node-patterns/SKILL.md) | Preserving child-process outcomes, exit status and output in Node scripts, command-line tools and test harnesses. |
| [python-patterns](skills/languages/python-patterns/SKILL.md) | Python types, runtime boundaries, defaults, exceptions, resource cleanup and async tasks. |
| [python-design](skills/languages/python-design/SKILL.md) | Class-based Python house style: operations, domain values, dependency protocols, naming and modules. |
| [bash-patterns](skills/languages/bash-patterns/SKILL.md) | Preserving arguments, command failures, query results and cleanup ownership in Bash scripts. |
| [godot-gdscript](skills/languages/godot-gdscript/SKILL.md) (draft) | Typed Godot scripts, headless probes, imports and scene measurements. |

The patterns and design skills of one language pair naturally; each works alone.

## Using a skill

Copy the complete skill directory from a selected source commit into the target
repository's `.agents/skills/<name>/` through its normal review process. Record
source URL, source directory, full commit SHA, and any selected release version
and tag in the target's `.agents/skills/UPSTREAM.md`. The SHA is the authoritative
pin. Imported files should match that commit; keep project-specific rules outside
the imported directory and document any necessary local modifications in the
provenance file.

Names, invocation examples and release tags are unchanged by source grouping.
Existing imports retain their pinned source paths; use the new path when importing
a revision after a move.

Every package keeps its required resources inside its own directory: references,
templates, scripts and their tests. Links must stay inside the package. A skill
refers to another skill by name, never by a relative path, because the consumer
decides which skills are installed and where. When two packages must each state
one rule, record the copy in both places with a comment naming the counterpart,
such as `<!-- Package-boundary copy: test-writing/references/fixtures.md states
this rule for ordinary tests. Keep both passages aligned. -->`. Paths start with
the counterpart's package name.

These comments record a maintenance relationship, not semantic agreement. Name
the authoritative owner when one passage is a copy. Prefer deriving a required
copy or checking it against that owner over relying on a reminder. Source-level
reuse can cross package boundaries while every committed package remains
independently installable. Keep contextual applications distinct when exact
wording would erase their different responsibilities.

A distribution may import an explicitly self-contained reference as a file,
recording its owning skill, version, source path and full commit. This does not
install or register the whole skill. The shared-value reference at
`skills/design/source-of-truth/references/authoritative-values.md` supports that
use and requires no sibling resources, as does
`skills/operations/runtime-operations/references/runtime-helpers.md`. Keep both
free of local links, so an importer that rejects them can carry the file. Preserve the imported bytes and record
the distribution's own adoption and routes separately.

## Verification

For source maintenance, install Node 24, Python 3.11 or later and GnuPG, run
`npm ci --ignore-scripts`, then `python3 scripts/check.py`. This command checks
packages and discovers helper suites under `scripts/` and `skills/`, including
the real GnuPG round trip and examples extracted from the TypeScript and Node
guidance. Empty, failed, skipped and incomplete suites fail the command. Missing
prerequisites fail explicitly. CI runs the same command. These local checks do
not establish live service or database acceptance.

`python3 scripts/validate-packages.py` alone checks frontmatter, local link
targets and anchors, package containment, unique names and that each recorded
copy names an existing counterpart that records it back. A source test applies
the same link check to this README and the repository instructions; dated records
under `validation/` may cite paths that have since moved. Behavioral scenarios in
`validation/` and bundled helper tests still need their own review.

`python3 scripts/check_shared_contracts.py` compares the selected TypeScript
module-syntax copy with its current owner. The
ordinary `scripts/check.py` gate runs it and the compatibility tests. This is a
bounded check of declared shared contracts, not a semantic scan of all guidance.

## Discovery and lesson capture

### Routing quality

A consumer must be able to find the relevant guidance without reading this
authoring repository's maintenance material. Additional reading must follow a
concrete task need, and required deeper guidance must remain reachable. Apply this
standard to our own catalog and instructions as well as their output.

Routing is an acceptance requirement when changing triggers, entrypoints, shared
guidance or packaging, and before releasing a skill. Run proportionate
practical trials using the [routing trial method](validation/discovery.md#routing-trial-method).
Preserve task constraints and check missed obligations as well as unnecessary
reading. Package validation alone cannot establish routing quality.

Do not set a universal word budget. Compare equivalent tasks and explain which
reads were unnecessary. Record remaining gaps; do not claim the requirement is
verified from word-count reductions alone. Ordinary prose edits need no new trial
unless they change routing or reveal concrete friction.

When authoring here, use the catalog and maintenance sections relevant to the
change. When consuming an installed skill, use its entrypoint and project
routes. Do not follow provenance back to this README unless the task needs source
maintenance, upgrade information or investigation of a concrete source issue.

### Selection and capture

Skill descriptions name the task or observed symptom that should select the
package. Keep them concise and put the main trigger first. The selected
`SKILL.md` supplies essential guidance and routes to conditional references;
open only the references needed for the current decision. Grouping this catalog
does not itself control which instructions an agent reads.

`pattern-capture` needs one thing from the project that installs it: a reporting
and repair checkpoint that is reachable before any skill is selected, so a
consequential guidance or routing problem met during ordinary work is reported
rather than worked around, and a reusable finding reaches this skill at a natural
checkpoint. The installing distribution or project owns that instruction: its
text, where it lives, the local link to the installed skill, the capture home,
and any text shortcut such as `/pattern-capture [idea]`, which is an
agent-interpreted shortcut and not a native slash-menu entry. This repository
states the need and does not dictate the consumer's wording or placement.

Verify spontaneous reporting through the
[reporting acceptance trials](validation/discovery.md#reporting-acceptance-trials).
A checkpoint being installed or an agent reporting that it read it does not by
itself establish that the agent notices and reports a problem during ordinary work.
Put the source location in provenance; never bake a machine-specific path into
the skill. Reading and proposing guidance can fit a review. Writing the source
repository or adopting a new pin follows the task's actual authorization. For
explicit requests, invoke `$pattern-capture` with an idea or refer to the
current discussion.

Test discovery with realistic requests and metadata before showing skill bodies
or expected answers. Record whether a trial used host-provided metadata, a
supplied metadata catalog, or a project hook. Check a nearby request that should
not activate the skill as well. A successful package check alone says nothing
about selection. See [the discovery review](validation/discovery.md).

## Skill releases

Version each skill independently. Its `SKILL.md` declares a string under
`metadata.version`, such as `"1.0.0"`. Publish an annotated Git tag named
`<skill-name>/v<version>` on the committed release; never move a published tag.
The tagged package and manifest version must agree. Unreleased skills can remain
pinned by commit until their first release. Tags of the retired collection
layout, `<collection>/v<version>`, remain as history and are not reused.

The version on `main` can also describe an unreleased revision after an earlier
tag. The tag remains the last released version until that revision is validated
and tagged; consumers keep their selected pins. A version bump alone publishes
nothing.

Use semantic versions for the skill's behavioral contract: its scope, required
behavior, defaults, exceptions and bundled resource interfaces.

- **Patch:** clarify or correct wording without changing intended requirements.
- **Minor:** add compatible guidance or capabilities within the existing contract.
- **Major:** change defaults, mandatory rules, scope or exceptions in a way that
  requires consumers to review their adoption.

Before tagging, validate the package and its behavioral scenarios, repeat the
applicable routing trials, and complete the
[self-conformance review](validation/self-conformance.md) for a skill that
bundles scripts, templates or an extension declaration. A release must contain
no unfinished scaffold or project-specific credentials or identifiers. Consumers
pin the full commit as well as the release label because tags are names, not an
integrity guarantee. Other skills in the repository need no version bump when
one skill is released.

### Authoring skills

Skills in this repository should meet the standards they teach. Apply relevant
guidance to the packages, helpers and documentation we maintain here. Start
with the named package when one is known; use the catalog to select additional
guidance from the task's actual trigger. Load only needed references. For example,
use source-of-truth when reconciling copied rules, verification-design when
selecting evidence, and pattern-capture when assessing a reusable finding or an
explicit capture request. Its simplicity test also applies to our own rules and
exceptions. Report a relevant conflict or gap rather than silently exempting the
repository.

During authoring, AGENTS.md requires writing and visual guidance where relevant.
Before tagging a release, also apply these skills to the content changed since the skill's
last tag, or to the whole package for a first release:

- [Clear writing](skills/authoring/clear-writing/SKILL.md), to the prose.
- [Diagrams and tables](skills/authoring/diagrams-and-tables/SKILL.md), to existing
  diagrams and tables and to passages a diagram or table would explain better.

This pass is a recommendation, not a release requirement. Clear Writing does not
yet cover every kind of prose a skill package contains, such as trigger
descriptions, defined terms, worked examples, pattern catalogs and templates.

When you apply them, record on the skill's validation page which skills were
applied and what they changed; "no change needed" is a valid result. When a pass
rewrites wording, an independent comparison of each changed passage with the
prior text is recommended: the first Clear Writing sweep found four meaning
changes that way.

## Adding a skill

- Keep it project-agnostic: no account details, credentials, service
  identifiers or private domain records, and no names of the projects or
  distributions that consume these skills. A skill about one project's systems
  does not belong here. Skills about Jonas himself, such as his email style,
  live in his separate local `personal-skills` repository.
- Make no claim about a consumer. A package states a need; where the consumer
  satisfies it is the installer's to decide. So a package names no path,
  filename, document home, command name or instruction wording in a consuming
  project, and ships no code a consumer imports or executes — only the interface
  contract such code is bound by. Guidance selected by a command or artifact in
  front of the reader belongs here; an outcome a project's own work must meet
  belongs to the installing distribution's conventions. An installing
  distribution states the same division in its own words, from its side; fix an
  overreaching package here rather than letting a consumer document the
  deviation. The retirements of `containerization` and `repository-services`
  record what this costs when it is noticed late.
- Put the manifest at `skills/<area>/<name>/SKILL.md`; choose the existing area
  whose task it serves. Keep skill names unique. Put every resource the skill
  needs inside its directory. `agents/openai.yaml` carries the display name for
  tools that read it.
- Choose a short lowercase hyphenated name for the activity or subject readers
  will seek. Use familiar terms and the actual language or tool when it narrows
  the scope. Preserve an established name unless clearer discovery justifies
  changing consumer paths.
- Use the [authoring skills](#authoring-skills) while writing the package.
- Record intended behaviour in `validation/<name>.md` when a skill has scope
  boundaries worth testing, and add a row to the table above.

## Origins

**docker-cli** and **docker-compose-cli** 0.1.0 split the retired
containerization package along the line between assembling one container command
and driving a project of them. The cut was chosen over one Docker package because
most compose accidents are a command that ran correctly against the wrong
project, decided by inputs the command line does not show — the caller's
`COMPOSE_*` variables and a `.env` file in the working directory — and that
trigger has nothing in common with getting a port, a secret or a mount right on
a single `docker run`. Four rules apply to both: run identity, the label scheme,
registering cleanup before creating, and sweep-and-prove. They are duplicated
with reciprocal copy records rather than linked, because each package must work
alone. One seam resists the cut: binding a run's own state locations is
triggered by `compose run` borrowing a service definition but fixed with a
`docker run` bind, so the trigger lives in docker-compose-cli and docker-cli
carries the mechanic. See [docker-cli](validation/docker-cli.md) and
[docker-compose-cli](validation/docker-compose-cli.md).

**docker-cleanup** 0.1.0 separates reclaiming a host's accumulated Docker state
from the two CLI packages, which own what one command or project created. All
three forbid blanket prune commands, from different directions: a prune can
reach resources the work did not create, and resources an audit never
classified. The lesson came
from clearing a development host that had run a retired project alongside two
unrelated ones. Three decisions in that pass are now rules. Age and retirement
do not establish that a volume is disposable — three volumes in an approved
group held credentials, a release tree and an unexpected database data
directory, so contents are read and rescued before removal. Two tags sharing one
image ID are one image, so a rename leftover is reported at zero size. A type's
reported size is not its reclaimable size, because images and build cache share
layers. The entrypoint gives a five-step method, names the selecting symptoms
and their non-triggers, and routes to one reference for the commands,
attribution signals and reporting shape. It is deliberately Docker-specific: the
method would translate to another engine, but every command in it is Docker's
and no other engine has been tried, so the first draft's engine-neutral name and
claim were both dropped. It stayed a third package rather than a reference inside
docker-cli because its trigger is a symptom — a build failing for space — not an
invocation under review, and because its substance is an authorization about
destructive action that a reader loading flag guidance should not pick up.
Example requests: "Use $docker-cleanup to find what is reclaimable on this
host", "Use $docker-cleanup to clear the retired project's container state." See
[validation](validation/docker-cleanup.md).

**test-writing** 0.1.0 fills the gap between verification-design, which chooses
the checks a change needs, and test-audit, which judges a settled suite. No
package was selected at the moment a test or a fixture is written, although
rules for that moment sat in four packages under other triggers. The lesson
that prompted it came from a project that keeps real personal data in an
ignored directory. A test about unlabelled numbers was written with a phone
number and an identity-like number copied from that data into a tracked file.
The entrypoint gives a workflow and routes to three references: unit tests,
integration tests and fixtures. Its new rule is that every value in a test is
made up, and that a test reproduces the shape of a real value, never its
content or a part of it. In the trials the instructions alone did not hold on
every model, and a project test that checks for copied values did. So the
fixtures reference says what such a check needs. The check itself belongs to
the project: the first versions bundled one, which now lives in the project
that prompted the skill, with the workflow around it. Example requests: "Use
$test-writing to add a regression test for this parser fix", "Use $test-writing
to build sample records for the importer tests." See
[validation](validation/test-writing.md).

**verification-design** and the since-retired **shared-code-design** captured two
architecture decisions exposed by a review of the local Atlas/Work proof of
concept in 2026-09. The former separates evidence at schema, domain,
independent-session, public-interface and built-artifact boundaries while
looking for repeated setup. The latter compared checked copies with generation
and versioned dependencies against the promise that each component builds
independently; it was retired on 2 October 2026 and its
[validation history](validation/shared-code-design.md) is preserved. The
installable skill uses language-neutral examples and imposes no project test
matrix or package manager. See its
[verification scenarios](validation/verification-design.md).

**containerization** was retired on 9 October 2026 at 1.1.0, split into
`docker-cli` and `docker-compose-cli` for CLI usage, with its convention-shaped
outcomes going to the consuming framework's local-containers convention and its
PostgreSQL and verification material to database-migrations and
verification-design. Its reuse of one service image for API, migration and seed
commands, added at 0.3.0, is an image-authoring outcome and left with the
convention. Its [validation history](validation/containerization.md) and Git
history are preserved.

**repository-services** was retired on 9 October 2026 at 0.3.1 and replaced by
`service-classes` 0.1.0. It mixed judgment with placement: the running and
scheduled classes and what each owes as evidence sat beside a `services/` home,
an index and guide file layout, five reserved action words, a control entry
point, a dispatcher implementation, a structural validator and an adoption
declaration. Everything that names a path, a filename, a command or a document
shape is a claim about a consuming project, so it went to the installing
distribution's convention; the classification and status judgment stayed. The
name went with the layout, because a routing trial had found the old catalog row
pulled a reader expecting service guidance into a home their project did not
have. Its [validation history](validation/repository-services.md) and Git
history are preserved.

**runtime-operations** 3.0.0 stopped shipping the Python helpers a consumer
imports. Six modules, a service-runtime template and their four test suites left
the package; the credential tiers, child-process rules, service-control method
and backup guarantees stayed, and the
[helpers contract](skills/operations/runtime-operations/references/runtime-helpers.md)
grew because the shipped loader used to demonstrate a contract it now has to
state. The interface version did not move: no signature or field changed, only
who distributes the code. The name did not change either, since the trigger and
the subject are untouched — a reader asking about a credential, a service
control or a backup still selects this package. The proposed three-way topical
split was assessed and declined.

**test-audit** 0.3.0 narrows its integration-test advice to the failure each
test can observe. Native contention, real permissions and built-artifact checks
remain distinct evidence even when they call the same domain operation. Its
full-suite rule now applies to complete coverage and timing claims; a static
audit need not run the suite. See [validation](validation/test-audit.md).

**clear-writing** brings the short-text guidance into a reusable prose skill,
with a shared core and separate references for instructions and short text. It
covers wording and meaning; visual form belongs to `diagrams-and-tables`, and
document ownership stayed with `project-docs`, which left this repository with
project-foundation on 4 October 2026. Jonas's email voice has its own skill
outside this repository. Its first prose trials are the conceptual
`source-of-truth` skill and the procedural `bash-patterns` skill; a later sweep
revised eight more packages. See [validation scenarios and
results](validation/clear-writing.md).

**postgres-design** was extracted from Personal Atlas's database conventions on
2026-09-29 and compared with work-system's migrations and data model. The
installable package uses synthetic examples and contains no project schema names,
service identifiers, vocabulary inventories or deployment policy. Work-system
contributed guidance on provenance versus identity, explicit conditions, atomic
commands and retries. Atlas credits the owner's Forge database conventions as an
earlier influence. Version 1.1.0 adds a reference on transactions over pooled
connections, drawn from the transaction runner of the local atlas-work-dev
services and checked against PostgreSQL 17. See
[validation and alignment](validation/postgres-design.md) for pinned sources,
adoption differences and review limits.

**project-docs** lived here until 4 October 2026, when it moved with
project-foundation to [its own repository](https://github.com/jonasferagen/project-foundation).
It was developed from a documentation review and cleanup in Personal on
2026-09-19. The reusable guidance is newly written, and the worked
example is synthetic. The source project credited Forge Agent Kit and Diátaxis
as earlier influences; the package contains no copied upstream skill files. It
supports establishing a documentation set, reviewing an existing one, and
reconciling it after changes, and adapts to the project's existing layout
rather than prescribing a stack, access model, merge policy or folder tree.
Example requests: "Use $project-docs to establish documentation for this
repository", "Use $project-docs to reconcile the docs after this release." See
[its validation scenarios](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/project-docs.md); it still needs
experience in a second real project.

The owner's Forge Agent Kit `selfcheck-guard` skill was folded into
**source-of-truth** at 1.1.0 on 2026-09-29, from the same commit as the
bash-patterns and test-audit imports, rather than added as a ninth skill. This
one already ended at a check — keep the restatement, add a gate that fails when
the homes disagree — and never said what keeps that check working after the next
restructure. The bar's six requirements and seven questions now sit in the
manifest at that rung, and the five properties behind it, each with the shape
that breaks it and the shape that holds, are in its
`references/durable-checks.md`: compute the invariant live instead of
re-blessing a golden, anchor to the check's own location or to version control,
read the manifest rather than copying it, fabricate the fixture, and report an
absent dependency as absent rather than as a failing test. Forge Project Policy
citations were redirected as in test-audit — two carried substance now stated in
place, and whether a check earns its recurring cost defers to the reading
project's own policy.

**change-workflow** was retired on 3 October 2026. It combined Git worktree
operations with verification, document maintenance, tracker procedures and
reporting conventions. Its [validation history](validation/change-workflow.md)
retains the source provenance and review evidence; the former package remains in
Git history.

**diagrams-and-tables**, named `diagrams` until 2026-09-30, merges the owner's
Forge Agent Kit `diagrams` skill, at `c98147a115a30f36b952df5faf1c869b54480c59`,
with the diagram conventions that `project-docs` had been carrying. Upstream
supplied form choice, the underused-tables argument, draw-less-link-more,
vertical-and-one-altitude, the drawing reference and ten worked examples; the
local reference supplied two sections upstream lacked — grounding every edge in
whatever owns it, and verifying that a diagram reads in the renderer and themes
its readers use, where a successful parse is explicitly not a readability check.
It is a top-level skill because form choice applies to plans, issue bodies,
design records and review feedback, not only to documentation.

`project-docs` was reduced in the same change to what is particular to a
documentation set — which document owns which view, glossary-led terms, and
freshness as part of doc review — so the craft has one home instead of two that
drift. Three provenance citations naming a private repository and its commits
were replaced with neutral descriptions, and one worked example's schema
vocabulary was renamed, so the package carries no project identifiers while
keeping the real shapes and counts the examples depend on. Example requests:
"Use $diagrams-and-tables to decide whether this section wants a diagram or a
table", "Use $diagrams-and-tables to split this overview before it gets any
wider." See [validation and alignment](validation/diagrams-and-tables.md).

**bash-patterns** was imported from the owner's Forge Agent Kit on 2026-09-29,
pinned at `c98147a115a30f36b952df5faf1c869b54480c59`. The upstream package
referenced no Forge systems, trackers or policy. Its behavioral guidance is
retained, with local metadata, repository authority guidance and revised prose.
It distinguishes a successful match, a successful absence and a failed
acquisition, and covers the defects that blur them: a `local` declaration
reporting its own status, an early pipeline reader turning a match into a SIGPIPE
failure under `pipefail`, and a process substitution whose producer status nobody
collects. Example requests: "Use $bash-patterns to check whether this backup
script's checks can pass when they should fail", "Use $bash-patterns on this
pipeline before I trust its exit code." Version 0.2.0 retains those rules in
focused references and adds argument boundaries, explicit status handling, file
iteration and resource ownership. Third-party defensive Bash guidance supplied
topics to assess; the additions are newly authored and runtime-checked. See
[validation and alignment](validation/bash-patterns.md).

**node-patterns** was written on 2026-09-30 as the Node counterpart to
bash-patterns, from a review of the local atlas-work-dev repository. That review
found one idiom for reading a child process's result copied into seven places;
it reported a timeout, a signal, a missing program and truncated output all as
exit 1. The review also found check scripts that exit before their piped output
is written, and a script root resolved from a URL path that fails under a
directory containing a space. Every behavior the package states was reproduced
with Node 24 on Linux before it was written down. It covers how Node reports
outcomes; which output may hold secrets, how a child's environment is built and
what a timeout should mean stay with runtime-operations or the project's own
guidance. Example requests: "Use $node-patterns to check that this harness
reports why docker failed", "Use $node-patterns on these check scripts before CI
relies on their exit status." See
[validation and alignment](validation/node-patterns.md).

**test-audit** was imported from the same Agent Kit commit on 2026-09-29, and
fills a gap this repository declared on purpose: `typescript-patterns` leaves
testing to the reading repository, so both consuming projects owned it locally
with no shared method. Its sharpest lens is the unfalsifiable request — a double
answers whatever the code asks it, so what the code claims about an external
contract was never checked against the real thing, which is not drift because
there was nothing to drift from. Three Forge Project Policy citations were
redirected: two carried substance now stated in place, and the third defers to the
reading project's own policy, because the upstream policy opens by declaring
nothing is in production while both consumers are. References to three sibling
Agent Kit skills became descriptions of the boundary, since a cross-package path
would break when this skill is installed alone. Example requests: "Use $test-audit
on the runner suite", "Use $test-audit to find what our mocks have never actually
verified." See [validation and alignment](validation/test-audit.md).

**typescript-patterns** and **typescript-design** separate the language and
house-style guidance in Jonas's TypeScript canon, first brought here on
2026-09-29. Both packages use a symptom table to select focused references,
remain installable alone, and leave testing and review workflows to the
consuming repository.

`typescript-patterns` owns language conventions, type safety, generics, module
syntax and compiler/lint enforcement. `typescript-design` owns the class-based
house style: operations, domain values, naming and placement, dependency ports,
orchestration, resolution, barrels and directories. Class-based operations
remain a strong convention with the same exceptions; this split changes where
rules are selected, not the design choices themselves.

To preserve the former package's full guidance when upgrading from
`typescript-patterns` 1.x, adopt **both** packages and update project guidance
that selected only the old skill. Existing commit-pinned copies remain intact.
Version 2.0.0 of `typescript-patterns` narrows its scope; version 1.0.0 of
`typescript-design` starts the extracted package. These manifest versions do not
publish release tags or update installed consumers.

Example requests: "Use $typescript-patterns to check this union and its label
table", "Use $typescript-design to name this module and its exports", and
"Use $typescript-design — this constructor takes six positional arguments."
See the [language validation](validation/typescript-patterns.md) and
[design validation](validation/typescript-design.md), including the split's
reference mapping and remaining limits.

**python-patterns** and **python-design** start the same language/design split
for Python at version 0.1.0. They cover selected failure-prone patterns and the
class-based house style, using Python conventions: keyword-only arguments,
dataclasses, protocols, snake_case names and cohesive modules.

Everything Claude Code's Python skill informed topic selection; Trail of Bits'
modern-python plugin helped identify tooling decisions to leave with consuming
projects. The prose and examples are newly authored and checked against Python's
documentation. No upstream skill files, hooks or installers were imported.
Source pins, adoption decisions and verification limits are recorded in the
[language validation](validation/python-patterns.md) and
[design validation](validation/python-design.md). Updates require deliberate
review; neither upstream is tracked automatically.

Example requests: "Use $python-patterns to review cancellation and cleanup in
this worker", "Use $python-design to give these operations and values clear
owners." Each package works alone; neither prescribes a toolchain or changes
installed consumers.

**source-of-truth** was extracted on 2026-09-29 from a duplication audit of
Personal Atlas: six parallel searches over validation rules, domain vocabularies,
logic expressed in more than one medium, configuration constants, types and
shapes, and documentation, with every candidate independently challenged before
acceptance. Its subject is the seam between media — a concept authored in a
schema, a setting or a document and restated in application code, another
language or prose, where no single search finds both sides and the restatement
falls behind silently. It deliberately excludes code shape, which belongs to
[typescript-design](skills/languages/typescript-design/SKILL.md), and schema design,
which belongs to [postgres-design](skills/design/postgres-design/SKILL.md). The
installable package is synthetic throughout and names no language, framework or
toolchain as a requirement. Several of its false-positive tests — a complete copy
versus a deliberate subset, a test that states its expectations being a third
home rather than a check, an opt-in test not counting as gate coverage — came
from the challenge step rejecting or correcting an initial finding. Example
requests: "Use $source-of-truth — this vocabulary is defined in the schema and
again in the reader", "Use $source-of-truth to decide where this constant belongs."
See [its validation scenarios](validation/source-of-truth.md); it has been applied
in one project only and is not yet released.

**jonas-email-style** lived here from 2026-09-24 until 2026-09-30, when it
moved with its history to Jonas's local `personal-skills` repository. It is
installed for his user account there rather than copied into projects.

**runtime-operations** supplies the common credential, Linux service and encrypted
backup machinery used by Personal Atlas and Work-system. Project adapters own
vault IDs, roles, schema scope and access checks. The package includes offline
helper tests; consumer adapters also exercise actual disposable restores.
Child-process, argument and verification-reporting guidance was added in 1.1.0
from a parallel review of the same two projects' tooling: withholding child
output, inherited stdin reaching a child that parses it, timeouts and argument
vectors; subcommand and argument rules, including what a script must never accept
from its caller; verifying that a read-only session setting survived a pooler; and
the rule that a verdict names its denominator, which is adopted from the owner's
Forge project policy.
See [validation scenarios](validation/runtime-operations.md).
