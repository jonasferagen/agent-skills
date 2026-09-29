# Domain Primitives

When a package owns a well-defined primitive for a domain concept, consumers
use it instead of introducing a parallel helper, inline equivalent, or shadow
structure. A primitive can be a value type such as `GridCoordinate`,
`DateRange`, or `Money`, or a stateful service such as `RouteIndex`.

Missing behavior becomes a named method, static operation, lookup table, or
sibling type on the primitive. Missing variants become additions to its module.
The primitive is the vocabulary; consumers speak it.

This is the front-door rule that [Behavior On The
Data](utilities-and-data.md#behavior-on-the-data) and [Utility
Extraction](utilities-and-data.md#utility-extraction) refine. Before deciding
where new behavior goes, ask whether an existing primitive already owns it.

## Rules

- Before adding a helper over a domain concept, find its existing primitive. If
  the behavior is general to that value, add it there.
- A fresh coordinate literal, direction union, currency string, date tuple, or
  offset table outside the owning package is a smell. Consume or extend the
  named primitive.
- Derive a value object's stable key through its instance method, such as
  `coordinate.toKey()`, rather than tearing it into fields for a static helper.
- Keep lookup tables beside the vocabulary they enumerate. A consumer-specific
  table stays with the consumer only when its policy is not intrinsic to the
  primitive.
- Refine a primitive in its owning package. Do not fork a local copy for
  ergonomics; if the primitive genuinely should not grow, name the consumer-side
  helper after the consumer concern.

## Vocabulary-Backed Value Names

Name value classes after the domain concept they embody, not after the
mechanical constraint enforcing it. `GridCoordinate` is better than
`IntegerPosition`; `EmailAddress` is better than `ValidatedString`.

When a passive vocabulary has a value-class counterpart, keep their nouns
aligned. If the value class admits sentinel state outside the vocabulary, the
domain name is no longer honest: model absence separately or choose a broader
name. Do not add an absence sentinel to the vocabulary merely to avoid
`undefined` or a decisive result type.

For precedence and absence choices, see [resolution and
defaults](resolution.md).

## Value-Equality Keys

JavaScript `Map` and `Set` key objects by identity. A collection keyed by a
value object's value therefore needs a stable primitive-owned key. Keep that key
inside the collection owner.

- Prefer `coordinate.toKey()` over
  `GridCoordinate.toKey(coordinate.x, coordinate.y)`. A static overload is for
  loose values at a boundary, not for deconstructing an existing value object.
- Stringify at the innermost collection boundary. Do not expose
  `Map<string, T>` when callers conceptually query by `GridCoordinate`; expose
  `valueAt(coordinate)` or return grouped value objects.
- A repeated `map.get(value.toKey())!` at call sites is the tell that the
  internal key leaked through a signature.

## Why

- Reuse compounds the primitive's value: more callers share invariants and
  tests instead of splitting fixes across parallel helpers.
- Call sites read in the domain vocabulary.
- Contributors find one canonical answer rather than competing equivalents.

## When Not To Use

- The helper needs consumer-specific context or policy the primitive should not
  see.
- The shapes resemble one another mechanically but represent different domain
  concepts.
- The behavior is a trivial one-site expression with no reusable invariant.

## Testability

A primitive must be testable in isolation. Construct it and assert its behavior
without booting the surrounding system or relying on ambient mutable state.

- If it requires a heavy collaborator, add a truthful port or document the two
  as one composite primitive.
- If it reads time, randomness, environment, or global state, inject that source
  through a callback or options object.
- Keep the primitive's contract tests beside its owner according to the
  repository's own testing conventions.
