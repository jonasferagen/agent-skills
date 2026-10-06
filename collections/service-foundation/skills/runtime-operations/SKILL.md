---
name: runtime-operations
description: "Design or change credential handling, local service controls and encrypted database backups. Use for secret custody, execution identities, lifecycle or recovery tooling, and their child-process and verification behavior."
metadata:
  version: "1.5.0"
---

# Runtime operations

Read the project's policy and operational guide first. Preserve its execution
identities, external-action gates and release process. This skill supplies a
common method and small Python helpers; project configuration stays in the repo.

## Credentials

Separate three capabilities: **Read** retrieves bounded data; **Operate** makes
ordinary authorized changes through the existing write interface; **Maintain**
changes database objects or performs privileged recovery. These are capability
tiers, not a requirement to use exactly three vaults or merge distinct roles.

- Keep distinct database credentials for distinct consumers. Owner commands,
  intake and scheduling can need separate identities within Operate.
- Service accounts read only their assigned vaults. Secret-store access is not
  a capability tier: a service account needs only read access to its vault,
  even when the vault holds a database writer's credentials. Maintain uses the
  owner's sign-in without a standing service account.
- Vault sharing shares access to every credential in that vault. Separate item
  names, tokens and database passwords do not create an item-level boundary.
  Share only where that access is intended.
- Runtime launchers require the selected service-account token; never fall back
  to owner authentication. Keep tokens outside Git in owner-only files under
  the user's configuration directory. Do not keep a second recoverable token
  copy; replace a lost token. Database passwords stay in the credential store.
- Fetch secrets in memory, verify the target and login, clear inherited database
  overrides and secret-store authentication, and pass only the selected
  consumer's credentials to its child. Use verified TLS for remote databases.
  Error output must not quote secrets or records.
- Use stable vault/item IDs. Moving an item can change its ID; reconcile every
  consumer before removing the old reference. Rotation changes the database
  login and stored item, then restarts affected services.
- Where a consumer depends on a read-only session, verify the setting took effect
  rather than assuming it. A session default, a transaction declared read-only and
  a check that the setting survived are three different guarantees. A pooler
  can discard a startup setting in transit. Without the check, a consumer that
  believes it is read-only can write.

[credentialStore.py](scripts/credentialStore.py) supplies token-file checks,
service-account item reads and owner-only item reads. Callers own project/role
validation and the child environment. The helper uses 1Password CLI, not
Developer Environments; do not substitute one credential mechanism silently
for another.

## Child processes

<!-- Package-boundary copy: node-patterns/SKILL.md (Close input the child does not need) states the Node mechanics of the stdin rule below. Keep both passages aligned. -->
Operational tooling mostly calls other programs. Each call is a place a secret
can escape, a command can hang, or an error can point to the wrong component.

- Withhold a child's output when it could hold a secret, a query or a record.
  Raise an error naming the command and its exit status instead. Say in a
  comment why the output is discarded, so a later maintainer does not restore
  it. Extract a code that classifies the error when diagnosis needs one. A
  child with no access to secrets may report normally; decide per command by
  what it could have been holding.
- Close stdin the child does not need. A child inherits the caller's stdin, so a
  caller fed by a heredoc leaves its own text there for the child to read as
  input. The symptom is distinctive: a command that works when typed and fails
  from inside a script, reporting a syntax or parse error about input nobody
  supplied. Suspect inherited stdin before suspecting the argument just built.
- Build the child's environment as a filtered copy rather than mutating the
  process environment, because that change affects every later call. Filter by
  prefix so a later release of a tool cannot reintroduce a variable that takes
  precedence over the intended credential.
- Pass an argument vector, never a string for a shell to parse.
- Bound every call with a timeout, and decide what a timeout means. Connection,
  statement and idle limits are three different bounds, and a script usually wants
  all three.
- Fail at the boundary that owns a missing prerequisite. A restore step that
  reports failure when no container runtime is installed sends the reader to
  diagnose the restore step instead of the missing runtime.

## Services

Expose `start`, `stop`, `restart`, `status` and `logs` for each named service.
`start` leaves an active service running; `restart` applies changed code or
credentials. If the control command has a default service, make it a viewer: a
preview that sends nothing. Keep it a separate unit from workers and outbound
senders.

- Let the process manager own the complete process group. Stop only the named
  unit, including after a failed start. An occupied port is a startup failure,
  never permission to kill its owner.
- Check readiness from the intended unit. An unrelated HTTP listener returning
  success does not establish startup. Status should expose the selected checkout.
- Run previews, including the viewer, as transient user services, and retained
  workers as installed units. Preserve pinned releases and settings across
  worker restarts; an ordinary control command does not install, enable or
  upgrade a worker.
- Keep secret values out of unit definitions and command arguments. Launchers
  read their token files when the service starts. Limit browser services to
  loopback and keep request-origin checks in the application.
- Do not restart outbound processing as a side effect of a viewer or credential
  change. Preserve the configured external-action gate.

