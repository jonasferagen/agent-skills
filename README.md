# Jonas’s agent skills

Jonas's reusable, project-agnostic agent skills. Each skill is one directory
under `skills/` with a `SKILL.md` manifest; that directory is the installable
unit.

## Project foundations

Use these independent skills together when bootstrapping a project or revisiting
its engineering expectations. Their display names describe their jobs; the
installation names stay stable.

| Display name / skill | Responsibility |
| --- | --- |
| [Project policy](skills/project-policy/SKILL.md) (`project-policy`) | Establish which requirements apply from users, data, exposure, lifetime, compatibility and recovery needs; assess changes to those requirements. |
| [Project documentation](skills/project-docs/SKILL.md) (`project-docs`) | Decide where knowledge belongs and keep it current. |
| [Diagrams and tables](skills/diagrams/SKILL.md) (`diagrams`) | Choose and verify useful visual explanations of relationships and comparisons. |
| [Clear writing](skills/clear-writing/SKILL.md) (`clear-writing`) | Express facts and instructions clearly without changing their meaning. |
| [Authoritative definitions](skills/source-of-truth/SKILL.md) (`source-of-truth`) | Give each rule a home and derive or check its other appearances. |

Start with the project's existing decisions. Establish a project-owned policy
using the policy skill's template when useful, then apply the other skills where
their subjects arise. This is a recommended set, not a dependency chain or an
automatic installer. Each package works alone; a small project may need only a
short policy and README. Existing projects keep their established document homes.

The project policy owns requirements; procedures and evidence live in their
existing guides and records. Every policy change receives an impact assessment.
Stricter requirements can create substantial downstream work, tracked with owners
and acceptance evidence before the changed use is considered ready. This starts
as a manual review; automation can grow from actual transitions.

## Code and design

