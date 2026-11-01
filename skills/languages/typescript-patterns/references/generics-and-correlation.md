# Generics and correlation

Use a generic to preserve a relationship: a caller's item type, a key and its
value, or a parser and its typed consumer. Prefer inferred types and the fewest
parameters that express that relationship. A fixed operation needs no generic
framework. A parameter appearing only in the result, such as `load<T>(): T`,
usually promises information the implementation does not have; require a
validator or return the actual known type.

## Keep keys related to values

```ts
function readProperty<T, K extends keyof T>(value: T, key: K): T[K] {
  return value[key];
}
```

This preserves which key selects which value. Returning `T[keyof T]` instead
loses that precision. For events, preserve the event name with its payload in a
mapped discriminated union or a typed event map. Independent unions of names
and payloads admit mismatched pairs. Do not silence a heterogeneous dispatcher
with casts before checking where the relationship was lost.

## Hide a type only after binding its consumer

A heterogeneous registry need not erase a parser to `Parser<unknown>` and a
handler separately to `(input: unknown) => ...`. A handler that requires one
specific input cannot safely accept arbitrary unknown values. Capture the
relationship while the generic is known, and expose a uniform operation that
validates before invoking that handler:

```ts
type Parser<Input> = (raw: unknown) => Input;
type Prepared<Result> = { run(): Result };

function defineOperation<Input, Result>(
  parse: Parser<Input>,
  handle: (input: Input) => Result,
): { prepare(raw: unknown): Prepared<Result> } {
  return {
    prepare(raw) {
      const input = parse(raw);
      return { run: () => handle(input) };
    },
  };
}
```

The closure retains the pairing while the caller sees one result contract.
This is one option when the relationship needs to survive storage; a simple
discriminated union or a direct generic call may be enough. Adapt parse failure,
async work and dependency passing to the existing operation contract. This
example allows the parser to throw; it does not define a project-wide error
policy or require a registry abstraction.

## Keep type machinery proportionate

Prefer direct indexed access and ordinary unions before recursive conditional
types. If a mapped type or overload solves a real relationship, keep a small
valid caller and an invalid caller that must fail compilation. For correlated
unions, include a mismatched key/payload pair; for a generic helper, include two
different input types so a widened result cannot masquerade as preservation.

Do not add overloads that promise more than the implementation checks. Keep the
implementation signature consistent with every exposed case. When inference
needs an explicit type argument at a real boundary, that alone is not a defect;
first ask whether the required relationship is actually available to infer.

Primary references: [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
and [function type parameter guidance](https://www.typescriptlang.org/docs/handbook/2/functions.html#guidelines-for-writing-good-generic-functions).
