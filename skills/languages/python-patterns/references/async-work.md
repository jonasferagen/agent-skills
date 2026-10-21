# Async work

## Give related tasks an owner

For related work that should fail as one unit, use `asyncio.TaskGroup` on Python
3.11 or later. It waits for its children; an ordinary child failure cancels the
remaining children and is reported through an exception group. Account for that
exception shape where the operation is handled.

```python
import asyncio
from typing import Protocol

class TextSource(Protocol):
    async def read(self, key: str) -> str: ...


async def read_pair(source: TextSource) -> tuple[str, str]:
    async with asyncio.TaskGroup() as tasks:
        first = tasks.create_task(source.read("first"))
        second = tasks.create_task(source.read("second"))
    return first.result(), second.result()
```

On Python 3.10 or earlier, where `TaskGroup` is absent, use `gather` and cancel
the remaining tasks yourself in an `except` block, or a task-group backport the
project already depends on.

Use `gather` when its semantics fit: default failure propagation does not cancel
all sibling work. With `return_exceptions=True`, results contain exceptions as
well as values; inspect and represent both before returning a success type.
A deliberately detached task needs an owner that retains it, observes failures
and joins or cancels it during shutdown.

## Preserve cancellation and bound work

Put cleanup in `finally`. If `CancelledError` is caught for cleanup, re-raise it.
Choose timeouts where their meaning is known to the caller. Do not swallow
cancellation inside a retry loop.

Keep blocking I/O off the event loop. `asyncio.to_thread` can adapt a blocking
call, but cancellation of its await does not stop an already running thread.
The underlying operation still needs its own deadline and resource owner.

Set concurrency from the resource being protected. A semaphore bounds active
work, not the number of tasks already created; a large or unbounded input needs
bounded submission or a worker queue. Reuse clients within their supported
lifetime instead of constructing one connection pool per item.

Verify success, child failure, caller cancellation and cleanup. A happy-path
result does not establish that sibling work stopped or resources were released.

Source: [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html).
