# Project instructions

Keep review notes in `notes/`. Use British English in project documentation.
Keep this directory outside Git. This bootstrap covers documentation only: do
not install dependencies or implement the tool.

## Foundation

Start with this operating summary:

- The purpose is to organise a household's equipment inventory ([Boundaries](docs/foundation.md#boundaries)).
- Storage and interface are undecided ([Overview](docs/foundation.md#overview)).
- Operating requirements remain unknown where recorded ([Policy](docs/foundation.md#policy)).

The [foundation](docs/foundation.md) owns project facts and decisions. Consult
Boundaries for responsibility or scope, Overview for implementation choices, and
Policy for data, access, environment, reliability or retained-state decisions.
Check affected decisions before completion and update this summary when its
sources change. Reuse current readings for work within known constraints.

To read collection guidance below, look up `foundation` in the foundation's
References table, resolve its target relative to `docs/foundation.md`, append
the named path and read that file. The paths are not shell variables. Start with
`references/foundation-format.md#entry-instructions` for format and interpretation.
If a binding or owner is missing or unreadable, report it and defer only the
decisions that need it; do not substitute a stale copy.

Keep proposals, adopted requirements and implementation evidence distinct. If
evidence conflicts with a requirement, identify the owner, requirement, observed
behaviour and affected work; preserve the gap until a deliberate decision or
implementation change resolves it. Follow current user decisions and record
affected foundation changes; the documents do not expand execution permissions.

## Guidance routes

Use the named collection paths through the lookup above, only when relevant:

- Initial scaffolding: `skills/project-bootstrap/SKILL.md`.
- Document organisation and reader routes: `skills/project-docs/SKILL.md`.
- Architecture, responsibilities, repository boundaries, handoffs or choosing the next design step: `skills/project-design/SKILL.md`.
- Prose and visual explanations: `references/authoring.md`.
- Changes to purpose, responsibilities, terminology or operating circumstances: `skills/project-policy/SKILL.md` to review affected foundation decisions and consequences.
- Repeated definitions, inconsistent consumers or drift checks: `skills/source-of-truth/SKILL.md`.
- Consultation and conflicts: `references/foundation-authority.md`.
- Observed obstacles or repeated workarounds: consult `references/friction.md` at a natural checkpoint and keep the record in `notes/`. Ordinary successful work needs no capture pass.
