# Next session

A consistency sweep of this repository is the pending work. Ten skills exist and
six of them arrived or changed on 2026-09-29, so conventions that used to be
implicit now have enough instances to disagree with each other. Expect two or
three passes; the first one decides the question the others depend on.

Read [README](README.md) first for what a skill is here, how one is installed,
and the release rules.

## First move: decide whether a shared reference can exist

Everything else in the list is smaller, and several items resolve differently
depending on this answer.

The README says a skill directory is the installable unit, copied whole into a
consuming repository. That makes a rule needed by two skills unhomeable: a
relative path like `../../other-skill/references/x.md` breaks the moment one
skill is installed without the other, so the only alternative is to state the
rule twice.

It is already stated twice. The shrink-only ledger rule and the report-only
drift-stamp anti-pattern are in both
[test-audit/references/triage.md](skills/test-audit/references/triage.md) and
[concept-homes/references/durable-checks.md](skills/concept-homes/references/durable-checks.md).
That is `concept-homes` violated by the repository that ships `concept-homes`,
and it was a deliberate choice both times rather than an oversight.

Options worth weighing, none free:

- **Accept the copies** and say so in the README, with a rule that a duplicated
  passage names the other home in a comment so a later edit finds its sibling.
- **A shared reference directory** that the install procedure copies alongside any
  skill that declares a dependency on it. This changes the install contract, so
  the README's "Using a skill" section and every consumer's `UPSTREAM.md` shape
  change with it.
- **Let one skill own it** and have the other describe the boundary in prose
  without a link, which is the pattern already used for neighbouring passes
  (see the locked decisions below). Cheapest, and it loses the detail.

Do not start renaming or splitting until this is settled — the answer decides
whether a split creates a shared page or another copy.

## Sweep list

Evidence gathered 2026-09-29; re-derive it rather than trusting these counts if
much time has passed.

**Manifest consistency.** `my-email-style` has no `metadata.version` field at all
and no `validation/my-email-style.md`; every other skill has both. Three
descriptions are unquoted (`my-email-style`, `project-docs`, `runtime-operations`)
where seven are quoted — YAML tolerates both, so decide whether it matters and
then be uniform.

**Versions ahead of their newest tag.** `project-docs` and `runtime-operations`
declare 1.1.0 against a `v1.0.0` tag; `concept-homes` declares 1.1.0 and has never
been tagged. Four skills sit at 0.1.0, untagged, which the README explicitly
permits for an unreleased skill. Decide which of the 1.1.0s are releases to tag
and which are pending, because the README states the tagged package and manifest
version must agree.

**No LICENSE and no `license:` fields.** The upstream kit this repository draws
from has both, and every skill here is meant to be copied into other
repositories. Its absence was noticed and deliberately not decided.

**Package shape.** `runtime-operations` is the only skill shipping `scripts/` and
`tests/` rather than prose and `references/`. That is justified by what it does,
but the README describes no such shape, so a reader cannot tell whether shipping
code is a general option or a one-off.

**Manifest-versus-reference balance.** `SKILL.md` runs from 80 to 317 lines and
reference counts from 0 to 13. There is no stated rule for what earns a place in
the manifest rather than a reference page, and the two extremes were written
under different assumptions.

**Naming.** Four shapes are in use: `<technology>-<activity>`
(`postgres-design`, `typescript-patterns`, `shell-patterns`), `<subject>-<noun>`
(`project-docs`, `concept-homes`, `runtime-operations`, `test-audit`,
`change-landing`), a bare plural (`diagrams`), and a possessive
(`my-email-style`). Renaming a skill breaks consumers' pins, so treat this as a
rule for new names unless a rename earns its cost.

**`project-docs` and `diagrams` overlap.** Both changed on 2026-09-29 when
`diagrams` became top-level and `project-docs` was reduced to what is particular
to a documentation set. The split was made in one pass and has not been reread
with fresh eyes.

**Unrendered Mermaid.** The 38 fenced blocks in
[diagrams/references/worked-examples.md](skills/diagrams/references/worked-examples.md)
were verified by reading, not by rendering, and their schema vocabulary was
renamed after import. Rendering them is a contained job and the only way to know
the rename left them valid.

## Locked decisions

Do not re-open these without a reason; they were each settled deliberately.

- **A skill directory is the installable unit.** No cross-package relative paths.
  There are currently none; nothing enforces it.
- **Neighbouring passes are described in prose, not named.** Where an upstream
  skill handed off to a sibling, the extraction states the boundary instead, so
  the package degrades gracefully when installed alone.
- **Project-agnostic means no private identifiers.** The README's "Adding a skill"
  section is the rule. Imports have had repository names, commit SHAs and schema
  vocabularies replaced.
- **Upstream policy citations are redirected, never carried.** The kit's project
  policy opens by declaring nothing is in production; both consuming projects are,
  and each has its own `docs/project-policy.md`. A citation either states its rule
  in place or defers to the reading project.
- **`diagrams` is top-level** because form choice applies to plans, issue bodies,
  design records and review feedback, not only documentation.
- **The durable-check material was folded into `concept-homes`**, not made its own
  skill, because that skill already ended at a check and never said what keeps one
  working.
- **`change-landing` is prepared, not adopted.** Whether a project authors in
  worktrees is that project's policy. It is registered in no consuming project and
  says in its own text that it describes a discipline a project opts into.
- **Upstream `handoff` was read and left out** of `change-landing`: orienting work
  that has not started is the opposite of reporting work that finished.

## Gotchas

**The upstream kit is not vendored here.** Six skills were imported from
`ferraforge/agent-kit` pinned at `c98147a115a30f36b952df5faf1c869b54480c59`, dated
2026-09-18. Clone it fresh if the sweep needs to compare; any working copy from
the importing session is gone.

**Upstream is older than most of the local extractions.** Where the two disagree,
the local version is usually the newer thinking. Do not treat upstream as
authoritative by default.

**One consuming project now trails this repository.** Personal Atlas's
`docs/change-workflow.md` is its own reduced extraction of the same upstream
material, and `change-landing` carries a newer hand-back rule: a field empty by
construction is omitted, while one that could have carried content reports `none`,
and terms-searched is owed only when the diff shows a rename or a delete. Atlas
asks for all of it unconditionally. Reconciling that is a change in Atlas, not
here, and it is not part of this sweep.
