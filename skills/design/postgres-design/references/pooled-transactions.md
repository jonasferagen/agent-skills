# Transactions on pooled connections

Use this guidance when application code runs transactions through a connection
pool under restricted database roles. It describes a transaction runner: the one
component that begins, binds, commits and releases every transaction. Handlers
receive a session from the runner and send statements through it; they never
control the transaction themselves. Examples are synthetic. The behavior below
was checked against PostgreSQL 17; check the target version.

## Give each transaction its authority

Let the pool log in as a role with no privileges granted to it directly:
`LOGIN NOINHERIT`, granted the service's capability roles (one `NOLOGIN` role
per kind of operation, holding exactly the privileges that operation needs)
`WITH INHERIT FALSE, SET TRUE` (PostgreSQL 16 and later). Privileges granted to
`PUBLIC`, such as the default `EXECUTE` on new functions, still apply to it;
revoke them where they matter. Each capability role holds only the privileges
its operations need, such as `EXECUTE` on command functions and narrow read
grants.

- Start each transaction with `SET LOCAL ROLE <capability>` right after `BEGIN`.
  `SET LOCAL` ends with the transaction, so the next transaction on that
  connection starts as the login again.
- Choose the capability from a closed map of operations to roles in code, never
  from request input. `SET` accepts no bind parameters (`SET LOCAL ROLE $1` is a
  syntax error), so quote the role as an identifier taken from that closed set.
- Before `COMMIT`, check that `current_user` is still the capability role. Work
  that runs `RESET ROLE` or `SET ROLE` inside the transaction would otherwise
  commit under a different authority.

This guards against mistakes, not against the code that uses the runner: that
code can act as any role the login may assume. One login per capability is the
stricter option when that matters.

## Make read-only transactions read-only

For a read, run `SET TRANSACTION READ ONLY` right after `BEGIN`, then confirm the
mode with a query such as `select current_setting('transaction_read_only')`,
which must return `on`. The query also takes the transaction's first snapshot.
After that, PostgreSQL refuses a switch back to read-write with SQLSTATE `25001`.
Before the first query, `SET TRANSACTION READ WRITE` still succeeds, so the
confirming query is part of the guarantee.

Set the mode on each transaction. A login or session default can be lost on the
way through a pooler, and it does not show that this transaction is read-only.

## Commit only what succeeded

After a statement fails, PostgreSQL rejects every later statement in that
transaction with SQLSTATE `25P02`. `COMMIT` of the aborted transaction does not
fail, however: it rolls back and answers with the command tag `ROLLBACK`. Check
the tag that `COMMIT` returns, and treat anything but `COMMIT` as a failure.
Otherwise the runner reports a rolled-back transaction as committed.

Work that catches a failed statement and returns normally leads the runner to
commit. Record the first failed statement in the session, refuse every statement
after it, and raise that failure instead of committing, even when the work
resolved. The tag check then remains a second line of defense. Map the domain
errors that constraints and functions raise, by SQLSTATE, after the runner has
rejected, not by catching them inside the work.

Keep transaction and session control in the runner. Before sending a statement
from the work, refuse `BEGIN`, `START`, `COMMIT`, `END`, `ROLLBACK`, `ABORT`,
`SAVEPOINT`, `RELEASE`, `PREPARE`, `RESET`, `DISCARD`, any `SET` without `LOCAL`,
and a `SET LOCAL` of the role, session authorization or transaction
characteristics. `SET CONSTRAINTS` can stay allowed: it lasts only for the
transaction. A check of the leading keywords catches mistakes; it is not a
security boundary. Logic that needs savepoints or another isolation level
belongs in a database function or a runner option, not in the work.

Send one statement per call through the extended query protocol. PostgreSQL
refuses a string that holds several statements there, with SQLSTATE `42601`.
Some drivers use the simple protocol for a query without parameters, which runs
every statement in the string; node-postgres does. A check that reads only the
first statement cannot vouch for the rest, so choose the extended protocol
explicitly.

## Return a clean connection

Session state survives `COMMIT`. A session-level `set_config(name, value,
false)`, a `SET ROLE` without `LOCAL`, a temporary table and a session advisory
lock taken inside the transaction all stay on the connection. The next request
that borrows it inherits them.

After the transaction ends, by commit or rollback, run `DISCARD ALL` before the
connection returns to the pool. It restores the settings, role and session
authorization of a new connection, and drops temporary tables, prepared
statements, cursors, listeners and advisory locks. It cannot run inside a
transaction block. `RESET ALL` is not a substitute: it leaves a session
`SET ROLE` in place.

Destroy the connection instead of returning it when the rollback or the reset
fails, or when the connection reported an error while it was checked out. A
connection can fail between statements; make sure the driver reports that as the
next statement's failure rather than as an unhandled event.

A pooler that assigns server connections per transaction can pass session-level
state to other clients, and a reset sent after the transaction is not guaranteed
to reach the same server connection. Behind such a pooler, keep all state
transaction-scoped: `SET LOCAL`, `set_config(name, value, true)` and
`pg_advisory_xact_lock`.

## Verify the runner

Test the runner's contract through its public interface:

- A failed statement that the work catches still prevents the commit.
- A refused control statement fails the transaction before it is sent.
- A role change inside the work fails the role check.
- A read-only transaction refuses a write and a switch back to read-write.
- Session state set in one transaction is gone in the next. A pool of one
  connection makes the reuse deterministic.

An embedded engine with a single connection can check the statement contract.
The login's real rights, `NOINHERIT` and grants need native PostgreSQL connections
made with the login's own credentials.
