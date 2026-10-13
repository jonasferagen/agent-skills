# Bash patterns scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Queries and streams

| Request and context | Expected behavior |
| --- | --- |
| `local output=$(producer)` inside a function | Flagged: the declaration reports `local`'s status, not the producer's. Split the declaration from the assignment. |
| `producer \| grep -q pattern` under `pipefail` | Flagged: the reader can close the pipe while the producer is still writing, and SIGPIPE turns a match into a failed pipeline. |
| The early limit is moved from `grep` into `sed q` | Still flagged when another command pipes into that `sed`; moving the limit does not remove the early reader. |
| A query reads a file directly rather than a pipe | Accepted: no upstream process exists to interrupt. |
| `grep ... >/dev/null` offered as a way to drain the producer | Rejected: GNU grep may stop reading once it knows output is discarded. |
| `\|\| true` proposed as a SIGPIPE remedy | Rejected: it discards real failures too and is not a general remedy. |
| `mapfile ... < <(producer)` | Flagged unless disregarding the producer's status is deliberate or that status is collected separately. |
| A stream must yield its first match and keep draining | An awk retain-and-continue shape is offered, with the caveat that awk's status does not distinguish absence. |
| Absence and query failure need different outcomes | Statuses are separated; grep's 1 for no match and 2 for error are distinguished. |
| Captured output must preserve trailing newlines or NUL bytes | Flagged: command substitution strips trailing newlines and Bash variables cannot carry NUL; a file or draining stream is used. |
| A here-string feeds possibly-empty input | Flagged where zero records must differ from one blank record, because the here-string adds a newline. |

## Status and control flow

| Request and context | Expected behavior |
| --- | --- |
| A function used as a condition relies on `set -e` | Flagged: that context suppresses it; required failures are propagated explicitly within the function. |
| Capture `$?` inside `if ! command` | Preserve the original status in an else branch before negation loses it. |
| A pipeline has two failing stages | Snapshot PIPESTATUS immediately; do not confuse pipefail's aggregate with both results. |
| A substitution fails before a successful final command | Do not treat its final zero status as evidence that every step succeeded. |
| A counter starts at zero under errexit | Avoid using post-increment's Boolean status as an accidental failure. |
| A background launch succeeds | Wait for its PID and collect the actual outcome; bare wait is insufficient. |
| A loop updates state in a pipeline | Account for subshell scope; a checked manifest can keep the loop in the parent. |

## Arguments and records

| Request and context | Expected behavior |
| --- | --- |
| A command contains empty arguments, spaces or wildcards | Preserve an array and quoted expansions; avoid reparsing with eval. |
| A quoted operand begins with a dash | Handle option parsing as well as shell quoting. |
| A literal search value contains a dot | Use fixed-string matching when regex semantics are unwanted. |
| A file name contains a newline | Use NUL records and check enumeration before consumption when failure matters. |

## Resources and scope

| Request and context | Expected behavior |
| --- | --- |
| Work and cleanup both fail | Preserve work failure, report cleanup failure; cleanup-only failure remains nonzero. |
| A sourced library installs global traps | Keep trap ownership with the caller or isolate the operation. |
| A temporary file is moved across filesystems | Do not claim atomic publication; acquire beside the destination and check writing first. |
| A universal strict-mode header is proposed as the fix | Rejected as universal; errexit does not catch every failure, and ownership of each status stays explicit. |

## Verification and adoption

| Request and context | Expected behavior |
| --- | --- |
| A changed check is verified by running it a few times | Called an observation, not proof; success, absence and acquisition failure are each exercised, with output large enough to expose a writer continuing past the match. |
| A custom syntax scanner is proposed to find these defects | Deprioritized in favour of the owning script's behavior tests and review: syntax alone does not establish whose status matters. |
| An existing application has different deployment or failure policy | Preserve its policy and keep changes scoped. |
| Adopting the skill into an existing project | No rewriting of working checks is implied; the repository's contracts decide whether an acquisition failure aborts or is tolerated. |

## Limits

- The fenced examples pass `bash -n`, and the stated behaviors were reproduced
  in 33 runtime cases on Bash 5.3 on Linux with GNU utilities, with disposable
  fixtures. Bash 3.2, BSD utilities and other shells are unverified; ShellCheck
  was not run.
- Atomic publication, hostile concurrent path replacement and process-tree
  shutdown are stated as limits, not established by probes.
