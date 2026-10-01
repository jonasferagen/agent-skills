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
| A test run starts a database container, then registers its cleanup | Cleanup by the run's label is registered before the container exists. | Author review only |
| Teardown removes test containers by a name pattern or with a prune command | Rejected: removal selects by the run's label, and prune commands can reach resources the run did not create. | Author review only |
| One teardown step fails | Later steps still run; failures are collected, the test failure stays the result, and cleanup alone failing fails the run. | Author review only |
| The test run is interrupted with Ctrl-C | The same teardown runs, then the process exits with 130. | Author review only |
| A test calls `docker compose` relying on the caller's environment | Every call passes project name, file and env file, and removes the `COMPOSE_*` variables that could redirect it. | Author review only |
| A test Compose file sets `container_name` or a fixed volume name | Flagged: those names escape the project and collide between runs. | Author review only |
| A test passes a database password with `--env NAME=value` | Moved into the CLI's environment and passed as `--env NAME`, so the value stays off the command line. | Author review only |
| `compose down` succeeds after a partly failed start | The label sweep and a final listing of leftovers still run; anything left fails teardown. | Author review only |
| A readiness check connects over the container's local socket | Replaced with a TCP query using a password; the initialization server accepts socket connections before the final server starts. | Author review only |
| API, migrator and seed use the same runtime files but every test seed requests another image build | Build one service image per run and reuse it with distinct commands and credentials; keep ownership and cleanup scoped to that run. | Author review only |
| Seed genuinely needs different system packages from the API | Keep a separate image and state why; do not force reuse for its own sake. | Author review only |
| A stack tool gains a second retained environment beside its development one | The environment names are a closed set; a name outside it is refused rather than passed to a project-scoped command | Author review; one implemented case |
| A seed or reset command is available for an environment whose data no seed can reproduce | Refused for that environment, decided while the arguments are parsed, so nothing is created | Author review; one implemented case |
| A confirmation flag for a destructive command is accepted where it has no meaning | Rejected: refuse it outside the case it applies to, so it cannot be carried unnoticed in a script | Author review; one implemented case |
| One service is pointed at a different environment from its peers | Rejected: one selection chooses the environment for every service, so a half-switched stack cannot be expressed | Author review; one implemented case |
| A stack has one development environment plus disposable test runs | The new section adds nothing beyond the existing storage and cleanup rules; it does not activate | Author review — non-activating case |

## Sources and scope

The package is newly authored as reusable local-service guidance. It contains no
project names, database identifiers, credentials or prescribed application stack.
The database reference uses PGlite only as an example of embedded PostgreSQL.
Official PGlite documentation and PostgreSQL's `CREATE INDEX` documentation were
checked for the concrete engine limitations cited in that reference.

## Verification results

The 0.3.0 image-reuse addition was author-reviewed against the two new scenarios
above. It has not been implemented or timed in a consuming project; the original
0.1.0 trial and verification below do not establish that it saves time.
On 2026-09-30, the current tree passed the package validator (15 packages),
the system skill validator for `containerization`, and `git diff --check`.

- Initial 0.1.0 package validator: passed on 2026-09-30; 12 installable packages checked.
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

## Owned test resources — 2026-09-30

Version 0.2.0 adds [owned test resources](../skills/containerization/references/owned-resources.md)
and links it from the manifest and the database-tests lifecycle. It was drawn
from three Docker harnesses in the local atlas-work-dev repository at `fb61765`:
the shared native-database helper copied into both services, and the integration
suite's stack harness. They had converged independently on run labels, early
cleanup registration, a label sweep after `compose down`, a leftover listing,
and removing the `COMPOSE_*` variables. The reference names no project
identifiers.

Checks behind specific statements: the stock PostgreSQL image's temporary
initialization server listening only on its socket is documented in the image's
entrypoint and relied on by the source harness. Compose's project label and
`--rmi local` behavior are documented Compose behavior. No new container trial
ran for this reference; the scenarios above remain author review.

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

## Discovery routing — 2026-09-30

The description was shortened. See [the discovery review](discovery.md) for the measured sizes, scope and verification. Earlier behavioral results do not establish the new discovery behavior.

## Multiple retained environments — 2026-09-30

Version 0.4.0 adds "Separate the environments a stack can run" and moves the
disposable-profile sentence into it, so the startup section no longer carries
both lifecycle and environment rules. No requirement was removed: that sentence
is preserved verbatim in its new home.

The mechanism came from one implemented case rather than a survey. A local
Compose stack that had served a development project and disposable test runs
gained a second retained environment for an imported copy of real data. Three
defects followed from the tool still assuming two kinds of environment:

- Its seed command accepted any project, so it would have written synthetic rows
  into the environment holding the real copy. The refusal now happens while the
  arguments are parsed.
- Its destructive-project guard admitted exactly two name shapes and refused
  everything else, which was correct but had to be extended deliberately rather
  than loosened: `compose down --remove-orphans` removes every container of the
  project it is given, so the closed set is the protection.
- A published-port default fell back to the development environment's fixed
  port when an environment did not declare one, which would have collided with
  the running development stack. This is the weakest of the three and is not
  stated as a rule in the skill; it is recorded here as the observation that
  suggested "give each its own published addresses".

Limits. One project supplied the mechanism, so recurrence is not established.
The guidance was applied to that project and its refusals were tested there
without a container engine; it has not been applied to another stack, another
container tool, or an environment set larger than three. The non-activating case
in the table above was reasoned through by the author, not observed. Nothing
here establishes that a generated implementation of this guidance works.
