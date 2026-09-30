# Status and control flow

## Handle the status before another command replaces it

Use an explicit branch when the original failure status matters:

```bash
if output=$(producer); then
    printf '%s\n' "$output"
else
    status=$?
    printf 'producer failed (%s)\n' "$status" >&2
    exit "$status"
fi
```

Inside a function, declare locals separately and use `return` for its contract.
In `if ! producer; then`, `$?` is the negated status, usually zero; capture the
original in an `else` branch instead. `A && B || C` also runs C when B fails,
so use `if` when C is meant only for A's false outcome.

`local`, `declare`, `export` and `readonly` can mask a command substitution's
status. Assign first, check it, then apply attributes. For `readonly`, declaring
an uninitialized variable and assigning later is itself an error.

## Treat shell options as context-sensitive checks

`set -e` has exceptions, including commands tested by `if`, `while`, `until`,
`!` and most positions in `&&`/`||` lists. A function invoked in such a context
also loses errexit behavior within its body. Explicitly propagate failures that
its contract needs. `ERR` traps have related exclusions; `set -E` changes trap
inheritance, not those exclusions.

Command substitution normally clears errexit in non-POSIX Bash unless
`inherit_errexit` is enabled. A successful last command can therefore hide an
earlier failure inside the substitution. Check multi-step work explicitly;
`inherit_errexit` is not a substitute for that review.

`set -u` distinguishes unset variables from empty values. `${value-default}`
uses a fallback only when unset; `${value:-default}` also replaces empty values.
Choose the intended contract. Arithmetic commands such as `((count++))` return
failure when their expression evaluates to zero; use `count=$((count + 1))`
when only assignment is intended, rather than suppressing arbitrary errors.

## Retain every status you need

With `pipefail`, the pipeline status is the rightmost nonzero status, not a
complete account of which stages failed. Snapshot `PIPESTATUS` immediately;
even an assignment or logging command replaces it. In this function fragment,
both branches collect the same vector so errexit cannot preempt inspection:

```bash
local -a statuses
if producer | consumer; then
    statuses=("${PIPESTATUS[@]}")
else
    statuses=("${PIPESTATUS[@]}")
fi
# Apply the caller's policy to statuses[0] and statuses[1].
```

A pipeline loop usually runs in a subshell; variable updates may not reach its
caller. Bash's `lastpipe` option can alter that behavior under specific job-control
conditions. Prefer redirecting a checked file into a loop when parent-shell
state matters, rather than depending on an ambient option.

A background launch's success is not the job's result. Capture `$!` immediately
and `wait "$pid"` for that job, saving a nonzero status through an explicit branch.
Bare `wait` waits for jobs but does not report each job's failure. For several
jobs, retain each PID and collect every result, including after an earlier
failure. Waiting is not cancellation; supervision, deadlines and descendants
need an explicit owning contract.

Sources: [set](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html),
[shopt](https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html),
[variables](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html),
[builtins](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html).
