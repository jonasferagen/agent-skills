# Runtime operations validation

The skill must preserve these decisions in realistic applications:

| Situation | Required result |
| --- | --- |
| Two projects share a reader vault | Separate database credentials; explain shared vault access. |
| Intake and owner commands have separate database roles | Keep secret access separate too; a single Operate tier does not merge identities. |
| Runtime token is absent while desktop 1Password is unlocked | Fail before reading an item; no owner fallback. |
| A privileged backup inherits a runtime token | Read through the owner's session; never treat a runtime token as maintenance authentication. |
| A different process owns a preview port | Fail readiness and stop only the attempted unit. |
| Start an already running preview | Leave it running; restart explicitly applies changes. |
| Restart an installed mail worker | Preserve its release and outbound settings; do not enable delivery. |
| A service control command with a default service is run without a service name | The default is the viewer, a transient preview that sends nothing; workers and outbound senders need their names. Whether a command should have a default at all is still open. |
| Reconstructible data versus a canonical queue | Keep backup triggers local; one mandatory restore routine can serve both when the owner chooses consolidation. |
| A tool invoked from a heredoc-fed script reports an unexplained parse error | Inherited stdin is suspected first; the child is given a closed stdin. |
| A script mutates the process environment before spawning a child | Replaced with a filtered copy passed to that child, so later calls are unaffected. |
| A formatter with no access to secrets fails | Reporting its output is acceptable; withholding is decided per command by what it could hold. |
| A consumer sets a read-only session default and assumes it holds | The setting is verified after connecting, because a pooler can discard it in transit. |
| A destructive job is offered as a flag on a safe subcommand | Split into its own subcommand, so the safe invocation is not one word from the dangerous one. |
| A script silently ignores a misspelled option | Changed to reject unknown arguments; the operator cannot otherwise tell a different act was performed. |
| A rehearsal subcommand defaults its target | The target becomes required; a default is how the wrong archive gets used. |
| A caller wants to pass an endpoint or query text to a boundary script | Refused; the script resolves and verifies its own endpoint and owns its statements. |
| A check reports success having compared zero tables | Treated as a defect in the check; the honest output is a refusal naming the empty denominator. |
| A capture's restore check fails | Nothing is published; a capture test makes that step fail and confirms it. |

Run the helper tests with `python3 -B -m unittest discover -s
collections/service-foundation/skills/runtime-operations/tests`. Validate the manifest with the skill-creator
validator. Consumer repositories verify their own project bindings and launchers.

Verification: helper failure-path tests pass, and both consumer adapters restored
synthetic archives. Work-system additionally checked rows, sequences, ACLs, command
ownership and runtime grants. Atlas also rehearsed a retained encrypted archive.
Live reader and operational credentials verified TLS and their expected database
roles. Work-system's live administrator password remains unprovisioned; these
checks do not claim a production Work backup.

## Clear writing pass — 2026-09-30

