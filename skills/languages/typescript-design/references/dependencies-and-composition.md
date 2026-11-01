# Dependencies and composition

## Express the capability actually consumed

Trace the entire path of a supplied dependency, including downstream calls.
A coordinator that forwards a client to another operation needs that operation's
capabilities too. Narrowing to only the methods the coordinator calls directly
can create an interface that hides a real dependency.

Choose a callback for one operation, an object interface for a cohesive role,
and a concrete type when the consumer owns it or relies on most of its API or
specific identity. `Pick<ExistingType, Keys>` can express a deliberate projection
without copying signatures when coupling to that existing type is appropriate.
Use a consumer-owned role when the capability should remain stable independently
of one provider. Do not duplicate a neutral contract that already has the right
owner merely to avoid an import.

```ts
interface ReadingSource {
  readonly read: () => number;
}

function totalReadings(source: ReadingSource, count: number): number {
  let total = 0;
  for (let index = 0; index < count; index++) total += source.read();
  return total;
}
```

A production adapter and a checked test literal can both supply this role. The
consumer neither chooses the source implementation nor acquires a right to
close it. If this operation simply accepted one callback, that could also be an
adequate API; do not require an interface for every function dependency.

A function-valued property can express a callback role without relying on method
parameter bivariance under strict function checking. Follow existing conventions
and check substitutability when parameter types differ; a compiling method
assignment is not a proof that a more specialized handler accepts all inputs.
If a projected fluent method returns polymorphic `this`, a `Pick` still retains
that relationship to its original type. A role returning `void` can be more
honest when the consumer discards chaining; preserve the full result when the
caller or an error path actually depends on it.

## Include lifetime and meaning

Structural compatibility cannot prove session affinity, ordering, atomicity,
resource ownership or cancellation semantics. A pool and an acquired session
can have identically named methods but different guarantees. Express acquisition
or a transaction callback when the consumer owns the lifetime; accept a
session-bound role when a caller already owns it. State the semantic guarantee
beside the interface and exercise it at the resource boundary. A renamed
interface or empty brand cannot implement that guarantee.

The composition boundary supplies concrete dependencies and owns their
acquisition and release. Borrowers do not dispose of an injected resource unless
that transfer is explicit. Return a disposer or an object with a disposal
operation when callers own a subscription or other retained resource. Preserve
its identity and idempotence obligations from the external API rather than
inventing a universal cleanup protocol.

## Keep adapters at their actual seam

Translate provider-specific payloads to the consumer's required values when
that protects a meaningful boundary. Do not export an SDK's large facade just
to name one small result. Keep provider fields that affect interpretation,
retries or refusal; narrowing must not erase a consequential state. Retain a
concrete provider contract where exposing it is the operation's actual purpose.

Assemble the dependency in an explicit entrypoint or factory rather than during
an unrelated import. A plain parameter or factory argument often provides the
needed seam; a dependency-injection container, base service class or plugin
registry needs a reason of its own. Exercise a simple checked double and a
representative real adapter separately when interoperability matters.

Primary references: [structural compatibility and function parameters](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
and [`Pick`](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys).
