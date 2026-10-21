# Node patterns scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| `typeof error.code === 'number' ? error.code : 1` after `execFile` | Flagged: a timeout, a signal, a missing program, an abort and an output overflow all become exit 1. The error is classified from `code`, `signal` and `killed`. |
| A failure message built only from the child's stderr | Flagged: stderr is empty when the program never started or was killed first; the message names the outcome, such as a timeout or a missing program. |
| Output captured before a timeout or overflow is parsed as the answer | Flagged: that output is partial. |
| A child catches the termination signal and exits 0 after the wrapper's timeout or `kill()` | The wrapper's timeout or cancellation decision stands; a null `error` does not undo it. |
| A `spawn` promise that settles only on `'exit'` | Flagged: a program that cannot start emits `'error'` and `'close'` but no `'exit'`, so the promise never settles. A script that also listens for `'error'` is accepted. |
| `code ?? 0` in an `'exit'` or `'close'` handler | Flagged: a signal leaves `code` null, so a killed child reads as success; 128 plus the signal number is the one-number mapping. |
| `execFile` runs a program that may read stdin | Flagged unless stdin is closed or ignored: the default pipe stays open and the child waits for the timeout. |
| `stdio: 'inherit'` in a script that may be fed by a heredoc | Flagged unless the child should read the caller's input; `['ignore', 'inherit', 'inherit']` is offered. |
| `source.pipe(destination)` where the source can fail | Flagged: the error does not reach the destination; `pipeline()` from `node:stream/promises` is offered. |
| A database client or socket created without an `'error'` listener | Flagged: an unhandled `'error'` event ends the process. An empty listener is accepted only with a comment naming the path that reports the failure. |
| `console.error(problems); process.exit(1)` in a check script | Flagged: piped output can be cut off when the reader is slower than the writer; `process.exitCode = 1` is used instead. |
| A signal handler that must exit immediately after cleanup | Accepted when it exits with 130 or 143, from the callback of its last write. |
| `new URL('..', import.meta.url).pathname` as a repository root | Flagged: percent-encoding breaks paths with spaces, and Windows paths gain a leading slash; `fileURLToPath` or `import.meta.dirname` is used. |
| A check prints "all files identical" | Flagged: a passing result names what it measured, and a check that measured nothing fails. |
| A check reports an unreadable input directory as a failed comparison | Flagged: input the check could not read is its own problem, separate from a comparison that failed. |
| A changed script is verified by running it in a terminal | Called incomplete: output larger than a pipe buffer into a reader that waits, another working directory and a path with a space are also exercised. |
| Lost output is checked with `\| tail -1` or `\| wc -l` | Called insufficient: a fast reader drains the pipe before Node queues anything; a reader that waits before reading is used. |
| A request to choose which child output may contain secrets | Deferred to the project's conventions or the user; this skill covers how Node reports outcomes. |
| Applying the skill to an existing codebase with working scripts | No rewrite is implied; the project's conventions decide what each script must report, and only the defects named here are changed. |
| A CommonJS script uses `import.meta.url` | Flagged: `import.meta` is unavailable there; `__dirname` is used. |

## Checks

`tests/test_examples.py` runs the `outcomeOf` example from `SKILL.md` against
real child processes: a clean exit, a non-zero status, a missing executable, a
closed stdin, the `timeout` option, a `maxBuffer` overflow, an abort, a child that
exits 0 after `kill()`, and an external `SIGKILL`. Run it from the package
directory with `python3 -m unittest discover -s tests`. It needs Python 3.11 or
later and `node` on `PATH`, and fails explicitly when `node` is absent.

## Limits

- Behavior is verified on Node 24 on Linux. Pipe write behavior differs by
  platform, and Windows paths were checked only through URL parsing.
- The lost-output case needs a reader slower than the writer: a fast reader
  such as `cat` receives everything, which is why the verification advice uses
  a reader that waits.
- Node documents that a child's stdio can remain open when `'exit'` fires; this
  was not reproduced, so the skill cites the documented behavior without an
  observed case.
- The skill gives no example of `EPIPE` on a child's stdin; that case is
  unverified.
- The test's children read and write fds 0 and 1 directly: a sandbox that
  denies `getsockname`, as one without network access can, makes Node give a
  child placeholder stdin and stdout.
