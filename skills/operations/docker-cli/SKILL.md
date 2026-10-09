---
name: docker-cli
description: "Write or review a `docker run`, `inspect`, `rm` or image invocation: argument boundaries, published ports, secrets, mounts, labels, identity and cleanup of resources a command creates. Use when a container command is being assembled or has behaved unexpectedly; multi-container projects belong to docker-compose-cli and host-wide reclaim to docker-cleanup."
metadata:
  version: "0.1.0"
---

# Docker CLI

A `docker` invocation is a command-line interface, and the usual command-line
failures apply to it: an argument that silently does nothing, a value that goes
somewhere observable, a resource created without anyone owning its removal. This
package covers driving the Docker CLI for single containers and images.

Two neighbours take the cases this one does not. A command that acts on a
project of several containers, through `docker compose`, belongs to
`docker-compose-cli`. Auditing and reclaiming what has accumulated on a host
across projects belongs to `docker-cleanup`. Both carry their own copies of the
identity and cleanup rules below, because each must work alone.

Deciding to use containers at all, and the outcomes a project's containers must
meet, are project convention rather than CLI usage.

## Name every resource a command creates

A `docker run` without `--rm` leaves a container. A `docker build` without a tag
leaves an untagged image. A `--volume` naming no source creates an anonymous
volume whose name is a hash nobody will recognise later.

- Pass `--rm` for a container that belongs to one command, so its removal does
  not depend on a later step running.
- Tag every image a command builds. An untagged image is indistinguishable from
  an abandoned one within the hour.
- Give every volume a name, or accept that the command owns deleting it before
  it exits. Anonymous volumes are the hardest resource on a host to attribute.

<!-- Package-boundary copy: docker-compose-cli/SKILL.md (Name every resource a command creates) states these rules for a project of containers. Keep both passages aligned. -->

## Give the work one identity

When a sequence of commands creates resources together, derive their names from
one identifier generated at the start, and label each resource with it.

Keep the identifier lower-case so it is valid in an image tag. Name each
resource with a shared prefix, such as `<namespace>-<id>-pg`, and label it with
the identifier, such as `--label <namespace>.run=<id>`, including images.

Names let a person find the resources. Labels let a later command select them by
owner. Select for removal by label, never by a name pattern alone: a pattern
matches whatever else happens to share the prefix, including another run's
resources and another project's.

<!-- Package-boundary copy: docker-compose-cli/SKILL.md (Give the work one identity) and docker-cleanup/SKILL.md (Attribute before classifying) state the label-over-pattern rule for their own scopes. Keep all three aligned. -->

## Keep secrets off the command line

Generate a password or token in memory. Pass it to the CLI through the CLI's own
environment and name it with `--env NAME`, with no value:

```sh
PGPASSWORD="$generated" docker run --env PGPASSWORD ...
```

`--env NAME=value` puts the value in the process list, where any user on the
host can read it, and in any error message that quotes the command. The
difference is the `=value`, which is easy to add back without noticing.

Redact generated secrets from command output and container logs before quoting
them in a failure message.

## Publish on loopback with an ephemeral port

Publish a port the host must reach as `--publish 127.0.0.1::5432`: loopback, and
an empty host port so the kernel assigns a free one. Read the assigned address
back with `docker port <container> 5432`, and check it is on loopback before
using it.

A fixed host port belongs to a service a person starts deliberately. A command
that needs one checks the port is free and fails when it is not, rather than
colliding with whatever already holds it.

An address a wrapper computed is not an address the container published. Read it
from `docker port`, so the wrapper and the daemon cannot disagree unnoticed.

## Bind a location the command owns

A container started from an existing service definition inherits that
definition's mounts and writes into locations the service owns: the tool's home,
its caches, its preferences, its per-project state. Bind a throwaway directory
over every mount point the command does not own, including the image's home when
the tool keeps state there. A run-time bind at the same target shadows the
definition's mount for that command alone.

Take that directory as a required argument of whatever assembles the command,
not an option with a default. A default is what the next call site omits, and
the omission is silent: the command succeeds, and the owned location is what
changed.

Mount an input the container only reads with `:ro`. A container does not widen
what the caller was authorized to reach.

<!-- Package-boundary copy: docker-compose-cli/references/project-isolation.md (Bind the run's own state locations) owns the `docker compose run` case this mechanic serves. Keep both passages aligned. -->

## Remove what the command created, and prove it

Register removal by label before the first resource exists. A failure between
creating a resource and registering its cleanup leaks it.

Run cleanup steps in reverse order of registration. Run every step even when an
earlier one fails, and collect the failures. Keep the original failure as the
result and report cleanup failures in addition to it; if only cleanup fails,
fail the command.

Make teardown idempotent, so a second request returns the first result. On
`SIGINT` or `SIGTERM` run the same teardown, then exit with 130 or 143 so the
caller sees an interruption. Remove the signal handlers as the last step.

Finish by listing what still carries the label and failing if anything remains,
naming it. That listing is what turns cleanup into evidence: a resource created
before its registration, or outside the sequence entirely, stays invisible
until it collides with something later.

Never clean up with `docker system prune`, `docker volume prune`, or
`docker image prune -a`. Each reaches resources this work did not create.

<!-- Package-boundary copy: docker-compose-cli/references/project-isolation.md (Remove, sweep and prove) and docker-cleanup/SKILL.md (Select resources explicitly) state the prune refusal for their own scopes. Keep all three aligned. -->

## Read the daemon rather than assuming it

`docker inspect` answers what a container actually got, which is not always what
the command asked for. Read back the mounts, the published ports, the labels and
the user when any of them carries operational meaning.

Check the daemon is reachable before a sequence that depends on it. A missing
daemon is an unmet prerequisite, not a skip, and every listing comes back empty
when it is absent — an empty result reads as a clean host.
