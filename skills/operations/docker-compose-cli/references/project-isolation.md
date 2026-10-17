# Project isolation and teardown

Use this reference when a compose command creates resources, borrows an existing
service definition, or has to leave nothing behind.

## Register cleanup before creating

Register removal by the project name and label before the first `compose up` or
`compose run`. A failure between creating a resource and registering its cleanup
leaks it, and the leak is invisible until it collides with something later.

Run cleanup steps in reverse order of registration. Run every step even when an
earlier step fails, and collect the failures. Keep the original failure as the
result and report cleanup failures in addition to it. If only cleanup fails,
fail the work.

Make teardown idempotent: a second request returns the first result. On `SIGINT`
or `SIGTERM`, run the same teardown, then exit with 130 or 143 so the caller
sees an interruption. Remove the signal listeners as the last teardown step.

## Bind the run's own state locations

A borrowed service definition is not a complete project. When using `extends`,
declare its required top-level named volumes, networks, secrets and configs in
the calling project; Compose does not bring those definitions across with the
service. Render the exact call with `docker compose config` before running it and
check that every inherited resource is declared.

Compose interpolates the files before it merges or overrides services. A
required `${NAME:?message}` in an extended service, or in a sibling service in
the selected file, can fail even when the caller overrides the field or never
starts the sibling. Provide the value or remove that requirement at its owner;
an override does not bypass it. Relative bind paths interpolated in an extended
file resolve from that file's directory. Check the rendered source paths with
the actual selected files, environment and working directory.

Because `extends` interpolates the whole file it reads, keep each fragment a
caller may extend, such as an optional variant overlay, in a file of its own.
Fragments that share a file make every caller set every fragment's required
values, including ones it never selects. Pass absolute paths into an extended
file, since a relative one resolves against that file's directory rather than
the caller's.

A `compose run` against an existing stack inherits that service definition's
mounts. It then writes into locations the service owns rather than the run: the
tool's home, its caches, its preferences, its per-project state. Cleanup by the
project name cannot reach those bytes, and the leftover listing below cannot see
them, because the location was never the run's to create or remove.

Bind a throwaway directory over every mount point the run does not own,
including the image's home when the tool keeps state there. A run-time bind at
the same target shadows the definition's volume for that run alone, so the
writes land where teardown already removes them.

Take that directory as a required argument of whatever assembles the run, not an
option with a default. A default is what the next call site omits, and the
omission is silent: the run passes, and the owned location is what changed.

<!-- Package-boundary copy: docker-cli/SKILL.md (Bind a location the command owns) carries this mechanic for a single command. Keep both passages aligned. -->

## Remove, sweep and prove

At teardown, remove the project in three steps:

1. `docker compose down --volumes --remove-orphans`, with every profile the work
   may have started. Add `--rmi local` to remove images compose built without a
   custom tag.
2. Remove any container, network, volume or image still carrying the project
   label or a label of your own, and any image tagged with the project's prefix.
3. List what still matches the project label or the image prefix. Fail the
   teardown if anything remains, and name it.

The third step turns cleanup into evidence. Without it, a stack that failed
before compose recorded it, or a resource created outside compose, stays
unnoticed.

Never clean up with `docker system prune`, `docker volume prune` or
`docker image prune -a`. Each reaches resources this work did not create.

<!-- Package-boundary copy: docker-cli/SKILL.md (Remove what the command created, and prove it) and docker-cleanup/SKILL.md (Select resources explicitly) state the prune refusal for their own scopes. Keep all three aligned. -->

## Keep secrets out of the file and off the command line

Generate a password or token in memory. Where compose needs an env file, create
it under an ignored directory with owner-only permissions and an exclusive-create
flag, so an existing file is never overwritten, and remove it at teardown.

Where a value can go to a single container instead, pass it through the CLI's own
environment and name it without a value. `--env NAME=value` puts the value in
the process list and in any error message that quotes the command.

Redact generated secrets from service logs and command output before quoting
them in a failure message.

## Check the daemon before the sequence

Check the daemon is reachable before work that depends on it. A missing daemon
is an unmet prerequisite, not a skip. Every listing comes back empty when it is
absent, and an empty result reads as a clean project.
