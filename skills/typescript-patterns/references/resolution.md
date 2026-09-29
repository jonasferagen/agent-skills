# Resolution And Defaults

## Contents

- [Resolve precedence once](#resolve-precedence-once)
- [Resolve child properties through their owner](#a-property-of-x-is-resolved-through-x)
- [Choose an absence shape](#choosing-the-absence-shape)
- [Keep a resolver honest](#keeping-a-resolver-honest-the-absence-ledger)

Resolution turns layered, optional, or inherited input into one decisive value.
Do it once, at the boundary where the value becomes usable. Do not carry the
same precedence chain through every consumer or reopen a resolved value as
another optional later.

## Resolve Precedence Once

Use a named resolver when a value can come from several sources:

```ts
const locale = LocaleResolver.resolve({
  request: request.locale,
  account: account.locale,
  system: DEFAULT_LOCALE,
});
```

### Rules

- Put precedence in one readable sequence.
- Return the narrowest honest shape: a total value, decisive result, null
  object, discriminated choice, or `undefined` when absence remains meaningful.
- Apply validation and normalization before downstream code sees the value.
- Keep a default beside the owner whose contract gives it meaning.
- Do not introduce a second spelling of absence downstream.
- Name the output `Resolved*` only when the decision is made and consumed at
  this boundary. A carried domain value normally uses its unmarked name; see
  [representation prefixes](naming-and-placement.md#representation-prefixes).

### Which Boundary

Resolve where all required sources first meet and before the value fans out.
Common boundaries include parsing an external request, composing a service,
loading configuration, building a view model, and adapting a persistence
result.

Do not resolve too early when later context is legitimately part of the
decision. Do not resolve too late when several consumers would repeat the same
precedence or default.

## Worked Example

Suppose a timeout comes from a request override, an account policy, or a system
default. The resolver owns both precedence and validation:

```ts
interface TimeoutInput {
  request?: number;
  account?: number;
  system: number;
}

class TimeoutResolver {
  static resolve(input: TimeoutInput): number {
    const value = input.request ?? input.account ?? input.system;
    if (!Number.isFinite(value) || value < 0) {
      throw new Error("Timeout must be a non-negative finite number");
    }
    return value;
  }
}
```

Consumers receive `number`, not the three-source policy. If `0` is meaningful,
the nullish chain preserves it; `||` would silently replace it.

## A Property Of X Is Resolved Through X

When a child setting exists to support a parent feature, resolve it through the
parent's enabled/disabled decision rather than treating it as an independent
knob. A retry delay is irrelevant when retry is disabled; a caption style is
irrelevant when captions are absent.

This keeps impossible combinations out of the resolved type. Prefer a tagged
shape when the child only exists in one arm:

```ts
type ResolvedRetry =
  | { enabled: false }
  | { enabled: true; attempts: number; delayMs: number };
```

## Choosing The Absence Shape

| Shape               | Use when                                                             | Contract                                 |
| ------------------- | -------------------------------------------------------------------- | ---------------------------------------- |
| Total value         | A safe default always exists                                         | Consumers never branch on absence        |
| Decisive result     | Absence/error needs a reason                                         | Success and failure are explicit arms    |
| Null object         | Consumers need the same methods and a no-op implementation is honest | No scattered optional chaining           |
| `undefined`         | Absence remains meaningful and simple                                | Every consumer must account for it       |
| Discriminated union | Several optional fields are really one exclusive choice              | Invalid combinations are unrepresentable |

Avoid sentinels hidden inside the value's ordinary vocabulary. `0`, `''`, or a
special enum member is an absence model only when the domain itself defines it
that way.

## Keeping A Resolver Honest: The Absence Ledger

A resolver can silently lag when its input contract gains an optional field.
Record the policy for every field in a total ledger:

```ts
type AbsenceDecision =
  | "required"
  | "defaulted"
  | "decided-at-boundary"
  | "intentionally-absent";

const TIMEOUT_ABSENCE = {
  request: "decided-at-boundary",
  account: "decided-at-boundary",
  system: "required",
} as const satisfies Record<keyof TimeoutInput, AbsenceDecision>;
```

The ledger makes contract growth fail closed. Prefer consuming it in the
implementation when that stays clear; an unused parallel map is only a review
ratchet. Pair it with behavior tests proving the declared default, rejection,
or intentional absence.

Use values, not missing keys, for exceptions. A missing entry says nothing;
`intentionally-absent` records a decision. See [Fail-Closed
Mirrors](typescript.md#fail-closed-mirrors).

## When Not To Use

- A direct optional read appears once and has no precedence or policy.
- The source already supplies a validated total value.
- The proposed resolver would merely rename a concrete dependency without
  reducing policy at the boundary.
- The value is a whole representation being lowered for later use; that is a
  compiler, not a resolver.
