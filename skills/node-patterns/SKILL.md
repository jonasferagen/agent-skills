---
name: node-patterns
description: "Write or review Node.js scripts, command-line tools and test harnesses so that their exit status and output report what actually happened. Use when code runs child processes (execFile, exec, spawn), sets an exit status, pipes streams, handles 'error' events or signals, or finds files relative to its own module; especially when a failure is reported as the wrong kind, output is cut off, or a script works only from one directory. Repository guidance determines what each script should do."
metadata:
  version: "0.1.1"
---

# Node Patterns

Read the repository's instructions first. They determine which scripts exist,
what each one checks and what should happen when it fails.

A Node script that runs another program must distinguish three outcomes: the
program succeeded, the program ran and reported a failure, and the program did
not run to completion. The last includes a missing executable, a timeout, a
signal and output larger than the script agreed to hold. Keep the facts that
separate these outcomes until the code that decides the result, and put them in
the message a person reads. The script's own result needs the same care: its
exit status and final output must survive until the process ends.

This skill covers how Node reports those outcomes. The project's operational
guidance decides which output may hold secrets, how to build a child's
environment and arguments, and what a timeout should mean. Code structure
belongs to its TypeScript or JavaScript guidance.

## Keep a child's outcome

`execFile` and `exec` pass a single `error` to their callback for every kind of
failure. Read three of its fields before deciding what happened:

| What happened | `error.code` | `error.signal` | `error.killed` |
| --- | --- | --- | --- |
| Exited with status 0 | `error` is `null` | | |
| Exited with a non-zero status | that status, a number | `null` | `false` |
| Stopped by the script: the `timeout` option or `child.kill()` | `null` | the signal sent, `SIGTERM` by default | `true` |
| Killed by a signal from elsewhere | `null` | that signal | `false` |
| Aborted through the `signal` option | `'ABORT_ERR'` | not set | not set |
| Did not start | a string such as `'ENOENT'` or `'EACCES'` | not set | not set |
| Output exceeded `maxBuffer` | `'ERR_CHILD_PROCESS_STDIO_MAXBUFFER'` | not set | not set |

This common shortcut turns every row after the second into "exit 1":

```js
// Reports a timeout, a signal, a missing program and truncated output as exit 1.
const code = error === null ? 0 : typeof error.code === 'number' ? error.code : 1;
```

Classify the error instead, and keep the classification until the caller
decides what it means:

```js
function outcomeOf(error) {
  if (error === null) return { kind: 'exited', status: 0 };
  if (typeof error.code === 'number') return { kind: 'exited', status: error.code };
  if (error.killed) return { kind: 'stopped', signal: error.signal };
  if (error.signal) return { kind: 'signaled', signal: error.signal };
  return { kind: 'not_completed', reason: error.code ?? error.message };
}
```

Name the outcome in the error message: "timed out after 120 s", "docker was not
found", "output exceeded 64 MiB". A message built only from the child's stderr
is empty when the program never started or was killed before writing, which is
when the reader most needs it. When a timeout or overflow stops the child, the
captured output is partial; do not parse it as a complete answer.

If a helper must reduce the outcome to one number, use the shell convention of
128 plus the signal number for a signal (`os.constants.signals` holds the
numbers). A missing program is still not the same as that program exiting 1, so
report the reason alongside the number.

## Wait for the right spawn events

- Listen for `'error'` as well as `'close'`. When the program cannot start,
  `'error'` fires and `'exit'` does not. `'close'` still fires, with a negative
  code: the error number, such as `-2` for `ENOENT`. A promise that waits only
  for `'exit'` never settles.
- Use `'close'` when you read the child's output. Node documents that the
  child's stdio streams may still be open when `'exit'` fires; `'close'` fires
  after they end.
- In both events, `code` is `null` exactly when `signal` is set. Map that case
  deliberately: `code ?? 0` reports a killed child as a success.

## Close input the child does not need

