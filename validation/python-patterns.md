# Validation scenarios — Python patterns

Version 0.1.0 starts a focused language and failure-handling package. Its
references cover selected patterns, not a complete Python style guide.

| Request and context | Expected outcome |
| --- | --- |
| JSON is cast to a TypedDict | Validate the runtime boundary; annotations and casts supply no validation. |
| An integer field receives `True` | Reject it when the domain excludes booleans, despite bool being an int subclass. |
| A timeout of zero becomes the default | Test absence explicitly and preserve meaningful zero. |
| Two dataclass instances share a list | Use a per-instance factory and make ownership explicit. |
| A frozen record contains a list | Do not claim deep immutability or assume it is hashable. |
| A generator is read twice | Recognize exhaustion; choose materialization only when repeated access and size justify it. |
| A file read fails before JSON parsing | Preserve acquisition failure separately from malformed JSON. |
| The second resource acquisition fails | Release the first through its owning context or ExitStack. |
| A subprocess times out or cannot start | Preserve distinct outcomes; do not collapse them into an exit code or empty success. |
| One TaskGroup child fails | Await sibling cancellation and cleanup; account for an exception group. |
| The caller cancels an async operation | Run cleanup and propagate cancellation. |
| gather uses return_exceptions=True | Include exception values in the result contract; never call them successful strings. |
| Work is sent to a thread | Do not claim task cancellation stops the running thread. |
| A semaphore guards a million created tasks | Bound task production too; a semaphore only limits active work. |
| A project supports Python 3.10 | Adapt syntax and concurrency choices without an implicit interpreter upgrade. |
| Asked to reorganize public operation classes | Select adopted design guidance separately. |
| Asked to migrate tooling or raise coverage | Defer to repository policy; this skill mandates neither. |

## Sources and adoption — 2026-09-30

[Everything Claude Code's Python patterns](https://github.com/affaan-m/everything-claude-code/blob/c70874fae9eb0e5ad0365beb7e2955899fd1d30f/skills/python-patterns/SKILL.md)
was inspected at `c70874fae9eb0e5ad0365beb7e2955899fd1d30f` (MIT,
copyright 2026 Affaan Mustafa). Protocols, dataclasses, exceptions, context
managers and concurrency were useful topics. This package does not reuse its
prose or examples. In particular, it avoids a gather example whose declared
string results could contain exceptions, representing errors as successful
strings, and blanket recommendations for slots.

[Trail of Bits' modern-python plugin](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python)
was inspected at `82fe8226252622fa807643bdca1710901198553a`
(CC-BY-SA-4.0). Its tooling focus helped define the boundary. No uv, ty or prek
migration, coverage threshold, SessionStart shim or other plugin code is
imported. Neither source underwent a full security audit. These are reviewed
references, not dependencies or trusted executable packages.

The prose and synthetic examples were written for this package. Each reference
links to official Python documentation supporting its language claims. Changes
should review those claims against the consuming interpreter range and inspect
any proposed upstream material afresh; there is no automatic upstream sync.

## Verification — 2026-09-30

The author reviewed every scenario above against the references. Clear writing
was applied to triggers, ownership and failure distinctions. Diagrams and tables
selected a symptom lookup and this scenario table; no lifecycle diagram was
needed for the individual patterns.

Across both Python packages, seven fenced examples parsed with Python 3.11's
syntax feature version and passed mypy 2.3.1 with `--strict --python-version
3.11`. Negative controls correctly rejected an incompatible protocol method
argument and an exception inserted into a declared string-result mapping.

Thirteen temporary runtime probes passed on CPython 3.11.15 and 3.14.4. They
covered integer boundary validation, independent mutable defaults, meaningful
zero, JSON success/syntax/acquisition distinctions, static operations, value
invariants and frozen mutation, protocol dependency use, partial acquisition
cleanup, subprocess success/nonzero/spawn failure/timeout, async success,
sibling cleanup after failure, caller cancellation, and exception-valued gather
results. The subprocess probes ran on Linux. These probes exercised the examples
and selected claims; they were not installed as skill helpers or consumer tests.

Package validation, isolated-copy validation, manifest checks, Markdown link
checks and whitespace checks passed. Both packages contain instruction files
and UI metadata only. No interpreter, formatter, checker or dependency manager
used during verification becomes a package requirement.

This is author review with executable probes, not an independent agent trial.
Live skill discovery, real consumer adoption, other platforms and every supported
Python version remain untested. The package is an unreleased starting set.

The entrypoint tables were rendered in a temporary 830-pixel content column
and inspected in external Chrome; text remained readable without horizontal
clipping. This was a local preview, not a check of every hosting renderer.
