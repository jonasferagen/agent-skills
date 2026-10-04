# Type review heuristics

Diagnostic prompts to apply when reviewing code — your own work in progress, or
a colleague's. None of these are enforced rules; they are questions worth
asking when the relevant signal shows up. Their value is in the violations they
surface, not in following them mechanically.

This package supplies the prompts, not a review workflow. When the task is to
review a tree, branch, pull request, or diff, follow the repository's review
workflow and use these prompts inside it.

If a prompt fires repeatedly across the codebase, the underlying pattern may
be stable enough to belong in the focused pattern docs. Some entries
below already cross-reference a constructive form there.

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

**Only one shape can be safe, and only under the compiler settings its row
names**; two shapes fail open:

| Shape | When a new variant is added | Verdict |
| --- | --- | --- |
| Returns a value on every path, **and** no `default` | TS2366 under `strictNullChecks` when the declared return type excludes `undefined`; TS7030 under `noImplicitReturns`, declared or inferred | Safe under those settings; leave it alone |
| `void` function, such as a bucketing loop, an `update()` body or a dispatcher | Nothing is forced, so the variant silently matches no case | Fails open, though it looks harmless |
| Permissive `default` | The `default` defeats the return-type protection, even in a function that returns a real value | Fails open |

A permissive `default` is why "it returns something, it must be fine" is wrong.
Check for the `default`, not just the return type.

Keep broad fallbacks for open runtime inputs: external JSON, URL params,
third-party values, or intentionally forward-compatible wire data.


## Fail-Open Mirror

A list, set, or record that must stay in step with a union or schema declared
elsewhere, where forgetting an entry is silent rather than a build failure.

**Diagnostic:** the change adds a member to a union, a key to a schema, or an
entry to a table — and somewhere else there is a second declaration over the
same vocabulary that the change did _not_ touch. Ask what happens to a member
that is present in one and absent from the other. If the answer is "it is
silently not carried / not rendered / not handled", the mirror is fail-open.

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

**Diagnostic:** when a change adds repeated `as`, `as unknown as`, or non-null
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