| Skill | Use it for |
| --- | --- |
| [typescript-patterns](skills/typescript-patterns/SKILL.md) | Shaping TypeScript: naming, types, classes, dependency ports, imports and directory layout. |
| [bash-patterns](skills/bash-patterns/SKILL.md) | Preserving command failures and query results in Bash checks, pipelines, captures and process substitutions. |
| [node-patterns](skills/node-patterns/SKILL.md) | Preserving child-process outcomes, exit status and output in Node scripts, command-line tools and test harnesses. |
| [postgres-design](skills/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, timestamps and integrity boundaries. |

## Changes and operations

| Skill | Use it for |
| --- | --- |
| [change-workflow](skills/change-workflow/SKILL.md) | Taking a change from an isolated worktree through synchronization, verification, merge and cleanup. |
| [containerization](skills/containerization/SKILL.md) | Building independent local service containers with explicit interfaces, repeatable migrations and disposable database tests. |
| [test-audit](skills/test-audit/SKILL.md) | Auditing a settled test suite for brittleness, coverage asymmetry, weak assertions, mock drift and non-determinism. |
| [runtime-operations](skills/runtime-operations/SKILL.md) | Credential handling, local service controls, child processes and encrypted PostgreSQL backups. |

These groups organize the catalog. Packages remain directly under `skills/`, so
changing a group does not change a skill's installation path.

## Using a skill

Copy the complete skill directory from a selected source commit into the target
repository's `.agents/skills/<name>/` through its normal review process. Record
source URL, source directory, full commit SHA, and any selected release version
and tag in the target's `.agents/skills/UPSTREAM.md`. The SHA is the authoritative
pin. Imported files should match that commit; keep project-specific rules outside
the imported directory and document any necessary local modifications in the
provenance file.

Each package must work when installed alone. Keep links and required resources
inside its directory. If two skills both need a short rule, repeat it in each
package and add a source comment in both places naming the other copy, so edits
find both. A shared directory would change the installation unit and is not part
of this repository's package format.

The entrypoint carries the purpose, essential constraints and links to details.
Put mode-specific procedures and longer examples in `references/` and link them
where they become useful; a short skill can stay in one file. A skill can bundle
`scripts/` when repeated operations need a reliable implementation and `tests/`
when those helpers need offline verification. The entire directory, including
those resources, is installed together.

Run `python3 scripts/validate-packages.py` after editing a package. It checks
frontmatter, local link targets and package containment; behavioral scenarios in
`validation/` and any bundled helper tests still need their own review.

Updates are deliberate: select a release, review its changes and local exceptions,
replace the complete directory, compare it with the source, validate the manifest
and links, then update provenance in the same commit. No automatic tracking of
`main`, global installation or database deployment is implied by an import.

## Skill releases

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

Skills in this repository should meet the standards they teach. Before tagging
a release, apply these skills to the content that changed since the skill's
last tag, or to the whole package for a first release:

- [Clear writing](skills/clear-writing/SKILL.md), to the prose.
- [Diagrams and tables](skills/diagrams/SKILL.md), to existing diagrams and
  tables and to passages a diagram or table would explain better.

This is a recommendation, not a release requirement. Clear Writing does not yet
cover every kind of prose a skill package contains, such as trigger
descriptions, defined terms, worked examples, pattern catalogs and templates.

When you apply them, record on the skill's validation page which skills were
applied and what they changed; "no change needed" is a valid result. When a pass
rewrites wording, an independent comparison of each changed passage with the
prior text is recommended: the first Clear Writing sweep found four meaning
changes that way. These skills guide authors; installed packages remain
independent of them.

## Adding a skill

- Keep it project-agnostic: no account details, credentials, service
  identifiers or private domain records. A skill about one project's systems
  does not belong here. Skills about Jonas himself, such as his email style,
  live in his separate local `personal-skills` repository.
- Put the manifest at `skills/<name>/SKILL.md`, with references and helper
  files beside it. `agents/openai.yaml` carries the display name for tools that
  read it.
- Choose a short lowercase hyphenated name for the activity or subject readers
  will seek. Use familiar terms and the actual language or tool when it narrows
  the scope. Preserve an established name unless clearer discovery justifies
  changing consumer paths.
- Use the [authoring skills](#authoring-skills) while writing the package.
- Record intended behaviour in `validation/<name>.md` when a skill has scope
  boundaries worth testing, and add a row to the table above.

## Origins

**clear-writing** brings the short-text guidance into a reusable prose skill,
with a shared core and separate references for instructions and short text.
It covers wording and meaning; document ownership belongs to `project-docs` and
visual form to `diagrams`. Jonas's email voice has its own skill outside this
repository.
Its first prose trials are the conceptual `source-of-truth` skill and the
procedural `bash-patterns` skill; a later sweep revised eight more packages. See
[validation scenarios and results](validation/clear-writing.md).

**postgres-design** was extracted from Personal Atlas's database conventions on
2026-09-29 and compared with work-system's migrations and data model. The
installable package uses synthetic examples and contains no project schema names,
service identifiers, vocabulary inventories or deployment policy. Work-system
contributed guidance on provenance versus identity, explicit conditions, atomic
commands and retries. Atlas credits the owner's Forge database conventions as an
earlier influence. See [validation and alignment](validation/postgres-design.md)
for pinned sources, adoption differences and review limits.

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
restructure. The bar and its seven questions now sit in the manifest at that rung,
and the five properties behind it, each with the shape that breaks it and the
shape that holds, are in its `references/durable-checks.md`: compute the invariant
live instead of re-blessing a golden, anchor to the check's own location or to
version control, read the manifest rather than copying it, fabricate the fixture,
and report an absent dependency as absent rather than as a failing test. Forge
Project Policy citations were redirected as in test-audit — two carried substance
now stated in place, and whether a check earns its recurring cost defers to the
reading project's own policy.

**change-workflow** merges the owner's Forge Agent Kit `worktree` and `reconcile`
skills, imported on 2026-09-29 and pinned at
`c98147a115a30f36b952df5faf1c869b54480c59`. It covers one change's whole path: a
worktree before the first write, keeping current by merge, the finishing pass a
rename or deletion owes, what counts as evidence about the tree that will actually
merge, cleanup against a containment count, and the hand-back that reports it. The
upstream packages were coupled to the owner's Forge fleet, and that coupling was
removed rather than softened — the landing-door contract and its operations
scripts, the lane lock and claim protocol, the container model in which the
integration lane is what the container runs from, and the fleet-shaped
authorization matrix. Seven Forge Project Policy citations were redirected: four
carried substance now stated in place, and three defer to the reading project's own
policy. Upstream's licence to treat undeclared state as disposable was inverted
rather than imported, because that policy opens by declaring nothing is in
production while both consumers are. Three divergences against Personal Atlas's own
newer reduced extraction of the same skills were settled deliberately, the sharpest
being the hand-back rule that a field empty by construction is omitted while one
that could have carried content reports `none`. Upstream's `handoff` skill was read
and left out: orienting work that has not started is the opposite of reporting work
that finished. **This is a discipline a project opts into**, which the skill says in
its own text; whether a project authors in worktrees is that project's policy
decision, and it is registered in no consuming project. Example requests: "Use
$change-workflow to open a lane for this fix", "Use $change-workflow — this branch is
green, what does landing it still owe?" See
[validation and alignment](validation/change-workflow.md).

**diagrams** merges the owner's Forge Agent Kit `diagrams` skill, at
`c98147a115a30f36b952df5faf1c869b54480c59`, with the diagram conventions that
`project-docs` had been carrying. Upstream supplied form choice, the
underused-tables argument, draw-less-link-more, vertical-and-one-altitude, the
drawing reference and ten worked examples; the local reference supplied two
sections upstream lacked — grounding every edge in whatever owns it, and verifying
that a diagram reads in the renderer and themes its readers use, where a
successful parse is explicitly not a readability check. It is a top-level skill
because form choice applies to plans, issue bodies, design records and review
feedback, not only to documentation.

`project-docs` was reduced in the same change to what is particular to a
documentation set — which document owns which view, glossary-led terms, and
freshness as part of doc review — so the craft has one home instead of two that
drift. Three provenance citations naming a private repository and its commits were
replaced with neutral descriptions, and one worked example's schema vocabulary was
renamed, so the package carries no project identifiers while keeping the real
shapes and counts the examples depend on. Example requests: "Use $diagrams to
decide whether this section wants a diagram or a table", "Use $diagrams to split
this overview before it gets any wider." See
[validation and alignment](validation/diagrams.md).

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
pipeline before I trust its exit code." See
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

**typescript-patterns** is Jonas's TypeScript pattern canon, brought into this
repository on 2026-09-29. It covers the shape of the code itself: naming and
placement, types and generics, class shape, domain primitives, dependency ports,
orchestration, resolution and defaults, imports and barrels, directory layout
and enforcement — a manifest plus thirteen reference pages, with a symptom table
routing from the smell at the call site to the narrowest page. Testing is
deliberately out of scope: test layout, fixtures and coverage policy belong to
the reading repository, and rules phrased around tests stay only where they are
really about design shape, such as the port-versus-cast decision in
`dependency-ports.md`. The package is self-contained — every relative link and
heading anchor resolves inside it, and it defers to the reading repository's own
instructions rather than to companion skills. Example requests: "Use
$typescript-patterns to name this module and its exports", "Use
$typescript-patterns — this constructor takes six positional arguments." See
[its validation scenarios](validation/typescript-patterns.md).

**source-of-truth** was extracted on 2026-09-29 from a duplication audit of
Personal Atlas: six parallel searches over validation rules, domain vocabularies,
logic expressed in more than one medium, configuration constants, types and
shapes, and documentation, with every candidate independently challenged before
acceptance. Its subject is the seam between media — a concept authored in a
schema, a setting or a document and restated in application code, another
language or prose, where no single search finds both sides and the restatement
falls behind silently. It deliberately excludes code shape, which belongs to
[typescript-patterns](skills/typescript-patterns/SKILL.md), and schema design,
which belongs to [postgres-design](skills/postgres-design/SKILL.md). The
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
