# Values and call sites

## Name call inputs before inventing a container

Python keyword-only arguments often solve a call-site problem directly:
`send(message, *, retry_limit=3, urgent=False)` lets callers name policy without
passing placeholder values. Keep a small obvious positional signature when it
reads naturally. Introduce an input dataclass when fields repeatedly travel
together or have shared meaning, not for every function with optional arguments.

## Give invariants one owner

A dataclass can be a passive record or a value object with behavior. A wire DTO
stays a transport contract; an internal value can own validation and derivation.
The following value has one invariant regardless of whether callers use a
factory. Its fields are immutable scalars:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class PageWindow:
    start: int
    stop: int

    def __post_init__(self) -> None:
        if (isinstance(self.start, bool) or not isinstance(self.start, int)
                or isinstance(self.stop, bool) or not isinstance(self.stop, int)):
            raise ValueError("page bounds must be integers")
        if self.start < 0 or self.stop < self.start:
            raise ValueError("page bounds must be ordered and non-negative")

    @property
    def length(self) -> int:
        return self.stop - self.start
```

Use a property for a cheap derived value without an operational side effect.
A network request or expensive operation deserves a method whose name exposes
that work. A helper that reads only one value and expresses behavior general to
it belongs on that value. Keep consumer-specific policy with its consumer.

## Resolve defaults where the sources meet

Keep precedence in one owner before values fan out to callers. Preserve zero,
false and empty values when meaningful; use `is None` for an absence fallback.
Return a decisive value when a safe default exists, `None` when absence is an
ordinary outcome, or a result carrying a reason when callers need to distinguish
outcomes. Do not invent a sentinel inside the ordinary domain vocabulary just
to avoid an optional type.

A frozen dataclass is only shallowly protected: nested mutable fields remain
mutable. A value used as a dictionary key needs stable equality and hashing;
choose immutable fields and deliberate equality semantics. Do not add
`unsafe_hash=True` to silence an error without proving that stability.

Source: [dataclasses](https://docs.python.org/3/library/dataclasses.html).
