# Class Shape

## Contents

- [Classes and managers](#classes-and-managers)
- [Narrative methods and named private steps](#narrative-methods-and-named-private-steps)
- [Promoting a passive type to a class](#promoting-a-passive-type-to-a-class)
- [Sibling families](#sibling-families-a-list-not-a-class-per-instance)
- [Class-owned constants](#class-owned-constants)

## Classes and Managers

Group operations into classes with descriptive PascalCase names.
`TaxResolver.resolveRate()` reads more clearly than an unqualified
`resolveRate()`—the domain and origin of the call are visible at the call
site without tracing imports.

Two shapes, picked by the operation's relationship to state. Neither is
preferred; pick the one that fits.

- **Stateful service**: an instance class with constructor-injected dependencies
  and public instance methods. The instance owns state that persists across
  calls. Example: `RouteIndex`—constructed once from resolved route data, then
  queried repeatedly through `get`, `neighborsOf`, and `reachableFrom`. Callers
  hold a reference for the operation's lifetime.
- **Stateless operations**: a class with `static` methods. No instance and no
  mutable fields. Example: `LocaleResolver.resolve`, `GridCoordinate.toKey`.
  The class exists to name the domain; invocations behave like free functions
  but read as `Domain.operation` at the call site.

A one-shot operation that needs internal scratch state but no externally-held
instance is still a stateful service. Expose it via a `static` factory that
constructs a private instance, runs it, and returns the result. Do not pass that
scratch state through static method parameters.
For example, a `DocumentCompiler.compile()` entry can privately construct one
compiler instance, wire its single-concern collaborators, run it, and return the
result without leaking scratch-state plumbing onto the call site.

Avoid bare `export function` for operations. Wrap them in a class instead,
static-method or stateful, per the two shapes above. **Purity is not an
exemption**: a stateless, side-effect-free operation is still an operation and
gets a static-method class (`PolygonFaces.resolveUp`, `InvoiceTotal.of`), not a
bare `export function`. The naming benefit, a `Domain.operation()` call that is
legible at the call site, applies whether or not the operation holds state. A
pure geometry or math kernel is exactly where the static-class shape justifies
its cost. Do not use `export const X = { method(), method() }` either: that is
a static class spelled oddly, with the same call-site cost and worse tooling
support. The trade-off (no tree-shaking, no direct use as higher-order
functions) is acceptable at typical project scale.

**First, check it should be a standalone operation at all.** A helper that takes
a single domain object and only reads its public surface is not an operation
_over_ that type — it is behavior that belongs _on_ it
([Behavior on the Data](utilities-and-data.md#behavior-on-the-data)). Reach for a
static-method class only once the logic genuinely spans several inputs, or needs
dependencies the type should not own (the companion-op case in
[Promoting A Passive Type](#promoting-a-passive-type-to-a-class)).

**The exceptions are narrow and specific** — everything else is an operation and
gets a class:

- **Value-boundary factories and guards.** A branded-ID constructor/validator
  (`asOrderId`, `asAccountId`) or a type guard over a closed value set is a
  passive value boundary, not a domain operation: it mints or narrows a brand.
  It may stay a bare exported function. When it already has a natural home
  class, prefer a static there (`PaymentKinds.isKnown`) over a standalone
  function.
- **React hooks** — the idiomatic `export function useX(...)` shape.
- **File-private helpers.** The rule governs the _exported_ surface. A
  non-`export` module-local function is implementation detail; leave it a bare
  function, or fold it to `private static` per the single-caller rule below.
- **Data, not operations.** A `const` lookup table, descriptor record, or
  registry map (`PAYMENT_METHODS`) is data, not an operation namespace; see
  [Class-Owned Constants](#class-owned-constants). Reach it through a class
  accessor when it has behaviour to guard (`PaymentMethods.get`); leave it a
  module `const` when it is pure free-standing data.
- **Style/token derivation helpers.** A deterministic token-to-record map
  exported beside the tokens it derives from, in a class-free style module, is
  the parameterized form of the data record rather than a domain operation. It
  may stay a bare exported function so the module remains class-free and keeps
  its camelCase data-module name
  ([naming-and-placement.md](naming-and-placement.md#file-naming)).

When a helper has a single caller, decide between a peer class and
`private static` on the caller by looking at the test surface. A helper with its
own unit tests has independent semantics worth naming at the top level. A
helper with no separate tests is scaffolding for one consumer — fold it as
`private static`.

### Narrative Methods And Named Private Steps

When a method feels branchy, first ask whether the awkwardness comes from the
method hiding distinct domain steps, an existing helper with a misleading name,
or a helper signature that exposes too much machinery. The goal is not "more
helpers"; the goal is for the method to read as the domain story.

Prefer this order:

- Rename an existing helper when it already owns the behavior but the call site
  does not say what decision is being made.
- Narrow or reshape a helper signature when callers pass plumbing values only to
  satisfy the helper.
- Extract a new private helper when the branch represents a real domain decision
  and the helper name can say that decision directly.
- Keep the branch inline when the best helper name would be vague, such as
  `handleAttached` or `doResolve`.

This works well for methods that compute a primary value, resolve
fallback/error cases, update an index/cache/side table, and return the value.
The top-level method should keep the sequence visible; named private steps
should carry the branch policy. Avoid scattering tiny helpers: a helper that
only hides three lines without improving the vocabulary makes the caller harder
to read.
If the method has a full multi-phase workflow rather than one local value story,
use [orchestration.md](orchestration.md) instead.

### Promoting A Passive Type To A Class

Type aliases and interfaces are passive contracts. When callers start adding
normalization, merge, construction, defaulting, derived fields, or "complete
enough to become X" checks around a type, name that behavior on a class instead
of scattering conditional object assembly at call sites.

Prefer promoting the shape itself to a class when it is runtime domain data that
travels through the system with invariants or cached derived values. Keep a
separate input/interface shape only for construction, wire DTOs, or truly
passive contracts.

Use a companion operation class when the behavior crosses multiple concepts,
belongs to a conversion boundary rather than to the data itself, or would force
the primary value module to import dependencies it should not own.
Serialization, persistence, platform APIs, and heavyweight runtime adapters are
good companion candidates when the primary type should stay small and
dependency-light. Name the companion after the operation it owns, keep it in
the owning domain, and expose thin forwarding methods from the primary class
only when those methods are the intended public API.

[naming-and-placement.md](naming-and-placement.md) covers the file shape that
follows from these rules: primary export per file, filename parity, and where
the promoted types live.

### Why Classes Over Bare Functions

`LocaleResolver.resolve()` communicates the domain at the call site without
forcing the reader to trace an import. The same naming idiom works for stateful
and stateless modules, so consumers do not have to learn a different shape per
file.

## Sibling Families: A List, Not A Class Per Instance

When several modules turn out structurally identical, with the same methods and
shape and differing only in fixed data, that repetition is the signal to
collapse them into one class. The class holds the family as a list, and its
`private static` factory methods supply the shared behavior. Each member becomes
a `static readonly` descriptor built from a factory; the data that varies (a
path, a schema, a key) is the only thing spelled out per entry.

This is easy to miss at the start, which is why it is worth naming. The first
one or two siblings each look like they deserve their own class — their own
type, their own filename, their own method bodies — so the per-instance shape
gets set before the duplication is visible. The shared shape becomes visible
only when the third and fourth copies repeat the same structure. Treat "this
new file is the last one with X's name swapped for Y's" as the trigger to stop
and extract a factory plus a list instead of adding another copy.

For example, one `ExportFormats` registry can own a format family, with
descriptors built by `delimited`, `fixedWidth`, and `binary` factories — each
member a `static readonly` descriptor spelling out only the data that varies,
such as an extension and an encoder. Bespoke formats stay hand-written only
when their shape is genuinely different.

Two clarifications keep this inside the [class rules](#classes-and-managers):

- The _registry_ is a static class and the factories are `private static`
  operations on it — not bare functions.
- The _members_ are typed value descriptors (data records such as an
  `extension` plus an `encode`) held in a list. That is data, and is distinct
  from the discouraged
  `export const X = { method() }`, which spells a module's _operation namespace_
  as an object. A module of operations should still be a class.

Keep a sibling hand-written when its shape is genuinely different, such as a
bespoke header layout or looser encoder. Do not bend the factory around one
odd case.

## Class-Owned Constants

When a fixed value is clearly part of a class's own behavior or defaults,
prefer placing it on the class as a `static readonly` field instead of leaving
it as a file-level `const`.

### Rules

- Use `private static readonly` for internal thresholds and defaults that only
  the class should consume. When a repository has a live configuration or
  tuning surface for a value, keep that product-specific mechanism in its local
  guidance and let the class-owned constant supply the default only when the
  local contract says so.
- Use `public static readonly` only when other modules intentionally depend on
  the value as a shared invariant.
- Keep values at module scope when they are better understood as free-standing
  data for the whole file, such as parser field sets, lookup tables, regexes,
  or test fixtures.
- Avoid turning computed runtime values into class constants just for
  consistency; values derived from environment state can stay as local helpers
  or constructor-time calculations.

### Why

- The value has a natural home, so readers know which class owns it.
- Call sites communicate intent better when shared invariants are named off the
  owning class.
- Internal defaults stay grouped with the implementation they tune instead of
  reading like anonymous file globals.
