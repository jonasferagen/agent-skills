# Types and boundaries

## Validate before narrowing

An annotation, `as`, `!` or generic result parameter supplies no runtime
validation. Treat external JSON, storage, network responses and untyped library
results as `unknown` until checked. Validate the fields and invariants the next
operation relies on, then carry the checked type inward. Reuse the project's
parser or schema library when it has one; a small guard can be enough for a
small contract. Choose unknown-field rejection, stripping or preservation from
the wire contract rather than imposing one policy on every reader.

A type predicate or assertion function is a claim the compiler trusts. Its body
must establish the whole promised shape, including nested values and optional
fields. A generic `parse<T>(raw): T` with no corresponding validator only moves
an assertion out of sight. If a schema owns validation, derive the static type
from it where supported instead of maintaining an unchecked second definition.

Validate once at the trust boundary and again when a later transformation can
break an invariant. Do not add repeated schema parsing inside an already typed
loop without a concrete reason. Use the project's distinction between malformed
input, a valid refusal and an internal defect; never make an invalid payload
look like an empty successful result.

## Keep assertions beside their proof

Prefer a check and control-flow narrowing to an assertion. Use `satisfies` for
a literal that must meet a contract while retaining specific inference, and an
annotation when callers should see the broader contract. Neither validates
runtime input. Follow the existing `type`/`interface` convention; interfaces do
not validate objects either.

An unavoidable assertion belongs beside the external declaration gap or local
invariant it bridges. Explain the proof and its limit. Repeated `as unknown as`
or `!` across callers usually identifies a missing boundary representation.
Do not weaken a type to `any` to move the error downstream. If an external API
forces `any`, confine it to the adapter and return a checked type.

Use `unknown` in catch handlers until the thrown value is narrowed; JavaScript
can throw a string or `null` as well as an `Error`. Preserve the cause according
to the project's error contract and avoid exposing raw payloads in diagnostics.

## Distinguish semantic primitives when mistakes are plausible

Brands help when multiple concepts share one primitive and swapping them is a
plausible error. Introduce them at a validating boundary and preserve them through
callers, including fixtures. Avoid brands that add assertion noise without
protecting a real distinction. Arithmetic on a branded number returns an
ordinary number; validate the result before restoring a numerical brand.

```ts
// Example: two validated string namespaces that must not be interchangeable.
declare const accountBrand: unique symbol;
declare const jobBrand: unique symbol;
type AccountId = string & { readonly [accountBrand]: true };
type JobId = string & { readonly [jobBrand]: true };

function parseAccountId(raw: unknown): AccountId {
  if (typeof raw !== "string" || !/^acct_[a-z0-9]+$/.test(raw)) {
    throw new Error("Expected an account identifier");
  }
  return raw as AccountId; // The format check above owns this brand.
}

function parseJobId(raw: unknown): JobId {
  if (typeof raw !== "string" || !/^job_[a-z0-9]+$/.test(raw)) {
    throw new Error("Expected a job identifier");
  }
  return raw as JobId;
}
```

A private constructor alone does not make a class's instance type nominal.
Private/protected instance members can enforce origin compatibility; an
unexported `unique symbol` property can also prevent ordinary outside callers
from fabricating a validated shape. Preserve such a guarantee when fixing an
unused-binding warning, but add it only where structural substitution is a
real problem. A brand supplies static separation, not validation or security;
an assertion can still bypass it.

Primary references: [type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions),
[narrowing and predicates](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates),
and [structural compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html).
