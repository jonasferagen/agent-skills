# Values and collections

## Keep missing distinct from false

Use `value is None` when only absence selects a fallback. `value or default`
also replaces zero, false and empty containers. When omission and explicit
`None` mean different things, use a private sentinel or a separate argument;
name both meanings in the contract.

Defaults are evaluated when the function is defined. Allocate per-call mutable
state inside the call, and use `field(default_factory=...)` for per-instance
dataclass collections. Copy an input only when the callee should own a snapshot;
an unsolicited copy can break intentional sharing.

```python
from dataclasses import dataclass, field

@dataclass
class Batch:
    labels: list[str] = field(default_factory=list)


def choose_limit(limit: int | None, *, default: int) -> int:
    return default if limit is None else limit
```

## Choose a data representation deliberately

Use a dataclass for named fields with generated initialization and equality.
Use a plain mapping or `TypedDict` for a mapping-shaped boundary, especially
when a wire format is already defined. A tuple suits a positional contract;
use named fields when callers keep guessing what each position means.

Dataclasses do not validate annotations. Put an invariant in construction or a
validated boundary; a `__post_init__` check protects ordinary generated-init
construction, not arbitrary later mutation. `frozen=True` prevents ordinary
field assignment but does not freeze a nested list or dictionary. Use immutable
members for a value intended to stay stable. Choose `slots=True` for a concrete
memory or attribute-layout need, after checking inheritance and tooling; it is
not a universal improvement.

## Choose NamedTuple when tuple behavior is the point

Use `typing.NamedTuple` when callers rely on the value being a tuple: they
unpack it, sort or hash it element by element, or pass it to code that expects
a plain tuple. Grid cells, coordinates and small vectors are typical. Use a
frozen dataclass otherwise. A NamedTuple brings the whole tuple contract:
indexing, `len`, iteration, and equality with any tuple holding the same items,
including another NamedTuple type. It cannot override `__new__`, so a
construction invariant needs a frozen dataclass.

```python
from typing import NamedTuple

class Cell(NamedTuple):
    x: int
    z: int

    def step(self, dx: int, dz: int) -> "Cell":
        return Cell(self.x + dx, self.z + dz)

x, z = Cell(2, 3).step(1, 0)  # unpacks as (3, 3)
assert Cell(2, 3) == (2, 3)
assert min({Cell(1, 0), Cell(0, 5)}) == Cell(0, 5)
```

## Keep iteration and ownership visible

An iterator can be exhausted. If two consumers need independent passes, accept
a reusable collection or materialize once where its memory cost is acceptable.
Do not use a generator merely to hide a loop with side effects. Comprehensions
work for a simple transformation/filter; use a loop when the branches or error
handling deserve names.

A generator that opens a file can keep it open while suspended after `yield`.
When a consumer may stop early, make closure explicit: let the caller own the
file context, or expose a context-managed iterator. Do not rely on garbage
collection to release a resource promptly. Use `zip(..., strict=True)` when
unequal lengths are a defect, and ordinary `zip` when truncation is intended.

Sources: [defaults](https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects),
[dataclasses](https://docs.python.org/3/library/dataclasses.html),
[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple),
[zip](https://docs.python.org/3/library/functions.html#zip),
[closing](https://docs.python.org/3/library/contextlib.html#contextlib.closing),
[closing async generators](https://docs.python.org/3/library/contextlib.html#contextlib.aclosing).
