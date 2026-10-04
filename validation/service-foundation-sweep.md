# Service foundation sweep — 2026-10-04

Each member's skill quality was reviewed before collection consistency. Coverage
includes both entrypoints and UI files, all three runtime helpers, the runtime
tests, installation tests and existing member validation scenarios. The shared
installation checker remains the coordinator's responsibility.

## Phase 1: member quality

### Service boundaries

The skill has a focused scope and preserves existing ownership decisions. Shared
application behavior, caller identity and retry identity remain distinct from
protocol adaptation. Its verification asks for evidence through every changed
transport rather than treating handler tests as adapter evidence. It does not
force service decomposition or a second transport. No concrete correction was
needed; its version remains 0.1.0.

### Runtime operations

The credential tiers and vault access distinctions, owner-versus-service-account
authentication, named-unit control, isolated restore and preservation of object
ownership are retained. Helper review found gaps between the method and code:

- Credential reads inherited stdin despite needing no input. They now close it.
  Failures name `op item get` and its exit status, or report a timeout/missing
  prerequisite, while withholding secret-bearing output.
- Service-control commands and backup subprocesses had no timeouts. Control
  commands now have a 45-second bound. Backup configuration adds an optional
  positive finite `command_timeout`, defaulting to 900 seconds, propagated to
  capture, crypto, restore, cleanup and administrative subprocesses. Short
  readiness probes are bounded separately. Explicit backup data still uses a
  pipe; calls with no data close stdin. Existing positional interfaces remain
  usable.
- A timed-out service launcher or readiness query could bypass the former final
  stop call after starting a unit. Startup/readiness failure now stops only the
  selected unit once activation was attempted, preserving the primary failure
  if that stop also fails. Failure to read initial state does not stop a unit
  this call has never attempted to start.
- An empty schema tuple removed every `pg_dump --schema` filter, implicitly
  selecting every non-system schema. Construction now refuses that empty scope
  before retrieving credentials.
- A failed or timed-out Docker start could create a container without reaching
  the former `created` flag. Each attempt now has a unique non-secret label;
  cleanup reconciles that label and the generated name, then removes only the
  matching full container ID. Unrelated namesakes are left alone. Cleanup failure
  preserves a preceding error and adds a secret-safe diagnostic. The guarded
  stderr fallback retains Python 3.10 compatibility when exception notes are
  unavailable and preserves the primary failure under warnings-as-errors.
- Attached `pg_dump` and `psql` client containers also need daemon-side cleanup
  when the Docker CLI times out; `--rm` alone does not stop a still-running
  container. They now share the attempt-name/label reconciliation helper with
  rehearsal containers. Both remove only the identified immutable ID; no
  credential value is added to the argument vector.
- Rehearsal treated every crypto `RuntimeError` as wrong-key denial. It now
  requires GnuPG bad-passphrase and decryption-failed statuses; a timeout, missing
  program, agent problem or unclassified crypto failure stops the rehearsal.
- The real crypto test relied on the developer's GnuPG home. It now owns a
  temporary home with mode 0700, uses synthetic data and keys, and stops only
  that home's agent. A missing GnuPG executable is an explicit skip; operational
  failures remain failures.

New tests cover these boundaries and the previously untested prepublication
encryption, integrity, round-trip and backup-directory permission failures.

The skill now documents the existing Supabase pooler/image assumptions, the
configurable backup bound and the viewer's already-declared exception to explicit
target selection. Endpoint validation, image choice, TLS, credential filtering,
default ownership preservation and the no-production-restore interface are
unchanged. Runtime operations is 1.3.0 for its compatible helper configuration
and focused conformance repairs.

## Phase 2: collection consistency

The collection still routes service ownership and adapters to service-boundaries,
and credentials/lifecycle/recovery to runtime-operations. Maintained-service
promotion selects both. Its collection entrypoint leaves provider, process
manager, database, transport and container adoption with the project; the member
now makes its bundled backup implementation's narrower profile explicit.

