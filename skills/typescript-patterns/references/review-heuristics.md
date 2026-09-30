# Review Heuristics

## Contents

- [Name vs type cohesion](#name-vs-type-cohesion)
- [Passive types and bare operations](#passive-type-carrying-behavior)
- [Union and mirror completeness](#disjoint-union-at-the-call-site)
- [Assertion pressure](#type-assertion-pressure)
- [Compatibility and stale references](#compatibility-shims)
- [Shell and family accretion](#accretion-on-a-shell-or-in-file-family)

Diagnostic prompts to apply when reviewing code — your own work in progress, or
a colleague's. None of these are enforced rules; they are questions worth
asking when the relevant signal shows up. Their value is in the violations they
surface, not in following them mechanically.

This is the authoring-time triage sheet: symptoms that should make an author
pause before choosing a constructive pattern. Reviewing a current tree, branch,
pull request, or diff is a separate task with its own workflow.

If a prompt fires repeatedly across the codebase, the underlying pattern may
be stable enough to belong in the focused pattern docs. Some entries
below already cross-reference a constructive form there.

## Name vs Type Cohesion

Default: when a parameter or variable is an instance of a project-owned type,
the name follows the type. See
[Name And Type Cohesion](types-and-generics.md#name-and-type-cohesion).
Renames are allowed and useful when they carry meaning the type cannot
(`target: Player`, `from`/`to`, `current`/`previous`).

**Diagnostic:** when many call sites accept the same project-owned type and _every_ parameter is renamed the same way, ask:

- Is the type misnamed? Maybe the class name should follow what callers naturally write.
- Is a missing wrapper or domain concept hiding here? Callers may all be talking about a higher-level concept that the existing type is only the implementation of.
- Or is the rename genuinely contextual at each site? Then leave it.

Third-party types are exempt: naming a vendor `Group` parameter `layoutGroup`
is descriptive, not divergent—the project does not own `Group`, so there is no
project type to rename in response.

The constructive forms of this rule are
[Parameter Objects](utilities-and-data.md#parameter-objects) for
call-site clarity and
[Parameter Bundling](utilities-and-data.md#parameter-bundling) when
parameters travel together as a unit.

## Passive Type Carrying Behavior

Interfaces, type aliases, and DTOs describe shapes; they should not force every
caller to rediscover how that shape becomes valid domain data.

**Diagnostic:** when a call site builds the same object shape with conditional
spreads, optional-field checks, merge/defaulting logic, derived min/max or
dimension calculations, or "complete enough to become X" tests, ask whether the
type should be a class or value object.

**Action prompt:** classify the shape before suggesting a fix: runtime domain
data, wire DTO, passive boundary contract, or conversion boundary. Runtime
domain data usually wants the class/value-object path described in
[Classes and Managers](class-shape.md#classes-and-managers).
Wire DTOs and passive contracts stay passive, but construction/defaulting
behavior should still have a named owner.

## Bare Function For An Operation

When a module `export function`s a stateless verb-on-data operation (engrave,
resolve, compute, extract, total), it reads as an exemption from the class-shape
rule — but purity is not the test.

**Diagnostic:** an exported bare function that _does_ something to data, and
falls under none of the narrow exceptions
[Classes and Managers](class-shape.md#classes-and-managers) lists, is an
operation in the wrong shape — even a pure geometry/math kernel.

**Action prompt:** an operation is a class, `Domain.operation()`, per that same
section. Flag the exported bare operation and name the owning class.

## Disjoint Union at the Call Site

When a flat union (string-literal union, tagged union) is consumed by a method
that handles only a subset of variants and `default`s on the rest, the union is
being deconstructed at the call site.

**Diagnostic:** when a `switch` on the union value has cases for some variants
and `default: noop` for the rest, and a sibling method has the _inverse_ split,
the union likely conflates two (or more) disjoint sub-domains that should be
separate discriminated unions.

**Action prompt:** name the sub-domains first. If each consumer owns a real
slice, consider splitting into a discriminated union so each consumer
pattern-matches only its sub-domain. The exhaustiveness check then enforces
that every consumer handles every variant of its slice.

## Non-exhaustive Closed Union

Closed project-owned unions should fail loudly when a new variant is added.

**Diagnostic:** when a `switch` or if/else chain claims to handle a full union
but ends in a broad `default`, `return undefined`, or no-op branch, ask whether
the code should use the `never` exhaustiveness pattern from
[Exhaustive Closed Unions](typescript.md#exhaustive-closed-unions).

**Only one shape is already safe**; two shapes fail open:

| Shape | When a new variant is added | Verdict |
| --- | --- | --- |
| Non-`void` return type **and** no `default` | TS2366 fires | Safe; leave it alone |
| `void` function, such as a bucketing loop, an `update()` body or a dispatcher | Nothing is forced, so the variant silently matches no case | Fails open, though it looks harmless |
| Permissive `default` | The `default` defeats the return-type protection, even in a function that returns a real value | Fails open |

A permissive `default` is why "it returns something, it must be fine" is wrong.
Check for the `default`, not just the return type.

Keep broad fallbacks for open runtime inputs: external JSON, URL params,
third-party values, or intentionally forward-compatible wire data.

## Fail-Open Mirror

A list, set, or record that must stay in step with a union or schema declared
elsewhere, where forgetting an entry is silent rather than a build failure.

**Diagnostic:** the diff adds a member to a union, a key to a schema, or an entry
to a table — and somewhere else there is a second declaration over the same
vocabulary that the diff did _not_ touch. Ask what happens to a member that is
present in one and absent from the other. If the answer is "it is silently not
carried / not rendered / not handled", the mirror is fail-open.

**The warning sign is an annotation that looks protective and is not.**
`readonly T[]`, `ReadonlySet<T>`, `Partial<Record<T, …>>`, and
`as Record<T, …>` all compile with a member **missing**: a subset of a `T[]` is
a valid `T[]`. Reviewers read these as forcing every member to be present. They
do not. Only `satisfies Record<Union, …>` is total.

**Action prompt:** invert the mirror per [Fail-Closed
Mirrors](typescript.md#fail-closed-mirrors): derive the union from the table, or
key the table by the union with an explicit opt-out value. Put it beside the
declaration it mirrors, so the compile error appears next to the code the next
author is changing. A mirror that genuinely cannot be made total (the source is
in another repo, or is legitimately open) is fine, but it should _say_ so at the
declaration rather than look like an oversight.

## Type Assertion Pressure

Assertions are sometimes necessary at boundaries, but repeated assertions
usually show where the type model is missing an invariant.

**Diagnostic:** when a diff adds repeated `as`, `as unknown as`, or non-null
assertions, ask which invariant is missing:

- Should an incoming literal use `satisfies` so the compiler checks the shape
  without widening it?
- Should a parser, type guard, value object, or throwing accessor own the
  boundary?
- Is a `Map.get`, array lookup, or lifecycle field proving the same invariant
  in several places?

Use [Assertion Ladder](typescript.md#assertion-ladder) and
[Indexed And Collection Access](typescript.md#indexed-and-collection-access)
as the constructive targets.

Production `as unknown as` should be rare and adjacent to the external API or
declaration hole it bridges. Test doubles can be looser, but they should still
make the boundary obvious.

## Compatibility Shims

Compatibility shims need a named external consumer or guarantee. Without one,
they cost documentation, surface area, and time new contributors spend asking
why they exist. Check the repository's deployed consumers and compatibility
guarantees. When every consumer can change in the same release, update the
surface and its call sites together. Keep a transition only when a named live
consumer or published contract requires it, with a clear removal condition.

**Diagnostic:** when changing a shim, check whether a live consumer still
justifies it. If not, delete it with the old surface.

Example smell: an empty compatibility subclass with no remaining consumers earns
nothing; delete it instead of preserving the old name as a facade.

## Stale Cross-References In Comments

A comment that names another part of the code with an explicit file-path string
(`see client/input/KeyBindings.ts`) goes stale the moment that file moves — no
tool updates it.

**Diagnostic:** when a comment references a symbol by hand-written path instead
of `{@link Symbol}`, flag it. Use the symbol link, which resolves and survives
renames. A path is only acceptable when there is no symbol to target (a config
file, asset, or route). Constructive form:
[Cross-References In Comments](typescript.md#cross-references-in-comments).

## Accretion On A Shell Or In-File Family

Accumulated file state is easy to miss because a large shell is built from many
locally tidy edits. Two visible signs predict that growth reliably.

**Diagnostic:** the change adds the _Nth near-identical sibling_ to a family
inside one file—another panel, handler, or adapter cloned from the previous one.
The second or third sibling is the extraction point: mint the
shared helper per
[Sibling Families](class-shape.md#sibling-families-a-list-not-a-class-per-instance),
and ask whether a family worth a helper is worth its own module.

**Diagnostic:** the diff adds a **field + constructor wiring + a public
method** to a long-lived shell or orchestrator in one change. That trio is a
collaborator being inlined. The feature likely belongs as (or inside) a class
beside the shell, per
[Lifecycle Orchestrators](orchestration.md#lifecycle-orchestrators).
Inline `emitter.on(...)` registrations carrying real behavior in a constructor
are the same smell in event-subscription form, and they tend to skip the
symmetric dispose a named subscription owner would provide.

A repository may use a warn-level file-size check to catch growth these prompts
miss. Treat it as a signal to apply these prompts, not as a limit to get under
by moving lines into an arbitrary helper.
