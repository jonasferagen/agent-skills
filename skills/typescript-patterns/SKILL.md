---
name: typescript-patterns
description: "The shared TypeScript pattern canon for naming, types, classes, dependency ports, orchestration, resolution, imports and directory layout. Use whenever authoring or refactoring TypeScript: naming a file, type or symbol; a call site growing positional arguments or `undefined` placeholders; a consumer taking a whole collaborator but using one method; defaults, overrides and absence shapes piling up; barrels or public surfaces blurring; or a compiler flag or lint rule being added or weakened. Reach for it even when the request is only \"clean this up\", \"does this look right\" or \"make this more idiomatic\". Covers the shape of the code itself, not testing or review workflow."
metadata:
  version: "1.0.0"
---

# TypeScript Patterns

The shared pattern canon for shaping TypeScript code. **Local docs own product
facts — grammar, framework setup, enforcement commands, package boundaries and
paths, exemplars, mutable schemas, and domain facts; this package owns the
transferable method.** Read the repository's own instructions first, and treat
a real contradiction between those owners as documentation drift to reconcile,
not as permission to pick whichever rule is easier. A repository links here
rather than restating the shared rules in a second canonical home.

This skill shapes code as it is authored or refactored: the shape of the code
itself, not the workflow around it. Testing conventions belong to the
repository.

## Workflow

1. Name the smell or decision at the call site before choosing a pattern.
2. Read the narrowest matching reference below, plus any directly related page
   it names. Do not load the whole canon by default.
3. Trace the shape through its consumers, tests, and public boundary. A local
   simplification that makes the transitive contract dishonest is not simpler.
4. Apply the smallest pattern that makes the intent explicit. Prefer removing a
   bad shape over wrapping it in a compatibility layer.
5. Update repository-owned examples or enforcement prose when the shared
   pattern changes what they say, then run the repository's own focused checks
   and merge-boundary gate.

## Start By Symptom

| Symptom or decision                                                            | Read                                                                                                                              |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| A class, helper, constant, or method has the wrong shape                       | [Class shape](references/class-shape.md)                                                                                          |
| A file or symbol needs a name, role suffix, representation prefix, or home     | [Naming and placement](references/naming-and-placement.md), then [directory patterns](references/directories.md)                  |
| A boolean name does not read as a predicate                                    | [Events and booleans](references/typescript.md#events-and-booleans)                                                               |
| A generic, cast, tuple, brand, null, boolean, union, or mirror feels unsafe    | [TypeScript conventions](references/typescript.md) and [types and generics](references/types-and-generics.md)                     |
| A helper reads one domain value, or parameters repeatedly travel together      | [Utilities and data](references/utilities-and-data.md) and [domain primitives](references/domain-primitives.md)                   |
| A call has too many positional arguments or `undefined` placeholders           | [Parameter objects](references/utilities-and-data.md#parameter-objects)                                                           |
| A value comes from overrides, defaults, inheritance, or several absence shapes | [Resolution and defaults](references/resolution.md)                                                                               |
| A consumer accepts a concrete collaborator but uses only part of it            | [Dependency ports](references/dependency-ports.md)                                                                                |
| A lifecycle or pipeline is spreading across a shell or service locator         | [Orchestration and pipelines](references/orchestration.md)                                                                        |
| An import, barrel, public surface, or third-party boundary is unclear          | [Imports and barrels](references/imports-and-barrels.md)                                                                          |
| A compiler flag, lint rule, or gate stage is being added, weakened, or scoped | [Enforcement](references/enforcement.md)                                                                                          |
| A strictness flag reports a binding whose only job is to exist                | [Reading a strictness finding](references/enforcement.md#reading-a-strictness-finding)                                            |
| A rule catches a real defect class and a correct-by-construction idiom alike  | [When a rule cannot express its exemption](references/enforcement.md#when-a-rule-cannot-express-its-exemption)                    |
| An authoring pass needs diagnostic prompts before changing the shape           | [Review heuristics](references/review-heuristics.md)                                                                              |

## Shape Escalation

Let a value climb only when its trigger fires:

1. Positional parameters become a
   [parameter object](references/utilities-and-data.md#parameter-objects) when
   optional values, same-shaped arguments, or placeholder `undefined`s obscure
   a call.
2. An inline object becomes a named contract when it escapes its local scope or
   is an options bag whose fields need names
   ([type placement](references/naming-and-placement.md#type-placement-three-tiers)).
3. Repeatedly co-travelling fields become a
   [domain aggregate](references/utilities-and-data.md#parameter-bundling) when
   they share meaning or behavior.
4. Passive data becomes a
   [value object or domain primitive](references/class-shape.md#promoting-a-passive-type-to-a-class)
   when normalization, invariants, defaults, or derived values accrete around
   it.

Stop at a named passive contract for DTOs, wire shapes, results, and one-shot
inputs. Promote only values that travel with behavior or invariants.

## Output shape

Leave the code with one legible pattern, its obsolete shape removed, local docs
synchronized, and verification named. When several patterns plausibly fit,
state the deciding trigger and why the alternatives do not match the ownership
or lifecycle in front of you.
