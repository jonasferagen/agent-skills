---
name: python-patterns
description: "Write or review Python types, data boundaries, defaults, exceptions, resource cleanup and async tasks. Use for language correctness and failure handling; class organization belongs to adopted design guidance."
metadata:
  version: "0.2.0"
---

# Python patterns

Apply focused Python language patterns. Read the repository's instructions,
supported Python versions and existing checks before choosing syntax or tools.
The examples target Python 3.11 or later; adapt to the project's actual minimum.
This skill imposes no interpreter upgrade or package-manager migration.

<!-- Package-boundary copy: python-design/SKILL.md carries the same repository authority rule. Keep both aligned. -->
The repository owns product contracts, framework choices, tooling and test
policy. When its instructions conflict with this package, report both passages
rather than silently changing either owner. Follow the user's explicit decision.

## Workflow

1. Name the concrete failure or type relationship that needs attention.
2. Read the narrowest reference below and trace its effect through callers.
3. Preserve distinctions between valid emptiness, absence and failure. Choose
   a representation and an error boundary that keep those distinctions visible.
4. Make the scoped change, then run the repository's relevant checks. A type
   checker verifies annotations; exercise runtime failures separately when the
   change depends on them. Report what each check actually established.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| A cast, annotation or protocol seems to promise validation | [Types and boundaries](references/types-and-boundaries.md) |
| Defaults leak between calls, or an empty value triggers a fallback | [Values and collections](references/values-and-collections.md) |
| A dataclass, iterator or collection has unclear mutation or ownership | [Values and collections](references/values-and-collections.md) |
| A failure becomes empty output, or cleanup is skipped | [Errors and resources](references/errors-and-resources.md) |
| Text I/O depends on the machine's default encoding | [Errors and resources](references/errors-and-resources.md) |
| An async task outlives its owner or hides failure | [Async work](references/async-work.md) |

## Scope and output

Leave the code with an honest type and failure contract, and name the evidence.
The repository's design guidance determines where operations and classes live.
Use the project's formatter, linter and type checker; do not add competing tools
or change coverage thresholds as part of an ordinary code edit.

This is a starting set, not a Python handbook. Packaging, framework architecture,
multiprocessing and performance tuning need task-specific guidance.