[serviceControl.py](scripts/serviceControl.py) implements Linux user-systemd
control. A consuming repository imports these helpers through the collection's
[loader](../../templates/repository-docs/tools/service_runtime.py), which checks
the [declared interface version](scripts/runtimeApi.py) before any import; see
[runtime helpers](../../references/runtime-helpers.md) for that contract and its
limits. Do not reach into the installed directory with an unchecked path. Project entrypoints supply unit names, non-secret settings and commands.
Use the same controller for installed and transient services; each project
binding selects the unit, expected checkout, command and optional prerequisite
startup. An active `start` checks readiness without replacing or stopping that
instance. HTTP `status` includes readiness, not merely process existence. A
configured checkout mismatch is refused before changing runtime state.

For a new HTTP binding, set `Service.health_service` and expose `/health` using
[ServiceHealth](scripts/serviceHealth.py)'s `service-health/v1` JSON envelope:
`schema`, `service`, `pid`, `checkout`, `status` and `details`. Return HTTP 200 for
`ready` and 503 for `degraded`; include only bounded, non-sensitive diagnostics.
The application owns meaningful dependency checks and its detail fields. The
controller verifies the service name, ready status, PID against the unit MainPID,
cgroup membership and both reported and configured checkout. This is readiness
of the named instance, not a continuous availability guarantee.

Existing bindings without `health_service` retain the plain-PID `/health` probe
until deliberately migrated. The helper does not install units, dependencies or
credentials. Keep automatic-start and restart policy with the unit owner.
If launch or readiness times out after starting an attempt, it stops only the
selected unit. A failed cleanup reports separately and preserves the primary
startup or readiness error.

## Arguments

Keep one script to one job. When jobs share setup, make them subcommands of one
script rather than separate scripts that repeat it. Use the same subcommand and
option names across a project's scripts for the same job and the same input;
two scripts taking an archive should not call it `--file` and `--archive`.

- Give a destructive or privileged job its own subcommand, never a flag on a safe
  one. The safe invocation should not be only one word away from the dangerous
  one.
- Reject an unknown argument. Ignoring a misspelled flag performs a different act
  than the operator asked for and gives them no way to tell.
- Require an explicit target for a job that acts on a named thing. A default
  target lets a rehearsal run against the wrong archive. The configured viewer
  default described under Services is the narrow exception; it does not justify
  a default archive, worker or outbound sender.
- Offer a resolve-and-report mode before a destructive act, so the operator
  authorizes a specific list rather than a pattern.
- Spell options out, and give nothing destructive a single-letter alias; an alias
  invites a guess.

A script that owns a credential owns its endpoint. Do not accept a connection
string, host, port, database, credential, query fragment or restore destination
from an argument or from a caller's request. Resolve them from the configured
source and verify them. This limits a script's reach to what its own identity
allows, not whatever its caller supplies. Where a script is a boundary other
programs call, bound the request too: a small fixed set of fields, a capped input
size, and every value validated before acting.

## Backups

Keep the trigger for a backup in project policy. Use one capture routine when
projects share the same machinery: encrypted export, integrity check and a full
disposable restore before publication. A project that tolerates data loss can
choose that stronger routine to avoid maintaining a separate path.

[databaseBackup.py](scripts/databaseBackup.py) supplies this routine and a
`backup`, `rehearse`, `admin -- COMMAND` interface. The project supplies its schema
scope, credential references, prerequisite roles and snapshot/access checks.
Preserve object ownership where SECURITY DEFINER commands depend on it. The
helper never chooses a production restore destination; rehearsals have no network,
published port, persistent data volume or production passwords.

The bundled implementation validates a Supabase pooler credential profile and
uses a pinned Supabase PostgreSQL container image. Other PostgreSQL targets need
a reviewed project binding; importing the method does not select a provider.
Configure at least one schema explicitly. `BackupConfig.command_timeout` sets a
positive finite limit for each backup command, defaulting to 900 seconds; review
that bound against the project's expected archive size before adoption.
Client and rehearsal container cleanup identifies each attempt by its generated
name and unique label, including after failed or timed-out startup or an attached
command. An operational crypto failure is not
evidence that a wrong key was denied; the helper requires GnuPG's bad-passphrase
status before recording that check.

Keys stay separate from archives; archives, metadata and receipts stay outside
Git. Publish without overwriting retained files. Verify archive identity, checksum
and decryption before restoration. Capture tests make each verification step
fail and confirm that nothing is published; project tests should exercise actual
restoration and permissions.
An archive covers only its selected schemas; document external dependencies and
login provisioning. Never imply it is a full managed-project backup.

## Verification

Exercise missing/wrong credentials, environment isolation, failed startup and
unrelated port ownership with synthetic inputs. Follow the repository's checks.
Check live service state only when relevant; documentation is not live evidence.
Do not widen permissions merely to make a test or operation pass.

<!-- Package-boundary copy: node-patterns/SKILL.md (Report a check's result) applies this denominator rule to check scripts. Keep both passages aligned. -->
<!-- Package-boundary copy: test-writing/SKILL.md (Workflow, step 6) applies this denominator rule to test runs. Keep both passages aligned. -->
A verdict names its denominator: what was compared, run or counted. When that
denominator is empty, the honest output is a refusal, not a pass. Examples of an
empty denominator: nothing compared, no tests collected, no archive matched, or
a filter or threshold that nothing could meet. A passing result that measured
nothing is a defect in the check. It is the failure mode that stays unnoticed
longest, because nobody investigates a pass. This is why capture tests exercise
failing verification, not only a passing one.
