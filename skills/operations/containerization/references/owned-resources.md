# Owned test resources

Use this guidance when a test run creates containers, networks, volumes, images
or files through Docker or Compose. The run must be able to find everything it
created, remove only that, and prove that nothing is left. The examples use the Docker CLI; apply the same ownership
rules with another container engine.

## Give the run one identity

Create a unique run ID when the run starts, from a timestamp and a random
suffix. Keep it lower-case so it is valid in image tags and Compose project
names. Derive everything the run creates from that ID:

- Name each resource with a common prefix, such as `<namespace>-<run id>-pg`,
  and use `<namespace>-<run id>` as the Compose project name.
- Label each resource with the ID, such as `<namespace>.run=<run id>`, including
  images the run builds. Compose also labels its resources with
  `com.docker.compose.project=<project>`.

Names help a person find a run's resources. Labels let cleanup select resources
by owner. Never select a run's resources by a name pattern alone, and never
clean up with `docker system prune`, `docker volume prune` or any command that
can reach resources this run did not create.

## Register cleanup before creating

Register removal by the run's label before the first `docker run` or
`compose up`. A failure between creating a resource and registering its cleanup
would otherwise leak it.

Run cleanup steps in reverse order of registration. Run every step even when an
earlier step fails, and collect the failures. Keep the test or setup failure as
the run's result and report cleanup failures in addition to it. If only cleanup
fails, fail the run.

Make teardown idempotent: a second request returns the first result. On
`SIGINT` or `SIGTERM`, run the same teardown, then exit with 130 or 143 so the
caller sees an interruption. Remove the signal listeners as the last teardown
step.

## Keep Compose on the intended project

Pass `--project-name`, `--file` and `--env-file` on every Compose call. Without
them, the caller's `COMPOSE_PROJECT_NAME`, `COMPOSE_FILE` or a developer's `.env`
file in the project directory can point the call at another stack. Also remove
`COMPOSE_PROJECT_NAME`, `COMPOSE_FILE`, `COMPOSE_PROFILES` and `COMPOSE_ENV_FILES`
from the environment of each call. An explicit flag takes precedence, but a
variable for an option you did not pass, such as the active profiles, still
applies.

A Compose file used for test stacks must not set `container_name` or fixed volume
names. Those names escape the project and collide when two runs overlap.

## Bind the run's own state locations

A run that starts a container from an existing service definition, such as
`docker compose run` against a developer stack, inherits that definition's
mounts. It then writes into locations the service owns rather than the run:
the tool's home, its caches, its preferences, its per-project state. Cleanup by
the run's label cannot reach those bytes, and the leftover listing above cannot
see them, because the location was never the run's to create or remove.

Bind a throwaway directory over every mount point the run does not own,
including the image's home when the tool keeps state there. A run-time bind at
the same target shadows the definition's volume for that run alone, so the
writes land where teardown already removes them.

Take that directory as a required argument of whatever assembles the run, not
an option with a default. A default is what the next call site omits, and the
omission is silent: the run passes, and the owned location is what changed.

## Publish on ephemeral loopback ports

Publish a test service on loopback with an ephemeral host port, as in
`--publish 127.0.0.1::5432` or an empty host port in Compose. Read the assigned
address back with `docker port` or `docker compose port` and check that it is on
loopback before using it. A fixed port belongs to a developer stack; a test run
that needs one checks it is free and fails when it is not.

## Keep secrets off command lines

Generate a run's passwords and tokens in memory. Pass each value to the Docker
CLI through the CLI's environment and name it with `--env NAME`, without a value.
The value then stays out of the process list and out of any error message that
quotes the command. Write an env file only when Compose needs one: create it
under an ignored run directory with owner-only permissions and an exclusive-create
flag so an existing file is never overwritten, and remove it at teardown.

Redact every generated secret from service logs and command output before
quoting them in a failure message.

## Remove, sweep and prove

At teardown, remove the stack in three steps:

1. `docker compose down --volumes --remove-orphans` with every profile the run
   may have started. Add `--rmi local` to remove images Compose built without a
   custom tag.
2. Remove any container, network, volume or image still carrying the run's
   label, and any image tagged with the run's prefix.
3. List what still matches the run label, the Compose project label or the image
   prefix. Fail the teardown if anything remains, and name it.

The third step turns cleanup into evidence. Without it, a stack that failed
before Compose recorded it, or a resource created outside Compose, stays
unnoticed until it collides with a later run.

## Start disposable databases cheaply

For a disposable PostgreSQL container, mount its data directory on `tmpfs`
(`--tmpfs /var/lib/postgresql/data`) so no volume exists to leak. Wait for
readiness with a query over TCP using a password, with a deadline. The image's
initialization runs a temporary server that listens only on its socket, so a
successful socket connection can come from that server rather than the final
one. Socket trust authentication also proves nothing about logins, so connect
with the credentials the test is about.

Check that the Docker daemon is available when the run starts. A missing daemon
fails a tier that requires it. It does not turn the tier into a skip.
