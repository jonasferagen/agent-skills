# Jonas’s agent skills

Jonas's reusable, project-agnostic agent skills. Standalone packages live under
`skills/<category>/<name>/`. Related skills and shared resources can instead form
one installable collection under `collections/<name>/`.

[Decision log](DECISIONS.md) records structural decisions and ideas for follow-up.

[Data foundations](docs/data-foundations.md) proposes the skills for the next
database-modeling stage; it is not an installed collection yet.

Categories group skills by their main task. A collection is an installation unit;
its individual skills remain task entry points loaded when needed.

## Projects

Part of the [project-foundation collection](collections/project-foundation/COLLECTION.md).

| Skill | Use it for |
| --- | --- |
| [Project bootstrap](collections/project-foundation/skills/project-bootstrap/SKILL.md) (`project-bootstrap`, draft) | Start a repository and establish boundaries, policy and overview, with an entry README. |
| [Project design](collections/project-foundation/skills/project-design/SKILL.md) (`project-design`, draft) | Shape responsibilities, workflows, handoffs and integration choices; select the next useful step. |
| [Git worktrees](collections/project-foundation/skills/git-worktrees/SKILL.md) (`git-worktrees`) | Use task worktrees for repository edits, with exceptions owned by repository policy. |
| [Project policy](collections/project-foundation/skills/project-policy/SKILL.md) (`project-policy`) | Establish which requirements apply from users, data, exposure, lifetime, compatibility and recovery needs; assess changes to those requirements. |
| [Project documentation](collections/project-foundation/skills/project-docs/SKILL.md) (`project-docs`) | Decide where knowledge belongs and keep it current. |
| [Authoritative definitions](collections/project-foundation/skills/source-of-truth/SKILL.md) (`source-of-truth`) | Give each rule a home and derive or check its other appearances. |

Project bootstrap establishes `docs/foundation.md` with five fixed tables:
References, Inheritance, Boundaries, Overview and Policy. The file holds data only.
The collection owns interpretation and project instructions own workflow routes.
Members bind their shared owner once and retain only local differences. Project-policy interprets
those facts and reviews their consequences when circumstances change. The
collection supplies the authoring guidance; the templates are not standalone manuals. Existing
projects keep their established document homes.

The foundation uses task worktrees for edits in Git repositories unless local
instructions explicitly opt out, for example for a deliberately single-agent
project. Work outside Git proceeds directly. Bootstrap places this default and
the Git skill route in project instructions; existing installations receive it
when their collection and instruction hook are deliberately updated.

The policy section holds only concise operating facts and adopted decisions by axis.
Project-policy interprets it alongside boundaries; downstream requirements,
working rules, impact assessments and evidence live in their own documents.
Every policy change receives an impact assessment.
Stricter requirements can create substantial downstream work, tracked with owners
and acceptance evidence before the changed use is considered ready. This starts
as a manual review; automation can grow from actual transitions.

## Authoring

Included in the project-foundation collection and available for other authoring tasks.

| Skill | Use it for |
| --- | --- |
| [Clear writing](collections/project-foundation/skills/clear-writing/SKILL.md) (`clear-writing`) | Express facts and instructions clearly without changing their meaning. |
| [Diagrams and tables](collections/project-foundation/skills/diagrams-and-tables/SKILL.md) (`diagrams-and-tables`) | Choose and verify useful visual explanations of relationships and comparisons. |

## Design

Source directory: `skills/design/`.

