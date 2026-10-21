---
name: database-migrations
description: "Design or review database migration history, runners, baselines, reproducible development setup and seed routines. Use when establishing a development database, changing how schema changes are applied or testing migration behavior; container packaging and ordinary query design are separate tasks."
metadata:
  version: "0.4.0"
---

# Database migrations

Preserve the relationship between migration source, recorded history and actual
schema state. Read the project's database conventions, supported starting states
and recovery requirements before changing its migration process. Use the existing
migration tool where it meets those requirements rather than writing a custom
runner. Where the project documents no database conventions, infer them from its
migration tool, manifests and CI configuration, state the assumption, and ask
the user when the choice matters.

Scope work to the requested database and environment. Retained development data
is not disposable by default, and migration design does not authorize applying a
change to a live database. Keep migration credentials separate from ordinary
runtime credentials when their required privileges differ.

## Reproduce development state

When establishing or changing a development database workflow, provide checked-in
commands to create its isolated storage, apply the canonical migrations and load
small synthetic examples. Reuse the existing migration tool, and load fixtures
through the application's own write path where one exists, otherwise through a
checked-in SQL or script seed run by the same tool; command names such as
`db:setup`, `db:migrate`, `db:seed` and `db:reset` illustrate the interface, not
a required framework or custom runner.

Keep normal migration and seed operations separate from destructive reset. Define
whether repeated seeding is idempotent or requires a fresh disposable database;
never silently truncate retained data. Separate required reference data from
optional dummy records. Synthetic fixtures should exercise useful relationships
and retrieval cases, use stable identities or a repeatable generator, and include
needed local payloads without importing retained assets or contacting live services.

Resolve and display the selected target without exposing secrets. Scope creation
and reset to a known disposable dev instance or path; if the project has a reset
command, it must reject unknown, shared, staging or retained targets. A target
is disposable when the checkout owns its storage (a path inside the repository,
or a loopback instance the project's own setup command created) or the user
confirms it; an environment label alone is not proof that the selected database
or associated files are disposable.
Keep storage, credentials and output paths isolated from other environments.
For file databases, distinct owned paths can supply isolation without a server.

Document prerequisites and the commands a fresh checkout needs. Exercise setup
from empty storage, a representative seeded read and the declared repeat behavior.
If the project has a reset command, check that it rejects a non-dev target
without changing it. These smoke checks
establish the setup routine; they do not require a full test suite or establish
upgrade, staging or production readiness. Tell the user explicitly when a check could not be run.

When an environment is added or repurposed, reassess its isolation, data retention,
migration delivery and recovery before reusing the dev routine. Keep one canonical
migration history across environments, with explicit platform prerequisites.
Shared environments need their own data and recovery policy; never carry dev's
reset or dummy-seed defaults into them implicitly.

## Preserve migration history

Use the project's migration tool when it supplies these guarantees:

- Apply migrations in a deterministic order and record each successful version
  with a checksum in a database ledger. Reject an edited applied migration or an
  unexplained mismatch between the ledger and available history.
- Serialize migration runners with a database lock or equivalent tool guarantee.
  Bound lock waiting and make failure visible to the caller.
- Commit each transactional migration and its ledger entry atomically. Stop on
  failure; never mark a partially applied migration as successful. For statements
  that cannot run in a transaction, define recovery before execution.
- Keep platform bootstrap separate from domain migrations. Roles, extensions or
  platform-provided schemas must be declared prerequisites, not missing objects
  that cause the runner to silently skip SQL.
- Use the original history, or an explicitly reviewed baseline for a named
  starting state. A derived baseline records its source and replaced history;
  it does not pretend every original migration ran. Do not flatten or filter
  migrations merely to make a new engine accept them.

An empty-database bootstrap and an existing-database upgrade are different
paths. The supported starting states are the existing database states the
project promises to upgrade from, such as the previous release's schema. Verify
the path being changed and name any path not exercised. For PostgreSQL, read
[database tests](references/database-tests.md) when selecting an embedded engine,
adapting platform bootstrap or checking migration behavior. For other engines,
the same rules apply through the engine's own tooling: a temporary file for a
file database, a disposable container with temporary storage for a server.

## Verify and report

For a runner change, exercise an empty database, a second no-op run, an altered
checksum and an intentional failure. Verify that failure leaves no successful
ledger entry and prevents later migrations. Use independent sessions to test
concurrent runners. Add an upgrade fixture when a supported existing state is
affected, and check retained rows as well as schema shape.

For an individual migration, select checks for its changed behavior and supported
starting states; do not rerun the full runner test matrix automatically. Test
nontransactional behavior on an engine that supports it.

Report to the user the source history or baseline, starting state, engine and
version, commands run, results and unverified paths. A test double for platform bootstrap
cannot establish the real platform's permissions. This skill works without a
container tool; container lifecycle mechanics belong to the chosen test harness.
