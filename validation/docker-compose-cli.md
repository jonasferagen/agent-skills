# Validation — Docker Compose CLI

## Initial package — 9 October 2026

Version 0.1.0 is the project-scoped half of the retired containerization
package's CLI material, from its `owned-resources` reference and its
environments section. The [containerization history](containerization.md) holds
the trials that produced those rules; this page records only what the split
changed and what the new boundary has to hold.

Nothing here is new guidance. The split is a routing change, so the outstanding
work is routing evidence, not behavioral evidence.

### Why the cut falls here

Most compose accidents are a command that ran correctly against the wrong
project. The project is decided by inputs the command line does not show: the
caller's `COMPOSE_PROJECT_NAME`, `COMPOSE_FILE`, `COMPOSE_PROFILES` and
`COMPOSE_ENV_FILES`, and a developer's `.env` file in the working directory. An
explicit flag takes precedence, but a variable for an option that was not passed
still applies, which is why the rule is to strip the variables rather than rely
on precedence.

That failure has nothing in common with getting a port, a secret or a mount
right on a single `docker run`, which is what made the cut worth making rather
than keeping one Docker package.

### What the split moved here

Project selection on every call with the environment stripped; the rule that a
value takes effect only where compose reads it; no `container_name` or fixed
volume names in a disposable file; project identity and the
`com.docker.compose.project` label; loopback publishing read back with
`compose port`; the closed set of project names with parse-time refusal; and, in
the reference, cleanup registration, the borrowed-definition case, the
three-step teardown with `--volumes --remove-orphans --rmi local`, the prune
refusal, env-file custody and the daemon check.

### Shared rules and their copies

Four rules apply to both CLI packages and are duplicated under reciprocal copy
records rather than linked: resource naming, run identity with
label-over-pattern selection, cleanup registered before creation, and the prune
refusal. `docker-cleanup` records the last two from its own side.

The borrowed-definition rule is the seam the cut does not separate cleanly. Its
trigger is `compose run` against a developer stack, so it is owned here; the fix
is a `docker run` bind, so `docker-cli` states the mechanic too, under a
reciprocal record.

### Checks

Repository package validation, the shared-contract comparison and
`git diff --check` passed. The suite runner was not run in this worktree because
`node_modules` is not tracked there and the change adds no helpers.

## Image and build policy — 0.2.0, 9 October 2026

The [routing trial](docker-routing-trial-2026-10-09.md) raised that `compose run`
builds implicitly, and its case 2 declined to add `--no-build`. The flag does not
exist on `run`, so the case was declining something unavailable. This revision
supplies the mechanic the package was missing, measured rather than read.

### What was measured

Against Docker 29.4.3 and Compose v5.1.3, with a two-service fixture holding a
`build:` service over a local base image. Each probe ran under its own project
name and label, and both projects were removed and proved empty afterwards.

| Probe | Observed |
| --- | --- |
| `compose run`, image absent | Built it: `Image <project>-probe Built` |
| `compose run --pull never`, image absent | Built it anyway |
| `pull_policy: never` in the file, image absent | Built it anyway |
| `compose run`, image present, Dockerfile changed | Ran the stale image; no rebuild, no warning |
| `compose up`, image absent | Built it |
| `compose up`, image present, Dockerfile changed | Ran the stale image; no rebuild, no warning |
| `compose up --no-build`, image absent | Refused: `No such image` |
| `image:` by tag with no `build:`, image absent | Refused: `No such image` |

Two findings, not one. An absent image is built by both commands, and `run` has
no flag that refuses it — `--no-build` exists only on `up`. A present image is
never rebuilt by either command, so changed build inputs run as a success
against whatever the first build produced. `--pull never` and `pull_policy:
never` govern pulling and do not reach either case; that is the misconception
the section names explicitly, because it is the first thing a reader reaches for.

### What the section requires

