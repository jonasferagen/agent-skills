# Validation and alignment — Bash Patterns

## Behavioral scenarios

These describe expected outcomes from the initial import. They are author-reviewed
scenarios; the later strengthening review records the runtime probes separately.

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

Covers preserving argument and record boundaries, command status, query results
and resource ownership in Bash. The reading repository owns command intent,
deployment policy and whether failed acquisition should abort. Other shells,
process supervision and a universal shell style are outside this package.

## Sources inspected

Imported from the owner's Forge Agent Kit `shell-patterns` skill at
`c98147a115a30f36b952df5faf1c869b54480c59` (2026-09-18) on 2026-09-29. The
upstream package carried no references to Forge systems, trackers or policy.
Its behavioral guidance is retained. The local package has its own manifest,
an explanation of what repository instructions decide, and clearer prose for
the command outcomes and failure cases.

## Review limits

- No independent agent evaluation has run against these scenarios.
- At the initial review, the guidance had not been applied to a shell suite in either consuming
  project, though both run shell that it covers: an encrypted backup and restore
  path in one, a test harness and service launcher in the other.
- Behavior is described for Bash. The early-reader and status-preservation rules
  generalize, but the specific constructs and exit codes are not verified against
  other shells.

## Strengthening review — 2026-09-30

Version 0.2.0 keeps the original query and pipeline rules in
`references/queries-and-streams.md`. Three new references cover status/control
flow, argument/record boundaries, and resource/shell-state ownership. The
entrypoint routes by symptom. This is a compatible expansion of the existing
skill; no second Bash skill or toolchain migration is introduced.

### Prior art and adoption

Reviewed [wshobson/agents bash-defensive-patterns](https://github.com/wshobson/agents/tree/156b7a5e7a8b93642628a339ee4039c925b34c7f/plugins/shell-scripting/skills/bash-defensive-patterns)
at `156b7a5e7a8b93642628a339ee4039c925b34c7f`, including its detailed reference
(MIT, copyright 2024 Seth Hobson). Arrays, temporary resources, argument parsing
and file publication were useful subjects to assess. The new prose and examples
are independently authored; no third-party files, hooks or helpers were copied.
This was a content review, not a full repository security audit.

Rejected a universal strict-mode header and the claim that errexit catches every
failure. Retained our producer-status rule where upstream process substitutions
omit it. Replaced inherited TMPDIR cleanup with ownership of a freshly acquired
path. The resource reference also corrects the assumption that a system-temp
file followed by mv necessarily gives atomic replacement. Sourced libraries,
cleanup failures and concurrent writers retain explicit limits.

The references link to Bash, GNU utility and POSIX documentation, plus
ShellCheck's argument-expansion guidance. The installed Bash builtin help and
runtime probes supplied local evidence when GNU's website timed out. Upstream
updates require fresh review; the package has no automatic upstream dependency.

### Added scenarios

| Request and context | Expected outcome |
| --- | --- |
| Capture `$?` inside `if ! command` | Preserve the original status in an else branch before negation loses it. |
| A pipeline has two failing stages | Snapshot PIPESTATUS immediately; do not confuse pipefail's aggregate with both results. |
| A function tested by if relies on errexit | Propagate required failures explicitly within the function. |
| A substitution fails before a successful final command | Do not treat its final zero status as evidence that every step succeeded. |
| A counter starts at zero under errexit | Avoid using post-increment's Boolean status as an accidental failure. |
| A background launch succeeds | Wait for its PID and collect the actual outcome; bare wait is insufficient. |
| A command contains empty arguments, spaces or wildcards | Preserve an array and quoted expansions; avoid reparsing with eval. |
| A quoted operand begins with a dash | Handle option parsing as well as shell quoting. |
| A literal search value contains a dot | Use fixed-string matching when regex semantics are unwanted. |
| A file name contains a newline | Use NUL records and check enumeration before consumption when failure matters. |
| A loop updates state in a pipeline | Account for subshell scope; a checked manifest can keep the loop in the parent. |
| Work and cleanup both fail | Preserve work failure, report cleanup failure; cleanup-only failure remains nonzero. |
| A sourced library installs global traps | Keep trap ownership with the caller or isolate the operation. |
| A temporary file is moved across filesystems | Do not claim atomic publication; acquire beside the destination and check writing first. |
| An existing application has different deployment or failure policy | Preserve its policy and keep changes scoped. |

### Actual verification

All seven fenced Bash examples passed `bash -n`. A temporary Python-driven
harness ran 33 runtime cases successfully on Bash 5.3.9/Linux with GNU utilities.
It exercised capture success/absence/partial failure, errexit suppression,
substitution failure masking, negation, arithmetic status, both pipeline statuses,
background failure and bare wait, loop scope, empty defaults, newline stripping,
pattern versus literal equality, literal grep success/absence/error/usage,
NUL filenames (spaces, newline, wildcard, backslash, leading dash), enumeration
and consumer failures, cleanup success/work failure/cleanup failure/both failures,
TERM cleanup, failed acquisition, a large early-reader SIGPIPE case, and a draining
reader with successful and failed producers. The harness used disposable fixtures
and was not installed as a skill helper.

The author reviewed every original and added scenario against the final text.
Clear writing preserved the original caveats and made ownership and conditions
explicit. Diagrams and tables selected a compact symptom lookup and scenario
matrix; no diagram was needed. Package, isolated-copy, manifest, local Markdown
link and whitespace checks passed. ShellCheck was unavailable and was not run.

No independent agent evaluation, Bash 3.2/BSD runtime trial or application-script
migration is claimed. Atomic publication, hostile concurrent path replacement and
process-tree shutdown were reviewed as limits, not established by these probes.

The entrypoint lookup was rendered in a temporary 830-pixel content column and
inspected in external Chrome; no clipped text or horizontal overflow was visible.