| Skill | Use it for |
| --- | --- |
| [service-boundaries](skills/design/service-boundaries/SKILL.md) | Define service ownership and shared behavior across HTTP and MCP adapters. |
| [relational-modeling](skills/design/relational-modeling/SKILL.md) (draft) | Structure known entities around retrieval questions and revise relationships through synthetic scenarios. |
| [postgres-design](skills/design/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, timestamps and integrity boundaries, and transactions on pooled connections. |

## Verification

Source directory: `skills/verification/`.

| Skill | Use it for |
| --- | --- |
| [verification-design](skills/verification/verification-design/SKILL.md) | Choose evidence for a change or milestone and consolidate checks by the failures they detect. |
| [test-writing](skills/verification/test-writing/SKILL.md) | Writing unit tests, integration tests and their fixtures, with made-up data and state each test owns. |
| [test-audit](skills/verification/test-audit/SKILL.md) | Auditing a settled test suite for brittleness, coverage asymmetry, weak assertions, mock drift and non-determinism. |

## Operations

Source directory: `skills/operations/`.

| Skill | Use it for |
| --- | --- |
| [containerization](skills/operations/containerization/SKILL.md) | Build service images, configure local stacks and manage isolated container test resources. |
| [database-migrations](skills/operations/database-migrations/SKILL.md) | Preserve migration history, review baselines and verify database bootstrap and upgrades. |
| [runtime-operations](skills/operations/runtime-operations/SKILL.md) | Credential handling, local service controls, child processes and encrypted PostgreSQL backups. |

## Workflow

Source directory: `skills/workflow/`.

| Skill | Use it for |
| --- | --- |
| [pattern-capture](skills/workflow/pattern-capture/SKILL.md) | Decide whether an engineering discovery generalizes and improve its existing skill home when authorized. |

## Languages and runtimes

Source directory: `skills/languages/`.

| Skill | Use it for |
| --- | --- |
| [typescript-patterns](skills/languages/typescript-patterns/SKILL.md) | TypeScript types, narrowing, generics, absence, module syntax and enforcement. |
| [typescript-design](skills/languages/typescript-design/SKILL.md) | Class-based TypeScript house style: operations, naming, ownership, ports, barrels and directory layout. |
| [python-patterns](skills/languages/python-patterns/SKILL.md) | Python types, runtime boundaries, defaults, exceptions, resource cleanup and async tasks. |
| [python-design](skills/languages/python-design/SKILL.md) | Class-based Python house style: operations, domain values, dependency protocols, naming and modules. |
| [bash-patterns](skills/languages/bash-patterns/SKILL.md) | Preserving arguments, command failures, query results and cleanup ownership in Bash scripts. |
| [node-patterns](skills/languages/node-patterns/SKILL.md) | Preserving child-process outcomes, exit status and output in Node scripts, command-line tools and test harnesses. |

Install each standalone package by its existing name, for example
`skills/languages/python-patterns/` to `.agents/skills/python-patterns/`.
Names, invocation examples and release tags are unchanged by source grouping.
Existing imports retain their pinned source paths; use the new path when importing
a revision after the move.

## Using a skill

Copy the complete skill directory from a selected source commit into the target
repository's `.agents/skills/<name>/` through its normal review process. Record
source URL, source directory, full commit SHA, and any selected release version
and tag in the target's `.agents/skills/UPSTREAM.md`. The SHA is the authoritative
pin. Imported files should match that commit; keep project-specific rules outside
the imported directory and document any necessary local modifications in the
provenance file.

For project-foundation, copy the complete
[collection](collections/project-foundation/COLLECTION.md) with its relative layout
intact. Its installation instructions define provenance and project routing.
For one project spanning repositories, use the collection's
[multi-repository guidance](collections/project-foundation/references/multi-repository.md)
to choose shared owners and local facts. One accessible installation can serve
members; independent installations remain an explicit distribution choice.

Collection members may link to each other and shared references or templates.
Standalone packages keep required resources inside their own directory. Links
must stay inside the applicable installation unit; do not duplicate guidance just
to make each collection entry point independently installable.

The entrypoint carries the purpose, essential constraints and links to details.
Put mode-specific procedures and longer examples in `references/` and link them
where they become useful; a short skill can stay in one file. A skill can bundle
`scripts/` when repeated operations need a reliable implementation and `tests/`
when those helpers need offline verification. The entire directory, including
those resources, is installed together.

Run `python3 scripts/validate-packages.py` after editing a package. It checks
frontmatter, local link targets and installation-unit containment; behavioral scenarios in
`validation/` and any bundled helper tests still need their own review.

Updates are deliberate: select a release, review its changes and local exceptions,
replace the complete directory, compare it with the source, validate the manifest
and links, then update provenance in the same commit. No automatic tracking of
`main`, global installation or database deployment is implied by an import.

## Discovery and lesson capture

### Routing quality

A consumer must be able to find the relevant guidance without reading this
authoring repository's maintenance material. Additional reading must follow a
concrete task need, and required deeper guidance must remain reachable. Apply this
standard to our own catalog, instructions and collections as well as their output.

Routing is an acceptance requirement when changing triggers, entrypoints, shared
guidance or packaging, and before releasing a collection. Run proportionate
practical trials using the [routing trial method](validation/discovery.md#routing-trial-method).
Preserve task constraints and check missed obligations as well as unnecessary
reading. Package validation alone cannot establish routing quality.

Do not set a universal word budget. Compare equivalent tasks and explain which
reads were unnecessary. Record remaining gaps; do not claim the requirement is
verified from word-count reductions alone. Ordinary prose edits need no new trial
unless they change routing or reveal concrete friction.

When authoring here, use the catalog and maintenance sections relevant to the
change. When consuming an installed collection, use its entrypoint and project
routes. Do not follow provenance back to this README unless the task needs source
maintenance, upgrade information or investigation of a concrete source issue.

### Selection and capture

Skill descriptions name the task or observed symptom that should select the
package. Keep them concise and put the main trigger first. The selected
`SKILL.md` supplies essential guidance and routes to conditional references;
open only the references needed for the current decision. Grouping this catalog
does not itself control which instructions an agent reads.

When installing `pattern-capture`, the consuming project's instructions can add
this checkpoint:

> Before finishing an architecture or consolidation review that produced concrete
> findings, use pattern-capture to assess the strongest reusable candidate against
> existing guidance. Do the same after a fix or user correction exposes a recurring
> design issue. Find the authoring source in imported-skill provenance and read
> only the catalog and likely owner. Report its home or why it stays local.
> Routine lookups and literal edits do not need this checkpoint.

Also route to pattern-capture when skill use reveals repeated friction, an
undocumented workaround or a correction that suggests missing guidance. Keep
this trigger in project or personal instructions so it is available before the
skill body is loaded. Load pattern-capture when the trigger applies; ordinary
successful skill use needs no capture pass.

Use a local link to the installed skill in that instruction. Put the source
location in provenance; never bake a machine-specific path into the skill.
Reading and proposing guidance can fit a review. Writing the source repository
or adopting a new pin follows the task's actual authorization.

For explicit requests, invoke `$pattern-capture` with an idea or refer to the
current discussion. To also accept `/pattern-capture [idea]`, add this project
instruction beside the checkpoint:

> Treat `/pattern-capture [idea]` as an explicit request to use the installed
> pattern-capture skill, even for a small idea. Assess whether it generalizes,
> prefer the simplest adequate rule and check its existing home. Follow the
> request's scope when proposing or making changes.

This is an agent-interpreted text shortcut. It does not add a native slash-menu
entry; native skill discovery depends on the client's supported invocation and
refresh behavior.

Test discovery with realistic requests and metadata before showing skill bodies
or expected answers. Record whether a trial used host-provided metadata, a
supplied metadata catalog, or a project hook. Check a nearby request that should
not activate the skill as well. A successful package check alone says nothing
about selection. See [the discovery review](validation/discovery.md).

## Skill releases

Collections are currently pinned as a whole by source commit. Their member
versions describe changed skill behavior; individual member tags do not establish
a compatible collection release. No collection release has been published.

Version each skill independently. Its `SKILL.md` declares a string under
`metadata.version`, such as `"1.0.0"`. Publish an annotated Git tag named
`<skill-name>/v<version>` on the committed release; never move a published tag.
The tagged package and manifest version must agree. Unreleased skills can remain
pinned by commit until their first release.

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

Validate the package and its behavioral scenarios before tagging, and see the
[authoring skills](#authoring-skills) recommended for releases. A release must
contain no unfinished scaffold or project-specific credentials or identifiers.
Consumers pin the full commit as well as the release label because tags are
names, not an integrity guarantee. Other skills in the repository need no
version bump when one skill is released.

### Authoring skills

Skills in this repository should meet the standards they teach. Apply relevant
guidance to the packages, helpers and documentation we maintain here. Start
with the named package when one is known; use the catalog to select additional
guidance from the task's actual trigger. Load only needed references. For example,
use source-of-truth when reconciling copied
rules, verification-design when selecting evidence, and pattern-capture when
assessing a reusable finding or an explicit capture request. Its simplicity
test also applies to our own rules and exceptions. Report a relevant conflict
or gap rather than silently exempting the repository.

During authoring, AGENTS.md requires writing and visual guidance where relevant.
Before tagging a release, also apply these skills to the content changed since the skill's
last tag, or to the whole package for a first release:

- [Clear writing](collections/project-foundation/skills/clear-writing/SKILL.md), to the prose.
- [Diagrams and tables](collections/project-foundation/skills/diagrams-and-tables/SKILL.md), to existing
  diagrams and tables and to passages a diagram or table would explain better.

This additional release pass is a recommendation, not a release requirement. Clear Writing does not yet
cover every kind of prose a skill package contains, such as trigger
descriptions, defined terms, worked examples, pattern catalogs and templates.

When you apply them, record on the skill's validation page which skills were
applied and what they changed; "no change needed" is a valid result. When a pass
rewrites wording, an independent comparison of each changed passage with the
prior text is recommended: the first Clear Writing sweep found four meaning
changes that way. Project-foundation includes these skills as dependencies. Other standalone
packages use them as authoring guidance without acquiring that dependency.

## Adding a skill

- Keep it project-agnostic: no account details, credentials, service
  identifiers or private domain records. A skill about one project's systems
  does not belong here. Skills about Jonas himself, such as his email style,
  live in his separate local `personal-skills` repository.
- Put standalone manifests at `skills/<category>/<name>/SKILL.md` and collection
  members at `collections/<collection>/skills/<name>/SKILL.md`. Keep skill names
  unique across both layouts. Put shared resources inside their collection.
  `agents/openai.yaml` carries the display name for tools that
  read it.
- Choose a short lowercase hyphenated name for the activity or subject readers
  will seek. Use familiar terms and the actual language or tool when it narrows
  the scope. Preserve an established name unless clearer discovery justifies
  changing consumer paths.
- Use the [authoring skills](#authoring-skills) while writing the package.
- Record intended behaviour in `validation/<name>.md` when a skill has scope
  boundaries worth testing, and add a row to the table above.

## Origins

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

Historical note: **shared-code-design** is now retired; see the
[decision log](DECISIONS.md).

**verification-design** and **shared-code-design** capture two architecture
decisions exposed by a review of the local Atlas/Work proof of concept in
2026-09. The former separates evidence at schema, domain, independent-session,
public-interface and built-artifact boundaries while looking for repeated setup.
The latter compares checked copies with generation and versioned dependencies
against the promise that each component builds independently. The installable
skills use language-neutral examples and impose no project test matrix or
package manager. See their [verification scenarios](validation/verification-design.md)
and [shared-code scenarios](validation/shared-code-design.md).

**containerization** 0.3.0 adds reuse of one service image for API, migration
and seed commands when their runtime files are the same. This came from the same
review; it does not prescribe a container tool or image cache. See
[validation](validation/containerization.md).

**test-audit** 0.3.0 narrows its integration-test advice to the failure each
test can observe. Native contention, real permissions and built-artifact checks
remain distinct evidence even when they call the same domain operation. Its
full-suite rule now applies to complete coverage and timing claims; a static
audit need not run the suite. See [validation](validation/test-audit.md).

**clear-writing** brings the short-text guidance into a reusable prose skill,
with a shared core and separate references for instructions and short text. It
covers wording and meaning; document ownership belongs to `project-docs` and
visual form to `diagrams-and-tables`. Jonas's email voice has its own skill
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

**project-docs** was developed from a documentation review and cleanup in
Personal on 2026-09-19. The reusable guidance is newly written, and the worked
example is synthetic. The source project credited Forge Agent Kit and Diátaxis
as earlier influences; the package contains no copied upstream skill files. It
supports establishing a documentation set, reviewing an existing one, and
reconciling it after changes, and adapts to the project's existing layout
rather than prescribing a stack, access model, merge policy or folder tree.
Example requests: "Use $project-docs to establish documentation for this
repository", "Use $project-docs to reconcile the docs after this release." See
[its validation scenarios](validation/project-docs.md); it still needs
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
