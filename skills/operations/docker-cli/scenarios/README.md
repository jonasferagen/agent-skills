# Docker CLI scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A `docker run` is assembled for a one-off task | `--rm`, a named or owned volume, and a tagged image if one is built. |
| A password is passed to a container | Through the CLI's environment and `--env NAME`, never `--env NAME=value`. |
| A host port is needed for a test service | `--publish 127.0.0.1::5432`, read back with `docker port`, checked for loopback. |
| A wrapper computes an address instead of reading it back | Flagged: the wrapper and the daemon can disagree unnoticed. |
| A command starts from an existing service definition | A throwaway directory is bound over every mount point the command does not own, as a required argument. |
| Resources are created before cleanup is registered | Flagged: the gap leaks whatever was created in it. |
| Teardown is asked to select by name prefix | Rejected: selection is by label; a prefix matches another owner's resources. |
| One teardown step fails | Later steps still run, failures are collected, the original failure stays the result. |
| A prune command would be faster than targeted removal | Rejected: it reaches resources this work did not create. |
| A request concerns several containers started together | Out of scope: docker-compose-cli owns project-scoped commands. |
| A request concerns a host full of unattributed resources | Out of scope: docker-cleanup owns host-wide attribution and reclaim. |
| A request asks which lifecycle a project's containers should declare | Out of scope: an outcome owned by the consuming project's convention. |

## Open

- The skill says nothing about implicit pull. `docker run` defaults to
  `--pull=missing`, so a missing image is fetched as a side effect of the run;
  `docker run --pull=never` refuses it with `No such image` (observed on Docker
  29.4.3). A project convention that forbids implicit pulls has no mechanic here
  yet; a revision should state the `--pull=never` default beside the identity
  and cleanup rules.

## Limits

- The port-selection and borrowed-definition rules come from reproduced defects
  and measured fixes in one project; the rest are author-reviewed.
- One routing trial reached this package and declined the compose and cleanup
  rows from its scope statement. No case has exercised this package against
  docker-compose-cli in conflict: one container inside an existing project.
