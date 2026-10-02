---
name: database-migrations
description: "Design or review database migration history, runners, baselines and upgrade verification. Use when changing how schema changes are applied or testing migration behavior; container packaging and ordinary query design are separate tasks."
metadata:
  version: "0.1.0"
---

# Database migrations

Preserve the relationship between migration source, recorded history and actual
schema state. Read the project's database conventions, supported starting states
and recovery requirements before changing its migration process. Use the existing
migration tool where it meets those requirements; extracting this guidance does
not call for a custom runner.

Scope work to the requested database and environment. Retained development data
is not disposable by default, and migration design does not authorize applying a
change to a live database. Keep migration credentials separate from ordinary
runtime credentials when their required privileges differ.

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
paths. Verify the path being changed and name any path not exercised. Read
[database tests](references/database-tests.md) when selecting an embedded engine,
adapting platform bootstrap or checking migration behavior.

## Verify and report

For a runner change, exercise an empty database, a second no-op run, an altered
checksum and an intentional failure. Verify that failure leaves no successful
ledger entry and prevents later migrations. Use independent sessions to test
concurrent runners. Add an upgrade fixture when a supported existing state is
affected, and check retained rows as well as schema shape.

For an individual migration, select checks for its changed behavior and supported
starting states; do not rerun the full runner test matrix automatically. Test
nontransactional behavior on an engine that supports it.

Report the source history or baseline, starting state, engine and version,
commands run, results and unverified paths. A test double for platform bootstrap
cannot establish the real platform's permissions. This skill works without a
container tool; container lifecycle mechanics belong to the chosen test harness.
