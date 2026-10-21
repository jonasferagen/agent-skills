# Types and boundaries

## Separate a type claim from validation

Annotations, `TypedDict`, `cast()` and `NewType` do not validate external data at
runtime. Use `object` for an unconstrained value that must be narrowed; reserve
`Any` for an intentional unchecked boundary. Parse external values once and
pass the validated representation onward. Keep unavoidable casts local and
explain the proof the checker cannot express.

Keep the validated representation precise where downstream code relies on it:
a `TypedDict` can describe a validated mapping, and a dataclass can name an
internal record. Neither choice requires converting every wire dictionary.
If variants carry different fields, model those variants instead of filling one
record with unrelated optional fields and relying on callers to know the phase.
Choose the representation for the invariants callers actually need.

For an integer count, decide whether booleans belong to the domain: `bool` is an
`int` subclass. This boundary deliberately rejects them:

```python
def parse_attempts(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("attempts must be an integer")
    if value < 0:
        raise ValueError("attempts must be non-negative")
    return value
```

Use an existing schema validator when the project already owns one. Do not add a
parallel handwritten schema or a new validation dependency for convenience.

## Express the relationship the caller needs

Accept `Iterable[T]` for one pass, `Sequence[T]` for repeated reads/indexing, and
`Mapping[K, V]` for read-only access through that interface. These annotations
neither copy the input nor freeze another owner's mutable object. Request a
concrete mutable collection only when mutation is part of the contract.

A `Protocol` describes a structural capability; implementations need not inherit
from it. Include every operation actually used. A `runtime_checkable` protocol
only checks attribute presence, not complete signatures or domain validity.

Use generics when an input/output relationship would otherwise be lost. Prefer
`Literal` or an enum for a finite vocabulary, and separate variants when payloads
differ. `assert_never` can expose an unhandled closed-union variant to a type
checker. A `dict[Enum, Value]` does not prove that every enum member is present;
check completeness explicitly when all members are required.

## Respect the supported interpreter

Built-in generics such as `list[str]` are available from 3.9; union notation
`T | None` from 3.10; `Self` and `assert_never` from 3.11; `type` statements and
type-parameter syntax from 3.12. Use compatible forms or a backport the project
already depends on when the project supports older versions. Do not remove
`from __future__ import annotations` (which keeps annotations as unevaluated
strings) without checking runtime annotation consumers such as dataclass
field inspection, `typing.get_type_hints` or validation libraries.

Sources: [typing](https://docs.python.org/3/library/typing.html),
[protocols](https://typing.python.org/en/latest/reference/protocols.html),
[built-in types](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool).
