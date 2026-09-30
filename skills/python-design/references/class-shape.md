# Class shape

## Choose by state and responsibility

A public domain operation uses a named class even when pure. A stateless
operation uses `@staticmethod`; a service whose state or collaborators survive
across calls uses instance methods and constructor injection. Put behavior
intrinsic to one domain value on that value before inventing a companion class.

```python
from collections.abc import Iterable

class InvoiceTotal:
    @staticmethod
    def of(amounts: Iterable[int]) -> int:
        return sum(amounts)
```

This names the operation at the call site as `InvoiceTotal.of(...)`. The
house preference is intentional even though Python modules can also supply a
namespace. Do not create an instance solely to call stateless methods, and do
not hide mutable service state in class attributes or a global singleton.

Use `@classmethod` when the method needs `cls`, commonly an alternate constructor
that should respect subclass construction. Use `@staticmethod` when it needs
neither an instance nor the class. A method that reads or changes an instance
uses `self`. Keep a fixed workflow readable as named steps; extract collaborators
when their responsibilities or lifetimes differ, not to satisfy a line limit.

## Keep the exceptions narrow

Module-level functions remain appropriate for:

- implementation helpers marked private by convention (`_helper`);
- framework-discovered entrypoints, fixtures, callbacks, decorators and
  context-manager factories where a function is the natural integration shape;
- small value-boundary parsers or type guards; prefer a method when a value
  class already owns the boundary;
- a thin CLI `main()` that adapts arguments and the exit status to domain code.

A callback can often be an existing bound or static method. Do not introduce a
wrapper solely to satisfy the house style. Tables, constants and descriptors are
data and may remain module values. A new operation does not become an exception
merely because it is a short pure function.

## Construction is a real boundary

Python has no enforced private constructor. An alternate `parse` or `from_*`
constructor does not prevent callers from using `Class(...)`. If every instance
must satisfy an invariant, validate ordinary construction as well, or make the
validated boundary's limited guarantee explicit. An underscore is an API
convention, not an access-control mechanism.

Keep invariants on the value; leave I/O, persistence and heavyweight adapters
with an owning service. Prefer composition to inheritance unless callers
actually rely on substituting subclasses. Repeated classes differing only in
fixed data are candidates for descriptors plus shared behavior, not another
copy with a new name.

Source: [method binding](https://docs.python.org/3/library/functions.html#classmethod).
