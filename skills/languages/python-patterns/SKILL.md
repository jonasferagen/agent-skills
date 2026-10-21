---
name: python-patterns
description: "Write or review Python types, data boundaries, numerical comparisons, defaults, exceptions, resource cleanup and async tasks. Use for language correctness and failure handling, not for module layout or class organization."
metadata:
  version: "0.5.0"
---

# Python patterns

Apply focused Python language patterns. Read the project's instructions,
supported Python versions and existing checks before choosing syntax or tools.
If none are documented, infer the minimum version and tools from
`pyproject.toml` (`requires-python`, tool sections), CI configuration and
tool-version files, and state the assumption in your report. The examples
target Python 3.11 or later; adapt to the project's actual minimum. This skill
imposes no interpreter upgrade or package-manager migration.

The project's own instructions decide product contracts, framework choices,
tooling and testing. When they conflict with this skill, report the conflict
to the user, quoting both passages, and ask which to follow. Follow the user's
explicit decision.

## Workflow

1. Name the concrete failure or type relationship that needs attention.
2. Read the narrowest reference below and trace its effect through callers.
3. Preserve distinctions between valid emptiness, absence and failure. Choose
   a representation and an error boundary that keep those distinctions visible.
4. Make the scoped change, then run the project's relevant checks. If the
   project has none, run `python -m compileall` on the changed files and a
   small script or test that exercises the changed behavior, and say so in the
   report. A type checker verifies annotations; exercise runtime failures
   separately when the change depends on them. Report what each check actually
   established.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| A cast, annotation or protocol seems to promise validation | [Types and boundaries](references/types-and-boundaries.md) |
| Float comparisons, rounded keys or precision conversions lose distinctions | [Numbers and identity](references/numbers-and-identity.md) |
| Defaults leak between calls, or an empty value triggers a fallback | [Values and collections](references/values-and-collections.md) |
| A dataclass, iterator or collection has unclear mutation or ownership | [Values and collections](references/values-and-collections.md) |
| A small value type could be a NamedTuple or a frozen dataclass | [Values and collections](references/values-and-collections.md) |
| A failure becomes empty output, or cleanup is skipped | [Errors and resources](references/errors-and-resources.md) |
| Text I/O depends on the machine's default encoding | [Errors and resources](references/errors-and-resources.md) |
| An async task outlives its owner or hides failure | [Async work](references/async-work.md) |

## Scope and output

Leave the code with an honest type and failure contract, and say which checks
established it. Where operations and classes live is a structural decision
outside this skill; follow the project's existing layout. Use the project's
formatter, linter and type checker; do not add competing tools
or change coverage thresholds as part of an ordinary code edit.

This is a starting set, not a Python handbook. Packaging, framework architecture,
multiprocessing and performance tuning need task-specific guidance.
