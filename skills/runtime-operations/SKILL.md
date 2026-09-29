---
name: runtime-operations
description: "Design and operate credential launchers, local services and encrypted database backups. Use when changing secret custody, execution identities, service start/stop/restart behavior or recovery tooling, and when an operational script spawns a child process, builds its environment, takes arguments or reports a verification result; repository policy owns authorization, deployment and the required recovery evidence."
metadata:
  version: "1.1.0"
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
- Service accounts read only their assigned vaults. Read permission on the
  secret store can supply a database writer. Maintain uses the owner's sign-in
  without a standing service account.
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
  a check that the setting survived are three different guarantees, and a pooler
  can discard a startup setting in transit. Without the check, a consumer that
  believes it is read-only can write.

[credentialStore.py](scripts/credentialStore.py) supplies token-file checks,
service-account item reads and owner-only item reads. Callers own project/role
validation and the child environment. It uses 1Password CLI, not Developer
Environments; do not substitute one credential mechanism silently for another.

## Child processes

Operational tooling is mostly other programs. Each call is a place a secret can
escape, a command can hang, or an error can accuse the wrong component.

- Withhold a child's output when it could hold a secret, a query or a record.
  Raise the command and its exit status instead, and say in a comment why the
  output is discarded, or the next reader will helpfully restore it. Extract a
  classified code where diagnosis needs one. A child with no access to secrets may
  report normally; decide per command by what it could have been holding.
- Close stdin the child does not need. A child inherits the caller's stdin, so a
  caller fed by a heredoc leaves its own text there for the child to read as
  input. The symptom is distinctive: a command that works when typed and fails
  from inside a script, reporting a syntax or parse error about input nobody
  supplied. Suspect inherited stdin before suspecting the argument just built.
- Build the child's environment as a filtered copy rather than mutating the
  process environment, which leaks into every later call. Filter by prefix so a
  tool's later release cannot reintroduce a variable that outranks the intended
  credential.
- Pass an argument vector, never a string for a shell to parse.
- Bound every call with a timeout, and decide what a timeout means. Connection,
  statement and idle limits are three different bounds, and a script usually wants
  all three.
- Fail at the boundary that owns a missing prerequisite. A restore step that
  reports failure when no container runtime is installed spends the reader's
  diagnosis on an innocent surface.

## Services

Expose `start`, `stop`, `restart`, `status` and `logs` for each named service.
`start` leaves an active service running; `restart` applies changed code or
credentials. Keep a default viewer distinct from workers and outbound senders.

- Let the process manager own the complete process group. Stop only the named
  unit. An occupied port is a startup failure, never permission to kill its owner.
- Check readiness from the intended unit. An unrelated HTTP listener returning
  success does not establish startup. Status should expose the selected checkout.
- Use transient user services for previews and installed units for retained
  workers. Preserve pinned releases and settings across worker restarts; an
  ordinary control command does not install, enable or upgrade a worker.
- Keep secret values out of unit definitions and command arguments. Launchers
  read their token files when the service starts. Limit browser services to
  loopback and keep request-origin checks in the application.
- Do not restart outbound processing as a side effect of a viewer or credential
  change. Preserve the configured external-action gate.

[serviceControl.py](scripts/serviceControl.py) implements Linux user-systemd
control. Project entrypoints supply unit names, non-secret settings and commands.
Transient HTTP services must expose `/health` with their PID as plain text after
startup validation; the helper verifies cgroup membership. It does not install
units, dependencies or credentials.

## Arguments

Keep one script to one job, and make jobs that share setup subcommands of one
script rather than separate scripts repeating it. Use the same verbs across a
project's scripts; two scripts taking an archive should not call it `--file` and
`--archive`.

- Give a destructive or privileged job its own subcommand, never a flag on a safe
  one. The safe invocation should not be one word from the dangerous one.
- Reject an unknown argument. Ignoring a misspelled flag performs a different act
  than the operator asked for and gives them no way to tell.
- Require the target of a job that acts on a named thing. A default target is how
  a rehearsal runs against the wrong archive.
- Offer a resolve-and-report mode before a destructive act, so the operator
  authorizes a specific list rather than a pattern.
- Spell options out, and give nothing destructive a single-letter alias; an alias
  invites a guess.

A script that owns a credential owns its endpoint. Do not accept a connection
string, host, port, database, credential, query fragment or restore destination
from an argument or from a caller's request. Resolve them from the configured
source and verify them. This keeps a script's reach equal to its own identity
rather than to whatever its caller supplies. Where a script is a boundary other
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

Keys stay separate from archives; archives, metadata and receipts stay outside
Git. Publish without overwriting retained files. Verify archive identity, checksum
and decryption before restoration. Capture tests should check failure before
publication, and project tests should exercise actual restoration and permissions.
An archive covers only its selected schemas; document external dependencies and
login provisioning. Never imply it is a full managed-project backup.

## Verification

Exercise missing/wrong credentials, environment isolation, failed startup and
unrelated port ownership with synthetic inputs. Follow the repository's checks.
Check live service state only when relevant; documentation is not live evidence.
Do not widen permissions merely to make a test or operation pass.

A verdict names its denominator: what was compared, run or counted. When that
denominator is empty — nothing compared, no tests collected, no archive matched,
an unsatisfiable threshold — the honest output is a refusal, not a pass. A green
result that measured nothing is a defect in the check, and it is the failure mode
that survives longest, because nobody investigates a pass. This is why capture
tests check failure before publication.
