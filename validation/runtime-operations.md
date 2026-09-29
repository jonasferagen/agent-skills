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

Run the helper tests with `python3 -B -m unittest discover -s
skills/runtime-operations/tests`. Validate the manifest with the skill-creator
validator. Consumer repositories verify their own project bindings and launchers.

Verification: helper failure-path tests pass, and both consumer adapters restored
synthetic archives. Work-system additionally checked rows, sequences, ACLs, command
ownership and runtime grants. Atlas also rehearsed a retained encrypted archive.
Live reader and operational credentials verified TLS and their expected database
roles. Work-system's live administrator password remains unprovisioned; these
checks do not claim a production Work backup.
