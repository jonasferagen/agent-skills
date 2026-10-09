---
name: containerization
description: "Build or review independent local service containers, startup, the environments a local stack can run, and disposable test resources. Use for service images and local stacks; production rollout policy belongs to the project."
metadata:
  version: "1.1.0"
---

# Containerization

Make each service reproducible from its declared source and dependencies. Keep
the service's data and rules under its control while allowing a local stack to
connect several services. Adapt to the project's language, runtime and container
engine; separate repositories do not require different conventions.

Use the project's established service contracts and migration procedure. When the
task changes those designs, `service-boundaries` and `database-migrations` provide
separate guidance where available. Neither is required for container packaging.

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

When the API, migrator and seed command need the same built runtime files, use
one image for that service and select the command and credentials at launch.
In a disposable test stack, build that image once per run and reuse it for those
commands. Repeated build requests during seed or migration add work without
checking a different artifact unless the build inputs have changed. Keep images
scoped to their owning service and test run so cleanup cannot remove another
run's resources. If the processes genuinely need different files or system
packages, keep separate images and state that reason. Measure setup cost before
adding a cache or image-publishing workflow.

## Make local startup and shutdown explicit

Use the existing container tool when suitable. Define one clear way to build,
start, inspect and stop the local stack. Expose host ports only where the local
client needs them; containers address dependencies through the stack's network.

Keep durable data in named storage owned by its service. Starting or rebuilding
must preserve it.

When a test run creates containers, networks, volumes or images, read
[owned test resources](references/owned-resources.md). It covers run identity
and labels, cleanup registered before creation, Compose isolation, ephemeral
ports, secrets and a final check that nothing remains.

Distinguish a running process from a ready service. Check dependency readiness
with a bounded wait, apply required migrations, and report ready only when the
service can serve its contract. Use the project's migration entrypoint and its
concurrency controls rather than adding migration logic to a container wrapper.
Handle termination, close connections and return failures through exit status.
Choose one owner for each scheduled job so the container and an external
orchestrator do not both run the same loop.

## Separate the environments a stack can run

Name the environments the stack serves and make the selection one value: a
project or profile that chooses every service together, so a half-switched stack
cannot be expressed. Give each its own storage, credentials and published
addresses, and keep the selection observable without printing secrets. A
disposable test profile uses separate storage and clearly identifies any
destructive reset command; do not infer that existing data is disposable from a
development label.

Treat the set of names as closed. A project-scoped command such as
`compose down --remove-orphans` acts on whatever name it is given, so an
unrecognised name must be refused rather than passed through. That refusal is
what stands between a typo and another stack's containers.

A command's blast radius depends on which environment is selected, and
documenting that is not enough. Refuse the commands that repopulate or delete
data for an environment whose data no seed can reproduce, and refuse their
confirmation flag where it does not apply, so it cannot be carried unnoticed in
a script.

Decide all of this while the arguments are parsed. The refusals are then
testable without a container engine, and a wrong selection fails before anything
is created.

Parse time does not settle what the container tool renders. A published address,
a volume name or an image tag takes effect only where the tool reads it, so
write each environment's own value into that file or those arguments. A wrapper
that keeps the value to itself, to check that a port is free or to print an
address, has not applied it: the tool then falls back to its single default,
usually the first environment's. Let a check read the value from the artifact
the tool reads, so the wrapper and the tool cannot disagree unnoticed.

## Verify and report

Build the actual image, start its declared dependencies, and exercise a useful
public operation. Where state exists, verify restart persistence. Check the
changed failure paths, such as missing configuration or a failed migration.
Disposable embedded database tests support this work; they do not prove the
container image, network, credentials or native database configuration works.

Report what was built and run, how services connect, the startup commands used and
known test limits. A missing required tool or dependency is an unmet prerequisite,
not a successful test. Preserve the test failure if cleanup also fails, and
report cleanup failure separately.
