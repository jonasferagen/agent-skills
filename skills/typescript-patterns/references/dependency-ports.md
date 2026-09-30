# Dependency Ports

## Contents

- [Trace the whole use path](#trace-the-whole-use-path)
- [Include lifecycle semantics](#include-lifecycle-semantics)
- [Choose the shape](#choose-the-shape)
- [Place and own the port](#put-the-port-with-the-consumer)
- [Keep provider types outside consumer ports](#keep-provider-types-outside-consumer-ports)
- [Testing consequence](#testing-consequence)

A dependency port is the smallest honest type a consumer needs from a
collaborator. Use one when a class accepts a concrete dependency but calls only a
stable slice of it. The concrete implementation satisfies the port structurally;
tests and alternate callers can supply a checked literal without casting.

## Trace The Whole Use Path

Type the parameter from the transitive closure of what happens to the value:
what the consumer calls directly **and** what every downstream recipient calls.
A class that only forwards a dependency is a conduit: its own calls do not prove
that the dependency can be narrowed.

- A coordinator that forwards a clock to several workers needs the union of all
  those workers' clock capabilities, not just the method it calls directly.
- A request handler that reads part of a client but hands it to retry code that
  requires the concrete client keeps the concrete type at that edge.
- A status view that only reads progress and subscribes to changes can accept a
  narrow `ProgressSource` role.

A port that compiles only because TypeScript accepts a narrower method parameter
bivariantly is not honest. If any downstream call requires the concrete class,
keep the concrete class at that edge.

## Include Lifecycle Semantics

Structural compatibility proves method shape, not lifetime, identity,
atomicity, ordering, or ownership. Those are capabilities too.

A database pool and a transaction-bound session may both expose
`query(text, values)`. A structural `QueryClient` therefore lets the pool
satisfy code that actually requires every statement to run on one acquired
session. The methods match and the lifecycle contract does not.

Make the semantic requirement visible in the parameter type:

- accept a transaction/session role when the caller is already inside one;
- accept a `withTransaction(callback)` or session-acquisition capability when
  the consumer owns the lifetime; or
- keep the concrete dependency when its full identity and ownership semantics
  are part of the contract.

Apply the same test to streams, locks, render contexts, filesystem handles, and
request-scoped services: if substituting an object with the same methods can
break ordering or ownership, the port is missing a capability.

## Choose The Shape

| Situation                                                                   | Shape                                       |
| --------------------------------------------------------------------------- | ------------------------------------------- |
| Plain subset of one existing class, with ordinary return types              | `Pick<Class, "member">`                     |
| Genuine role that several implementations can satisfy                       | Named interface                             |
| Picked method returns polymorphic `this` but the consumer discards chaining | Interface whose method returns `void`       |
| Method shape matches but one session/lifetime/identity is required          | Named semantic role or acquisition callback |
| Consumer owns, constructs, or uses most of the dependency                   | Concrete class                              |

`Pick` prevents copied method signatures from drifting. A named interface is
better when the abstraction is a role rather than a projection of one class.
Polymorphic `this` is the important exception: inside `Pick`, `this` still means
the origin class, so a literal cannot satisfy the supposedly narrow type. Use a
named interface returning `void` when the consumer discards chaining.

## Put The Port With The Consumer

The consumer owns the capability it requires. Declare a one-consumer port beside
that consumer. When sibling consumers share the same role, place one neutral
`*Ports.ts` module beside them and import it; do not copy equivalent interfaces
into each file.

Name the role or target, not the implementation. `InvoiceDeliveryTarget` says
what delivery acts on; `MailerSubset` merely advertises how the type was made.

## Keep Provider Types Outside Consumer Ports

A consumer-owned port should not import a provider's heavyweight facade merely
to name a small result or capability. If a value exists only because the
consumer displays or persists a subset of provider output, define that passive
DTO beside the consumer port and reduce the provider value in the composition
adapter. If the capability already has a lower-level neutral owner, import that
contract directly instead of reaching through the provider package.

For example, a report screen can own the timing/outcome DTO it consumes instead
of importing a job runner's internal result type. A composition adapter reduces
the provider result to that DTO. Neutral capabilities such as logging come from
their own lower-level owner rather than through the provider facade.

The decision test is ownership, not structural assignability: if changing the
provider's internal result should not force the consumer contract to change,
the provider type does not belong in the port. Keep the concrete type when the
consumer genuinely needs the provider's full semantics.

## Testing Consequence

A correct port lets a test supply a plain object literal that the compiler checks
against production use. If the test still needs `as unknown as`, classify the
case before changing production code: the test may need a real domain fixture,
may be reaching into private state, or may be modeling an opaque browser/vendor
boundary that cannot be represented honestly. The decision sequence belongs to
the repository's own testing conventions.

Do not add a port solely to eliminate a cast when the consumer genuinely needs
the concrete dependency. A justified cast at an external boundary is safer than
a false abstraction that allows invalid production values.

Related: [class shape](class-shape.md),
[type placement](naming-and-placement.md#type-placement-three-tiers).
