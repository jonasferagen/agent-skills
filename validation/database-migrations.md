# Validation — Database migrations

## Extraction — 2 October 2026

Extracted the migration-history section and database-testing reference from
containerization 0.5.0. The reference now states its resource ownership requirement
locally; Docker/Compose cleanup mechanics remain in containerization. New framing
distinguishes a runner change from a single migration and makes supported starting
states explicit. Existing [containerization evidence](containerization.md) is
historical context, not a behavioral trial of this new package.

| Request and context | Expected outcome |
| --- | --- |
| Review a migration runner without containers | Inspect order, ledger, checksums, atomicity, bounded locking and failure behavior without requiring containerization. |
| An applied migration was edited | Reject unexplained history mismatch; do not mark later migrations successful. |
| Two runners start together | Verify serialization through independent sessions and bounded failure. |
| Platform objects are unavailable locally | Declare bootstrap prerequisites or a reviewed baseline with provenance; retain the original history. |
| An empty database test passes | Do not claim a supported upgrade preserves existing rows without exercising that state. |
| Embedded tests pass under a privileged connection | Keep actual login, contention and unsupported server features unverified. |
| Change one migration | Select evidence for the migration and affected starting states; do not automatically run every runner test. |
| Change only a container image | Containerization is the relevant task; do not redesign migration history. |

These scenarios received author review. No independent agent trial or live
database test was run. Package and link checks are recorded with the extraction
in the containerization validation page.

## Development environments — 4 October 2026

The Forge request identified a missing lifecycle outcome: dev setup should create
isolated storage, apply migrations and supply useful synthetic data before a full
test suite exists. Inspection of Forge's asset-catalog operating guide showed
existing migration and synthetic-trial capabilities; no live database was read.
The new guidance specifies the reusable outcome without prescribing Laravel,
PostgreSQL, a custom runner or immediate staging provisioning. Retained dev state
is not a reset target. Adding or repurposing an environment requires reassessment.

Postgres-design now includes development lifecycle in implementation design;
database-migrations owns setup and seed mechanics. Relational-modeling remains
scoped to conceptual questions. These are unreleased source changes; no consumer
pin or Forge runtime was changed.

Validation: `python3 scripts/check.py` passed all four checks after installing the
locked TypeScript dependency and rerunning outside the sandbox. The initial
sandbox run failed GPG and Node child-process checks; the unrestricted rerun
passed. `git diff --check` passed. No database runtime test was performed.
Practical routing evidence is retained in `database-environment-routing.md`.
