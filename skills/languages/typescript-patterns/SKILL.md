---
name: typescript-patterns
description: "Write or review TypeScript types, narrowing, generics, absence, tuples, brands and module syntax. Use also for compiler strictness and lint enforcement; class organization and naming belong to adopted design guidance."
metadata:
  version: "2.0.3"
---

# TypeScript patterns

Apply TypeScript language patterns and type-safety conventions. This package
does not prescribe class-based operations, filename conventions or directory
layout. Repository design guidance owns those choices; typescript-design is a
suitable companion when available.

<!-- Package-boundary copy: typescript-design/SKILL.md carries the same repository authority, workflow and output expectations. Keep both aligned. -->
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
| A cast, tuple, brand, optional value or union feels unsafe | [Language conventions](references/typescript.md) |
| A table must cover every member of a vocabulary | [Fail-closed mirrors](references/typescript.md#fail-closed-mirrors) |
| A generic should preserve an input/output relationship | [Types and generics](references/types-and-generics.md) |
| An import spelling or type-only dependency is unclear | [Module imports](references/imports.md) |
| A compiler flag or lint rule is added, weakened or scoped | [Enforcement](references/enforcement.md) |
| Code needs type-safety diagnostic questions | [Type review heuristics](references/review-heuristics.md) |

## Output shape

Leave the code with one legible pattern and its obsolete shape removed,
synchronize local docs, and name the verification. When several patterns
plausibly fit, state the deciding trigger and why the alternatives do not match
the ownership or lifecycle in front of you.
