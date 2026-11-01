# Values and phases

## Shape inputs around how callers use them

Keep a short obvious positional signature. Introduce a named parameter object
when optional arguments, same-shaped values or boolean switches obscure a call.
TypeScript has no keyword-only parameter syntax, so a small options object can
make those choices visible without forcing callers to pass placeholder
`undefined` values. Destructure at the owning boundary when it helps, and retain
meaningful defaults there instead of independently resolving them in every
adapter.

Name a passive input/result contract when it escapes its local scope or several
callers need to agree on its meaning. Avoid extracting every inline object type.
Group values when they share meaning or invariants; matching field lists alone
do not justify one universal domain object. Preserve units, validation state and
source identity in names or contracts when callers rely on those distinctions.
Use the project's naming conventions rather than mandating a `Types` suffix.

## Place behavior without requiring a class

A wire payload is a passive boundary representation. A domain value can remain
a record with named functions, come from a validating factory, or use a class
when behavior, identity or construction invariants make that clearer. Repeated
normalization and derived calculations should have one named owner, but that
owner need not be a method on every record. Keep I/O or provider dependencies
outside the value when their lifetime does not belong to it.

A parser or factory should return a value callers can use under its promised
contract. If ordinary structural construction can bypass a required invariant,
make the construction boundary explicit and choose the required type/runtime
protection. TypeScript patterns covers how guards, brands and assertions
establish those guarantees. Do not treat a private constructor as proof of a
nominal instance type or add a class solely for a filename convention.

For repeated sibling implementations differing only in fixed data, a typed
list of descriptors and one function can express the variation. Keep a genuinely
different implementation separate rather than building a generic pipeline for
it. A family with no dynamic extension requirement does not automatically need
a registry.

## Expose what a stage actually completed

A phase boundary earns a named result when it establishes a materially different
invariant, not just because a helper ran. Return a completed contract instead
of exposing a partially filled `Partial<WholeResult>` that downstream callers
must repair. Keep mutable working fields private to the builder or operation,
and expose only what a caller needs after the stage.

For example, parsing can produce an input with checked field shapes; resolution
can produce an input whose external references have been resolved. Make the
second operation consume the first result and return its own guarantee. Avoid
conflating absence, refusal and unfinished construction under one `valid` flag.
Discriminated unions and runtime validation are language mechanisms for those
contracts; choose the owning stage here and check the mechanisms separately.

When an API returns state, decide whether it transfers an independent snapshot
or borrows an owned value. Put that contract at the operation that controls the
lifetime. A readonly annotation alone cannot decide ownership. A mutating builder
or an in-place update can be efficient and honest when the caller knows who owns
the state; do not impose copying as a structural preference.

For an implementation replacement, preserve public inputs, outputs, errors and
relevant effect order. Name which adapter selects old or new code during a
transition and what evidence permits retiring the old path. Keep serialization
and older saved values in scope when the changed representation affects them;
a TypeScript interface does not migrate stored data or preserve runtime class
identity. A plan should state those obligations without starting an unrequested
conversion.

Primary references: [object and optional property types](https://www.typescriptlang.org/docs/handbook/2/objects.html)
and [parameter objects via destructuring](https://www.typescriptlang.org/docs/handbook/2/functions.html#parameter-destructuring).
