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
| A command reuses the mounts of a developer's long-lived container setup | A throwaway directory is bound over every mount point the command does not own, as a required argument. |
| Resources are created before cleanup is registered | Flagged: the gap leaks whatever was created in it. |
| Teardown is asked to select by name prefix | Rejected: selection is by label; a prefix matches another owner's resources. |
| One teardown step fails | Later steps still run, failures are collected, the original failure stays the result. |
| A prune command would be faster than targeted removal | Rejected: it reaches resources this work did not create. |
| An image an earlier step built is expected to be present | `--pull=never`, so a missing image fails as `No such image` rather than being fetched silently. |
| A request concerns several containers started together | Out of scope: a project of several containers is driven through `docker compose`. |
| A request concerns a host full of unattributed resources | Out of scope: host-wide attribution and reclaim is a separate audit task. |
