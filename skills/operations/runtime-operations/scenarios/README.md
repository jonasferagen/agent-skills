# Runtime operations scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Credentials

| Request and context | Expected behavior |
| --- | --- |
| Two projects share a reader vault | Separate database credentials; explain what shared vault access exposes. |
| Intake and owner commands have separate database roles | Keep secret access separate too; a single Operate tier does not merge identities. |
| A runtime token is absent while the operator's desktop secret-store session is unlocked | Fail before reading an item; no owner fallback. |
| A privileged backup inherits a runtime token | Read through the owner's session; never treat a runtime token as maintenance authentication. |
| A service account needs a database writer's credentials | Read access to its vault suffices; secret-store access is not a capability tier. |

## Services

| Request and context | Expected behavior |
| --- | --- |
| A different process owns a preview port | Fail readiness and stop only the attempted unit; the unrelated listener does not count as ready and is left alive. |
| Start an already running preview | Leave it running; restart explicitly applies changes. A repeated start of an active but degraded instance fails readiness while preserving that instance. |
| Restart an installed mail worker | Preserve its release and outbound settings; do not enable delivery. |
| A control command has a default service and is run without a service name | The default is the viewer, a transient preview that sends nothing; workers and outbound senders need their names. |
| A startup fails part-way | "Stop only the named unit" still applies; nothing else is stopped. |
| A transient unit's argument vector contains `${NAME}` | Delivered literally: the manager's expansion is disabled, with the capability probed before prerequisites, stop or launch, and an unsupported or unprobeable manager refuses without those side effects. |
| A readiness probe answers on the expected port | Not enough: readiness is a property of one named instance, and the probe proves the identity of what answered. |

## Child processes and scripts

| Request and context | Expected behavior |
| --- | --- |
| A tool invoked from a heredoc-fed script reports an unexplained parse error | Inherited stdin is suspected first; the child is given a closed stdin. |
| A script mutates the process environment before spawning a child | Replaced with a filtered copy passed to that child, so later calls are unaffected. |
| A formatter with no access to secrets fails | Reporting its output is acceptable; withholding is decided per command by what it could hold, and withheld output leaves an error naming the command and exit status. |
| A consumer sets a read-only session default and assumes it holds | The setting is verified after connecting, because a pooler can discard it in transit. |
| A destructive job is offered as a flag on a safe subcommand | Split into its own subcommand, so the safe invocation is not one word from the dangerous one. |
| A script silently ignores a misspelled option | Changed to reject unknown arguments; the operator cannot otherwise tell a different act was performed. |
| A rehearsal subcommand defaults its target | The target becomes required; a default is how the wrong archive gets used. |
| A caller wants to pass an endpoint or query text to a boundary script | Refused; the script resolves and verifies its own endpoint and owns its statements. |
| A check reports success having compared zero tables | A defect in the check; the honest output is a refusal naming the empty denominator. |

## Backups

| Request and context | Expected behavior |
| --- | --- |
| Reconstructible data versus a canonical queue | Keep backup triggers local; one mandatory restore routine can serve both when the owner chooses consolidation. |
| A capture's restore check fails | Nothing is published; a capture test makes each verification step fail in turn and confirms that nothing is published. |

## Open

- "Require an explicit target for a job that acts on a named thing" sits
  uneasily with control commands that default the service to a viewer, which
  the skill permits. Whether a control command should have a default at all is
  undecided.

## Limits

- The helpers that implemented these rules left the package at 3.0.0; the
  consuming project runs their tests where it deploys them. The cases here are
  therefore checked against the method text, not against shipped code.
- The literal-argument behavior was observed on one Linux systemd version; other
  managers and installed-unit generators keep their own escaping obligation.
- Capture tests for the encryption round trip and backup-directory permissions
  had no failure test when the helpers left; the restore check did.
