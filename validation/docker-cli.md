# Validation — Docker CLI

## Initial package — 9 October 2026

Version 0.1.0 is one half of the retired containerization package's CLI
material, taken from its `owned-resources` reference and from the parse-time
rules in its environments section. The
[containerization history](containerization.md) holds the trials that produced
those rules; this page records only what the split changed and what the new
boundary has to hold.

Nothing in this package is new guidance. Each rule arrived with evidence
recorded against containerization, including the measured port-selection defect
and the borrowed-definition case from 1.1.0. The split is a routing change, so
the outstanding work is routing evidence, not behavioral evidence.

### What the split moved here

Single-container and image mechanics: resource naming and `--rm`, run identity
and labels, secrets through `--env NAME`, loopback publishing with an ephemeral
port read back through `docker port`, binding a location the command owns,
cleanup registration with reverse-order teardown and signal handling, the
sweep-and-prove listing, the prune refusal, and reading the daemon with
`docker inspect`.

### Shared rules and their copies

Four rules apply to both CLI packages and are duplicated under reciprocal copy
records rather than linked, because each package must work alone: resource
naming, run identity with label-over-pattern selection, cleanup registered
before creation, and the prune refusal. `docker-cleanup` records the third and
fourth from its own side.

The borrowed-definition rule is the one seam the cut does not separate cleanly.
Its trigger is `docker compose run` against a developer stack, so it is owned by
`docker-compose-cli`; the fix is a `docker run` bind, so the mechanic is also
stated here. Both passages carry the copy record.

### Checks

Repository package validation, the shared-contract comparison and
`git diff --check` passed. The suite runner was not run in this worktree because
`node_modules` is not tracked there and the change adds no helpers.

## Behavioral scenarios

These scenarios define expected behavior for the initial package. Each rule's
original evaluation is recorded under
[containerization](containerization.md#behavioral-scenarios); the status below
describes evidence for this package's own boundary.

| Request and context | Expected outcome | Evaluation status |
| --- | --- | --- |
| A `docker run` is assembled for a one-off task | `--rm`, a named or owned volume, and a tagged image if one is built | Inherited from containerization |
| A password is passed to a container | Through the CLI's environment and `--env NAME`, never `--env NAME=value` | Inherited: author review |
| A host port is needed for a test service | `--publish 127.0.0.1::5432`, read back with `docker port`, checked for loopback | Inherited: reproduced defect and fix in one project |
| A wrapper computes an address instead of reading it back | Flagged: the wrapper and the daemon can disagree unnoticed | Inherited: reproduced defect |
| A command starts from an existing service definition | A throwaway directory is bound over every mount point the command does not own, as a required argument | Inherited from containerization 1.1.0, measured |
| Resources are created before cleanup is registered | Flagged: the gap leaks whatever was created in it | Inherited: author review |
| Teardown is asked to select by name prefix | Rejected: selection is by label; a prefix matches another owner's resources | Inherited: author review |
| One teardown step fails | Later steps still run, failures are collected, the original failure stays the result | Inherited: author review |
| A prune command would be faster than targeted removal | Rejected: it reaches resources this work did not create | Inherited: author review |
| A request concerns several containers started together | Out of scope: `docker-compose-cli` owns project-scoped commands | Author review only |
| A request concerns a host full of unattributed resources | Out of scope: `docker-cleanup` owns host-wide attribution and reclaim | Author review only |
| A request asks which lifecycle a project's containers should declare | Out of scope: an outcome owned by the consuming framework's convention | Author review only |

## Limits

The [routing trial](docker-routing-trial-2026-10-09.md) exercised this package
against its three near-neighbours. Its case 1 reached this package and the
consuming framework's convention together, and declined the compose and cleanup
rows citing this package's own scope statement. No defect in this package's text
was found.

That trial is entrypoint routing, not independent discovery: the agents read
project instructions and a collection entrypoint, not host-supplied skill
metadata. One run demonstrates the route, not its reliability. No case exercised
this package against `docker-compose-cli` in conflict — one container inside an
existing project, where both could reasonably be selected.

## Raised, not repaired

**This package says nothing about implicit pull.** While measuring compose's
build policy for `docker-compose-cli` 0.2.0, the single-command side turned out
to have the same shape with a simpler remedy. `docker run` defaults to
`--pull=missing`, so a missing image is fetched as a side effect of the run;
`docker run --pull=never` refuses it with `No such image`, verified against
Docker 29.4.3. This package's "Pin the image" neighbours in the consuming
framework's convention require that a run never pull implicitly, and this
package supplies no mechanic for that, exactly as `docker-compose-cli` did not
for builds.

The remedy is one flag rather than compose's file restructuring, so the two
sections would not be a package-boundary copy. Recorded here rather than patched
because the compose change was the authorized scope; a revision should state the
`--pull=never` default alongside the existing identity and cleanup rules.
