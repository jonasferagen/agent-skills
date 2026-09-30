---
name: bash-patterns
description: "Write or review Bash scripts that preserve argument boundaries, command status, query results and cleanup ownership. Use for pipelines, captures, file iteration, traps and background work; repository policy determines command intent and failure handling."
metadata:
  version: "0.2.0"
---

# Bash patterns

Read the repository's instructions, supported Bash version and required command
implementations first. They determine what commands should do and whether failed
acquisition must abort or may be handled as an optional operation. These patterns
do not impose a shell migration, logging framework or universal strict-mode header.

A Bash check must distinguish a match, a valid no-match result and a failure to
obtain input. Preserve the status and data needed to tell them apart regardless
of process timing or output size. Likewise, preserve argument boundaries and
make resource ownership explicit.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| A match changes with output size, or captured input hides failure | [Queries and streams](references/queries-and-streams.md) |
| A condition, pipeline or background job reports the wrong status | [Status and control flow](references/status-and-control-flow.md) |
| Spaces, empty values, globs or leading dashes change a command | [Arguments and records](references/arguments-and-records.md) |
| Temporary files, traps or file replacement have unclear ownership | [Resources and scope](references/resources-and-scope.md) |

## Verify the behavior

Trace which command owns each result before changing its shell syntax. Keep the
change scoped and run the repository's existing checks. Use `bash -n` for syntax
and ShellCheck when available; neither establishes runtime failure handling.

Exercise success, valid absence and acquisition failure, including partial
output followed by failure where meaningful. Include enough output to expose an
early reader, and arguments with spaces, wildcard characters, leading dashes and
empty values. For lifecycle changes, check cleanup and the original failure
status. Successful sampled runs do not prove an early-reader pipeline is safe.
Prefer behavior checks to a custom syntax scanner: syntax alone cannot identify
whose status matters. Report what ran and any platform assumptions.

This package owns Bash mechanics. Deployment policy, credential handling,
process supervision and whether a command may mutate a system remain with the
repository and the user's task. It does not authorize unrelated rewrites.
