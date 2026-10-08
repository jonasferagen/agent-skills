# Validation — Service boundaries

## Extraction — 2 October 2026

Extracted the service-contract section from containerization 0.5.0. Added a
focused verification pass for adapter mapping, identities, rejection cases and
established retry behavior. Container packaging is outside this package's scope.

| Request and context | Expected outcome |
| --- | --- |
| Add MCP access to an operation already exposed over HTTP | Reuse the application handler and validation; preserve caller and retry identities. |
| One adapter grants a stronger role | Identify the authority change and preserve the operation's established authorization boundary. |
| Two services access one service's internal tables directly | Review the declared ownership and public operations without imposing a repository merge. |
| A command has durable effects and an established retry identity | Verify that both affected transports carry it to the shared handler and preserve replay behavior. |
| Handler tests pass but an adapter has not been exercised | Leave that adapter's mapping and identity behavior unverified. |
| Only HTTP is required | Add no MCP adapter and impose no service decomposition. |
| Change only a container build | Use the build workflow; do not redesign application handlers. |

These scenarios received author review. No independent agent trial or HTTP/MCP
implementation test was run. Package and link checks are recorded with the
extraction in the containerization validation page.

## Published filesystem boundary — 8 October 2026

The earlier author-reviewed scenarios exercised private tables and transport
adapters, but omitted a published filesystem resource. The unqualified phrase
"mounting its data" could reject that valid contract and encourage an unnecessary
service wrapper. The correction distinguishes published resources from private
implementation storage and adds that distinction to boundary verification. This
was a semantic coverage gap; package integrity checks could not detect it.

The environment-requirements trial record below retains the published-filesystem,
private-storage, external-database and owned-output cases and their limits.

See [environment requirement trials](environment-requirements-2026-10-08.md).
