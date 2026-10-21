# Resources and scope

## Own temporary resources and cleanup

Create a temporary directory with `mktemp -d`, check acquisition, then register
cleanup for precisely that directory. Use a task-specific variable; `TMPDIR` is
an existing environment input to temporary-file tools. Never clean a path borrowed
from an inherited variable as though this invocation created it.

This standalone-script example preserves a work failure if cleanup also fails;
a cleanup-only failure becomes the script result. The template syntax works with
GNU and BSD mktemp. It owns the script's traps:

```bash
#!/usr/bin/env bash
work_dir=$(mktemp -d "${TMPDIR:-/tmp}/bash-work.XXXXXXXX") || exit "$?"
cleanup() {
    local status=$? cleanup_status=0
    trap - EXIT
    rm -rf -- "$work_dir" || cleanup_status=$?
    if (( cleanup_status != 0 )); then
        printf 'temporary cleanup failed (%s)\n' "$cleanup_status" >&2
        if (( status == 0 )); then
            status=$cleanup_status
        fi
    fi
    exit "$status"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
# Perform checked work inside "$work_dir" here.
```

The INT/TERM handlers deliberately exit, then EXIT runs cleanup. They do not
promise immediate cancellation of foreground children or process trees. No trap
can handle SIGKILL or a machine crash. A reusable sourced library must not replace
its caller's traps; let the caller own cleanup or isolate the operation in a
subshell with its own scope. Define how interruptions and partial results are
reported rather than claiming that a trap makes every exit safe.

## Publish only completed output

Writing directly to a destination can truncate it before the producer fails.
When readers must see either the old file or the completed replacement, create a
temporary file in the destination directory, check the producer and validation,
then rename it over the destination. Clean the owned temporary file on failure.

Same-filesystem rename supplies atomic replacement of a directory entry; a move
from the system temporary directory may cross filesystems and become a copy.
Atomic visibility does not imply crash durability, preserved permissions/ACLs,
no-overwrite semantics or protection against concurrent writers. Set the required
metadata before publishing and use the project's locking (or `flock(1)` on a
lock file beside the destination when it has none) or a stronger storage
primitive when those guarantees matter. An existence test followed by `mv` does
not prevent a race; interactive flags are not an unattended conflict policy.

## Keep shell state local

Use a subshell for an operation that needs a different working directory or shell
options without changing its caller. Check `cd` before relative-path work. A
script that is sourced runs in the caller's shell: `exit`, `set`, `shopt`, traps
and working-directory changes can affect that caller. Keep library definitions
separate from executable entrypoints and preserve the existing integration form.

Use the supported Bash and utility versions. Associative arrays and `mapfile`
need Bash 4 or later; `wait -n` needs 4.3, `mapfile -d` and `inherit_errexit`
4.4. Check the specific feature instead of assuming every machine with Bash has it.

Sources: [mktemp](https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html),
[trap](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html),
[rename](https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html).
