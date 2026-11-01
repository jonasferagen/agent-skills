# Values and collections

## Preserve absence and meaningful empty values

Use `??` for an absence fallback when `0`, `false` or `""` remains meaningful.
Use a truthiness fallback only when the contract deliberately treats those
values as absent. Keep external `null` semantics when the wire format uses
null; do not normalize it to `undefined` without checking what that changes.

An omitted property differs from a present property whose value is `undefined`.
With `exactOptionalPropertyTypes`, `field?: T` permits omission but not an
explicit `undefined` assignment unless that is part of `T`. This matters in
patches where omission means unchanged and `null` means clear. Reading an
optional field still needs an absence check. A default parameter applies only
to `undefined`, not `null`.

## Put cardinality in the producing type

Treat dynamic indexing and `Map.get` as potentially absent. Guard a one-off
lookup; give repeated required lookups a named accessor that reports the missing
identity. `noUncheckedIndexedAccess` exposes unchecked array and index-signature
reads; it is not enabled by `strict`. Do not scatter non-null assertions to
clear its findings.

When a producer guarantees a fixed pair or a nonempty list, state that in its
return type: `readonly [T, T]` or `readonly [T, ...T[]]`. A length check on an
ordinary array does not generally refine it into a tuple. Transformations such
as `map` can lose tuple shape; check the resulting type instead of assuming the
proof survives. Construct fixed positions explicitly when that is clearer than
an assertion.

```ts
function parseTriple(raw: unknown): readonly [number, number, number] {
  if (!Array.isArray(raw) || raw.length !== 3) {
    throw new Error("Expected three finite numbers");
  }
  const [x, y, z]: unknown[] = raw;
  if (!finiteNumber(x) || !finiteNumber(y) || !finiteNumber(z)) {
    throw new Error("Expected three finite numbers");
  }
  return [x, y, z];
}

function finiteNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}
```

`every` skips holes in sparse arrays, so it cannot by itself prove every tuple
position exists. This parser checks each position and reconstructs the tuple.
Relations such as equal lengths of parallel arrays or a count divisible by four
need a runtime check where they enter; a simple tuple type does not express them.

A `number` type does not prove finiteness, integrality, range or units. For
integer counters or quantities that must remain exact, check safe integer and
range constraints where accepted or derived. Preserve the existing rounding,
randomness and arithmetic order during a type-only change; those are runtime
semantics, not annotation choices.

## Readonly is an access contract, not a snapshot

`Readonly<T>` is shallow. A readonly property containing a mutable array still
allows writes to that array; `readonly T[]` prevents array writes through that
reference but does not freeze its items or other aliases. `as const` retains
literal information and makes literal properties readonly to the type checker;
it does not recursively freeze the runtime object. A readonly view of caller
state can change when the caller mutates its original reference.

If the operation promises an independent snapshot, copy the owned mutable levels
or use the project's immutable representation. If it only borrows a value for
the call, make that contract clear instead of adding cloning. `Object.freeze`
is shallow too. A type-level `DeepReadonly` can describe an access restriction
but cannot replace runtime ownership or copying.

When snapshot independence matters, exercise nested writes through the original
alias and later writes to the returned value. A successful type check cannot
prove either runtime isolation or deterministic replay.

Primary references: [object types, readonly and tuples](https://www.typescriptlang.org/docs/handbook/2/objects.html),
[`noUncheckedIndexedAccess`](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html),
and [`exactOptionalPropertyTypes`](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html).