Installation guidance preserves source pins and local edits, replaces complete
directories, and does not permit consumers to bless drift. Membership and member
names are unchanged. Collection version 0.2.0 records the runtime update; the
coordinator owns final JSON version reconciliation and inventory regeneration.

## Verification

- Baseline: 12 runtime tests ran; 11 passed and the crypto round trip failed.
  A fresh synthetic GnuPG home reproduced the failure inside the sandbox because
  `gpg-agent` could not start. The isolated test then passed outside the sandbox.
- Final runtime suite: `python3 -B -m unittest discover -s
  collections/service-foundation/skills/runtime-operations/tests -v` ran 34 tests,
  all passed, zero skipped. Only the GnuPG boundary ran for real; service,
  1Password and database/container boundaries used synthetic mocks. Automatic
  approval allowed the isolated test process outside the sandbox.
- New conformance tests were run before helper repairs and failed for inherited
  stdin, missing bounds/status diagnostics, missing empty-schema rejection and
  unhandled timeout behavior. Prepublication failure injections also exercise
  the existing publication guarantees.
- Follow-up timeout regressions were observed before the ownership fixes:
  installed and transient launchers and readiness-query timeouts did not stop
  the selected unit; attached clients did not reconcile their container or fail
  when cleanup alone failed. The repaired tests cover those cases, unrelated
  name collisions and preserving the original service/container error.
- A real synthetic wrong-passphrase probe emitted
  `ERROR symkey_decrypt.maybe_error 11_BAD_PASSPHRASE` and `DECRYPTION_FAILED`.
  Classification tests reject agent problems and unclassified decryption errors
  as evidence of wrong-key denial.
- Installation suite: 11 synthetic tests passed with no skips. Member
  `quick_validate.py` checks and scoped `git diff --check` passed.

Clear Writing, its instruction guidance, Skill Creator and the repository's
Test Writing unit/integration/fixture guidance informed this review. Supabase
guidance was read because the bundled helper has provider assumptions; no
Supabase API, endpoint profile, schema, live database or provider feature changed.

Primary references support the concrete boundary checks:
[Python subprocess behavior](https://docs.python.org/3/library/subprocess.html),
[`pg_dump` schema selection](https://www.postgresql.org/docs/current/app-pgdump.html),
[Docker container filters](https://docs.docker.com/reference/cli/docker/container/ls/),
and [GnuPG machine-readable statuses](https://raw.githubusercontent.com/gpg/gnupg/master/doc/DETAILS).

## Limits and follow-up

No live service, systemd unit, 1Password session, Docker daemon or database was
used. No real secret or archive was read. Docker filter/cleanup behavior was
checked through its command boundary and primary documentation, not a daemon
trial. Python 3.10 itself was unavailable; the missing-`add_note` path was tested
with an exception that exposes no callable note method.

No new collection trigger or reference route was added. A fresh installed-consumer
trial before release should ask for a backup on an ordinary PostgreSQL target:
the agent must identify the bundled provider profile, preserve the project's
chosen provider and bind recovery tooling deliberately. Also repeat the
maintained-service transition trial against the final pin. Source/package checks
alone do not prove those decisions or native discovery.

Further useful improvements:

- Move credential and backup procedures into conditional references if repeated
  service-control trials show they cause unnecessary reading. Keep essential
  identity and external-action constraints in the entrypoint.
- Decide whether backup provider/image validation should become an explicit
  project-supplied profile in a later change. Preserve the current target checks
  until the alternative has equivalent rejection tests.
- Add controlled daemon restore trials for startup uncertainty and snapshot/access
  checks in a consumer that owns the required platform. This sweep does not
  establish actual Docker restoration or PostgreSQL permissions.
- Review bounded passphrase transport and atomic archive/metadata publication
  separately. Those preexisting edges warrant focused evidence rather than a
  broad rewrite during this sweep.

## Coordinated completion

The [coordinated sweep](collection-sweep.md) records the final source inventories,
combined checks and retained consumer trials. Earlier pending or partial results
on this page describe the review stage at which they were recorded. No release
or installed Forge pin was changed.
