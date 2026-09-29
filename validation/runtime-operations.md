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

Run the helper tests with `python3 -B -m unittest discover -s
skills/runtime-operations/tests`. Validate the manifest with the skill-creator
validator. Consumer repositories verify their own project bindings and launchers.

Verification: helper failure-path tests pass, and both consumer adapters restored
synthetic archives. Work-system additionally checked rows, sequences, ACLs, command
ownership and runtime grants. Atlas also rehearsed a retained encrypted archive.
Live reader and operational credentials verified TLS and their expected database
roles. Work-system's live administrator password remains unprovisioned; these
checks do not claim a production Work backup.
