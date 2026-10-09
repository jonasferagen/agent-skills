---
name: docker-compose-cli
description: "Write or review a `docker compose` invocation and the file it reads: project selection, inherited environment, profiles, borrowed service definitions and project-scoped teardown. Use when a compose command acts on the wrong stack, leaks resources or ignores a value; single containers belong to docker-cli and host-wide reclaim to docker-cleanup."
metadata:
  version: "0.1.1"
---

# Docker Compose CLI

Every `docker compose` command acts on a project, and the project it acts on is
decided by more inputs than the command line shows. The caller's environment, a
developer's `.env` file in the working directory and the file's own defaults all
reach the same decision. Most compose accidents are a command that ran correctly
against the wrong project.

Two neighbours take the cases this one does not. A single container or image
command belongs to `docker-cli`. Auditing and reclaiming what has accumulated on
a host across projects belongs to `docker-cleanup`. Both carry their own copies
of the identity and cleanup rules below, because each must work alone.

Deciding to use containers at all, and the outcomes a project's containers must
meet, are project convention rather than CLI usage.

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
selection's. Let any check read the value from the artifact compose reads, so
the two cannot disagree unnoticed.

## Name every resource the project creates

A compose file used for disposable work must not set `container_name` or a fixed
volume name. Both escape the project and collide when two projects overlap. Let
compose derive them from the project name, which is the identity being passed on
every call.

Tag an image the project builds, or let compose's own project-scoped tag stand;
an untagged build artifact is indistinguishable from an abandoned one within the
hour.

<!-- Package-boundary copy: docker-cli/SKILL.md (Name every resource a command creates) states these rules for a single command. Keep both passages aligned. -->

## Give the work one identity

Derive the project name from one identifier generated when the work starts, and
keep it lower-case so it is valid in an image tag. Compose labels its own
resources with `com.docker.compose.project`, which is the authoritative signal
for everything it created. Add a label of your own for resources assembled
outside it.

Select resources for removal by label, never by a name pattern alone: a pattern
matches whatever else happens to share the prefix, including another project's
resources.

<!-- Package-boundary copy: docker-cli/SKILL.md (Give the work one identity) and docker-cleanup/SKILL.md (Attribute before classifying) state the label-over-pattern rule for their own scopes. Keep all three aligned. -->

## Publish on loopback with an ephemeral port

Leave the host port empty in the file so the kernel assigns a free one, and read
the assigned address back with `docker compose port <service> <port>`. Check it
is on loopback before using it.

A fixed host port belongs to a stack a person starts deliberately. Disposable
work that needs one checks the port is free and fails when it is not.

## Treat the set of project names as closed

A project-scoped command acts on whatever name it is given.
`compose down --remove-orphans` against a mistyped name does not fail — it acts
on a project that now exists because the typo created it, or on a real project
that was not the intended one.

Refuse a name outside the known set rather than passing it through. That refusal
is what stands between a typo and another stack's containers. Decide it while
the arguments are parsed, so it is testable without a container engine and a
wrong selection fails before anything is created.

Refuse the commands that repopulate or delete data for a project whose data no
seed can reproduce, and refuse their confirmation flag where it does not apply,
so it cannot be carried unnoticed in a script. Do not infer from a development
name that the data behind it is disposable.