<!-- Package-boundary copy: runtime-operations/SKILL.md (Child processes) states this rule for any language. Keep both passages aligned. -->
By default, `execFile`, `exec` and `spawn` give the child a stdin pipe and never
close it. A child that reads stdin when it is not a terminal then waits until a
timeout kills it, and the script reports a timeout or an unexplained failure.
Pass `stdio: ['ignore', 'pipe', 'pipe']` to `spawn`, or call `child.stdin.end()`
on the child that `execFile` returns.

`stdio: 'inherit'` shares the script's own stdin with the child. A script fed by
a heredoc or a pipe hands that input to the child, which may parse it as its own.
Use `['ignore', 'inherit', 'inherit']` unless the child should read the caller's
input.

## Connect streams with pipeline

`source.pipe(destination)` does not pass a source error to the destination: the
destination neither finishes nor is destroyed. A script that waits for the
destination then hangs. If nothing listens for errors on the source, the error
crashes the process instead. `pipeline()` from `node:stream/promises` destroys
every stream when one fails and rejects with that error, much as `pipefail`
does for a shell pipeline.

## Handle every 'error' event

An `'error'` event with no listener is thrown and ends the process with a stack
trace. Child processes, sockets, streams, servers and database clients report
failures this way. Some emit errors when no operation is in progress, such as an
idle pooled database connection that the server closes.

Attach a listener to each emitter you create and decide what its error means:
fail the pending operation, record the error for the next operation, or log it.
An empty listener hides the failure. Use one only when another path reports the
same failure, such as the next query on a broken connection failing, and say so
in a comment.

## Finish output before exiting

`process.exit()` ends the process without waiting for writes to stdout or
stderr that are still queued. Node queues a write to a pipe once the pipe is
full, so output is lost when the reader is slower than the script. In a test
with Node 24 on Linux, a reader that waited one second before reading received
803 of 12,002 lines written before `process.exit(1)`, about one pipe buffer. A
file, a terminal and a fast reader such as `cat` received every line. The loss
therefore appears with busy log collectors and slow consumers, and rarely when
the script runs in a terminal.

- Set `process.exitCode` and return. The process then ends after its work and
  pending writes finish.
- If the process must end at once, such as at the end of a signal handler, call
  `process.exit()` from the callback of the last write.
- When the script handles `SIGINT` or `SIGTERM` to clean up, exit with 128 plus
  the signal number: 130 for `SIGINT` and 143 for `SIGTERM`. The caller then sees
  an interruption, not a success or an ordinary failure.

## Find files from the module

Resolve paths relative to the script with
`fileURLToPath(new URL('..', import.meta.url))`, or with `import.meta.dirname`
where the supported Node versions provide it (20.11 and later).

`new URL('..', import.meta.url).pathname` keeps URL encoding. A directory named
`my repo` becomes `my%20repo`, which does not exist on disk, and on Windows the
result starts with `/C:/`. Paths relative to `process.cwd()` break when the
script runs from another directory. Use the working directory only for paths the
caller supplies.

## Report a check's result

A check script usually reports every problem it finds, not only the first.
Collect the problems, print them, then set `process.exitCode = 1`.

<!-- Package-boundary copy: runtime-operations/SKILL.md (Verification) states this denominator rule. Keep both passages aligned. -->
A passing result names what it measured: "14 files compared", not "all files
identical". When the check measured nothing, because it found no files, an empty
directory or a filter that matched nothing, fail instead of passing. Report
input the check could not read, such as a missing directory, as its own problem,
separate from a comparison that failed.

## Verify the behavior

For a changed script or helper, exercise success, a non-zero exit, a program
that is not installed and a timeout. Where the script sets an output limit,
exceed it. Each case should produce its own message and status.

To catch lost output, write more than a pipe buffer holds (64 KiB on Linux) into
a reader that waits before reading, as in `node script.mjs 2>&1 | (sleep 1; wc -l)`,
and compare the count with the same output written to a file. A fast reader can
hide the loss. Run the script from another directory and from a path that
contains a space. Successful runs in a terminal do not show that output survives
a pipe or that paths resolve elsewhere.
