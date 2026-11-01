# Operations and state

## Choose the shape by what the caller needs

A TypeScript module already groups related exports. A stateless operation with
explicit inputs can be an exported function. Use an object when callers need a
small capability set as a value, a closure when a factory should capture private
state or configuration, and an instance when methods share a meaningful
identity, lifecycle or invariants. A class can also make a substantial local
builder easier to understand. Keep the project's existing API when it already
expresses the contract well.

Do not wrap every exported function in a static-method class or replace every
class with functions. A static member can be a natural companion to a value's
construction or operation, but supplies no per-instance lifetime. A consistent
project style can be a legitimate reason for a shape; it is not a universal
TypeScript requirement. Prefer composition over inheritance when the need is
to supply a collaborator rather than support real subtype behavior.

Separate passive data from stateful services in the public API when consumers
serialize, replay or inspect the data. Methods and runtime identity need an
explicit encoding/reconstruction contract if that value crosses a data boundary;
a type annotation alone cannot supply one.

## Make private state belong to a lifetime

A mutable module-level variable is shared by its importers in that runtime
module instance. It does not become fresh per request or simulation because a
function call begins. Put per-operation state in the call, and per-session state
in an explicitly created owner. Defaults or lookup data can remain module-level
when that sharing is intentional.

```ts
interface CounterSession {
  next(): number;
  reset(): void;
}

function createCounterSession(initial: number): CounterSession {
  let value = initial;
  return {
    next: () => ++value,
    reset: () => { value = initial; },
  };
}
```

The returned callbacks close over one session's state and do not require a
receiver. An instance is equally suitable when its identity or other methods
make the lifetime clearer. Do not add a global registry or service locator
just to distribute one owner's state.

When an API returns a callback from a class, inspect how callers invoke it. A
method using `this` needs its receiver preserved through binding or a wrapper,
or an arrow property where that tradeoff fits. Keep cleanup callback identity
stable when an external registration API relies on it. Choose the ownership
and registration shape here; verify receiver and type details with the project's
language checks. An ordinary method is fine when callers always invoke it on
the instance.

## Put varying policy at the operation

Pass time, randomness or policy through the operation's parameters or its
constructed owner when callers need to vary them. Do not make callers patch a
module global to test one instance's behavior. Keep a small fixed sequence as
named calls, and extract a collaborator when its responsibility or lifetime
differs. A configurable registry or workflow framework needs a real extension
requirement, not merely several steps.

For a scoped refactor, exercise two independent owners and repeated calls. For
resource-owning objects, check that construction and disposal happen at the
intended lifetime. Performance-sensitive code may legitimately reuse mutable
working state; preserve that contract rather than imposing allocation on every
step.

Primary reference: [TypeScript classes, ordinary objects and functions](https://www.typescriptlang.org/docs/handbook/2/classes.html#why-no-static-classes).
