# Utilities And Data

## Contents

- [Utility extraction](#utility-extraction)
- [Behavior on the data](#behavior-on-the-data)
- [Parameter objects](#parameter-objects)
- [Parameter bundling](#parameter-bundling)
- [Shared defaults](#shared-defaults)

## Utility Extraction

Place generic, reusable operations in shared modules rather than as
private/static methods on the class that happens to use them first.

### Rules

- If a method operates only on its parameters and has no dependency on the
  containing class, it is a candidate for extraction.
- Group utilities by domain, not by the first consumer.
- The extracted operation is still a **class**, not a bare `export function` — a
  static-method (or stateful) class named for its domain, so the call site reads
  as `Domain.operation()`. This is [class-shape.md](class-shape.md#classes-and-managers)'s
  rule, and "utility" is not an exemption—purity is not either. A repository
  may enforce this convention mechanically; the command and configuration stay
  in that repository.
- Reach for a barrel only when the helper is a genuine cross-directory boundary;
  a helper used by siblings in one directory stays an internal sibling import.
  Barrels are opt-in API surfaces, not folder paperwork — see
  [imports-and-barrels.md](imports-and-barrels.md) (files are internal by
  default).

### Why

- Discoverability: utilities are findable by domain, not buried in unrelated
  classes.
- Reuse: a second consumer does not need to know which class originally hosted
  the logic.

## Behavior On The Data

When a helper takes a single domain type and is general to that type, it belongs
on the type—not as a private/static method on the first consumer, and not as a
free function beside it. `range.isEmpty()` reads more clearly than
`SchedulePlanner.isEmpty(range)` and stays correct when a second consumer asks
the same question.

### Rules

- If a helper takes one domain object and only consults its public surface, move
  it onto that object as a method.
- Applies equally to `private static` helpers and free functions in a sibling
  file.
- Singleton-instance classes (`Weekday.MONDAY`, ...) and value-type classes
  (`GridCoordinate`, `DateRange`) are both fair game.
- Name the method after what it answers, not how it is used by the first
  consumer.

### Why

- The same predicate ends up duplicated across every consumer that re-asks the
  question.
- The call site reads as a domain operation, not as an external query about the
  domain.
- Future contributors looking for "what can I ask a date range?" find the
  answer on `DateRange`, not scattered across consumers.

### When Not To Use

- The helper depends on context the domain type cannot see.
- The helper is consumer-specific orchestration that happens to take a domain
  object as its first argument.
- The "behavior" is one trivial line at one call site and unlikely to be
  repeated.

## Parameter Objects

A parameter object is a call-site clarity tool for one operation. It names each
input at the call site and keeps optional/defaulted knobs out of positional
slots; it does not have to be a reusable domain concept.

### Rules

- Use a parameter object when an operation has several inputs and at least one
  is optional/defaulted, two fields have the same structural type, or callers
  pass `undefined` only to reach a later argument.
- Keep positional parameters for one or two obvious required values, tiny private
  helpers, math-like APIs, or signatures that must match an external interface.
- Name the shape by role: `XInput` for the main command payload, `XOptions` for
  optional/defaultable knobs, `XContext` for mutable pipeline state, and
  `XResult` for outputs.
- Keep one-shot input/options interfaces near the operation that consumes them.
  Promote them only when they cross a folder/package boundary or become part of
  the public surface.
- Do not use an object to hide unrelated concepts. If a subset of fields travels
  together with shared semantics, extract that subset as a domain aggregate
  first.

### Why

- Call sites say what each value means, so same-shaped sets/maps/booleans do not
  rely on argument order.
- Optional policy knobs can be omitted naturally instead of forcing
  `undefined` placeholders.
- Adding a new optional field does not churn every caller or make overloads
  necessary.

### When Not To Use

- The operation has a small, stable positional signature whose order is obvious.
- The object would contain only unrelated values with no readable command shape.
- The parameters are not just call inputs but a reusable domain concept; use
  Parameter Bundling instead.

## Parameter Bundling

When two or more parameters consistently travel together across signatures, they
are a candidate for an aggregate type. The aggregate carries shared behavior and
reads as a single domain concept at call sites.

### Rules

- When the same parameter pair appears across many signatures and has shared
  semantics, extract it into a named type.
- Place behavior on the aggregate once it exists. The pair's shared logic
  belongs on the aggregate, not duplicated across consumers.
- Do not bundle parameters whose names carry asymmetric meaning the type cannot
  express.

### Why

- A missing aggregate type usually means the same validation, iteration, or
  comparison logic is duplicated at each call site.
- Once the aggregate exists, behavior-on-the-data refactors become possible.

### When Not To Use

- Parameters that travel together in exactly one local helper.
- Parameter pairs whose only relationship is being in the same signature. The
  bundle has to mean something as a unit.

## Shared Defaults

When the same constants or defaults are read by more than one module, give them
one dedicated owner named for the concern instead of leaving a near-copy in each
consumer or hosting them on whichever class needed them first. This is
[Utility Extraction](#utility-extraction) for data: group by domain, not by
first consumer.

### Rules

- A value only one class consumes stays
  [class-owned](class-shape.md#class-owned-constants). Extract to a shared module
  once a second peer module needs the same value, or the values form a coherent
  group worth finding in one place.
- Name the module for the concern and export typed, grouped constants. For
  example, `RetryDefaults.ts` may expose `INTERACTIVE_RETRY` and
  `BACKGROUND_RETRY`. A small applier beside the constants is fine when several
  call sites set the same fields identically—as a static on the owning class,
  since an applier is an operation
  ([class shape](class-shape.md#classes-and-managers)).
- Keep the shared module a leaf: it should import only third-party types and
  nothing from the subsystems that consume it, so any module can read it without
  adding a cross-subsystem edge or a cycle.
- Group by what genuinely shares values; do not collapse different values into
  one "universal" constant for tidiness. If two consumers need different numbers
  because their context differs (for example interactive and background retry
  policies), keep separate named groups and say why.
- Keep compile-time defaults in typed code when they are code-owned: typed data
  stays greppable and refactor-safe. Reach for loaded configuration when the
  value must change without a code release, and give that configuration an
  owning schema.
- A repository-specific live tuning surface may layer over the shared default.
  That runtime mechanism stays in the product documentation rather than this
  canon.
- Per-record variation is not a shared default. Values that differ per tenant,
  document, asset, or other authored input belong on the validated data
  contract.

### Why

- "Where is the default for X?" gets one answer instead of several near-copies
  that drift apart.
- Typed grouped constants survive rename/refactor and appear in "find
  references"; an external config file silently tolerates a typo or a `NaN`.
- The leaf-module rule lets every subsystem share the defaults without inverting
  or tangling dependencies.

The authoring-time diagnostic for spotting candidates—including the related
"name vs type" signal—lives in [review heuristics](review-heuristics.md).
