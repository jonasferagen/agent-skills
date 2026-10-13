# Docker Compose CLI scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Project selection and identity

| Request and context | Expected behavior |
| --- | --- |
| A compose call relies on the caller's environment | Every call passes project name, file and env file, and removes the four `COMPOSE_*` variables. |
| Only the flags that were passed are relied on for precedence | Flagged: a variable for an unpassed option, such as active profiles, still applies. |
| A project has no env file | `--env-file` is still passed, pointed at an empty file the call owns such as `/dev/null`; omitting the flag is what lets a `.env` beside the compose file be picked up, and compose rejects a path that does not exist. |
| A wrapper holds a port or image tag to check it, without writing it where compose reads it | Flagged: compose falls back to its own default, usually the first selection's. |
| A wrapper passes the project name on every invocation | No second copy exists, so no further check is needed. |
| A disposable compose file sets `container_name` or a fixed volume name | Flagged: those names escape the project and collide between runs. |
| `compose down --remove-orphans` is called with a mistyped project name | Refused at parse time; an unrecognised name is not passed through. |
| A destructive reset is requested for a project whose data no seed reproduces | Refused, and its confirmation flag refused where it does not apply. |
| A development project name is taken as evidence that its data is disposable | Rejected: the label alone is insufficient. |
| `compose run` borrows a developer stack's service definition | A throwaway directory is bound at every mount point the run does not own, as a required argument. |
| A borrowed service uses a named volume declared only in its source file | The calling project declares the volume too; `extends` does not carry the source file's top-level declaration. |
| An override replaces a borrowed bind containing a required variable, or selects a file with an unused sibling requiring one | The required interpolation is still checked before merge or service selection; provide the value or repair the source requirement. |
| An extended file interpolates a relative bind path while the caller runs Compose elsewhere | Check `docker compose config` with the actual files, environment and working directory; the bind resolves from the extended file's directory. |

## Images and builds

Measured against Docker 29.4.3 and Compose v5.1.3 with a two-service fixture
holding a `build:` service over a local base image, each probe under its own
project name and label.

| Request and context | Expected behavior |
| --- | --- |
| A `compose run` or `compose up` is written against a `build:` service | Flagged: an absent image is built with no evidence, and `run` has no flag that refuses it (`--no-build` exists only on `up`). An explicit build step runs first, and `build:` stays out of the file a run reads so a missing image fails as `No such image`. |
| A changed Dockerfile is expected to take effect on the next `run` or `up` | Flagged: neither command rebuilds a present image, so the run succeeds against the previous build. |
| `--pull never` or `pull_policy: never` is offered as the way to stop a build | Rejected: both govern pulling and neither prevents a build. |
| One compose file must serve both the build and the run | A pre-run check that the image is present and carries the recorded identity. |

## Teardown and scope

| Request and context | Expected behavior |
| --- | --- |
| Teardown runs `compose down` but skips the leftover listing | Flagged: a stack that failed before compose recorded it stays invisible. |
| A prune command would be faster than project-scoped teardown | Rejected: it reaches resources this work did not create. |
| A request concerns one container or image command | Out of scope: docker-cli owns single-command mechanics. |
| A request concerns a host full of unattributed resources | Out of scope: docker-cleanup owns host-wide attribution and reclaim. |
| A request asks what a composed set must declare about its variants and prerequisites | Out of scope: an outcome owned by the consuming project's convention. |

## Open

- Whether image selection deserves naming in the skill's description is
  undecided; changing it makes routing an acceptance requirement.

## Limits

- The port-fallback and borrowed-definition rules come from reproduced defects
  and measured fixes in one project; the build-policy rules were measured as
  above; the rest are author-reviewed.
- The `extends` declaration, interpolation and relative-path cases were
  reproduced with synthetic files using Docker 29.4.3 and Compose v5.1.3;
  `config` exercised parsing only, not a running container or registry pull.
- One routing trial exercised the borrowed-definition seam and found the
  missing-env-file defect now repaired. The risk that a request naming a stack
  selects docker-cli on the word "container" did not occur in its four cases.
