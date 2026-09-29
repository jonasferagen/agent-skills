---
name: shell-patterns
description: "Preserve command failures and query results while authoring or reviewing Bash checks, pipelines, captures and process substitutions. Use whenever a shell check decides something: a pipeline whose reader can stop early, a captured command substitution, a `local` declaration that swallows a producer's status, a `grep -q` or `head` in front of a still-writing producer, or a process substitution whose status nobody collects. Reach for it when a check passes and should not have, or fails only under load or on a larger input. Covers preserving the status that answers the question; repository docs own command-specific behavior."
metadata:
  version: "0.1.0"
---

# Shell Patterns

**Local docs own command-specific behavior — which checks exist, what each one
asserts, and whether an acquisition failure aborts or is tolerated; this package
owns the transferable method.** Read the repository's own instructions first.

Shell checks must distinguish a successful match, a successful absence, and a
failed acquisition. Preserve the status that answers each question, without
depending on scheduling or the current output size. Repository contracts decide
whether an acquisition failure aborts, refuses ownership, or permits an optional
best-effort operation.

## Choose the query shape

| Input | Shape |
| --- | --- |
| Existing shell array | A loop for one lookup; an associative array for repeated membership checks, when keys cannot be empty |
| File | Query it directly, for example `grep -m1 -- "$pattern" "$file"` |
| Small command output | Capture it, explicitly check acquisition status, then inspect the captured value |
| Large stream | Consume to EOF while retaining the needed result |

Inside a function, a checked text capture can preserve the producer's status:

```bash
local output
output=$(producer) || return "$?"
grep -qx -- "$wanted" <<< "$output"
```

Keep the declaration separate: `local output=$(producer)` reports the status of
`local`. Handle the query's status separately when absence and query failure need
different outcomes; grep uses 1 for no match and 2 for an error. Do not rely on
`set -e` inside a function called as a condition: that context suppresses it.

Command substitution removes trailing newlines and Bash variables cannot carry
NUL bytes. Use a file or a draining stream when those bytes matter. A here-string
adds a newline, so handle empty input explicitly if zero records differs from
one blank record. Take the first line of captured text with
`first=${output%%$'\n'*}` when that representation fits the contract.

## Read the whole pipeline

Under `pipefail`, an early reader can close its pipe while the writer is still
producing output. SIGPIPE then turns a successful match into a failed pipeline.
`grep -q`, `grep -m`, `head`, and `sed q` can all stop early. Moving the limit
into `sed` still leaves the defect when another command pipes into that `sed`.
An early query reading a file directly has no upstream process to interrupt.

For a stream, a reader can retain the first result and continue draining:

```bash
producer | awk '!found && /pattern/ { print; found = 1 }'
```

This emits the first match; awk's success status does not distinguish absence.
Test the retained output separately when the caller needs a predicate.

`grep ... >/dev/null` is not a portable promise to drain: GNU grep may stop
reading when it knows its output is discarded.

`grep ... < <(producer)` and `mapfile ... < <(producer)` do not collect the
producer's status. Use process substitution only when disregarding that status
is deliberate, or when it is collected separately. Blanket `|| true` handling
also discards real failures; it is not a general SIGPIPE remedy.

## Verify the behavior

For a changed check, exercise success, absence, and acquisition failure,
including partial output followed by failure where meaningful. Use output large
enough to expose an upstream writer continuing after the match. Zero failures in
sampled runs is an observation, not proof that an early-reader pipeline is safe.
Prefer the owning script's behavior tests and review over a custom syntax
scanner: syntax alone does not establish whose status matters.
