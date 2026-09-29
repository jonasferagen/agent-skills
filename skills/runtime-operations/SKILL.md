---
name: runtime-operations
description: Design and operate credential launchers, local services and encrypted database backups. Use when changing secret custody, execution identities, service start/stop/restart behavior or recovery tooling; repository policy owns authorization, deployment and the required recovery evidence.
metadata:
  version: "1.0.0"
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

[credentialStore.py](scripts/credentialStore.py) supplies token-file checks,
service-account item reads and owner-only item reads. Callers own project/role
validation and the child environment. It uses 1Password CLI, not Developer
Environments; do not substitute one credential mechanism silently for another.

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
