---
name: typescript-design
description: "Design or refactor the structure of TypeScript code: module APIs, functions, closures/classes, instance lifetimes and dependency interfaces. Use for local code organization; type correctness and application-wide operation ownership are separate."
metadata:
  version: "2.1.0"
---

# TypeScript design

Express a chosen responsibility through a clear TypeScript API, module and state
lifetime. Choose functions, closures, objects and classes by the contract they
serve. The project owns naming, framework conventions, runtime boundaries,
compiler versions and tools; read its instructions and the affected package's
configuration first. Preserve an established public style unless changing it is
part of the task.

Moving an existing operation's private state into a closure or instance,
reshaping its parameters, or narrowing a dependency interface stays within this
skill when its responsibilities and effects remain unchanged. Follow the local
reference directly; those code changes alone do not require loading general
application-design guidance.

## Work from a caller

1. Establish whether the request is a review, a plan or an implementation. Trace
   a representative caller through inputs, collaborators, state and results.
   Identify the concrete coupling, unclear lifetime or awkward API before
   proposing a shape.
2. Read the matching reference below. Express the responsibility with the
   smallest useful module, callable, value or instance. More files, interfaces,
   classes or immutable records are not evidence of better design.
3. Preserve public behavior and relevant callers during a scoped refactor. In
   a plan, name the migration boundary, compatibility obligations and checks
   needed before switching; a plan alone does not authorize a rewrite.
4. For implementation, check affected callers with the project's compiler and
   exercise the runtime contract that motivated the change. Report the design
   decision, evidence and remaining limits. A compiling interface does not prove
   resource ownership, independent state or preserved runtime behavior.

## Choose the reference

| Structural question | Read |
| --- | --- |
| Export a function, capture state in a closure, or create an instance? | [Operations and state](references/operations-and-state.md) |
| Where should contracts and exports live, who owns a shared record type, or why do imports cycle? | [Modules and surfaces](references/modules-and-surfaces.md) |
| Pass a callback, a narrow interface or a concrete dependency? | [Dependencies and composition](references/dependencies-and-composition.md) |
| Group arguments, place value behavior, or expose a completed stage result? | [Values and phases](references/values-and-phases.md) |

## Keep the responsibility boundary clear

This skill addresses how an agreed responsibility is represented in TypeScript.
Application design addresses which operation owns a rule or effect and how its
state is published or recovered. Repository design addresses distribution and
repository boundaries. Use those methods when the task actually changes those
decisions; a local API cleanup does not require an architecture review.

TypeScript patterns addresses validation, narrowing, exhaustive unions, generics,
readonly guarantees and compiler/module correctness. For example, choosing the
module that owns a stage result is a design question; proving its variants are
handled is a patterns question. Both may apply to one change, and each works
without the other installed.

Framework and platform lifecycles remain with their own guidance. A framework
entrypoint keeps its supported shape; this skill neither supplies a UI framework
nor authorizes a JavaScript migration or a new class-based house style.
