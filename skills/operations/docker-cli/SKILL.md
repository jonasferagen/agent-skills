---
name: docker-cli
description: "Write or review a `docker run`, `inspect`, `rm` or image invocation: argument boundaries, published ports, secrets, mounts, labels, identity and cleanup of resources a command creates. Use when a container command is being assembled or has behaved unexpectedly. Multi-container projects driven through `docker compose`, and host-wide reclaim of accumulated state, are separate tasks."
metadata:
  version: "0.2.0"
---

# Docker CLI

A `docker` invocation is a command-line interface, and the usual command-line
failures apply to it: an argument that silently does nothing, a value that goes
somewhere observable, a resource created without anyone owning its removal. This
package covers driving the Docker CLI for single containers and images. A
project of several containers is driven through `docker compose`, which has its
own command-line interface and its own project-scoped teardown; auditing and
reclaiming what has accumulated on a host across projects is a separate task.

## Name every resource a command creates

A `docker run` without `--rm` leaves a container. A `docker build` without a tag
leaves an untagged image. A `--volume` naming no source creates an anonymous
volume whose name is a hash nobody will recognise later.

- Pass `--rm` for a container that belongs to one command, so its removal does
  not depend on a later step running.
- Tag every image a command builds. An untagged image is indistinguishable from
  an abandoned one within the hour.
- Give every volume a name, or rely on `--rm`, which removes the container's
  anonymous volumes with it; without `--rm` they stay behind, and they are the
  hardest resource on a host to attribute.
- Label a network the command creates the same way as every other resource,
  and remove it in the same teardown.
- Pass `--pull=never` when an earlier step built or pulled the image, so a
  missing image fails as `No such image` instead of being fetched as a side
  effect of the run. When no earlier step did, leave the default pull policy.

## Give the work one identity

When a sequence of commands creates resources together, derive their names from
one identifier generated at the start, and label each resource with it.

Keep the identifier lower-case so it is valid in an image tag: letters, digits
and hyphens, such as `$(date -u +%Y%m%d)-$(head -c4 /dev/urandom | od -An -tx1 | tr -d ' ')`.
Name each resource with a shared prefix, such as `<namespace>-<id>-pg`, and
label it with the identifier at creation, so the label-based cleanup below
matches exactly what was created:

```sh
docker build  --label "$NS.run=$ID" --tag "$NS-$ID-app" .
docker volume create --label "$NS.run=$ID" "$NS-$ID-data"
docker network create --label "$NS.run=$ID" "$NS-$ID-net"
docker run --rm --label "$NS.run=$ID" --name "$NS-$ID-pg" ...
```

A volume or network created implicitly by `docker run` carries no label, so
create it explicitly first. The namespace is a short fixed lower-case name for
the tool or project doing the work, such as `svc-test`, so its labels cannot be
confused with another tool's.

Names let a person find the resources. Labels let a later command select them by
owner. Select for removal by label, never by a name pattern alone: a pattern
matches whatever else happens to share the prefix, including another run's
resources and another project's.

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
using it: the printed address must start with `127.0.0.1:` (or `[::1]:`).

A fixed host port belongs to a service a person starts deliberately. A command
that needs one checks the port is free and fails when it is not, rather than
colliding with whatever already holds it; `ss -ltn '( sport = :5432 )'` (or
`lsof -iTCP:5432 -sTCP:LISTEN` on macOS) printing a listener means it is taken.

An address a wrapper computed is not an address the container published. Read it
from `docker port`, so the wrapper and the daemon cannot disagree unnoticed.

## Bind a location the command owns

A container started with the mounts of a longer-lived setup, such as a
developer's running stack or a tool's installed configuration, writes into
locations that setup owns: the tool's home, its caches, its preferences, its
per-project state. Bind a throwaway directory over every mount point the command
does not own, including the image's home when the tool keeps state there. A
run-time bind at the same target shadows the inherited mount for that command
alone. Find those mount points with
`docker inspect --format '{{range .Mounts}}{{.Destination}} {{end}}' <container>`
on the longer-lived container, and the image's own declared volumes with
`docker image inspect --format '{{.Config.Volumes}}' <image>`.

Take that directory as a required argument of whatever assembles the command,
not an option with a default. A default is what the next call site omits, and
the omission is silent: the command succeeds, and the owned location is what
changed.

Mount an input the container only reads with `:ro`. A container does not widen
what the caller was authorized to reach.

## Remove what the command created, and prove it

These rules apply to a script or harness that assembles the command and owns
its cleanup. For a one-off interactive `docker run --rm`, the container's own
removal is the cleanup.

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

In shell, the skeleton is a `cleanup` function registered before the first
`docker` command that creates anything, selecting by the label from "Give the
work one identity". Steps run in reverse order of creation, every step runs
even when one fails, the function is safe to call twice, and a signal exits
with 130 or 143 after the same teardown:

```sh
L="label=$NS.run=$ID"; ran=0
cleanup() {
  [ "$ran" = 1 ] && return 0; ran=1; fails=""
  docker ps -aq        --filter "$L" | xargs -r docker rm -f      || fails="$fails containers"
  docker network ls -q --filter "$L" | xargs -r docker network rm || fails="$fails networks"
  docker volume ls -q  --filter "$L" | xargs -r docker volume rm  || fails="$fails volumes"
  docker images -q     --filter "$L" | xargs -r docker rmi -f     || fails="$fails images"
  left=$( { docker ps -aq --filter "$L"; docker network ls -q --filter "$L"
            docker volume ls -q --filter "$L"; docker images -q --filter "$L"; } )
  [ -z "$fails" ] && [ -z "$left" ] || { echo "cleanup failed:$fails left: $left" >&2; return 1; }
}
trap 'cleanup; exit 130' INT; trap 'cleanup; exit 143' TERM; trap cleanup EXIT
```

Never clean up with `docker system prune`, `docker volume prune`, or
`docker image prune -a`. Each reaches resources this work did not create. Even
with a `--filter label=` added, prefer the explicit listings above, so the
removal and the leftover check use the same selection.

## Read the daemon rather than assuming it

`docker inspect` answers what a container actually got, which is not always what
the command asked for. Read back the mounts, the published ports, the labels and
the user when any of them carries operational meaning.

Check the daemon is reachable before a sequence that depends on it, with
`docker info >/dev/null` and a non-zero exit treated as failure. A missing
daemon is an unmet prerequisite, not a skip, and every listing comes back empty
when it is absent — an empty result reads as a clean host.
