# TypeScript design scenarios

Requests, context and expected behavior for evaluation. Ordinary use reads the
entrypoint and references selected by the task. Record observed results with
the change that ran them, not here.

## Structure and lifetimes

| Request and context | Expected behavior |
| --- | --- |
| An existing operation only needs a different instance lifetime or narrower interface | Use the local design reference directly when responsibilities and effects stay unchanged; avoid an unrelated application-architecture review. |
| A stateless exported function is proposed for conversion into a static class | Keep or change its shape for a concrete caller need or adopted project convention; no universal class mandate. |
| A stateful class already exposes a useful public contract | Preserve it unless a demonstrated issue or authorized change justifies replacement. |
| Two simulation runs unexpectedly share module-level mutable state | Give state an explicit per-run owner, through a parameter, factory/closure or instance; verify independence and repeated calls. |
| An instance method is returned as a callback and loses its receiver | Choose binding, a wrapper or an appropriate arrow property; preserve callback identity needed for cleanup. |
| A deterministic operation depends on time or randomness through globals | Put the varying dependency at the operation's call or constructed owner without imposing a container. |
| A public module exposes every helper through a wildcard barrel | Identify the intended caller surface and preserve required exports while keeping implementation details internal. |
| A type-only cycle is removed but runtime ownership still crosses both ways | Trace actual responsibilities and initialization; an erased edge alone does not establish a sound structure. |
| Importing a reusable module opens a client or reads browser storage | Move composition to the intended entrypoint while preserving any deliberately import-driven registration contract. |
| A feature contains multiple related exports in one file | Keep the cohesive module unless responsibility, lifetime or dependency differences justify a split. |
| The project prescribes a naming or directory convention | Follow it without treating the convention as a universal TypeScript rule. |

## Interfaces, values and phases

| Request and context | Expected behavior |
| --- | --- |
| A coordinator forwards its client to deeper operations | Trace all recipients before narrowing the dependency contract. |
| A consumer uses one stable capability of a large provider | Choose a callback, role or appropriate projection; preserve meaningful result and lifetime requirements. |
| A Pick includes a fluent method returning polymorphic this | Inspect the retained receiver/result relationship; do not claim it creates an independently implementable role. |
| A narrower handler passes a method-shaped assignment | Check the substitutability requirement rather than relying on method bivariance. |
| A pool satisfies the same method shape as an acquired session | Preserve session/transaction semantics in the contract and verify the actual resource boundary. |
| A borrowed dependency is closed by its consumer | Keep acquisition and teardown with the lifetime owner unless transfer was part of the contract. |
| A proposed interface imports the provider's internal result type | Decide whether the consumer needs that full contract or a stable local value; avoid both facade leakage and invented duplicate contracts. |
| An options call requires booleans and placeholder undefined values | Consider a small named parameter object while preserving defaults and public compatibility. |
| A passive record gains repeated derived calculations | Give behavior one owner, without requiring a class or an inheritance hierarchy. |
| Several implementations differ only in descriptor data | Consider one operation with typed data; do not force genuinely different semantics into a framework. |
| A pipeline exposes Partial of its eventual result between stages | Expose completed stage guarantees and keep mutable working state owned internally. |
| A type-only rewrite changes persisted or replayed values | Preserve serialization, interpretation, effects and compatibility obligations; typing alone proves none of them. |

## Selection and scope

| Request and context | Expected behavior |
| --- | --- |
| Refactor only a TypeScript simulation engine's module APIs and run-state lifetime | Stay inside the selected engine boundary, preserve runtime callers and behavior, and keep presentation/platform code on its existing path. |
| Fix one TypeScript exhaustive switch or parser/handler type relationship | Select TypeScript patterns; do not initiate a structural refactor. |
| Decide which application operation owns publication and recovery | Select application design; language alone does not decide ownership. |
| Change a repository's package exports or distribution boundary | Select repository design for that boundary; an internal API cleanup alone does not authorize it. |
| A framework defines an entrypoint shape | Preserve it and follow framework-specific guidance when lifecycle details matter. |
| Review a TypeScript design without implementing it | Report findings, evidence and the smallest recommendation; do not rewrite code. |
| A JavaScript-only task requests a literal presentation change | Do not activate this skill or infer a language migration. |

## Evidence limits

Compiler-example tests exercise the session and dependency examples, including
runtime isolation and receiver-free callbacks. They do not establish a whole
application's architecture, replay parity or framework integration. Tests need
Python 3.11+, Node 24 and TypeScript 5.0+ (`tsc` on PATH); the source gate supplies
its pinned compiler. Pure design cases require practical agent trials rather
than treating a passing compiler as design acceptance.
