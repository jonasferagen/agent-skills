# Types And Generics

## Name And Type Cohesion

When a variable or parameter is an instance of a project-owned type, use the
type name as the default name in `camelCase`.

Examples:

- `billingPeriod: BillingPeriod`
- `gridCoordinate: GridCoordinate`
- `localeResolver: LocaleResolver`

Rename when the local role carries meaning the type cannot: `from`/`to`,
`current`/`previous`, `source`/`target`, or `fallback`/`primary`.

Third-party types are exempt because the project does not own their vocabulary:
`layoutGroup: Group` is clearer than `group: Group` when a vendor group plays a
domain role.

If many call sites use the same non-matching name for a project-owned type, the
type may be misnamed or a missing wrapper/domain concept may be hiding there.
The review-time diagnostic lives in
[review heuristics](review-heuristics.md#name-vs-type-cohesion).

## Generic Types And Methods

Use type parameters when the code preserves a real relationship between types.
Generics are not a style goal on their own; they are how a class or method says
"the output is tied to this input", "this key selects this payload", or "this
registry keeps the caller's item type intact".

## Rules

- Reach for a generic when a method returns the same shape it receives, maps a
  key to a typed value, wraps a caller-supplied item type, or keeps a parser /
  resolver result precise without casts.
- Name the type parameter after its domain role when it has one. `TEventMap`,
  `TPart`, or `TNode` is more useful than a bare `T` once the type parameter
  has a role.
- Prefer explicit domain primitives and methods when the concept is fixed.
  `GridCoordinate`, bounded quantities, and numeric invariant guards usually read
  better as named domain behavior than as generic tuple or record machinery.
- Do not introduce a generic framework for a one-site helper. Wait until the
  same type relationship appears in a second caller, then extract it to the
  owning domain module. See
  [Utility Extraction](utilities-and-data.md#utility-extraction).
- Avoid generic pipeline classes or registries for fixed workflows; a flat
  named sequence is clearer unless the step list is dynamic.

## Good Signals

- An event name determines the event payload.
- A registry, collection, or cache is independent of the stored item type.
- A helper should preserve a narrowed object or option shape supplied by the
  caller.
- Repeated parsing or validation code returns the caller's requested contract
  and otherwise forces `as` casts at every call site.

## Smells

- The type parameter appears only once in the signature.
- The generic hides a domain concept that already has a named primitive.
- The implementation still branches on every concrete case; the generic only
  moved the complexity behind a type parameter.
- The call site must provide an explicit `<T>` because inference cannot see the
  relationship. That can be valid at module boundaries, but it deserves a
  second look.
