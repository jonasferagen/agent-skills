# Dependency boundaries

## Share a contract rather than an implementation accident

When several modules use an underscored helper, inspect whether it represents
a shared capability or whether callers are reaching past the intended boundary.
Give a genuinely shared operation a named internal API and a result contract,
or move behaviour back to its owner. Removing the underscore alone is not a
design: decide what inputs, failures and stability callers may rely on.
An internal API need not become an externally supported package API.

Return domain results independently of their display text when callers need
to branch, aggregate or test them. For diagnostics used across stages, stable
codes, source locations and structured details can carry meaning while the CLI
or other adapter renders messages. Avoid parsing prose to recover a decision.
A local exception with a useful message is enough when no caller needs more.

## Describe the consumer's actual capability

Use a consumer-owned `Protocol` for a stable role that several implementations
can satisfy. Use `Callable` for one callback when that expresses the contract
fully. Keep a concrete type when the consumer owns it, needs most of its API,
or depends on semantics that a narrower role cannot honestly promise.

```python
from typing import Protocol

class ReceiptSink(Protocol):
    def store(self, receipt: bytes) -> None: ...


class ReceiptWriter:
    def __init__(self, sink: ReceiptSink) -> None:
        self._sink = sink

    def write(self, receipt: bytes) -> None:
        self._sink.store(receipt)
```

Trace forwarded uses too. A facade that calls one method but passes the object
to code needing five methods cannot claim a one-method contract. A protocol
checks structure, not session affinity, ownership, ordering or atomicity; state
those requirements and enforce them where resources are acquired. A connection
pool and a transaction session can share method names without being substitutes.

If a property is only read, expose a read-only property in the protocol instead
of a writable attribute that promises mutation. Keep provider implementation
types outside consumer contracts when a small consumer-owned result is enough.
Do not duplicate an existing lower-level neutral contract merely to avoid an
import.

## Own acquisition and teardown

Inject time, randomness and external clients where they affect behavior. Do not
build a service locator or dependency-injection framework for a few collaborators.
The composition root acquires resources and arranges teardown. Borrowers do not
close injected resources unless that ownership transfer is part of the contract.

Use a context manager to expose a service lifetime when callers must release
resources. For partial acquisition failure, register cleanup as each resource
is obtained. Replacing a subscription or client must release the old owned
resource and establish a clear handoff; avoid hidden module-import side effects.

Source: [protocols](https://typing.python.org/en/latest/reference/protocols.html).
