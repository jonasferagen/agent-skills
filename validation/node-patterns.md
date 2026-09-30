# Validation and alignment — Node Patterns

## Behavioral scenarios

These describe expected outcomes. Unless a trial below records otherwise, they
are author-reviewed scenarios, not results of an independent agent evaluation.

| Request and context | Expected outcome |
| --- | --- |
| `typeof error.code === 'number' ? error.code : 1` after `execFile` | Flagged: a timeout, a signal, a missing program, an abort and an output overflow all become exit 1. The error is classified from `code`, `signal` and `killed`. |
| A failure message built only from the child's stderr | Flagged: stderr is empty when the program never started or was killed first; the message names the outcome, such as a timeout or a missing program. |
| Output captured before a timeout or overflow is parsed as the answer | Flagged: that output is partial. |
| A `spawn` promise that settles only on `'exit'` | Flagged: a program that cannot start emits `'error'` and `'close'` but no `'exit'`, so the promise never settles. |
| `code ?? 0` in an `'exit'` or `'close'` handler | Flagged: a signal leaves `code` null, so a killed child reads as success. |
| `execFile` runs a program that may read stdin | Flagged unless stdin is closed or ignored: the default pipe stays open and the child waits for the timeout. |
| `stdio: 'inherit'` in a script that may be fed by a heredoc | Flagged unless the child should read the caller's input; `['ignore', 'inherit', 'inherit']` is offered. |
| `source.pipe(destination)` where the source can fail | Flagged: the error does not reach the destination; `pipeline()` from `node:stream/promises` is offered. |
| A database client or socket created without an `'error'` listener | Flagged: an unhandled `'error'` event ends the process. An empty listener is accepted only with a comment naming the path that reports the failure. |
| `console.error(problems); process.exit(1)` in a check script | Flagged: piped output can be cut off; `process.exitCode = 1` is used instead. |
| A signal handler that must exit immediately after cleanup | Accepted when it exits with 130 or 143, from the callback of its last write. |
| `new URL('..', import.meta.url).pathname` as a repository root | Flagged: percent-encoding breaks paths with spaces, and Windows paths gain a leading slash; `fileURLToPath` or `import.meta.dirname` is used. |
| A check prints "all files identical" | Flagged: a passing result names what it measured, and a check that measured nothing fails. |
| A changed script is verified by running it in a terminal | Called incomplete: output larger than a pipe buffer into a reader that waits, another working directory and a path with a space are also exercised. |
| Lost output is checked with `\| tail -1` or `\| wc -l` | Called insufficient: a fast reader drains the pipe before Node queues anything; a reader that waits before reading is used. |
| A request to choose which child output may contain secrets | Deferred to the project's operational guidance; this skill covers how Node reports outcomes. |
| Adopting the skill into a project with working scripts | No rewrite is implied; repository guidance decides what each script must report. |

## Scope boundaries

Covers how Node reports the outcome of child processes, streams, `'error'`
events and the script's own exit, and how a script finds files relative to
itself. It does not cover which output may hold secrets, how a child's
environment or arguments are built, or what a timeout should mean; the
runtime-operations skill and the reading project own those. Code structure
belongs to TypeScript or JavaScript guidance. Two rules are repeated from
runtime-operations, with a package-boundary comment on each copy: closing a
child's unneeded stdin, and naming a verdict's denominator.

## Sources inspected

The package was written from a review of the local atlas-work-dev repository at
`fb61765` on 2026-09-30. That repository is local only and has no remote.

- One idiom for reading an `execFile` result appears in seven places: the
  services' shared test Docker helper (copied into both services), the
  integration suite's Docker helper, the stack script, and three tests. Four
  copies fall back to `1` and three to `-1`.
- Two check scripts call `process.exit(1)` after printing their problems.
- One check script resolves its repository root from a URL path, while its two
  sibling scripts use `fileURLToPath`.
- The integration harness shows the practices the package keeps: a signal
  handler that cleans up and exits with 130 or 143, `'error'` listeners on
  database clients, and response bodies cancelled after readiness checks.

The package contains no project names, paths or identifiers.

## Verification results

Each stated behavior was reproduced with Node 24.15.0 on Linux on 2026-09-30,
in a scratch directory outside the source repository:

- `execFile` results: a non-zero exit, the `timeout` option, `child.kill()`, an
  external `SIGKILL`, an abort through `signal`, `ENOENT`, `EACCES` and a
  `maxBuffer` overflow produce the `code`, `signal` and `killed` values in the
  table. The `outcomeOf` example classifies all seven failure kinds as the
  table says.
