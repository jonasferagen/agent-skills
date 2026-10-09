---
name: runtime-operations
description: "Design or change credential handling, local service controls and encrypted database backups. Use for secret custody, execution identities, lifecycle or recovery tooling, and their child-process and verification behavior."
metadata:
  version: "3.0.0"
---

# Runtime operations

Read the project's policy and operational guide first. Preserve its execution
identities, external-action gates and release process. This skill owns the method
and the interface contract operational tooling must satisfy; project configuration
stays in the repo.

No code ships here. The modules a service controller imports are deployed by the
project's framework, which also chooses the secret store, the process manager and
the database provider they bind. [The helpers contract](references/runtime-helpers.md)
states the surface those modules must offer, the binding a project supplies, and
what survives an update. Read it before writing a controller, rather than
inferring the surface from an installed module's source.

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

Which secret store holds these credentials is the project's choice, and this
method selects none. A store usually offers more than one way to authenticate —
an operator's interactive session, a service-account token, a local agent or
desktop integration — and they are not interchangeable: each carries a different
identity and a different reach. Name the mechanism the tooling uses, in the
tooling, and never substitute another silently. Reading a credential is itself a
child process, so the rules below govern it: its error output names the command,
the identity it used and the exit status, and nothing more.

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
- Pass an argument vector, never a string for a shell to parse. A downstream
  service manager can still expand that vector; select literal handling at that
  boundary and verify the values received by the child.
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
preview that sends nothing. Keep it a separate service from workers and outbound
senders.

- Let the process manager own the complete process group. Stop only the named
  service, including after a failed start. An occupied port is a startup failure,
  never permission to kill its owner.
- Readiness is a property of one named instance, not of a port. An unrelated
  listener returning success does not establish startup. A probe that proves
  identity establishes it: the service it claims to be, its process identity
  against the manager's own record, its membership in that service's process
  group, and the checkout it reports against the configured one. Status should
  expose the selected checkout.
- An ephemeral preview and a retained worker have different lifetimes, so the
  process manager holds them differently: a preview exists only while it runs,
  and a worker keeps an installed definition. Preserve pinned releases and
  settings across worker restarts; an ordinary control command does not install,
  enable or upgrade a worker.
- Keep secret values out of service definitions and command arguments. Launchers
  read their token files when the service starts, and each command fetches its
  own credentials. Limit browser services to loopback and keep request-origin
  checks in the application.
- Do not restart outbound processing as a side effect of a viewer or credential
  change. Preserve the configured external-action gate.

A controller binds one service and asks for one action. The contract reference
owns which fields a binding supplies, what omitting each one selects, and how the
five actions behave. Three of its rules are method rather than mechanism, so a
controller written against any implementation keeps them: a checkout mismatch is
refused before anything changes runtime state, a `start` that only wanted
readiness neither replaces nor stops an already active instance, and a failed
start stops only what it attempted while preserving the original error.

For the project-wide view a controller prints one bounded line per instance
instead of its reader-facing output: the service, the checkout, one state from a
closed vocabulary, and the unit, endpoint, lifecycle class, detail and attention
fields where they exist. Only `status` reports, because the other actions change
state and a report is a reading. That is why a service whose unit is held by
another checkout reports that fact rather than refusing, while an active service
that will not answer readiness reports a failure: readiness is what a running
service was asked for. Keep every line scannable. Long output — a journal, a
durable receipt, a database probe — belongs to `status <name>`, which a reader
asks for after a row says something is owed.

That report's schema and its closed state and lifecycle vocabularies have one
owner outside this skill: the `service-classes` skill, which states what each
state means and which class a project-wide launch may touch. Validate every
reported value against that owner rather than inventing one, and declare a
lifecycle class rather than leaving a consumer to guess what starting the
service would do; an undeclared class reads as unclassified and is skipped.

## Scheduled runs

A scheduled service installs a schedule, not a listener. Each run is a finite job
that finishes, so the controller operates the schedule and reports evidence of
runs rather than readiness. Keep the trigger in project policy; the schedule is
how that policy is applied.

- An unattended run must be safe at the moment it happens, because nobody chooses
  that moment. It must not need an attended precondition: a prompt, a credential
  typed in, a quiet period or a resource an operator would otherwise have
  reserved. If the work needs any of those, the schedule ships the part that does
  not and the attended part stays a command.
- Let a run decline rather than disturb live work. A run that takes the lock a
  person is using, or starts a dependency for its own convenience, has chosen its
  own completion over the system it runs inside.
- A scheduled run may do the paid or costly work its policy chose, and must bound
  it: cap the cost of one run, never repeat work already recorded as done, and
  stop after repeated failure instead of retrying unattended. Spending that the
  policy did not choose is the defect, not spending as such. No control action
  spends: an operator inspecting a schedule must not be billed for it.
- Share one lock between the schedule and manual invocation of the same job, so
  they defer instead of overlapping. Two copies of the same job are rarely safe
  just because one was asked for.
- Report the schedule and the last run's durable outcome together. An active
  schedule is not evidence of a run, and a run is not evidence of success. Keep
  that record outside the service definition, because a stopped or replaced
  service must not take the evidence with it.
- Decide what a missed window means and say so. A host that was off through the
  window can run late or skip; skipping silently is the choice that looks like
  success. Add a randomized delay where many hosts would otherwise act together.
- Derive the schedule's name from the selected checkout so a second checkout
  cannot adopt the first one's schedule, its runs or its evidence.
- `stop` stops and disables the schedule and leaves every completed run in place.
  Nothing an ordinary control does may prune, forget or overwrite retained
  evidence.

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

A backup is worth what it can prove. Each item below is a separate guarantee, and
a routine that omits one has not established it:

- **The export covers what was configured.** Configure at least one schema
  explicitly; an archive covers only its selected schemas. Document external
  dependencies and login provisioning, and never imply the archive is a full
  managed-project backup.
- **The credential profile is the intended one.** Verify the project, login, port,
  database and endpoint before exporting, and connect with verified TLS. Which
  provider and endpoint shape those values describe is a project binding, and
  adopting the method does not select a provider.
- **The archive matches itself.** Verify archive identity, checksum and
  decryption before restoration, and compare the encryption round trip against
  the captured bytes.
- **A wrong key was observed being denied.** An operational failure in the crypto
  tool is not evidence that a wrong key was refused. Require the tool's reported
  bad-passphrase status before recording that check.
- **The archive restores.** Restore in full into a disposable instance, in one
  transaction, failing on the first error; then inspect the result and compare it
  with what the capture recorded. Preserve object ownership where privileged
  definitions depend on it.
- **The rehearsal can reach nothing real.** A rehearsal runs with no network, no
  published port, no persistent data volume and no production passwords, and the
  routine never chooses a production restore destination.
- **Nothing is published until every step passed.** Keys stay separate from
  archives; archives, metadata and receipts stay outside Git; publication never
  overwrites a retained file. Capture tests make each verification step fail and
  confirm that nothing is published; project tests exercise actual restoration
  and permissions.
- **Every command is bounded, and every attempt is reclaimed.** Give each backup
  command a positive, finite timeout and review that bound against the project's
  expected archive size. Identify each disposable instance by its own generated
  name and a unique label, so cleanup after a failed, timed-out or attached
  command removes what this attempt created and never a namesake.

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
