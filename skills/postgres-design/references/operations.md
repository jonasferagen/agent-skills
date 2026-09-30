# Operations across rows and systems

Use this guidance when a schema supports commands, dependent state transitions,
retries or concurrent workers. It does not require every application to introduce
a database command API or a queue.

## Complete changes

Keep a business operation's validation and related database writes in one
transaction through the project's authoritative write boundary. Include required
evidence associations and audit outcomes in that transaction so a failure leaves
no partial result. Adapters should go through that write boundary rather than
reimplement its rules.

For retryable operations, define an operation identity separately from entity
identity. Record enough accepted intent and outcome to distinguish an identical
retry from a conflicting instruction under the same key. Return the existing
outcome for a repeat; surface conflicts rather than silently accepting them.
Decide how rejected attempts may be corrected and retried.

## Concurrent writes

A check followed by a write is insufficient if another transaction can change
the checked state. Back duplicate prevention with a unique constraint. Protect
cross-row invariants with a strategy suited to their scope: locks, serialized
commands or a suitable isolation level with retries.

Consider both the absent-row case and the complete relationship graph. Locking
an existing row cannot alone protect an identity that has not been inserted;
checking each edge independently can admit a cycle under concurrent writes.
Use a consistent lock order and test the competing transactions that matter.

For worker claims, define lease ownership, expiry, recovery and stale-worker
rejection. A single human owner can still have several agents and schedulers
writing concurrently. Separate their execution permissions according to the
project's model.

## External effects

A database transaction cannot commit an external delivery atomically. When
delivery must follow a committed change, record its pending intent in the same
transaction, then perform delivery separately. Retain attempts and provider
references needed for recovery. Handle the case where delivery succeeds but
recording its result fails; do not promise exactly-once effects from a local
deduplication key alone.
