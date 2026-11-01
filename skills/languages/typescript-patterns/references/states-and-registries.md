# States and registries

## Keep each variant with its payload

Use a discriminated union when a state determines which data exists. A record
with `status` plus unrelated optional fields admits combinations the operation
cannot handle. Do not use `Partial<WholeState>` to stand for every lifecycle
phase when each phase has different invariants.

```ts
type TaskState =
  | { readonly kind: "idle" }
  | { readonly kind: "running"; readonly startedAt: number }
  | { readonly kind: "failed"; readonly reason: string };

function assertNever(value: never): never {
  throw new Error("Unhandled task state");
}

function stateLabel(state: TaskState): string {
  switch (state.kind) {
    case "idle": return "Waiting";
    case "running": return `Started at ${state.startedAt}`;
    case "failed": return state.reason;
    default: return assertNever(state);
  }
}
```

For a closed union, the `never` check makes an omitted variant a compile error,
even in a `void` dispatcher. Reuse the project's helper when it has one. A
non-defaulting value-returning switch may already be protected by its return
type and compiler settings; inspect them before claiming exhaustiveness or
rewriting correct code. A broad fallback defeats that protection.

Open runtime input needs a separate parsing or compatibility decision. Do not
cast an unknown event into a closed union and call the final `never` branch
validation. A consumer intentionally handling only some variants can retain
that subset contract; do not force unrelated consumers to act on every event.

## Make complete tables complete by construction

Choose the vocabulary's owner. Derive the union from the authoritative table
when its keys define the vocabulary. When a union is authoritative, check the
table against `Record<Union, Value>`:

```ts
type TaskKind = TaskState["kind"];
const BADGES = {
  idle: "quiet",
  running: "busy",
  failed: "warning",
} as const satisfies Record<TaskKind, string>;
```

A checked annotation also enforces the required keys; use `satisfies` when its
more specific inference helps. Check the literal at its declaration. Ordinary
structural assignment is not a universal exact-object guarantee: extra fields
can arrive through variables, spreads or open input. Parse those according to
the boundary contract.

`readonly Kind[]`, `Set<Kind>`, `Map<Kind, Value>`, `Partial<Record<Kind, Value>>`
and `satisfies readonly Kind[]` allow missing members. They prove membership or
permit partiality; they do not establish a complete inventory. An `as Record`
assertion can conceal the omission. Where a table intentionally declines a
member, represent that decision explicitly, for example with `null` or a tagged
value, instead of an unexplained missing entry.

When values are open-ended, completeness against an arbitrary string is not
meaningful. Use an honest lookup type and handle absence. For a closed external
vocabulary, use generation or a focused contract check when the project needs
cross-boundary equality; a comment cannot keep two definitions synchronized.

Primary references: [discriminated unions and `never`](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)
and [`satisfies`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator).
