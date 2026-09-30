# Validation — Containerization

## Behavioral scenarios

These scenarios define expected behavior for the initial package. The author
reviewed the instructions against them. One independent agent outline trial is
recorded below; generated container implementations have not been tested.

| Request and context | Expected outcome | Evaluation status |
| --- | --- | --- |
| Containerize two services in separate repositories | Each builds from declared inputs and owns storage and credentials; a local stack wires public contracts. No repository merge is required. | Author review only |
| Standardize a Python service after a TypeScript service | Reuse lifecycle and migration conventions; preserve the language and select suitable test tooling. | Author review only |
| Expose the same correction through HTTP and MCP | Both adapters establish caller identity and use one application handler; retry identity reaches the handler unchanged. | Author review only |
| The image works only with a sibling source checkout mounted | Identify the undeclared build dependency and verify a standalone image without source mounts. | Author review only |
| Runtime credentials appear in a Dockerfile or build argument | Move them to runtime configuration and keep secrets outside the build context and image. | Author review only |
| A service and an orchestrator both schedule the same job | Choose one schedule owner and preserve an explicit one-shot operation. | Author review only |
| A new database lacks platform-provided roles or functions | Declare platform bootstrap separately; do not skip failing domain migrations. | Author review only |
| Historical migrations need a managed platform absent locally | Use the platform or a reviewed derived baseline with provenance and explicit limits. Keep original history. | Author review only |
| A baseline is used to mark all original migrations successful | Reject the fabricated history; record the baseline and its replaced history explicitly. | Author review only |
| Two processes start migrations together | Require serialized migration execution and bounded visible failure; test contention with independent native sessions. | Author review only |
| An applied migration changes after its first run | Detect the checksum mismatch and stop before later migrations. | Author review only |
| A migration fails after changing a table | Roll back transactional work and its ledger entry, or use documented recovery for a nontransactional step; do not mark success. | Author review only |
| Embedded PostgreSQL lacks a required extension | Select compatible native tests or disclose the gap; do not transform SQL silently. | Author review only |
| An in-memory test passes under one privileged connection | Limit the claim to what ran; actual login grants, concurrent sessions and transport still need suitable checks. | Author review only |
| Test assertions fail and database cleanup also fails | Preserve the test failure, report cleanup failure separately and return a failing status. | Author review only |
| All embedded tests pass but the service image has not run | Report the embedded evidence and leave image/startup verification unclaimed. | Author review only |
| Local container work explicitly defers production operations | Complete the requested local setup without adding backup systems, a secret manager or deployment requirements. | Author review only |
| A request would reset an existing development volume | Establish that the data is disposable or that deletion is authorized; the development label alone is insufficient. | Author review only |

## Sources and scope

The package is newly authored as reusable local-service guidance. It contains no
project names, database identifiers, credentials or prescribed application stack.
The database reference uses PGlite only as an example of embedded PostgreSQL.
Official PGlite documentation and PostgreSQL's `CREATE INDEX` documentation were
checked for the concrete engine limitations cited in that reference.

## Verification results

- Package validator: passed on 2026-09-30; 12 installable packages checked.
- System skill quick validation: passed on 2026-09-30 for `containerization`.
- Whitespace check: `git diff --check` passed on 2026-09-30; new files were
  additionally checked directly before handoff.
- Independent behavioral evaluation: one outline trial passed on 2026-09-30,
  with the scope and limitations below.
- Built container, embedded database or native PostgreSQL execution: not run;
  this package contains instructions and no executable helper.

Record actual trials and remaining limits here before describing the behavioral
scenarios as verified. Passing manifest validation establishes package structure
and local links, not the quality of generated container implementations.

## Independent outline trial — 2026-09-30

A separate agent read the package and answered a synthetic request for a Python
catalog and TypeScript jobs service in separate repositories. The request named
HTTP/MCP, in-memory PostgreSQL tests, managed-platform roles, a concurrent-index
migration, a suggested SQL-filtering/baseline shortcut, cleanup failures, and
deferred production credentials/backups. It received no expected-answer checklist.

Observed response:

- Kept both languages/repositories, independent images, data and identities.
- Routed HTTP/MCP through shared handlers with retry identity and authorization.
- Rejected silent SQL removal and fictitious historical migration entries.
- Separated platform bootstrap from domain history and explained baseline checks.
- Required native testing and recovery for the concurrent-index migration.
- Limited embedded claims, preserved original errors during cleanup, and kept
  production operations deferred.

Result: the response followed the intended guidance for this combined scenario.
This was a read-only planning trial, not evidence that generated code builds,
migrations execute or containers work. Other scenarios remain author review only.
