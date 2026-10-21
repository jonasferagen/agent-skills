# Operations and state

## Choose by state and responsibility

A module-level function is a natural owner for an operation whose dependencies
and inputs are explicit and whose state lasts only for the call. A module
already supplies a namespace; a public operation need not acquire a wrapper
class. Put behaviour intrinsic to one domain value on that value when it
clarifies the contract.

```python
from collections.abc import Iterable

def invoice_total(amounts: Iterable[int]) -> int:
    return sum(amounts)
```

Use an instance when collaborators, configuration, a cache, mutable state or a
resource lifetime belong together across operations. Constructor injection makes
those dependencies visible. A one-shot builder can also be a useful class when
its methods coordinate substantial local working state; keep its mutation
private to that operation and expose the completed result.

A static method can group an operation with an existing value or service when
callers benefit from that association. A project may also choose a consistent
class-based API. Preserve such public contracts unless changing them is in scope;
do not add or remove wrappers solely to impose this skill's preference.
Do not hide mutable service state in class attributes or a global singleton.

Use `@classmethod` when the method needs `cls`, commonly an alternate constructor
that should respect subclass construction. Use `@staticmethod` when it needs
neither an instance nor the class. A method that reads or changes an instance
uses `self`. Keep a fixed workflow readable as named steps; extract collaborators
when their responsibilities or lifetimes differ, not to satisfy a line limit.

Preserve framework-discovered functions, fixtures, callbacks, decorators and
context-manager factories in their natural integration shape. A callback can
also be an existing bound or static method; no wrapper is needed merely to
change its category.

## Give a varied policy value its operation as owner

A policy value that tests or callers need to vary, such as a margin or limit,
belongs to the operation that applies it. Prefer a keyword-only or constructor
parameter whose default is the policy. A named default may live with its
owning module or class. Tests pass the value they
exercise rather than patching a module global. Such a patch changes the value
for every reader while it lasts and misses code that imported the name with
`from module import NAME`.

```python
from collections.abc import Iterable

DEFAULT_MARGIN = 0.10


def violations(gaps: Iterable[float], *, margin: float = DEFAULT_MARGIN) -> list[float]:
    return [gap for gap in gaps if gap < margin]
```

A test calls `violations(gaps, margin=0.6)`. The default is bound when the function
is defined, so patching `DEFAULT_MARGIN` later does not change it.

## Construction is a real boundary

Python has no enforced private constructor. An alternate `parse` or `from_*`
constructor does not prevent callers from using `Class(...)`. If every instance
must satisfy an invariant, validate ordinary construction as well, or make the
validated boundary's limited guarantee explicit. An underscore is an API
convention, not an access-control mechanism.

Keep invariants on the value; leave I/O, persistence and heavyweight adapters
with an owning service. Prefer composition to inheritance unless callers
actually rely on substituting subclasses. Repeated classes differing only in
fixed data are candidates for one class whose varying data lives in instance
attributes or a descriptor (an attribute object with `__get__`/`__set__`, as
`property` is), not another copy with a new name.

Source: [method binding](https://docs.python.org/3/library/functions.html#classmethod).
