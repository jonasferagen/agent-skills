---
name: docker-compose-cli
description: "Write or review a `docker compose` invocation and the file it reads: project selection, inherited environment, profiles, borrowed service definitions and project-scoped teardown. Use when a compose command acts on the wrong stack, leaks resources or ignores a value. Single-container `docker` commands and host-wide reclaim of accumulated state are separate tasks."
metadata:
  version: "0.5.0"
---

# Docker Compose CLI

Every `docker compose` command acts on a project, and the project it acts on is
decided by more inputs than the command line shows. The caller's environment, a
developer's `.env` file in the working directory and the file's own defaults all
reach the same decision. Most compose accidents are a command that ran correctly
against the wrong project. This package covers the `docker compose` command
line; a single container or image command through plain `docker`, and auditing
what has accumulated on a host across projects, are separate tasks.

The project-selection rules apply to every compose call. The naming, port and
teardown rules apply to a disposable project that a script or test harness
creates and removes; a long-lived development stack a person starts by hand may
keep its fixed names and ports, and is never torn down under these rules. The
flags named here (`--no-build`, `--pull`, `--policy`, `--env-file`) are Compose
v2 flags; check `docker compose version` when one is rejected.

[Project isolation and teardown](references/project-isolation.md) holds the
inherited-environment rules, the borrowed-definition case and the teardown
sequence.

## Pass the project on every call

Pass `--project-name`, `--file` and `--env-file` on every invocation, including
the ones that only read. Without them the caller's `COMPOSE_PROJECT_NAME`,
`COMPOSE_FILE` or a `.env` file in the project directory can point the call at
another stack.

Where the project has no env file, `--env-file` still has to be passed, because
leaving it out is what lets a `.env` beside the compose file be picked up. Point
it at an empty file the call owns — `/dev/null` serves on a POSIX host — rather
than at a path that does not exist, which compose rejects. Passing nothing is
not the same as passing nothing to read.

An explicit flag takes precedence, but a variable for an option that was not
passed still applies — the active profiles being the one that catches people.
Remove `COMPOSE_PROJECT_NAME`, `COMPOSE_FILE`, `COMPOSE_PROFILES` and
`COMPOSE_ENV_FILES` from each call's environment rather than relying on
precedence alone.

A value a wrapper keeps to itself has not been applied. A published address, a
volume name or an image tag takes effect only where compose reads it, so write
each selection into the file or the arguments compose will read. A wrapper that
holds the value in order to check a port or print an address has not changed
what compose does: compose falls back to its own default, usually the first
selection's. Let any check read the value from where compose reads it — the
compose file, its env file or the command-line arguments — so the two cannot
disagree unnoticed.

## Name every resource the project creates

A compose file used for disposable work must not set `container_name` or a fixed
volume name. Both escape the project and collide when two projects overlap. Let
compose derive them from the project name, which is the identity being passed on
every call.

Tag an image the project builds, or let compose's own project-scoped tag stand;
an untagged build artifact is indistinguishable from an abandoned one within the
hour.

## Decide the image before the command runs

A service with a `build:` section builds its image whenever that image is
absent, on `compose run` as well as `compose up`. `compose up` takes
`--no-build` to refuse it. `compose run` has no such flag, so a run against a
`build:` service cannot be told not to build.

Once the image exists, neither command rebuilds it. A changed Dockerfile or a
changed build input is not noticed: the command runs the image already there and
reports success. The two behaviours compose into one hazard — the first run
builds an image nothing recorded, and every later run uses whatever that first
build produced.

Build in a step of its own, `docker compose build` or `--build` passed
deliberately, so the build has its own output and its own evidence. Then keep
`build:` out of the file a run reads: declare the service's `image:` by tag
there, and let the build step produce that tag. A run whose image is missing
then fails with `No such image` rather than building one, which is the refusal
`compose run` offers no flag for.

Where one file has to serve both — for example, the project's existing compose
file is the one under review and splitting it is out of scope — check before
starting the run that the image is present and carries the identity the project
recorded, and fail naming the image when it does not. `--pull never` and `pull_policy: never` do not cover
this: both govern pulling, and neither prevents a build.

`pull_policy: never` also holds against a plain `docker compose pull`: the
service is reported as skipped and the command exits zero even when the image
is absent, so a pull step cannot be taken as evidence that every image is
present. Pass `--policy missing` to `compose pull`, or `--pull missing` to
`compose up`, when the step must fetch an absent image; either overrides the
file's `never`. Without one, a later `up` or `run` fails with `No such image`.

## Give the work one identity

Derive the project name from one identifier generated when the work starts, and
keep it lower-case so it is valid in an image tag. Compose labels its own
resources with `com.docker.compose.project`, which is the authoritative signal
for everything it created. Add a label of your own for resources assembled
outside it.

Select resources for removal by label, never by a name pattern alone: a pattern
matches whatever else happens to share the prefix, including another project's
resources.

## Publish on loopback with an ephemeral port

Leave the host port empty in the file so the kernel assigns a free one, and read
the assigned address back with `docker compose port <service> <port>`. Check it
is on loopback before using it.

A fixed host port belongs to a stack a person starts deliberately. Disposable
work that needs one checks the port is free and fails when it is not.

## Validate the project name

A project-scoped command acts on whatever name it is given.
`compose down --remove-orphans` against a mistyped name does not fail — it acts
on a real project that happens to carry that name, or on an empty one and
reports success, so nothing surfaces the mistake.

If you build a wrapper around compose, validate the project name against an
allow-list before passing it to compose. That refusal is what stands between a
typo and another stack's containers. Decide it while the arguments are parsed,
so it is testable without a container engine and a wrong selection fails before
anything is created.

Never run a destructive reset or `down --volumes` on a project whose data you
cannot reproduce. Do not infer from a development name that the data behind it
is disposable.
