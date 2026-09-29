# Validation and alignment — Bash Patterns

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation or a live run.

| Request and context | Expected outcome |
| --- | --- |
| `local output=$(producer)` inside a function | Flagged: the declaration reports `local`'s status, not the producer's. Split the declaration from the assignment. |
| A function used as a condition relies on `set -e` | Flagged: that context suppresses it; the status is handled explicitly. |
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
| A changed check is verified by running it a few times | Called an observation, not proof; success, absence and acquisition failure are each exercised, with output large enough to expose a writer continuing past the match. |
| A custom syntax scanner is proposed to find these defects | Deprioritized in favour of the owning script's behavior tests and review: syntax alone does not establish whose status matters. |
| Adopting the skill into an existing project | No rewriting of working checks is implied; the repository's contracts decide whether an acquisition failure aborts or is tolerated. |

## Scope boundaries

Covers preserving command status and query results in Bash. It does not cover
shell style, portability to other shells, what a given repository's checks should
assert, or whether a failed acquisition should abort — the reading repository owns
those.

## Sources inspected

Imported from the owner's Forge Agent Kit `shell-patterns` skill at
`c98147a115a30f36b952df5faf1c869b54480c59` (2026-09-18) on 2026-09-29. The
upstream package carried no references to Forge systems, trackers or policy.
Its behavioral guidance is retained. The local package has its own manifest,
an explanation of what repository instructions decide, and clearer prose for
the command outcomes and failure cases.

## Review limits

- No independent agent evaluation has run against these scenarios.
- The guidance has not yet been applied to a shell suite in either consuming
  project, though both run shell that it covers: an encrypted backup and restore
  path in one, a test harness and service launcher in the other.
- Behavior is described for Bash. The early-reader and status-preservation rules
  generalize, but the specific constructs and exit codes are not verified against
  other shells.
