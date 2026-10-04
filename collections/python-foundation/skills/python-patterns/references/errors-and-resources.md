# Errors and resources

## Catch the failure you can handle

Keep the `try` block small enough that the handler cannot mistake an unrelated
failure for the one it expects. Prefer performing a filesystem operation and
handling its error to checking existence first: the state can change between
check and use. A simple mapping lookup with a default can use `get`; exception
handling is not a style requirement for every branch.

Translate an exception only where the caller needs a different abstraction,
using `raise DomainError(...) from exc` to retain its cause. Include useful
context without dumping secrets or an entire untrusted payload. Leave exceptions
unchanged when the caller can already act on them. Log at the boundary that
handles or reports the failure, avoiding duplicate logs at every rethrow.

Return `None` or an empty collection only when it is a valid domain outcome.
An unavailable service is not evidence that a search found no matches. Catch
`Exception` broadly only at an intentional reporting or isolation boundary;
do not turn interrupts, process exit or cancellation into success.

For text I/O, specify the encoding required by the file contract on both reads
and writes. Preserve locale-dependent handling when the locale is part of that
contract; do not assume every external file is UTF-8. Keep decoding failures
distinct from file acquisition errors and format syntax errors.

## Close what you acquire

Use `with` or `async with` for owned resources. Use `ExitStack` or
`AsyncExitStack` when acquisition is conditional or repeated; register each
cleanup as soon as its resource is acquired so later acquisition failure still
unwinds earlier resources. A borrowed resource remains its owner's to close.

In a generator context manager, cleanup belongs in `finally` around `yield`.
A class context manager suppresses a body exception if `__exit__` returns a
truthy value. Suppress only an explicitly handled failure. Do not use `return`
in `finally`, which can replace a pending return or exception.

This example translates only JSON syntax failure. Missing files, permission
errors and text-decoding failures retain their own meanings. It promises a
decoded JSON value, not validation against an application schema:

```python
import json
from pathlib import Path

class ConfigSyntaxError(ValueError):
    pass


def read_config(path: Path) -> object:
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ConfigSyntaxError(f"Invalid JSON in {path.name}") from exc
```

## Preserve subprocess outcomes

Use an argument sequence with `shell=False` for ordinary commands. Choose stdin
explicitly; use `DEVNULL` when the child must not read caller input. For a command
that must succeed, use `run(..., check=True, timeout=...)` with a task-appropriate
limit. Keep `CalledProcessError`, `TimeoutExpired` and startup `OSError`
distinguishable. On POSIX, a negative return code identifies a signal.

Capture output only when it is bounded; `capture_output=True` buffers in memory.
A timeout's output is partial. `Popen.communicate(timeout=...)` requires explicit
kill and drain after timeout, unlike `run`, which handles the direct child.
Neither promise implies that all descendants have been stopped.

Sources: [exceptions](https://docs.python.org/3/tutorial/errors.html),
[text file encoding](https://docs.python.org/3/library/functions.html#open),
[context managers](https://docs.python.org/3/library/contextlib.html),
[subprocess](https://docs.python.org/3/library/subprocess.html).
