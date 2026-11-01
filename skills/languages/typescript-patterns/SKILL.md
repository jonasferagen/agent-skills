---
name: typescript-patterns
description: "Write or review TypeScript validation, narrowing, exhaustive unions and registries, generics, collection access and readonly contracts. Use also for TypeScript compiler or module issues; code organization and JavaScript-only work are separate."
metadata:
  version: "3.0.0"
---

# TypeScript patterns

Make types describe what the code actually guarantees. Start at the project's
instructions and the affected package's compiler, runtime and check commands.
Read inherited compiler settings as well as local overrides. Use the project's
supported TypeScript version; examples use TypeScript 5.0 or later. Adapt to an
older supported version without silently upgrading it.

Keep the requested scope. The project owns architecture, class or function
style, naming, frameworks, validation libraries, failure policy and tooling.
Follow its choices and report a conflicting recommendation with the concrete
consequence. This skill does not authorize a JavaScript migration, broader
strictness rollout or reorganization.

## Work from the failure

1. Name the value, relationship or invariant the type must preserve, including
   the callers that depend on it. Distinguish trusted internal data from input
   crossing a runtime boundary.
2. Read the matching reference below. Choose the smallest representation that
   keeps the guarantee visible; avoid replacing an ordinary function with a
   generic framework or turning every primitive into a brand.
3. Exercise the guarantee at its actual boundary. Type relationships need a
   compiler check with valid and deliberately invalid callers. Runtime
   validation, copying and failure handling need runtime evidence too. Follow
   the project's checks and report what remains unverified.

A transpiler, bundler or type-stripping runtime may execute code without checking
its types. Confirm that the check command includes the changed source and its
relevant callers; a successful build alone does not establish type safety.

## Choose the reference

| Problem in the code | Read |
| --- | --- |
| External data is cast, a guard overpromises, or IDs can be confused | [Types and boundaries](references/types-and-boundaries.md) |
| States admit impossible combinations, a switch ignores a variant, or a table omits a member | [States and registries](references/states-and-registries.md) |
| Zero becomes a default, a lookup uses `!`, a tuple loses its shape, or a snapshot is still mutable | [Values and collections](references/values-and-collections.md) |
| A key loses its payload type, a parser loses its handler relationship, or generics require casts | [Generics and correlation](references/generics-and-correlation.md) |
| Compiler flags, JavaScript interop, import extensions or runtime globals disagree | [Toolchain and modules](references/toolchain-and-modules.md) |

Read only the relevant routes. JavaScript child-process behavior belongs to
Node patterns; operation ownership and module layout belong to the project's
adopted design guidance. Neither requires a TypeScript rewrite.
