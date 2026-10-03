# One project across repositories

A repository boundary does not necessarily define a separate project. Before
bootstrapping, establish whether this is an independent project, the shared
foundation owner, or a member of an existing project. Preserve an existing choice.

## Shared owners and local facts

Each repository starts at its local foundation, normally `docs/foundation.md`,
with Boundaries, Overview and Policy sections. Shared owners and independent
projects record their decisions there. Members declare the parent and retain
only local facts, implementation choices and adopted exceptions in the same three
tables. A section with no local differences keeps its table header and says so;
do not copy shared rows to fill it. Honor established homes when no move is requested.

Keep project-wide decisions in the selected authoritative repository. Detailed
role assignments and handoffs can remain in an existing architecture owner linked
from boundaries. Internal design and commands belong to the implementing
repository's architecture and procedures. Plans, evidence and status retain their
own homes. Scope shared technical choices explicitly; a coordinator's own stack
or packaging is not automatically a choice for its members.

## Bind the external owner once

Use an existing project settings owner when one exists; otherwise declare each
external root once in the local foundation. This applies the
[source-of-truth lookup rule](../skills/source-of-truth/references/definitions.md#choose-the-home-that-decides).
For example, a member could declare:

```yaml
references:
  orchard: /workspaces/orchard
inherits: $orchard/docs/foundation.md
```

Here `$orchard` is a documentation reference, not a shell environment variable.
Resolve its value from the declaring repository's foundation, then append the
suffix. An absolute filesystem root or canonical repository-content URL may be
used. Resolve a relative root against the file declaring it, never the shell's
current directory; check it from actual task worktrees before adopting it.
URL roots must identify an accessible content base and revision policy. Do not
assume a repository landing page can be read as a raw file directory.

Use references as inline code, such as `$orchard/docs/foundation.md#policy`;
ordinary Markdown links do not expand variables. Put concrete relative links to
the local foundation in README and AGENTS, and have instructions explain how to
resolve its named routes before following them. Keep missing-owner handling
locally readable. Imported documents resolve their own references in their own
scope; do not carry the child's binding into a parent or infer extra parents.
Detect a repeated foundation in the parent chain and report the cycle.

Each independently usable repository owns its binding. A workspace may own the
binding instead when an existing registry is accessible to every consumer.
Changing the declared binding relocates every symbolic route in that repository.
Machine consumers need a real resolver or generated concrete values checked
against that binding; these Markdown declarations provide neither.

## Inherit within scope

`inherits` declares the default parent for all three matching sections. An explicit
section source may select an established owner instead. Read the selected owner
before relying on an inherited value; follow its reference scope and revision
policy. Apply these rules by subject and stated scope:

- An omitted local row inherits the shared decision. With no parent, omission is
  unknown. Neither omission nor an empty section waives a rule.
- A present unknown or blank cell stays unresolved for that local fact; do not
  fill it from the parent. Unknown implementation details do not suspend shared
  constraints or waive a known obligation.
- A local fact adds detail. An implementation choice can be made locally where
  the shared owner delegates it, within the inherited constraints.
- A conflicting statement is not automatically an override. An adopted exception
  identifies the shared rule, affected scope, replacement, reason, decision
  authority and review or expiry condition. Link its decision record from the row.

Use project-policy for changed circumstances, adopted policy changes and conflicts,
including consequences in other repositories. Follow existing user authorization;
do not invent an approval step or adopt an exception by proximity. Missing or
conflicting authority blocks only decisions that depend on resolving it.

## Collection and access

Document ownership and skill distribution are separate choices. One complete
collection in the shared owner can serve members with access. Route through the
named root to that installation and keep provenance with it. Separate pinned
installations are valid when independent checkout or execution requires them;
they must not create competing project decision owners.

Declare whether consumers read the shared main checkout or a selected snapshot.
Do not silently substitute another task's unlanded work or a stale copy. A snapshot
needs its revision and update mechanism recorded. If authority is unavailable,
report the missing dependency and defer decisions needing it. Preserve unrelated
authorized work. Record access from main checkouts, task worktrees and relevant
execution environments; untested environments stay explicit gaps.

## Reconcile and verify

Compare values before removing copies and preserve unique facts in their owners.
Repair active README and agent routes; retain dated evidence as history.
Verify that a shared change reaches members, a local choice leaves other members
unchanged, an explicit unknown remains visible, and conflicting or unavailable
authority cannot silently authorize work. Test changing only the binding in an
isolated copy and following its routes from main and actual nested worktrees.
Check section anchors as well as files. Report what was exercised and what was
only reviewed; bootstrap establishes documents and routes, not automatic runtime
inheritance or proof of compliance.