Version 1.1.1 revises the manifest; see the [package
sweep](clear-writing.md#package-sweep--2026-09-30). Metaphors such as "accuse
the wrong component" were replaced, long rules were split from their exceptions,
and the withheld-output rule now says to raise an error naming the command and
exit status, as `databaseBackup.py` does. Scripts and tests are unchanged; the
helper tests pass. Review found one edit that settled an open ambiguity; it was
reverted, and three wording corrections followed.

Left unresolved, because each answer changes behavior:

- "Use the same verbs across a project's scripts" is illustrated with option
  names (`--file`, `--archive`), not verbs.
- The manifest asks for a code comment explaining why child output is discarded;
  `databaseBackup.py` and `credentialStore.py` withhold output without one.
- "Capture tests should check failure before publication" can mean that tests
  check a failed capture is never published, or that capture checks for failure
  before publishing.

## Diagrams and tables pass — 2026-09-30

No change; see the [package
pass](diagrams-and-tables.md#package-pass--2026-09-30). Tables of tiers, helpers
and service commands would have moved facts between sections or needed values
the text does not state. Newly found: the text does not say whether the default
viewer is one of the previews that run as transient user services, or whether
"Stop only the named unit" also limits what a failed startup may stop.

## Resolutions — 2026-09-30

Version 1.2.0 carries these changes.

The owner accepted every recommendation from the contradiction review, and chose
option (c) for the naming rule. Helper tests pass (12 tests).

- Naming across scripts: "Use the same verbs" was illustrated with option names.
  The manifest now asks for the same subcommand and option names for the same
  job and the same input, keeping the `--file`/`--archive` example.
- Withheld output: the manifest asks for a comment saying why child output is
  discarded, and the helpers had none. The prose is unchanged;
  `databaseBackup.py` `run()` and `crypt()` and `credentialStore.py`
  `item_fields()` now carry that comment.
- Capture tests: "check failure before publication" had two readings. The
  manifest now says capture tests make each verification step fail and confirm
  that nothing is published. `test_failed_restore_does_not_publish` does this
  for the restore check; the encryption round-trip and backup-directory
  permission checks have no failure test yet, which stays open. A scenario above
  records the rule.
- Default viewer: the text did not say whether the viewer is a preview. The
  manifest now says that where a control command has a default service, it is a
  viewer, a preview that sends nothing, run as a transient user service, as
  work-system's `view` is.
- Failed start: the manifest now says "Stop only the named unit" applies after a
  failed start too, matching `serviceControl.py` and its test.
- Secret-store access: "Read permission on the secret store" read like the
  **Read** tier. The manifest now says secret-store access is not a capability
  tier; a service account needs only read access to its vault, even for a
  writer's credentials.
- Empty denominator: "an unsatisfiable threshold" named a cause rather than an
  empty set. The example now reads "a filter or threshold that nothing could
  meet", close to the paired `node-patterns` wording, which is unchanged.

Open questions, not changed:

- "Require an explicit target for a job that acts on a named thing" sits
  uneasily with the consumer control scripts, which default the service to
  `view` or `live`, and with the manifest's default viewer.
- `credentialStore.py` and `crypt()` raise errors that do not name the command
  and exit status, as the child-process rule asks.

## Discovery routing — 2026-09-30

The description was shortened. See [the discovery review](discovery.md) for the measured sizes, scope and verification. Earlier behavioral results do not establish the new discovery behavior.

## Shared HTTP service control and health — 2026-10-04

Unreleased service-foundation 0.3.0 / runtime-operations 1.4.0 extends the existing
controller to structured HTTP identity/readiness for both installed and transient
units. ServiceHealth owns `service-health/v1`; the configured binding verifies
service, MainPID, cgroup, reported/configured checkout, readiness and details shape.
Legacy PID health remains compatible for bindings that have not selected the new
contract. Installed release/startup policy stays in the unit; transient startup
stays explicit. Status now includes HTTP readiness. A repeated start of an active
but degraded instance fails readiness while preserving that instance. Checkout
mismatch refuses before dependency callbacks or mutation.

The complete source checker passed four checks: 21 skill entries/five collections,
39 runtime tests, 11 collection tests and 16 script tests, with zero skips. New
checks exercise structured identity, wrong checkout, active degraded preservation
and degraded status. A disposable mutation bypassing checkout verification made
the real HTTP probe regression fail as expected. The collection inventory and
whitespace checks passed. Sandboxed GnuPG checks could not run; the complete suite
rerun with local execution access passed.

Disposable real user-systemd installed and transient units independently exercised
start/stop/restart/status/logs, idempotent start, PID replacement on restart,
wrong-checkout stop refusal, degraded status/start preservation and occupied-port
startup refusal while leaving the unrelated listener alive. Only these synthetic
units were linked/stopped/removed. A first harness run hit socket TIME_WAIT when
rebinding the test listener; the fixture was corrected to reuse that address and
both complete lifecycle traces passed.

A fresh-context design trial through project-foundation reused the common controller
and health helper while retaining distinct unit lifetimes and valuable-state custody.
The companion [framework validation](https://github.com/jonasferagen/project-foundation/blob/main/validation/repository-services.md)
records its full read audit and the status/wording routing controls. Consumer
readiness checks remain necessary; these synthetic checks establish helper behavior,
not the health of every bound application.


## Literal transient arguments — 2026-10-07

An environment-profile adoption in Forge reproduced a framework defect: passing
an argument vector to systemd-run still lets the manager expand `${NAME}` before
an `env -i` wrapper executes. A literal synthetic HOME `/tmp/literal-${NAME}`
became `/tmp/literal-`. The [upstream systemd-run manual source](https://raw.githubusercontent.com/systemd/systemd/main/man/systemd-run.xml)
documents manager expansion and the `--expand-environment` switch introduced in
254. This is a downstream interpreter boundary, so argument-vector construction
alone cannot establish literal delivery.

Runtime-operations 2.0.0 now probes the client's advertised
`--expand-environment=` capability before prerequisites, stop/reset or launch,
and passes `--expand-environment=no` for transient services. Missing support or
an unavailable probe refuses without those side effects. Status, stop, logs,
already-active start and installed-unit actions retain their prior behavior.
The major skill version records changed transient host requirements and the
removal of implicit manager expansion. Python import API 1.1 remains unchanged;
consumers deliberately review host capability and existing bindings. Installed
unit generators retain their own escaping/literal-mode obligation.

The change uses existing runtime-operations ownership, clear-writing and
pattern-capture: preserve literal values through the manager, not merely through
the caller's argv. No new skill or launcher abstraction is added. A narrow
independent source review verified capability ordering, the changed binding
semantics and unaffected installed/status behavior; no material finding remains.
The existing Services entry directly states the capability and reaches the
runtime-helpers compatibility section. Source-authoring and real consumer use
exercised that route; no new discovery entry was introduced or cold-reader cost
reduction claimed.

`python3 scripts/check.py` passes all five checks on Python 3.14.4 and Node
24.15.0: 23 complete packages and 8 + 42 + 77 + 26 = 153 tests, no skips. The
runtime suite includes four new tests for literal argv, unsupported/unavailable
capability refusal before side effects and unaffected status/active-start. An
isolated mutation removing `--expand-environment=no` fails the new argv regression.
`git diff --check` passes. Canonical imported-package tests do not require a live
service manager.

A separate real observation used this changed `serviceControl.control` on host
systemd 259.5 with an owned random transient unit and synthetic loopback observer.
The script filename itself contained `${SYNTHETIC_UNSET}`; the child received
`literal ${SYNTHETIC_UNSET} $HOME $$ %n` unchanged, retained the literal synthetic
HOME, and excluded a synthetic manager-provided sentinel through `env -i`.
The controller verified the actual unit/cgroup PID health, then stopped that
owned unit; its final state was `not-found`/`inactive`. No global manager
environment or unrelated unit was changed. Temporary observer files were removed.
This establishes one Linux/systemd 259 observation, not coverage of every manager
version, installed-unit generator or application service.

This is a checked source revision without a release tag or full package release
self-conformance claim. Project-foundation and Forge must deliberately update
their complete checked imports before claiming adopted behavior. Other source
worktrees, including an unrelated partial runtime-artifact guidance edit, were
preserved and are not part of this change.
