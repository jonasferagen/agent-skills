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
| A request concerns one container or image command | Out of scope: `docker-cli` owns single-command mechanics | Author review only |
| A request concerns a host full of unattributed resources | Out of scope: `docker-cleanup` owns host-wide attribution and reclaim | Author review only |
| A request asks what a composed set must declare about its variants and prerequisites | Out of scope: an outcome owned by the consuming framework's convention | Author review only |

## Limits

No automatic discovery trial has been run. The routing acceptance requirement
applies before a release tag, and the trial must separate four near-neighbours:
this package, `docker-cli`, `docker-cleanup` and the consuming framework's
local-containers convention. The risk specific to this package is that a request
naming a stack or several services could select `docker-cli` on the word
"container" alone.