An explicit build step, then `build:` kept out of the file a run reads so that a
missing image fails as `No such image`. Where one file must serve both, a
pre-run check that the image is present and carries the recorded identity. The
fallback is stated as a requirement because no flag covers it on `run`.

The trigger description is unchanged, so this adds no routing surface and needed
no new routing trial. A silent build and a stale image both fall inside the
existing "ignores a value" trigger. Whether image selection deserves naming in
the description is left open: changing it would make routing an acceptance
requirement under the [routing rule](../README.md#routing-quality).

### Checks

`python3 scripts/check.py` and `git diff --check` passed.

## Behavioral scenarios

Each rule's original evaluation is recorded under
[containerization](containerization.md#behavioral-scenarios); the status below
describes evidence for this package's own boundary.

| Request and context | Expected outcome | Evaluation status |
| --- | --- | --- |
| A compose call relies on the caller's environment | Every call passes project name, file and env file, and removes the four `COMPOSE_*` variables | Inherited: author review |
| Only the flags that were passed are relied on for precedence | Flagged: a variable for an unpassed option, such as active profiles, still applies | Inherited: author review |
| A wrapper holds a port or image tag to check it, without writing it where compose reads it | Flagged: compose falls back to its own default, usually the first selection's | Inherited: reproduced defect and fix in one project |
| A wrapper passes the project name on every invocation | No second copy exists, so no further check is needed | Inherited: author review |
| A disposable compose file sets `container_name` or a fixed volume name | Flagged: those names escape the project and collide between runs | Inherited: author review |
| `compose down --remove-orphans` is called with a mistyped project name | Refused at parse time; an unrecognised name is not passed through | Inherited: author review |
| A destructive reset is requested for a project whose data no seed reproduces | Refused, and its confirmation flag refused where it does not apply | Inherited: author review |
| A development project name is taken as evidence that its data is disposable | Rejected: the label alone is insufficient | Inherited: author review |
| `compose run` borrows a developer stack's service definition | A throwaway directory is bound at every mount point the run does not own, as a required argument | Inherited from containerization 1.1.0, measured |
| Teardown runs `compose down` but skips the leftover listing | Flagged: a stack that failed before compose recorded it stays invisible | Inherited: author review |
| A prune command would be faster than project-scoped teardown | Rejected: it reaches resources this work did not create | Inherited: author review |
| A `compose run` or `compose up` is written against a `build:` service | Flagged: an absent image is built with no evidence, and `run` has no flag that refuses it | Measured against a live daemon, 0.2.0 |
| A changed Dockerfile is expected to take effect on the next `run` or `up` | Flagged: neither command rebuilds a present image, so the run succeeds against the previous build | Measured against a live daemon, 0.2.0 |
| `--pull never` or `pull_policy: never` is offered as the way to stop a build | Rejected: both govern pulling and neither prevents a build | Measured against a live daemon, 0.2.0 |
| A request concerns one container or image command | Out of scope: `docker-cli` owns single-command mechanics | Author review only |
| A request concerns a host full of unattributed resources | Out of scope: `docker-cleanup` owns host-wide attribution and reclaim | Author review only |
| A request asks what a composed set must declare about its variants and prerequisites | Out of scope: an outcome owned by the consuming framework's convention | Author review only |

## Limits

The [routing trial](docker-routing-trial-2026-10-09.md) exercised this package
against its three near-neighbours. The risk recorded here before it ran — that a
request naming a stack could select `docker-cli` on the word "container" alone —
did not occur in any of the four cases.

Its case 2 exercised the borrowed-definition seam and read the convention's
outcome together with this package's mechanics, reporting the anchor link
between them as what joined the two passages. It also found one defect in this
package, now repaired at 0.1.1: the rule to pass `--env-file` on every call
could not be followed by a project with no env file, because compose rejects a
path that does not exist and omitting the flag is what lets a `.env` be picked
up.

That trial is entrypoint routing, not independent discovery: the agents read
project instructions and a collection entrypoint, not host-supplied skill
metadata. One run demonstrates the route, not its reliability.
