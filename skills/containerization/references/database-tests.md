# Disposable PostgreSQL tests

Use a fresh database to verify migrations and domain behavior without touching
retained local or shared data. Choose the cheapest engine that can observe the
behavior under test, and state which behavior still needs native PostgreSQL.

## Select the engine

For suitable domain tests, an embedded PostgreSQL build can create a database in
memory inside the test process. PGlite is one JavaScript example, not a required
library or a reason to change the service's language. It runs PostgreSQL compiled
to WebAssembly and supports ephemeral memory storage. See the maintained
[PGlite description](https://pglite.dev/docs/about) when evaluating it.

A SQLite schema or a mock query function does not execute PostgreSQL migrations.
If no compatible embedded engine exists for the required features, use a
disposable native PostgreSQL instance with temporary storage. Report which
choice was made; do not call native container tests in-process tests.

Check the selected engine and version against the migrations before adopting it.
An embedded engine may differ in available extensions, connections, server
configuration and platform integrations. For example, PGlite has a single
exclusive connection; its documented [connection model](https://pglite.dev/docs/)
cannot establish the behavior of concurrent independent PostgreSQL sessions.

## Keep migration provenance visible

Use the same domain migration source as the service whenever compatible. Give
the harness a small, named platform bootstrap only when required. It may create
roles or a stand-in platform function for a domain test, but state what it
models. A stand-in does not verify the real platform's authentication or grants.

If the original migrations depend on an unavailable platform, choose explicitly:

1. Run them against a disposable instance of that platform; or
2. Create a reviewed baseline for a documented starting state. Record the source
   revision, migration names and checksums it derives from, any omitted platform
   objects, and the later migrations that apply on top.

Keep the original history. Do not erase unsupported statements with a regular
expression, catch migration errors and continue, or mark skipped migrations as
applied. If a baseline represents a squash, its ledger records that baseline;
it does not fabricate successful runs of the replaced files. Compare the derived
domain objects with the source where practical and report any unverified gap.

Baselining an existing database also requires evidence that its schema matches
the baseline. A new empty test database cannot supply that evidence. Similarly,
bootstrap success does not prove an upgrade preserves existing rows.

## Give each test run a complete lifecycle

1. Allocate a fresh in-memory database or isolated disposable native instance.
   Do not fall back to a developer or production connection when setup fails.
2. Apply declared platform bootstrap and the chosen migration history in order.
   Use the service's migration runner where possible, including its ledger.
3. Insert small synthetic fixtures through the appropriate boundary. Exercise
   the real command or query and assert its effects, errors and replay behavior.
4. Close clients and dispose of the database even when setup or assertions fail.
   Keep the original failure as the test result; report a cleanup failure as
   additional evidence. If only cleanup fails, fail the run. For containers and
   other engine resources, [owned test resources](owned-resources.md) describes
   how a run finds and removes exactly what it created.

Separate database state between tests unless a suite deliberately shares a
fixture. Prefer injection of a database connection over environment mutations
that could redirect unrelated tests. Close pools and workers so the runner can
exit without a forced success status.

For a migration-runner change, exercise an empty database, a second no-op run,
an altered checksum and an intentional migration failure. Verify that the
failure leaves no successful ledger entry and prevents later migrations. Test
the concurrent-runner lock using independent native sessions; serial embedded
calls do not exercise contention. Add an upgrade fixture when the change
affects a supported existing state.

Some PostgreSQL commands require special transaction handling. For example,
[`CREATE INDEX CONCURRENTLY`](https://www.postgresql.org/docs/current/sql-createindex.html)
cannot run inside a transaction block. Do not remove that behavior to make the
harness pass; test the migration runner's explicit handling on native PostgreSQL.

## Match the evidence to the claim

| Evidence | What it can establish | What still needs a separate check |
| --- | --- | --- |
| Embedded PostgreSQL tests | Supported SQL, constraints, domain commands, transactions and fixtures | Native server features and differences in the selected engine |
| Native PostgreSQL with independent clients | Role grants, connection behavior, advisory locks, contention and required extensions | Container packaging and service transport |
| Built service and database containers | Image contents, startup, migrations, network, runtime identity and persistence | Managed-platform behavior absent from the local stack |
| Public HTTP or MCP calls | Adapter input/result mapping and the identity passed to the shared handler | The other transport unless it is also exercised |

Use native tests for the features the service relies on: distinct login roles,
authentication and TLS, session-dependent behavior, concurrent transactions,
advisory locks, extension loading, and database process restarts. Some SQL role
behavior may be testable in an embedded engine; that does not verify connections
using actual credentials. Name untested requirements instead of describing an
embedded suite as production parity.
