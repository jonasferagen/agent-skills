---
name: bash-patterns
description: "Write or review Bash checks that preserve command failures and query results. Use for pipelines, command substitution, captured output and process substitution, especially when a check passes incorrectly or fails only with larger input. Repository guidance determines what each command should do."
metadata:
  version: "0.1.0"
---

# Bash Patterns

Read the repository's instructions first. They determine which checks exist,
what each check asserts and how it handles a failure to obtain input.

A Bash check must distinguish a match, a valid no-match result and a failure to
obtain input. Preserve the command status needed to tell these outcomes apart,
regardless of process timing or output size. Follow the repository's contract
when input cannot be obtained: it may require aborting, refusing an ownership
claim, or continuing with an optional best-effort operation.

## Choose the query shape

| Input | Shape |
| --- | --- |
| Existing shell array | A loop for one lookup; an associative array for repeated membership checks, when keys cannot be empty |
| File | Query it directly, for example `grep -m1 -- "$pattern" "$file"` |
| Small command output | Capture it, check whether the command succeeded, then inspect the captured value |
| Large stream | Consume to EOF while retaining the needed result |

Inside a function, a checked text capture can preserve the producer's status:

```bash
local output
output=$(producer) || return "$?"
grep -qx -- "$wanted" <<< "$output"
```

Keep the declaration separate: `local output=$(producer)` reports the status of
`local`, hiding the producer's status. Handle the query's status separately when
absence and query failure need different outcomes; grep uses 1 for no match and
2 for an error. Do not rely on `set -e` inside a function called as a condition:
that context suppresses it.

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

Do not assume `grep ... >/dev/null` will consume the whole stream. GNU grep may
stop reading when it knows its output is discarded.

`grep ... < <(producer)` and `mapfile ... < <(producer)` do not collect the
producer's status. Use process substitution only when disregarding that status
is deliberate, or when it is collected separately. Adding `|| true` to suppress
SIGPIPE failures also discards other failures, so it is not a general remedy.

## Verify the behavior

For a changed check, exercise a match, no match and failure to obtain input.
Include partial output followed by failure where meaningful. Use enough output
to expose a writer that continues after the reader finds a match. Successful
sampled runs do not prove that a pipeline with an early reader is safe.
Prefer the owning script's behavior tests and review to a custom syntax scanner:
syntax alone does not establish which command's status the check needs.
