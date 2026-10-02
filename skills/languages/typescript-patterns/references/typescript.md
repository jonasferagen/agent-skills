# TypeScript Conventions

## Contents

- [Nullability and declarations](#nullability)
- [State modeling and exhaustiveness](#state-modeling)
- [Fail-closed mirrors](#fail-closed-mirrors)
- [Typed events](#typed-events)
- [Safety and assertions](#safety)
- [Tuples and branded IDs](#tuple-aliases)
- [Nominal class instances](#nominal-class-instances)

## Nullability

Prefer `undefined` for internal absence unless an external contract requires
`null`.

### Blank String Normalization

When blank and whitespace-only strings mean absent, normalize at the boundary:

```ts
return value?.trim() || undefined;
```

Use this only when an empty string is not meaningful. `||` is intentional here:
`trim()` returns `''`, which should collapse.

### Optional Parameters

Use `param?: T` when omission is the normal case. Reserve
`param: T | undefined` for a required argument slot imposed by an external
signature or a later positional argument.

```ts
static resolve(base: Locale, override?: Locale): Locale;

// The slot itself is required by the implemented interface.
static resolve(base: Locale, override: Locale | undefined): Locale;
```

A required parameter containing `undefined` is a smell; make its reason visible
in the API shape.

### Unused Parameters In An Imposed Signature

When you do not use a parameter but cannot remove it, because a used parameter
follows it in a signature you do not own, give it the underscore prefix the
toolchain already exempts. Deleting it would shift every parameter after it.

```ts
codec.explainsEntry = (_revision, address, snapshots) =>
  addressIsExplained(address, snapshots);
```

This is the language's own convention for the case, not a suppression. A
policy that bans it outright is unimplementable wherever callbacks are
implemented against a foreign interface. It applies only where removal is
unavailable: an unused **trailing** parameter is deleted, and an unused local or
import is always deleted.

## Type Declarations

- Use `interface` for object shapes, DTO contracts, and component props.
- Use `type` for unions, primitives, mapped/conditional types, and function
  signatures.
- Export shared contracts from explicit contract modules. Keep helper types
  private until they escape their owner.

## Literal Shape Validation

Use `satisfies` when a literal must conform to a contract while retaining its
specific inferred shape. Good fits include lookup tables, fixtures, data
payloads, and registry maps whose exact keys matter. Prefer an ordinary
annotation when callers should see only the broad contract.

Remember that `satisfies readonly T[]` proves membership, not completeness. The
[fail-closed mirror](#fail-closed-mirrors) rule covers exhaustive inventories.

## State Modeling

Use literal unions for simple modes and tagged variants when states carry
different payloads.

```ts
type Status = "idle" | "running" | "failed";

type Result<T> = { ok: true; value: T } | { ok: false; error: string };
```

### Exhaustive Closed Unions

When a project-owned union is closed and a consumer claims to handle every
variant, make the claim exhaustive.

```ts
function label(status: Status): string {
  switch (status) {
    case "idle":
      return "Waiting";
    case "running":
      return "Working";
    case "failed":
      return "Failed";
    default:
      return assertUnreachable(status);
  }
}

function assertUnreachable(value: never): never {
  throw new Error(`Unexpected variant: ${JSON.stringify(value)}`);
}
```

Use the repository's shared `never` helper when it has one. A real fallback is
correct for open runtime input such as external JSON, URL parameters, or a
forward-compatible wire contract.

Implicit return checking catches a missing case only under `strictNullChecks`
(TS2366, and only for a declared return type that excludes `undefined`) or
`noImplicitReturns` (TS7030). Read the repository's compiler settings before
relying on it. Two shapes commonly fail open:

- A `void` switch silently does nothing for a new member.
- A permissive `default` defeats exhaustiveness even when the function returns a
  value.

Spell a legitimate fallback member as its own case; reserve `default` for the
`never` guard over a closed union.

## Fail-Closed Mirrors

A mirror is any declaration that must list every member of a union or every key
of a schema declared elsewhere: command spellings, parser allowlists, labels,
or per-stage handlers. A mirror must be total by construction so forgetting an
entry fails where the decision belongs.

### The Subset Trap

These shapes reject invalid members but compile with a valid member missing:

```ts
const ROUTED_STATES: readonly WorkflowState[] = ["queued"];
const EXPORTED_MODES: ReadonlySet<Mode> = new Set(["basic"]);
const LABELS: ReadonlyMap<Status, string> = new Map();
const HANDLER_FOR_EVENT: Partial<Record<EventName, Handler>> = {};
const stats = {} as Record<MetricName, number>;
const FIELDS = ["name"] as const satisfies readonly FieldName[];
```

A subset of `T[]`, `Set<T>`, or `Map<T, V>` is valid. `Partial` explicitly opts
out, a cast hides the missing entries, and array `satisfies` checks membership
only. Read the annotation; do not trust its protective appearance.

<!-- Package-boundary copy: typescript-design/references/naming-and-placement.md (Complete registries) summarizes this rule. Keep both aligned. -->

### The Two Total Shapes

Choose by the source of truth.

**Derive the union from the table** when the data is the vocabulary:

```ts
const FORMATTERS = {
  date: formatDate,
  money: formatMoney,
} as const satisfies Record<string, Formatter>;

export type FormatterName = keyof typeof FORMATTERS;
```

Derive ordered keys from this same table rather than maintaining another list.

**Key the mirror by the union** when the union or schema is authoritative:

```ts
export const COMMAND_FOR_MODE = {
  basic: "run",
  preview: "preview",
  internal: null,
} as const satisfies Record<Mode, string | null>;
```

Give opting out a value such as `null` or a tagged decision. An explicit decline
is reviewable; a missing property is invisible.

Put the obligation beside the declaration it mirrors so the author who extends
the vocabulary gets the compile error. If the source is open-ended data, say so
and add a contract test when the stakes justify one. A closed vocabulary in
another repository can still be held equal through generated types or a
cross-contract test; a comment claiming equality does not enforce it.

### Fail-Closed Discovery Boundaries

Discovery code often hides the same omission behind a filter. When a directory,
registry, or payload owns a naming convention, distinguish unrelated entries
from malformed candidates and reject the latter.

```ts
const migrationFiles = names.filter((name) => name.endsWith(".sql"));
const migrations = migrationFiles.map((name) => MigrationName.parse(name));
```

`MigrationName.parse` should reject a malformed versioned SQL name. Keeping
only names that already match the full version pattern would silently drop the
malformed migration. The boundary would appear healthy while an owned input
never entered the system.

Use a parse/partition step when every candidate must be accepted or explained:

- ignore entries outside the owned category by an explicit, narrow rule;
- parse every candidate inside the category;
- reject duplicates, malformed names, and unsupported variants with the source
  identifier in the error; and
- test one valid, one unrelated, and each invalid candidate class.

Name registries for the obligation they transfer, not merely the property they
describe.

## Typed events

- Bind emitters and listeners to a typed event map so payload-required events
  enforce payload presence.

## Safety

- Avoid `any`; parse `unknown` at boundaries.
- Keep narrow typing where data enters through IO, storage, or external APIs.
- Use `JSON.stringify(value)` rather than `String(value)` when reporting an
  unknown object; the latter silently becomes `[object Object]`.
- Reuse a project-owned `messageFromUnknown`-style helper at catch/loader
  boundaries when one exists.

### Assertion Ladder

Reach for the narrowest proof that preserves the domain story:

1. Parse or validate `unknown` at the boundary.
2. Use a type guard or assertion method for a reusable runtime check.
3. Promote repeated validation/defaulting into a value object.
4. Use `satisfies` for checked literals whose precise shape matters.
5. Use `as` only when TypeScript cannot see a proof the code already owns.

Keep casts beside the boundary they cross. Production `as unknown as` should be
rare, local to an external declaration hole, and explained.

### Non-Null Assertions

Treat `!` as an invariant claim, not convenience syntax. Prefer an early guard,
a throwing owner accessor, a value object that owns the invariant, or an
explicit lifecycle state. Use `!` only when the proof is local and stable.

### Indexed And Collection Access

Treat indexing as a lookup that can fail unless the type proves otherwise.

- **Make the producing type prove it** when the cardinality is fixed and small:
  `readonly [T, ...T[]]` for non-empty, `readonly [T, T]` for a pair. Declare it
  where the value is built, not where it is read. One declaration removes the
  need for a guard at every downstream read site; a guard covers one read, and
  the next reader adds another.
- Keep the proof through transformation. Both `.map()` and a spread widen a
  tuple back to an array, so a rebuilt collection silently loses the guarantee
  its source had. Destructure, or annotate the rebuilt tuple.
- Guard one-off array, tuple, `Map`, and record lookups locally.
- Put repeated throwing lookups behind an owner method that names the invariant.
- Move repeated `map.get(...)!`, `array[index]!`, `shift()!`, or `pop()!`
  proofs behind a named boundary.
- Treat dynamic records and environment maps as untrusted input: read,
  validate, then pass a typed value onward.

The first bullet has a limit. A type states a fixed shape, not a relation:
"length divisible by four", "these two arrays stay parallel", "this index came
from that collection's length". Assert a relational constraint once, at the
boundary that accepts the value, and say in that signature what it refuses.
Re-proving it at each read is the outcome this rule exists to prevent.

## Narrowing `unknown[]` To A Typed Tuple

Give `Array.prototype.every` an explicit predicate so TypeScript narrows the
elements:

```ts
function assertVec3(value: unknown, context: string): [number, number, number] {
  if (
    !Array.isArray(value) ||
    value.length !== 3 ||
    !value.every(
      (item): item is number =>
        typeof item === "number" && Number.isFinite(item),
    )
  ) {
    throw new Error(`${context}: expected three finite numbers`);
  }

  return [value[0], value[1], value[2]];
}
```

Without the predicate, `every` returns `boolean` and the element type remains
unsafe.

## Tuple Aliases

Tuples are boundary contracts, not rich domain models. Use them when position is
the contract: wire DTOs, static input, storage payloads, and low-level buffers.
Promote to a value object when the value gains behavior, invariants, equality,
derived fields, frame, or unit semantics.

Do not create parallel aliases merely to document two namespaces. If the
distinction matters at runtime, give the concepts nominal value types.

## Branded IDs

Introduce a brand only when:

1. The primitive type carries several semantic namespaces.
2. Wrong-namespace assignment is plausible.
3. A validating factory is cheap.

Skip the brand when a richer value class already enforces the distinction.

- Convert raw values at parse/normalization boundaries and carry the brand from
  there.
- Do not assign raw strings to `OrderId`, `AccountId`, or `SessionId` in normal
  implementation code.
- Build fixture IDs through the same helper.
- Keep any unavoidable external-boundary cast local and explained.

### Nominal Class Instances

A class whose constructor is private is not nominally typed. The private
constructor stops the class being **constructed** elsewhere; its instance type
stays structural, so any object literal with matching public members still
satisfies it. For a class whose whole contract is "a validating factory produced
this", that gap defeats the point — the unvalidated literal is exactly what the
factory existed to exclude.

Only a private or protected **instance member** makes the instance type nominal.
Prefer the type-only form: it costs no emitted field, and an unused-locals check
cannot report it, because it declares no value to be unread.

```ts
declare const orderBrand: unique symbol;

export class ValidatedOrder {
  declare readonly [orderBrand]: true;

  private constructor(readonly lines: readonly OrderLine[]) {}

  static parse(input: unknown): ValidatedOrder {
    /* validate, then construct */
  }
}
```

An ordinary private field brands equally well but emits a runtime property and
looks unused to both a reviewer and an unused-binding check; see
[reading a strictness finding](enforcement.md#reading-a-strictness-finding).

Brand a class only where a structural impostor is actually reachable: a
validating factory, a parse boundary, or a token another module could otherwise
fabricate. A class that is merely inconvenient to build by hand does not need
one.
