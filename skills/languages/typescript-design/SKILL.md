---
name: typescript-design
description: "Apply the class-based TypeScript house style when shaping operations, domain values, dependency ports, naming, directories, barrels, resolution or orchestration. Use for code organization and ownership decisions."
metadata:
  version: "1.0.2"
---

# TypeScript design

Apply the class-based TypeScript house style. Exported operations use static
or stateful classes, with the narrow exceptions in
[class shape](references/class-shape.md#classes-and-managers).
Type checking and compiler settings remain the repository's language guidance.

<!-- Package-boundary copy: typescript-patterns/SKILL.md carries the same repository authority, workflow and output expectations. Keep both aligned. -->
**The repository's local docs own product facts: grammar, framework setup, enforcement commands, package
boundaries and paths, exemplars, mutable schemas, and domain facts. This package
owns the transferable method.** Read the repository's own instructions first.
When the local docs and this package really contradict each other, report it to
the user as documentation drift between two owners, quoting both passages. Do
not settle it by editing either side, and do not follow whichever rule is
easier. A repository links here rather than restating the shared rules in a
second canonical home.

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

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| A class, operation, constant or method has the wrong shape | [Class shape](references/class-shape.md) |
| A file needs a name, role, representation prefix or home | [Naming and placement](references/naming-and-placement.md), then [directories](references/directories.md) |
| A symbol, boolean or comment link needs a consistent name | [Naming conventions](references/conventions.md) |
| A helper reads one domain value, or inputs travel together | [Utilities and data](references/utilities-and-data.md), then [domain primitives](references/domain-primitives.md) |
| A call has too many positional arguments or placeholders | [Parameter objects](references/utilities-and-data.md#parameter-objects) |
| Overrides, defaults or absence decisions repeat | [Resolution and defaults](references/resolution.md) |
| A consumer uses only part of a concrete collaborator | [Dependency ports](references/dependency-ports.md) |
| A lifecycle or pipeline spreads across a shell | [Orchestration and pipelines](references/orchestration.md) |
| A barrel, public surface or external boundary is unclear | [Imports and barrels](references/imports-and-barrels.md) |
| Code needs design diagnostic questions | [Design review heuristics](references/review-heuristics.md) |

## Shape Escalation

Escalate a value to the next shape only when that step's trigger fires:

| Step | Current shape                          | Becomes                                                                                           | Trigger                                                                            |
| ---- | -------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1    | Positional parameters                  | [parameter object](references/utilities-and-data.md#parameter-objects)                            | optional values, same-shaped arguments, or placeholder `undefined`s obscure a call |
| 2    | Inline object                          | named contract ([type placement](references/naming-and-placement.md#type-placement-three-tiers))  | it escapes its local scope or is an options bag whose fields need names            |
| 3    | Fields that repeatedly travel together | [domain aggregate](references/utilities-and-data.md#parameter-bundling)                           | they share meaning or behavior                                                     |
| 4    | Passive data                           | [value object or domain primitive](references/class-shape.md#promoting-a-passive-type-to-a-class) | normalization, invariants, defaults, or derived values accumulate around it        |

Stop at a named passive contract for DTOs, wire shapes, results, and one-shot
inputs. Promote only values that travel with behavior or invariants.

## Output shape

Leave the code with one legible pattern and its obsolete shape removed,
synchronize local docs, and name the verification. When several patterns
plausibly fit, state the deciding trigger and why the alternatives do not match
the ownership or lifecycle in front of you.
