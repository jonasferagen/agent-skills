# Queries and streams

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

Do not assume `grep ... >/dev/null` will consume the whole stream. GNU grep
detects a discarded standard output and may stop at the first match as `-q`
does; the GNU manual documents `-q` as exiting immediately on the first match.
Confirm the installed grep's behavior rather than relying on it either way.

`grep ... < <(producer)` and `mapfile ... < <(producer)` do not collect the
producer's status. Use process substitution only when disregarding that status
is deliberate, or when it is collected separately. Adding `|| true` to suppress
SIGPIPE failures also discards other failures, so it is not a general remedy.


For literal whole-line membership use `grep -Fx -- "$wanted" "$file"`;
`-x` alone still interprets regular expressions. GNU grep uses 0 for a match,
1 for no match and 2 for an error; other implementations may use other statuses
above 1 for errors. Do not silently map query errors to absence.

Sources: [GNU grep](https://www.gnu.org/software/grep/manual/grep.html),
[Bash pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html).
