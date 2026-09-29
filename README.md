# Skills

Jonas's reusable, project-agnostic agent skills. Each skill is one directory
under `skills/` with a `SKILL.md` manifest; that directory is the installable
unit.

| Skill | Use it for |
| --- | --- |
| [runtime-operations](skills/runtime-operations/SKILL.md) | Credential tiers, local service controls, child processes and arguments, and a shared encrypted PostgreSQL backup mechanism. |
| [shell-patterns](skills/shell-patterns/SKILL.md) | Preserving command failures and query results in Bash checks, pipelines, captures and process substitutions. |
| [test-audit](skills/test-audit/SKILL.md) | Auditing a settled test suite for brittleness, coverage asymmetry, weak assertions, mock drift and non-determinism. |
| [diagrams](skills/diagrams/SKILL.md) | Choosing the smallest useful diagram, table or matrix, drawing it so it reads, and grounding every edge in its source. |
| [postgres-design](skills/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, automatic timestamps and integrity boundaries. |
| [project-docs](skills/project-docs/SKILL.md) | Establishing, reviewing or reconciling repository documentation: glossaries, ownership, diagrams and project instructions. |
| [my-email-style](skills/my-email-style/SKILL.md) | Drafting, rewriting or shortening email that Jonas will send, in Norwegian or English, so it sounds like him. |
| [typescript-patterns](skills/typescript-patterns/SKILL.md) | Shaping TypeScript as it is authored or refactored: naming, types, class shape, dependency ports, orchestration, imports and enforcement. |
| [concept-homes](skills/concept-homes/SKILL.md) | Deciding which medium owns a concept, and keeping every other appearance of it derived from that home or loudly checked against it. |

Drafts that are not skills yet live in `docs/`, starting with
[prose styles](docs/prose-styles.md).

## Using a skill

Copy the complete skill directory from a selected release commit into the target
repository's `.agents/skills/<name>/` through its normal review process. Record
source URL, source directory, release version, tag and full commit SHA in the
target's `.agents/skills/UPSTREAM.md`. The SHA is the authoritative pin. Imported
files should match that commit; keep project-specific rules outside the imported
directory and document any necessary local modifications in the provenance file.

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

Use semantic versions for the skill's behavioral contract: its scope, required
behavior, defaults, exceptions and bundled resource interfaces.

- **Patch:** clarify or correct wording without changing intended requirements.
- **Minor:** add compatible guidance or capabilities within the existing contract.
- **Major:** change defaults, mandatory rules, scope or exceptions in a way that
  requires consumers to review their adoption.

Validate the package and its behavioral scenarios before tagging. A release must
contain no unfinished scaffold or project-specific credentials or identifiers.
Consumers pin the full commit as well as the release label because tags are names,
not an integrity guarantee. Other skills in the repository need no version bump
when one skill is released.

## Adding a skill

- Keep it project-agnostic: no account details, credentials, service
  identifiers or private domain records. A skill about Jonas himself (such as
  his writing style) is fine; a skill about one project's systems is not.
- Put the manifest at `skills/<name>/SKILL.md`, with references and helper
  files beside it. `agents/openai.yaml` carries the display name for tools that
  read it.
- Record intended behaviour in `validation/<name>.md` when a skill has scope
  boundaries worth testing, and add a row to the table above.

## Origins

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

**shell-patterns** was imported from the owner's Forge Agent Kit on 2026-09-29,
pinned at `c98147a115a30f36b952df5faf1c869b54480c59`. The upstream package
referenced no Forge systems, trackers or policy, so its guidance is unchanged and
the adaptation is only the manifest and a paragraph naming what local docs decide.
It distinguishes a successful match, a successful absence and a failed
acquisition, and covers the defects that blur them: a `local` declaration
reporting its own status, an early pipeline reader turning a match into a SIGPIPE
failure under `pipefail`, and a process substitution whose producer status nobody
collects. Example requests: "Use $shell-patterns to check whether this backup
script's checks can pass when they should fail", "Use $shell-patterns on this
pipeline before I trust its exit code." See
[validation and alignment](validation/shell-patterns.md).

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

**concept-homes** was extracted on 2026-09-29 from a duplication audit of
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
requests: "Use $concept-homes — this vocabulary is defined in the schema and
again in the reader", "Use $concept-homes to decide where this constant belongs."
See [its validation scenarios](validation/concept-homes.md); it has been applied
in one project only and is not yet released.

**my-email-style** was derived on 2026-09-20 from Jonas's sent Gmail: the last
100 messages before 2026-09-18 (about 55 with real prose) plus 17 older English
messages. It moved here from the Personal project's shared files on 2026-09-24.
Re-derive it from a fresh sample if his style drifts; the manifest says how the
corpus was chosen.

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
