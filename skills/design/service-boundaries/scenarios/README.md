# Service boundaries scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Add MCP access to an operation already exposed over HTTP | Reuse the application handler and validation; preserve caller and retry identities. |
| One adapter grants a stronger role | Identify the authority change and preserve the operation's established authorization boundary. |
| Two services access one service's internal tables directly | Review the declared ownership and public operations without imposing a repository merge. |
| A command has durable effects and an established retry identity | Verify that both affected transports carry it to the shared handler and preserve replay behavior. |
| Handler tests pass but an adapter has not been exercised | Leave that adapter's mapping and identity behavior unverified. |
| Only HTTP is required | Add no MCP adapter and impose no service decomposition. |
| A tool writes into a shared directory its provider publishes | A published resource, not private storage: the write completes when the published contract says; report no persistence caveat. |
| A consumer needs a durability guarantee the contract does not state | Raise it with the provider; do not add a consumer-side probe. |
| A consumer reads private service storage outside any published contract | A boundary bypass; route through the owner. |
| Consumers copy the host path behind a provider's shared directory | Bind the selector the provider publishes instead of the path behind it. |
| Change only a container build | Use the build workflow; do not redesign application handlers. |

## Limits

- All cases are author-reviewed; no independent agent trial or HTTP/MCP
  implementation test has run.
- The published-filesystem distinction was added after the original cases
  omitted it, a semantic gap package checks cannot detect.
