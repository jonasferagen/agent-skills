# Jonas’s agent skills

Jonas's reusable, project-agnostic agent skills. Every skill is a standalone
package at `skills/<area>/<name>/`, installed by its name and complete in its
own directory. Areas group skills by their main task for browsing; they do not
require loading every skill in the group, and they are not installation units.
A skill marked (draft) is a first version whose scope is still settling: expect
its contract to change, and read its scenarios for what it is evaluated against.

A package may carry `scenarios/README.md`: the requests, context and expected
behavior it is evaluated against. Ordinary use of a skill does not read it.

A consuming project may install several skills from here together. It owns
its own selection, lock, checks and upgrade rules; this repository supplies the
packages and their versions.

## Authoring

| Skill | Use it for |
| --- | --- |
| [clear-writing](skills/authoring/clear-writing/SKILL.md) | Express facts and instructions clearly without changing their meaning. |
| [diagrams-and-tables](skills/authoring/diagrams-and-tables/SKILL.md) | Choose and verify useful visual explanations of relationships and comparisons. |

## Design

| Skill | Use it for |
| --- | --- |
| [repository-design](skills/design/repository-design/SKILL.md) | Define repository ownership, public commands and boundaries, external references, handoff contracts and independent verification. |
| [single-source-of-truth](skills/design/single-source-of-truth/SKILL.md) | Give each rule a home and derive or check its other appearances. |
| [application-design](skills/design/application-design/SKILL.md) | Shape application operations, internal boundaries, state ownership, injected dependencies and recovery. |
| [service-design](skills/design/service-design/SKILL.md) | Define runtime ownership, public interfaces, caller identity, retry behavior and storage custody. |
| [relational-modeling](skills/design/relational-modeling/SKILL.md) (draft) | Structure known entities around retrieval questions and revise relationships through synthetic scenarios. |
| [postgres-design](skills/design/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, timestamps and integrity boundaries, and transactions on pooled connections. |

Repository-design applies to content, library, application and infrastructure
repositories. Application-design and service-design specialize the decisions
inside applications and across running services; each package works alone.
Boundary contract review and external-reference discovery are part of
repository-design. Consumer adoption remains explicit and pinned.

## Operations

| Skill | Use it for |
| --- | --- |
| [service-classes](skills/operations/service-classes/SKILL.md) (draft) | Decide whether a capability is a service and whether it is running or scheduled, what evidence each class owes, and what a status report may claim. |
| [database-migrations](skills/operations/database-migrations/SKILL.md) | Preserve migration history, review baselines and verify database bootstrap and upgrades. |
| [docker-cli](skills/operations/docker-cli/SKILL.md) | Write or review a single container or image command: ports, secrets, mounts, labels, identity and the cleanup of what it created. |
| [docker-compose-cli](skills/operations/docker-compose-cli/SKILL.md) | Write or review a compose command and the file it reads: project selection, inherited environment, borrowed definitions and project-scoped teardown. |
| [docker-cleanup](skills/operations/docker-cleanup/SKILL.md) | Audit a Docker host's accumulated images, volumes, networks and build cache, and reclaim space by attributed owner and tier. |

Service homes, document shapes, control commands and their checks are the
consuming project's own, and service-classes states only what a
service and its status owe. Promotion from a spike to maintained service use
selects service-design for runtime boundaries and service-classes for
classification, as the work requires.

The three Docker packages split one tool by the moment it is used: assembling a
command, driving a project of containers, or accounting for what a host has
accumulated. Each is standalone and carries its own copy of the identity,
label-over-pattern and prune-refusal rules they share. The outcomes a project's
containers must meet — lifecycle, state custody, image pinning, composed sets —
are project decisions rather than CLI usage and belong to the consuming
project.

## Verification

| Skill | Use it for |
| --- | --- |
| [repository-maintenance](skills/verification/repository-maintenance/SKILL.md) | Review structural and semantic drift across a repository's responsibilities, instructions, implementation, checks and open work. |
| [verification-design](skills/verification/verification-design/SKILL.md) | Choose evidence for a change or milestone and consolidate checks by the failures they detect. |
| [test-writing](skills/verification/test-writing/SKILL.md) | Writing unit tests, integration tests and their fixtures, with made-up data and state each test owns. |
| [test-audit](skills/verification/test-audit/SKILL.md) | Auditing a settled test suite for brittleness, coverage asymmetry, weak assertions, mock drift and non-determinism. |

Choose by the requested task; new regression work does not require a suite audit.
Repository-maintenance assesses an existing repository's coherence; it does not
own project governance, maintenance scheduling or local document shapes.

## Languages and runtimes

| Skill | Use it for |
| --- | --- |
| [node-patterns](skills/languages/node-patterns/SKILL.md) | Preserving child-process outcomes, exit status and output in Node scripts, command-line tools and test harnesses. |
| [python-patterns](skills/languages/python-patterns/SKILL.md) | Python types, runtime boundaries, numerical comparisons, defaults, exceptions, resource cleanup and async tasks. |
| [python-design](skills/languages/python-design/SKILL.md) | Python program structure: responsibilities, phase contracts, state ownership, shared interfaces and naming. |
| [bash-patterns](skills/languages/bash-patterns/SKILL.md) | Preserving arguments, command failures, query results and cleanup ownership in Bash scripts. |
| [godot-gdscript](skills/languages/godot-gdscript/SKILL.md) (draft) | Typed Godot scripts, headless probes, imports and scene measurements. |

The Python patterns and design skills pair naturally; each works alone.

## Using a skill

Copy the complete skill directory from a selected source commit into the target
repository's `.agents/skills/<name>/` through its normal review process. Record
its provenance once, in the target's machine-readable dependency lock: the
source URL, full commit SHA, source directory, any selected release version and
each installed file's digest. A target that keeps no lock records the same
facts in the one provenance file it keeps, and never in both. The SHA is the
authoritative pin. Imported files should match that commit; keep
project-specific rules outside the imported directory, and record any necessary
local modification beside the pin.

Names, invocation examples and release tags are unchanged by source grouping.
Existing imports retain their pinned source paths; use the new path when importing
a revision after a move.

Every package keeps its required resources inside its own directory: references,
templates, scripts and their tests. Links must stay inside the package. A shipped
skill may name another skill but never links to it or depends on it: when two
packages need the same rule, each states it in full in its own words. Packages are generic: they make no
claims about a particular consuming project's process, records or conventions,
and their examples are synthetic.

A consuming project may import an explicitly self-contained reference as a file,
recording its owning skill, version, source path and full commit. This does not
install or register the whole skill. The shared-value reference at
`skills/design/single-source-of-truth/references/authoritative-values.md` supports that
use and requires no sibling resources. Keep it free of local links, so an
importer that rejects them can carry the file. Preserve the imported bytes and record
the project's own adoption and routes separately.

## Maintenance checks

For source maintenance, install Node 24 and Python 3.11 or later, then run
`python3 scripts/check.py`. It runs every `test_*.py`
suite under `scripts/` and `skills/`, including each package's own `tests/`.
Empty, failed, skipped and incomplete suites fail it, and missing prerequisites
fail explicitly. CI runs the same command. These local checks do not establish
live service or database acceptance.

### Where a package keeps its checks

| Directory | Holds |
| --- | --- |
| `references/` | Guidance applied while using the skill |
| `scripts/` | Tools the skill uses |
| `tests/` | Executable checks of behavior the package owns, as `test_*.py` suites `check.py` discovers; each suite declares its prerequisites in its docstring and runs from an independent copy of the package with `python3 -m unittest discover -s tests` |
| `scenarios/README.md` | Maintained requests, context and expected behavior, with current limits beside the behavior they qualify; case directories with synthetic inputs only when a case needs them |

Create none of these empty, and require no uniform section template beyond
useful case meaning. Scenarios hold inputs and expectations, not observed
outputs, timestamps or run reports. Source-wide package checks, cross-skill
consistency checks and the [selection scenarios](scripts/tests/selection-scenarios.md)
stay in `scripts/tests/`.

### Evaluating a skill against its scenarios

Give a fresh agent the case's request and context with the installed package,
not the expected behavior, under the isolation rules in
[routing quality](#routing-quality). Judge the artifacts against the expected
behavior; note missed obligations and unnecessary reading as well as wrong
answers. Record the observed results, the commit evaluated and the context
configuration with the change that ran them — its commit message, review or the
project's work record — not in the package. A run that shows a failure worth
keeping adds a regression case; one that shows a limit states it beside the
behavior it qualifies. One passing run demonstrates a route, not its reliability.

## Discovery and routing

### Routing quality

A consumer must be able to find the relevant guidance without reading this
authoring repository's maintenance material. Additional reading must follow a
concrete task need, and required deeper guidance must remain reachable. Apply this
standard to our own catalog and instructions as well as their output.

Routing is an acceptance requirement when changing triggers, entrypoints, shared
guidance or packaging, and before releasing a skill. Run proportionate practical
trials by the method below. Preserve task constraints and check missed obligations
as well as unnecessary reading. Package validation alone cannot establish routing
quality.

#### Routing trial method

Select realistic cases for the changed routes:

| Case | Observe |
| --- | --- |
| Cold entry into ordinary consumer work | Reads before useful work and irrelevant activation |
| Work requiring deeper guidance | Whether required references are reached and obligations preserved |
| Nearby work outside the changed skill's scope | Whether the agent avoids unrelated guidance |
| Source authoring when consumption or authoring routes change | Whether relevant maintenance rules still apply |

Start a new agent for each case with no forked conversation history, prior case
results, expected findings or preloaded skill bodies. Record the context
configuration and the exact skill metadata supplied at startup, including stale
or absent entries; fresh conversation context does not establish fresh metadata.
If the host cannot provide this isolation, record the run as an informed review
or walkthrough, which cannot pass independent acceptance.

Place the consumer fixture outside this repository with an installed copy, a
realistic project instruction hook and provenance. Start from that hook or from
normal discovery metadata; do not supply the expected route, and record whether
entry was explicit invocation, supplied metadata or project instructions. A
source-authoring trial starts in an isolated copy of this repository. Keep live
systems outside the trial. Reused agents can implement fixes and review known
findings; their results stay separate from independent acceptance.

Have the evaluator record the files actually read, approximate words, repeated
reads, truncation and reused context, distinguishing instruction reads from
catalogs, generated-output review and mechanical checks. Classify each material
read as required, useful or irrelevant with a reason, and report required
guidance missed and output constraints preserved or violated. An unexercised
case is a limitation.

A consumer reaching source maintenance material without a task reason is a
finding; so is missing necessary deeper guidance, even when reading falls.
Compare equivalent tasks across revisions and record the smallest supported fix
and remaining gaps. A single successful run demonstrates a route, not its
reliability. Capture a demonstrated problem in the owning package's scenarios;
do not turn every observation into another mandatory instruction.

Do not set a universal word budget. Compare equivalent tasks and explain which
reads were unnecessary. Record remaining gaps; do not claim the requirement is
verified from word-count reductions alone. Ordinary prose edits need no new trial
unless they change routing or reveal concrete friction.

When authoring here, use the catalog and maintenance sections relevant to the
change. When consuming an installed skill, use its entrypoint and project
routes. Do not follow provenance back to this README unless the task needs source
maintenance, upgrade information or investigation of a concrete source issue.

### Selection

Skill descriptions name the task or observed symptom that should select the
package. Keep them concise and put the main trigger first. The selected
`SKILL.md` supplies essential guidance and routes to conditional references;
open only the references needed for the current decision. Grouping this catalog
does not itself control which instructions an agent reads.

Put the source location in provenance; never bake a machine-specific path into
the skill. Reading and proposing guidance can fit a review. Writing the source
repository or adopting a new pin follows the task's actual authorization.

Test discovery with realistic requests and metadata before showing skill bodies
or expected answers. Record whether a trial used host-provided metadata, a
supplied metadata catalog, or a project hook. Check a nearby request that should
not activate the skill as well; the
[selection scenarios](scripts/tests/selection-scenarios.md) list such pairs. A
successful package check alone says nothing about selection.

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

Before tagging, review the package and its scenarios by hand, repeat the applicable
routing trials, and complete the release review below for a skill that bundles
scripts, templates or an extension declaration. A release must contain no
unfinished scaffold or project-specific credentials or identifiers. Consumers
pin the full commit as well as the release label because tags are names, not an
integrity guarantee. Other skills in the repository need no version bump when
one skill is released.

### Release review

For a skill that bundles scripts, templates or an extension declaration, a
release review applies the standards the skills teach to the package itself.
Review the whole package before
its release is tagged against the rules its own content and this repository's
authoring skills state — every file, not only the changes since an earlier
release — together with the catalog text and instructions that describe it.
Ordinary edits need only the checks in [AGENTS.md](AGENTS.md#verification). A
finding that recurs is a candidate for a mechanical check.

Run the mechanical checks first; they decide structure only:
`python3 scripts/check.py` (a package
without tests reports that coverage as absent rather than treating a zero-test
run as evidence), and
`git diff --check $(git hash-object -t tree /dev/null) HEAD -- skills/<area>/<name>`
for whitespace errors in every committed file of the package.

Then apply each owner's own review steps to the package's files:

| Rule owner | Apply to | Review steps |
| --- | --- | --- |
| Source of truth | Rules, vocabularies, paths and counts stated in more than one package file or in the catalog | [Review and verification](skills/design/single-source-of-truth/SKILL.md#review-and-verification) |
| Source of truth, check design | Bundled scripts and their tests | [Keep the check durable](skills/design/single-source-of-truth/references/check-design.md#keep-the-check-durable) |
| Verification design | Scenarios, examples and claims about what a skill or check proves: each names the boundary observed and the evidence, and distinguishes a walkthrough from an exercised run | [Match each claim to an observable boundary](skills/verification/verification-design/SKILL.md#match-each-claim-to-an-observable-boundary) |
| Clear writing | All prose, including descriptions, templates and examples | [Check the result](skills/authoring/clear-writing/SKILL.md#check-the-result), plus [instruction guidance](skills/authoring/clear-writing/references/instructions.md) for instructions |
| Diagrams and tables | Each diagram and table, and passages that would explain better as one | [Semantic review](skills/authoring/diagrams-and-tables/references/review.md) and [visual verification](skills/authoring/diagrams-and-tables/references/verification.md) |
| Documentation | Links resolve, including anchors and links outside the package; each statement has one current owner; historical text is labelled as such | Check each link's target and anchor; compare current and historical passages |
| Routing quality | Entry points, triggers and conditional references | [Routing trial method](#routing-trial-method) |
| Application design | Application designs and runtime helpers produced by a skill, when present | [Check behavior at the owning boundary](skills/design/application-design/SKILL.md#check-behavior-at-the-owning-boundary) |
| Other skills in this repository | Helpers and tests, such as Python scripts and their suites | Select from the catalog by trigger |

A skill gaining a rule owner adds a row here in the same change.

For each finding, record the rule, the file, the concrete consequence and its
disposition: fixed, or an explicit exception stating its reason, scope, who
accepted it and the condition for reviewing it again. The reviewer proposes an
exception; the repository owner accepts it. When the package cannot follow one
of its own rules, report that against the rule or the package rather than
exempting it silently. Wording changed during the review needs an independent
comparison of each changed passage with the prior text before release.

Record with the release — in the annotated tag or the change that tags it — the
commit reviewed and whether the reviewer had a fresh context; whether the
evidence is an informed review, a walkthrough or an independent acceptance trial
under the routing trial method's isolation rules; the rules applied and the files
each covered; findings with dispositions and exceptions with review conditions;
and checks that could not run, separately from checks that passed. The skill is
ready to tag when the mechanical checks pass, the routing trials meet the
[routing acceptance requirement](#routing-quality), and every material finding is
fixed or covered by an accepted exception.

### Authoring skills

Skills in this repository should meet the standards they teach. Apply relevant
guidance to the packages, helpers and documentation we maintain here. Start
with the named package when one is known; use the catalog to select additional
guidance from the task's actual trigger. Load only needed references. For example,
use single-source-of-truth when reconciling copied rules, verification-design when
selecting evidence. Report a relevant conflict or gap rather than silently
exempting the repository.

During authoring, AGENTS.md requires writing and visual guidance where relevant.
A skill that bundles scripts, templates or an extension declaration needs the
whole-package [release review](#release-review) before tagging, which already
applies both skills below. Before tagging any other release, also apply them to
the content changed since the skill's last tag, or to the whole package for a
first release:

- [Clear writing](skills/authoring/clear-writing/SKILL.md), to the prose.
- [Diagrams and tables](skills/authoring/diagrams-and-tables/SKILL.md), to existing
  diagrams and tables and to passages a diagram or table would explain better.

This changed-content pass is a recommendation, not a release requirement.
Clear Writing does not yet cover every kind of prose a skill package contains,
such as trigger descriptions, defined terms, worked examples, pattern catalogs
and templates.

When this pass rewrites wording, have a reviewer without the author's rationale
compare each changed passage with the prior text, as release review requires for
the packages it covers: the first Clear Writing sweep found four meaning changes
that way, now kept as regression cases in that skill's scenarios. Note which
skills were applied in the change's record; "no change needed" is a valid
result.

## Adding a skill

This repository owns reusable technical and authoring methods. Project setup,
process and coordination belong to the consuming project, as do its decisions,
priorities, responsibilities, requirements, local procedures and evidence. A
skill here supplies the method; the consuming project supplies its defaults.

- Keep it project-agnostic: no account details, credentials, service
  identifiers or private domain records, and no names of the projects that
  consume these skills. A skill about one project's systems
  does not belong here. Skills about Jonas himself, such as his email style,
  live in his separate local `personal-skills` repository.
- Make no claim about a consumer. A package states a need; where the consumer
  satisfies it is the installer's to decide. So a package names no path,
  filename, document home, command name or instruction wording in a consuming
  project, and ships no code a consumer imports or executes — only the interface
  contract such code is bound by. Guidance selected by a command or artifact in
  front of the reader belongs here; an outcome a project's own work must meet
  belongs to the consuming project. The consuming project states the same
  division in its own words, from its side; fix an
  overreaching package here rather than letting a consumer document the
  deviation. The retirements of `containerization` and `repository-services`
  record what this costs when it is noticed late.
- Put the manifest at `skills/<area>/<name>/SKILL.md`; choose the existing area
  whose task it serves. Keep skill names unique. Put every resource the skill
  needs inside its directory.
- Choose a short lowercase hyphenated name for the activity or subject readers
  will seek. Use familiar terms and the actual language or tool when it narrows
  the scope. Preserve an established name unless clearer discovery justifies
  changing consumer paths.
- Use the [authoring skills](#authoring-skills) while writing the package.
- Add `scenarios/README.md` when the skill has scope boundaries worth testing,
  `tests/` when it ships behavior a check can own (see
  [where a package keeps its checks](#where-a-package-keeps-its-checks)), and a
  row to the catalog table above.

## Origins

Attribution for material that came from elsewhere, and the moves and
retirements a consumer upgrading from an older pin needs to know. Git history
holds the rest.

### Attribution

- **bash-patterns**, **test-audit**, **diagrams-and-tables** (then named
  `diagrams`) and the durable-check material in **source-of-truth** were
  imported on 29 September 2026 from the owner's Forge Agent Kit at
  `c98147a115a30f36b952df5faf1c869b54480c59`, from its `shell-patterns`,
  `test-audit`, `diagrams` and `selfcheck-guard` skills. Prose was revised,
  sibling-skill links became descriptions of the boundary, and citations of that
  kit's project policy were replaced with statements in place or deferred to the
  reading project's own policy.
- **python-patterns** and **python-design** drew their topic selection from
  Everything Claude Code's Python patterns at
  `c70874fae9eb0e5ad0365beb7e2955899fd1d30f` (MIT, copyright 2026 Affaan
  Mustafa) and the tooling boundary from Trail of Bits' modern-python plugin at
  `82fe8226252622fa807643bdca1710901198553a` (CC-BY-SA-4.0). No prose, examples,
  hooks or code were reused; neither upstream is tracked automatically.
- **bash-patterns** 0.2.0 assessed topics from wshobson/agents
  bash-defensive-patterns at `156b7a5e7a8b93642628a339ee4039c925b34c7f` (MIT,
  copyright 2024 Seth Hobson); its prose and examples are independently
  authored.
- **diagrams-and-tables** consulted Mermaid's official documentation, OWASP's
  system-modeling scope and OMG BPMN 2.0.2 for notation boundaries; its examples
  keep real shapes and counts from the owner's projects with synthetic names.
- **postgres-design**, **source-of-truth**, **node-patterns**,
  **verification-design**, **test-writing** and the
  Docker packages were written from reviews of the owner's own projects. The
  packages carry no project schema names, identifiers, paths or credentials.

### Moves and retirements

| Former package | Date | Where it is now |
| --- | --- | --- |
| runtime-operations 4.0.0 | 23 October 2026 | Retired by the Owner's decision: it described one framework's credential tiers and controller helpers. `f34f731` is the last commit that ships it; existing pins retain it. |
| project-design 0.2.0, project-contracts 0.2.0 | 22 October 2026 | repository-design owns repository boundaries, external discovery and handoff contracts; application-design owns internal operations. Broad conceptual-model and provider-selection tutorials are outside the replacement scope. Existing pins retain the former packages. |
| service-boundaries 0.5.0 | 22 October 2026 | service-design owns service interfaces, identity, storage custody and evidence matched to the task. Existing pins retain the former package. |
| project-planning 0.1.0, project-bootstrap 0.5.0, pattern-capture 0.3.1, project-policy 0.4.0 | 12 October 2026 | project-bootstrap, since retired; `183148d34dd1434df0402a0c6e69b195da84a525` is the last commit here that ships them |
| work-records 1.0.0 | 12 October 2026 | project-bootstrap; `e2e0ed4` is the last commit here that ships it |
| typescript-patterns 2.0.3, typescript-design 1.0.3 | 13 October 2026 | Retired by the Owner's decision; `605cded` is the last commit that ships them, with the shared-contract check that compared their module-syntax copies and the TypeScript example check |
| containerization 1.1.0 | 9 October 2026 | CLI usage split into docker-cli and docker-compose-cli; PostgreSQL and verification material to database-migrations and verification-design; convention-shaped outcomes, including one service image for API, migration and seed commands, to the consuming project |
| repository-services 0.3.1 | 9 October 2026 | Judgment kept as service-classes 0.1.0; the `services/` home, document shapes, reserved actions, dispatcher and validator to the consuming project |
| project-docs | 4 October 2026 | [project-foundation](https://github.com/jonasferagen/project-foundation) |
| change-workflow | 3 October 2026 | Retired; Git worktree operations, verification, document maintenance and reporting conventions belong to the consuming project |
| shared-code-design | 2 October 2026 | Retired; its distribution-boundary criteria are not carried by another package |
| jonas-email-style | 30 September 2026 | The owner's local `personal-skills` repository, installed for his user account |

Installed copies keep working at their pinned commits. A consumer upgrading from
containerization or repository-services adopts the successor packages and moves
the convention-shaped outcomes into the project itself.

### Current maintenance notes

- The Docker packages duplicate four shared rules under reciprocal copy records
  rather than linking, because each must work alone; the borrowed-definition
  rule is triggered in docker-compose-cli and fixed with a docker-cli bind.
