# Foundation format and interpretation

Use this reference when reading, creating or changing a foundation. Ordinary
consultation does not require activating project-policy. Use that skill when
operating facts, obligations or their consequences change.

## Fixed document shape

The [template](../templates/docs/foundation.md) defines the format: `# Foundation`,
a `Date: YYYY-MM-DD · Revision: N` line, then References, Inheritance, Boundaries,
Overview and Policy in that order. Each section has exactly one table with the
template's column names. Keep empty tables as their header and separator only.
Do not add prose, comments, YAML, instructions, extra headings or extra tables.
Store project-specific facts in rows; link detailed owners or exception records
from cells. Procedures, skill routes, interpretation rules and evidence belong
in project instructions, the collection or their existing document owners.

References and Inheritance are declarations. Boundaries defines purpose, scope
and responsibility; Overview records technical choices and open options; Policy
records operating facts and adopted constraints. Use the same columns for owners
and members. Members retain only local differences in the three fact tables.
Use `Unknown` for an unresolved value and `None` for an established absence;
remove unused inherited rows rather than filling them with unknowns. Row names
are unique within a table; scope distinct cases in their row names or values.

The format applies to new foundations and requested migrations. Existing separate
document homes remain valid until deliberately migrated; do not reformat a project
just to answer a question. The [format checker](../scripts/validate-foundation.py)
checks files using this format against the template. It does not assess truth,
resolve references, infer permissions or establish implementation compliance.

## References

Each References row binds one key to one external root. Keys use lowercase letters,
digits, underscores or hyphens, beginning with a letter. Targets are literal paths
or canonical repository-content URLs. A reference grants no policy authority by
itself. This uses the existing [source-of-truth lookup rule](../skills/source-of-truth/references/definitions.md#choose-the-home-that-decides).

Read `$key/suffix` by taking that file's declared key and appending the suffix.
Resolve relative roots against the declaring foundation's directory, never the
shell's current directory. Values are not shell variables; do not execute them.
Keep symbolic paths in inline code; ordinary Markdown links do not expand them.
Machine consumers need a real resolver or generated concrete values.

Resolve each parent's references in its own foundation, without importing the
child's bindings. A reference must have a binding before it can be used. Report
missing bindings or unreadable targets and defer only decisions needing them;
do not substitute a stale copy. Project instructions own environment access and
revision selection, including main-checkout versus snapshot choices. URL roots
must identify accessible content; do not assume a repository landing page is a
raw file directory. Snapshots need a revision and update mechanism.

## Inheritance

Each Inheritance row names one of Boundaries, Overview or Policy and the authority
for that section, including its anchor. For example, the Policy authority may be
`$orchard/docs/foundation.md#policy`. Rows may select different owners. An absent
row means that section has no parent; an empty Inheritance table means all three
sections are locally owned. Do not infer an authority from the References table.

Read the selected section before relying on inherited decisions. Follow further
inheritance in the owning foundation's context. Detect cycles by the resolved
foundation and section together: two sections may legitimately share one file.
Stop the affected chain on a cycle and report it; unrelated work can continue.

Within the declared subject and scope:

- An omitted fact row inherits from its section's parent. Without a parent it is
  unknown. An empty local fact table inherits the whole selected section.
- A present unknown stays unresolved for that local fact; do not fill it from the
  parent. Unknown readiness or implementation details cannot waive shared obligations.
- Local facts add detail. Delegated implementation choices remain within shared
  constraints; a shared owner's own stack or packaging applies only to its scope.
- Conflicting local text is not automatically an exception. An adopted exception
  links a decision identifying the shared rule, affected scope, replacement,
  reason, decision authority and review or expiry condition.

Use [foundation authority](foundation-authority.md) for consultation and conflicts,
and [project-policy](../skills/project-policy/SKILL.md) for changed obligations and
their consequences. Follow existing user authorization; do not invent approvals.

## Entry instructions

Bootstrap gives AGENTS a concrete relative link to the local foundation and a
route to this reference. For a shared installation, AGENTS must include the
minimal lookup instruction needed to reach it: read the named References row,
append the guidance path, then read that file. Keep the external root only in
References. Do not require the foundation to explain this procedure or require
loading project-policy to resolve a reference.

Keep missing-owner behavior locally readable in AGENTS, since the shared guidance
may itself be unavailable. Put working-agreement and skill routes in AGENTS or
its linked instruction owner, not in the foundation tables. Reuse current readings;
ordinary edits within known constraints need no full guidance reread.
