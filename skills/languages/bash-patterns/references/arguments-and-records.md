# Arguments and records

## Preserve argument boundaries

Store a command in an array, and invoke `"${command[@]}"`. Keep each argument as
one element; `"$@"` forwards the original positional arguments while `"$*"`
joins them. A scalar command string cannot preserve arbitrary boundaries without
reparsing; do not introduce `eval` or `bash -c` to undo that loss.

This function accepts a literal search value followed by file operands:

```bash
find_literal() {
    if (( $# < 2 )); then
        printf 'usage: find_literal NEEDLE FILE...\n' >&2
        return 2
    fi
    local needle=$1
    shift
    local -a command=(grep -F -e "$needle" --)
    "${command[@]}" "$@"
}
```

Quote data expansions in command arguments to avoid splitting and glob expansion.
Quoting does not stop option parsing: use `--` when the command supports it, or
an explicit operand form such as `./-report`. Some commands still treat `-` as
stdin after `--`; make literal path intent explicit when that matters.

Use a fixed `printf` format, such as `printf '%s\n' "$value"`; a value used as
the format can interpret percent directives and backslash escapes. In `[[ ]]`,
quote the right operand of `==` for literal equality; an unquoted right operand
is a pattern. For `=~`, decide deliberately whether regex syntax is intended.
Quoting alone does not validate an arithmetic expression: check external numeric
input and its range before arithmetic evaluation.

For option parsing, check argument count before reading `$2` or shifting two
positions. Distinguish a missing value from an explicitly empty value according
to the option's contract. Handle `--` and unknown options deliberately; nounset
errors are not a useful argument parser.

## Preserve record boundaries and producer failure

Do not iterate over `$(ls ...)` or whitespace-split command output. Paths can
contain whitespace and newlines. Use NUL-delimited records for arbitrary paths;
Bash can read each record into a variable even though a variable cannot contain
the NUL delimiter itself.

The following function expects an existing absolute input directory, a manifest
path (a temporary file the caller created and will remove, as in
[Resources and scope](resources-and-scope.md)), and a `process_file` function. It uses `find -print0`; verify that
option on the target platform. Acquisition finishes successfully before any
consumer side effects start:

```bash
process_tree() {
    local input_dir=$1 manifest=$2 file
    find "$input_dir/." -type f -print0 > "$manifest" || return "$?"
    while IFS= read -r -d '' file; do
        process_file "$file" || return "$?"
    done < "$manifest"
}
```

The manifest must be outside the searched tree. Redirecting a checked manifest
keeps loop state in the current shell and avoids losing `find`'s status through
process substitution. It costs disk space and does not freeze the files listed;
subsequent open failures still need handling. For line-oriented text, use
`IFS= read -r line`; add `|| [[ -n $line ]]` only if a final unterminated line
counts as a record. Do not accept a partial NUL-delimited record as a valid path.

For globs, choose empty-match behavior (`nullglob`, `failglob` or an explicit
check) and hidden-file policy. The default unmatched glob remains a literal
pattern. Scope option changes so they do not leak into callers.

Sources: [arrays](https://www.gnu.org/software/bash/manual/html_node/Arrays.html),
[conditional expressions](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html),
[ShellCheck SC2086](https://www.shellcheck.net/wiki/SC2086),
[find safe filename handling](https://www.gnu.org/software/findutils/manual/html_node/find_html/Safe-File-Name-Handling.html).
