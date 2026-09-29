# Skills

Jonas's reusable, project-agnostic agent skills. Each skill is one directory
under `skills/` with a `SKILL.md` manifest; that directory is the installable
unit.

| Skill | Use it for |
| --- | --- |
| [project-docs](skills/project-docs/SKILL.md) | Establishing, reviewing or reconciling repository documentation: glossaries, ownership, diagrams and project instructions. |
| [my-email-style](skills/my-email-style/SKILL.md) | Drafting, rewriting or shortening email that Jonas will send, in Norwegian or English, so it sounds like him. |
| [typescript-patterns](skills/typescript-patterns/SKILL.md) | Shaping TypeScript as it is authored or refactored: naming, types, class shape, dependency ports, orchestration, imports and tests. |

Drafts that are not skills yet live in `docs/`, starting with
[prose styles](docs/prose-styles.md).

## Using a skill

For a repository-local import, copy the complete skill directory (for example
`skills/project-docs/`) to the target's `.agents/skills/<name>/` through its
normal review process. Record this repository URL and the exact source commit
in the target's provenance notes. On updates, review the diff and preserve any
documented local adaptations. Keep target-specific instructions outside the
imported directory where practical.

Nothing here installs a skill globally or into another project; each adoption
is its own step.

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

**typescript-patterns** is a verbatim import of the `typescript-patterns` skill
from the MIT-licensed [Forge Agent Kit](https://github.com/ferraforge/agent-kit),
taken on 2026-09-29 at commit `c98147a115a30f36b952df5faf1c869b54480c59`. Unlike
the skills above it is not originally authored here, so its upstream
[LICENSE](skills/typescript-patterns/LICENSE) travels inside the skill
directory and must stay with any copy. Two local adaptations make it standalone:
that license file, and one reference in `references/testing.md` that upstream
links to its sibling `test-audit` skill, reduced to plain text. The manifest
also defers to `code-review`, `code-audit`, `test-audit` and `selfcheck-guard`,
which live in the kit and are not packaged here; those deferrals read as named
upstream skills rather than links. Re-import by replacing the directory at a
newly chosen commit, then reapply both adaptations and record the new commit.

**my-email-style** was derived on 2026-09-20 from Jonas's sent Gmail: the last
100 messages before 2026-09-18 (about 55 with real prose) plus 17 older English
messages. It moved here from the Personal project's shared files on 2026-09-24.
Re-derive it from a fresh sample if his style drifts; the manifest says how the
corpus was chosen.
