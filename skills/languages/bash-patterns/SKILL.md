---
name: bash-patterns
description: "Write or review Bash scripts that preserve argument boundaries, command status, query results and cleanup ownership. Use for pipelines, captures, file iteration, traps and background work; the project decides what each command must do and which failures abort."
metadata:
  version: "0.3.0"
---

# Bash patterns

Read the project's instructions first: the Bash version it supports, which
command implementations it requires (GNU or BSD utilities, for example) and
what each script must do. Those decide whether a failed acquisition (input that
could not be read or produced) must abort or may be treated as an optional
step. When nothing documents them, infer them from the shebang lines, CI
configuration, container images and tool-version files, state the assumption
in your report, and ask the user when the choice changes behavior. When
nothing settles the version, assume Bash 4.4 or later and say so; feature
minimums are `wait -n` 4.3, `mapfile -d` and `inherit_errexit` 4.4, `${var@Q}`
4.4, `wait -p` 5.1. These patterns do not impose a shell migration, logging
framework or universal strict-mode header.

A check (any command whose status decides what the script does next) must
distinguish a match, a valid no-match result and a failure to obtain input.
Preserve the status and data needed to tell them apart regardless of process
timing or output size. Likewise, preserve argument boundaries and make resource
ownership explicit: for each result, name the command that owns it, meaning the
one whose status and output the script must report rather than a later
command that merely consumed them.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| A match changes with output size, or captured input hides failure | [Queries and streams](references/queries-and-streams.md) |
| A condition, pipeline or background job reports the wrong status | [Status and control flow](references/status-and-control-flow.md) |
| Spaces, empty values, globs or leading dashes change a command | [Arguments and records](references/arguments-and-records.md) |
| Temporary files, traps or file replacement have unclear ownership | [Resources and scope](references/resources-and-scope.md) |

## Verify the behavior

Trace which command owns each result before changing its shell syntax. Keep the
change scoped and run the project's existing checks. Use `bash -n` for syntax
and ShellCheck when available; neither establishes runtime failure handling.

Exercise success, valid absence and acquisition failure, including partial
output followed by failure where meaningful. Include enough output to expose an
early reader (a consumer such as `grep -q` or `head` that closes the pipe before
the producer has finished writing), and arguments with spaces, wildcard
characters, leading dashes and empty values. A fake producer makes the failing
case reproducible: `producer() { head -c 200000 /dev/zero | tr '\0' x; echo
match; return 3; }` emits more than a pipe buffer, then a match, then fails;
the check must report the failure, not a match. For changes to setup and
cleanup (temporary files, traps,
background jobs), check that cleanup runs and the original failure status
survives. Successful sampled runs do not prove an early-reader pipeline is safe.
Prefer behavior checks to a custom syntax scanner: syntax alone cannot identify
whose status matters. Report to the user what ran and any platform assumptions.

This skill covers Bash mechanics. Deployment rules, credential handling,
process supervision and whether a command may mutate a system are decided by
the project and the user's task. It does not authorize unrelated rewrites.
