# Skills

Jonas's reusable, project-agnostic agent skills. Each skill is one directory
under `skills/` with a `SKILL.md` manifest; that directory is the installable
unit.

| Skill | Use it for |
| --- | --- |
| [runtime-operations](skills/runtime-operations/SKILL.md) | Credential tiers, local service controls and a shared encrypted PostgreSQL backup mechanism. |
| [postgres-design](skills/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, automatic timestamps and integrity boundaries. |
| [project-docs](skills/project-docs/SKILL.md) | Establishing, reviewing or reconciling repository documentation: glossaries, ownership, diagrams and project instructions. |
| [my-email-style](skills/my-email-style/SKILL.md) | Drafting, rewriting or shortening email that Jonas will send, in Norwegian or English, so it sounds like him. |
| [typescript-patterns](skills/typescript-patterns/SKILL.md) | Shaping TypeScript as it is authored or refactored: naming, types, class shape, dependency ports, orchestration, imports and enforcement. |

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

**my-email-style** was derived on 2026-09-20 from Jonas's sent Gmail: the last
100 messages before 2026-09-18 (about 55 with real prose) plus 17 older English
messages. It moved here from the Personal project's shared files on 2026-09-24.
Re-derive it from a fresh sample if his style drifts; the manifest says how the
corpus was chosen.

**runtime-operations** supplies the common credential, Linux service and encrypted
backup machinery used by Personal Atlas and Work-system. Project adapters own
vault IDs, roles, schema scope and access checks. The package includes offline
helper tests; consumer adapters also exercise actual disposable restores.
See [validation scenarios](validation/runtime-operations.md).