- `spawn` of a missing program emits `'error'` and then `'close'` with code
  `-2`; `'exit'` does not fire.
- An `execFile` child running `cat` waits for its timeout; `child.stdin.end()`
  and `stdio: ['ignore', …]` let it finish.
- `.pipe()` leaves the destination unfinished and not destroyed after a source
  error; `pipeline()` rejects with that error.
- A socket with no `'error'` listener ends the process with an unhandled
  `'error'` event.
- About 3 MB written in one call before `process.exit(1)` was cut off when
  stdout or stderr was a pipe, and arrived complete when written to a file or a
  pseudo-terminal. Setting `process.exitCode`, or exiting from the write
  callback, delivered all of it.
- `new URL('..', import.meta.url).pathname` produced `dir%20with%20space/`, which
  does not exist; `fileURLToPath` produced the real directory. A `file:///C:/`
  URL's `pathname` starts with `/C:/`. `import.meta.dirname` is available in
  Node 24.

The package validator and `git diff --check` passed. Clear Writing guided the
drafting; no separate comparison pass was recorded.

## Pipe loss depends on the reader — 0.1.1

While fixing the atlas-work-dev check scripts on 2026-09-30, the old
`process.exit(1)` version of a check delivered all 12,002 problem lines through
`| cat` and `| wc -l`: many small writes each fit the pipe while a fast reader
drained it, so nothing was queued. The same script with a reader that waited
one second before reading delivered 803 lines, about one 64 KiB pipe buffer, on
two runs; the `process.exitCode` version delivered all 12,002 both times. Version
0.1.1 states that the loss needs a reader slower than the writer, and replaces
the `| tail -1` verification advice, which a fast reader passes, with a reader
that waits.

## Conformance trial — 2026-09-30

Two fresh agents received the same prompt: a strict conformance pass over every
`.mjs` file in atlas-work-dev against the repository's own conventions and
imported skills, finding the guidance themselves. The prompt did not mention
Node, child processes or this skill. The baseline ran at `fb61765` without the
package. The trial ran at `d100bd0`, where the package is installed and listed
in the repository's agent instructions. The three scripts differ between those
commits only by a new rules check in one of them.

**Discovery.** The trial agent found the package through the repository's agent
instructions, called it the main guidance for the files, and cited its sections
by name in each finding.

| Scenario above | Baseline, without the package | Trial, with it |
| --- | --- | --- |
| Collapsed `execFile` outcome | Noticed only a symptom: a missing Docker CLI reported as "not running", flagged as an unmet prerequisite | Flagged the idiom, confirmed the symptom with a stub, proposed classifying the error |
| `code ?? …` mapping of a signal | Not found | Flagged; 128 plus the signal number proposed |
| `execFile` stdin left open; `stdio: 'inherit'` | Not found | Both flagged; the trial confirmed inherited stdin reaching a stub |
| `process.exit(1)` after the problem list | Not found; the baseline praised another script's `process.exitCode` | Flagged in both check scripts; 593 of 4,001 problem lines got through a pipe |
| `.pathname` as the repository root | Found, through source-of-truth's anchoring rule | Found |
| A pass that measured nothing | Not found | Flagged in both check scripts; confirmed with empty service directories |
| Unreadable input reported as a failed comparison | Not found | Flagged |
| `spawn` promise that must settle | Not examined | Accepted: the script listens for `'error'` |

The package's scenarios for streams, `'error'` listeners and signal handlers had
no subject in these three files and were not exercised.

**Attention.** The baseline reported several findings the trial did not, all
outside this package's scope. Examples: a stack command that removes orphans for
any project name, an exported variable that overrides the run label, and
contract-check fallbacks that let malformed examples pass. With the package
installed, the strict pass concentrated on process behavior. A conformance pass
that should cover everything may need to name every applicable skill, or run
once per skill.

## Review limits

- The conformance trial is one run of each agent; it shows discovery and use,
  not a stable detection rate.
- Behavior was reproduced on Linux only. Pipe write behavior differs by
  platform, and Windows paths were checked only through URL parsing.
- The Node documentation's statement that stdio can remain open when `'exit'`
  fires was not reproduced; a 5 MB test delivered all output before `'exit'`.
  The package cites the documented behavior without claiming an observed case.
- An `EPIPE` on a child's stdin did not end the process in a test, so the
  package gives no example of it.
