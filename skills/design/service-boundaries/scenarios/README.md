# Service boundaries scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Add MCP access to an operation already exposed over HTTP | Reuse the application handler and validation; preserve caller and retry identities. |
| One adapter grants a stronger role | Identify the authority change and preserve the operation's established authorization boundary. |
| Two services access one service's internal tables directly | Review the stated ownership and public operations without imposing a repository merge. |
| A command has durable effects and an established retry identity | Verify that both affected transports carry it to the shared handler and preserve replay behavior. |
| Handler tests pass but an adapter has not been exercised | Leave that adapter's mapping and identity behavior unverified. |
| Only HTTP is required | Add no MCP adapter and impose no service decomposition. |
| A consumer needs a durability guarantee the shared resource's documented interface does not state | Raise it with the resource's owner; do not add consumer-side checks of the owner's internals. |
| A consumer reads another service's storage outside any documented interface | A boundary bypass; route through the owner. |
| A single application with no second service | Per-service storage and identity rules do not apply; review handlers, transports and callers only. |
| Change only a container build | Outside this skill; do not redesign application handlers. |

## Limits

- The skill ships no HTTP or MCP test harness; adapter behavior is verified with
  the project's own tests plus the manual checks listed in SKILL.md.
