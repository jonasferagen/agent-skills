---
name: containerization
description: "Build, review or standardize local service containers: independent builds and state, HTTP or MCP boundaries, repeatable database migrations, disposable PostgreSQL tests, and test runs that own and remove the containers, networks, volumes and images they create. Use for development containers and local service stacks; production rollout policy remains with the project."
metadata:
  version: "0.2.0"
---

# Containerization

Make each service reproducible from its declared source and dependencies. Keep
the service's data and rules under its control while allowing a local stack to
connect several services. Adapt to the project's language, runtime and container
engine; separate repositories do not require different conventions.

## Establish the scope

Read the existing build, service entrypoints, migrations and local run commands.
Identify which service owns each database, credential, public operation and
background job. Preserve the user's chosen repository boundaries and deployment
scope. Containerizing local development does not authorize production migration,
data deletion or changes to a running shared service.

Prefer a small, working local setup. Keep explicitly deferred production work
deferred: this skill does not require a secret manager, backup system, public
ingress, high availability or a deployment platform.

## Build each service independently

- Build from the service's own checkout and declared dependency inputs. A sibling
  checkout or host-installed package must not silently supply missing code.
- Use the ecosystem's lockfile and reproducible install command. Declare the
  runtime/base image version and system packages needed to run the service.
- Keep credentials, local databases and unrelated host files outside the build
  context. Supply runtime configuration at launch; never bake secrets into an
  image, build argument or committed example.
- Copy built runtime files into the image. Development bind mounts are optional;
  verify the built image once without them so a mount cannot conceal a bad build.
- Name required configuration and defaults in one maintained place. Fail early
  for missing required values, without printing secrets.

## Connect services through their contracts

Give each service its own storage and runtime identity. Other services use its
published operations rather than reaching into its tables or mounting its data.
A composition file may wire addresses and dependencies without owning domain
rules. Independent services need not share a source tree or release together.

When both HTTP and MCP expose an operation, route them through the same
application handler and validation. Adapters translate protocol inputs, establish
the caller identity and map results; they do not duplicate business rules or
grant a stronger role. Carry the operation's retry identity through both paths
when it can cause durable effects. Add only the transports the task calls for.

Keep credentials scoped to the component using them. A migration process may
need DDL privileges; a normal request handler should use the service's narrower
runtime role. An orchestrator receives only the access its operations need.

## Make local startup and shutdown explicit

Use the existing container tool when suitable. Define one clear way to build,
start, inspect and stop the local stack. Expose host ports only where the local
client needs them; containers address dependencies through the stack's network.

Keep durable data in named storage owned by its service. Starting or rebuilding
must preserve it. A disposable test profile uses separate storage and clearly
identifies any destructive reset command; do not infer that existing data is
disposable from a development label.

When a test run creates containers, networks, volumes or images, read
[owned test resources](references/owned-resources.md). It covers run identity
and labels, cleanup registered before creation, Compose isolation, ephemeral
ports, secrets and a final check that nothing remains.

Distinguish a running process from a ready service. Check dependency readiness
with a bounded wait, apply required migrations, and report ready only when the
service can serve its contract. Starting two instances must not race migrations.
Handle termination, close connections and return failures through exit status.
Choose one owner for each scheduled job so the container and an external
orchestrator do not both run the same loop.

## Preserve migration history

Use the project's migration tool when it supplies these guarantees:

- Apply migrations in a deterministic order and record each successful version
  with a checksum in a database ledger. Reject an edited applied migration or an
  unexplained mismatch between the ledger and available history.
- Serialize migration runners with a database lock or equivalent tool guarantee.
  Bound lock waiting and make failure visible to the caller.
- Commit each transactional migration and its ledger entry atomically. Stop on
  failure; never mark a partially applied migration as successful. For statements
  that cannot run in a transaction, define recovery before execution.
- Keep platform bootstrap separate from domain migrations. Roles, extensions or
  platform-provided schemas must be declared prerequisites, not missing objects
  that cause the runner to silently skip SQL.
- Use the original history, or an explicitly reviewed baseline for a named
  starting state. A derived baseline records its source and replaced history;
  it does not pretend every original migration ran. Do not flatten or filter
  migrations merely to make a new engine accept them.

An empty-database bootstrap and an existing-database upgrade are different
paths. Verify the path being changed and name any path not exercised. Read
[database tests](references/database-tests.md) when selecting an embedded engine,
adapting platform bootstrap or checking migration behavior.

## Verify and report

Build the actual image, start its declared dependencies, and exercise a useful
public operation. Where state exists, verify restart persistence. Check the
changed failure paths, such as missing configuration or a failed migration.
Disposable embedded database tests support this work; they do not prove the
container image, network, credentials or native database configuration works.

Report what was built and run, how services connect, migration provenance and
known test limits. A missing required tool or dependency is an unmet prerequisite,
not a successful test. Preserve the test failure if cleanup also fails, and
report cleanup failure separately.
