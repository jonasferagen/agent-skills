---
name: docker-cleanup
description: "Audit and reclaim a Docker host's accumulated images, volumes, networks and build cache, including state left by retired, renamed or unrelated projects. Use when a build, pull or container fails for disk space, when the daemon's usage is unexplained, or after retiring a project; removing what one command or project created belongs to docker-cli and docker-compose-cli."
metadata:
  version: "0.1.1"
---

# Docker cleanup

A development host accumulates Docker state from every project that has run on
it. Reclaiming that space is an attribution problem before it is a deletion
problem: establish who owns each resource and whether its contents can be
reproduced, then remove only what that answer covers.

This package is Docker-specific. Its method — attribute, tier, inspect, prove —
would carry to another container engine, but every command, label key and
subcommand named here is Docker's, and nothing in it has been tried elsewhere.
For another engine, treat this as a model to translate rather than guidance to
follow.

## Select this skill when

Any one of these conditions is enough:

- A build, pull, container start or database write fails for space, or reports
  `no space left on device`.
- The host's free space is falling and the Docker daemon is a plausible cause,
  or `docker system df` reports a total nobody can account for.
- The owner asks what Docker is holding, which resources are unused, or what
  could be reclaimed — including when the answer is expected to be "nothing".
- A project was retired, renamed, moved between hosts or had its prefix changed,
  and its images, volumes or networks may remain.
- A host needs room before a new stack, a large image or a long build.
- A shared, long-lived host is due a periodic audit.

The trigger is the symptom, not a decision to delete. An audit that ends in
"everything here is in use or belongs to another project" is a complete result.

## Do not select this skill for

- **Resources one command or project created.** Work that creates containers,
  networks, volumes and images owns them for its length and removes them by its
  own label. That lifecycle belongs to `docker-cli`, and its project-scoped form,
  including the mounts a borrowed service definition hands a run, to
  `docker-compose-cli`. This skill is what finds such bytes once they have
  already escaped and their owner is no longer obvious.
- **Host disk pressure that is not Docker's.** Logs, package caches, build
  outputs, source trees and editor state outside the daemon are out of scope.
  Report them as a likely cause when the inventory clears Docker; do not remove
  them under this skill.
- **Removing a running stack.** Stopping or retiring a service that is in use is
  the owner's decision about that service, not a reclaim.

## Work in five steps

Keep the order. Each step depends on the previous one being complete.

| Step | Produces |
| --- | --- |
| Inventory | Every image, volume, network, container and cache entry, with sizes |
| Attribute | An owner for each resource, or an explicit unknown |
| Classify | Each resource in the safe, review-first or not-ours tier |
| Act | The removals that tier permits, selected by name or ID |
| Prove | Measured reclaim, and what remains with the reason |

[Inventory and attribution](references/inventory.md) holds the commands, the
attribution signals and the reporting shape.

## Attribute before classifying

Account for running containers first. List them with the images they run and the
volumes they mount, and treat every resource they use as in use, whatever its
name suggests.

Attribute each remaining resource from the strongest signal available: a Compose
project label, a run or project label, an image reference held by a stopped
container, then a name prefix. A name prefix is the weakest signal. Use it to
group resources for review, never as the sole basis for removal.

Record an owner that cannot be established as unknown rather than guessing. An
unknown owner is review-first, never safe.

<!-- Package-boundary copy: docker-cli/SKILL.md (Give the work one identity) and docker-compose-cli/SKILL.md (Give the work one identity) state the label-over-pattern rule for resources their own work created. Keep all three aligned. -->


Neither age nor a project's retirement establishes that a resource is
disposable. A retired project's volume can hold the only copy of a credential,
an export or a build output. Establish that the contents are reproducible, or
that losing them is authorized.

## Classify into three tiers

**Safe** resources hold no data that removal would lose. Remove this tier
without asking:

- An image with no container and no tag, or a tag that shares its image ID with
  a tag still in use. Removing the second tag removes a name, not bytes.
- Build cache, through `docker builder prune`. Cache entries hold intermediate
  layers only. When a cached build downloads a large dependency, report the cost
  of recreating it before pruning rather than after.
- A network with no attached container, belonging to a retired project.

**Review-first** resources need the owner's explicit approval, one group at a
time:

- Every named volume. A volume's name does not state its contents.
- A named image that a rebuild could not reproduce without a network fetch, and
  any base image that other work on the host would re-pull.
- Any resource whose owner is unknown, or whose owner is the host's editor or
  agent tooling rather than a project.

**Not-ours** resources are reported and never touched: anything attributed to a
project outside the task's scope, and anything a running container uses. Report
their size so the whole picture is visible, and state plainly that they were
left alone.

## Select resources explicitly

Remove by the exact name or ID the inventory recorded. Do not run
`docker system prune`, `docker volume prune`, `docker image prune -a`, or any
other command that selects across the daemon by age or dangling status. Such a
command can reach a resource the audit never classified, including one created
between the inventory and the removal. `docker builder prune` is permitted
because it reaches only build cache.

A pattern may select a group for the inventory and for the approval request. The
removal still names what the approved group contained.

<!-- Package-boundary copy: docker-cli/SKILL.md (Remove what the command created, and prove it) and docker-compose-cli/references/project-isolation.md (Remove, sweep and prove) state the prune refusal for their own scopes. Keep all three aligned. -->


## Inspect a volume before removing it

Read a volume's contents before removal, including a volume in an approved
group: mount it read-only in a throwaway container and list it. Report what is
there, and copy out anything that is not reproducible before the volume goes. A
credential directory, an export, a dump or a release tree deserves a copy to a
path the owner keeps, and that location belongs in the result.

Stop and ask when a volume's contents contradict its expected owner, or when
they look like the only copy of something. Approval to remove a group is not
approval to destroy data the group was not understood to hold.

## Prove the result

Re-measure usage after acting, and report the reclaim achieved by group against
what each group was expected to release. A group that released far less than its
listed size means the inventory misread something: name the discrepancy rather
than reporting the expected figure.

Reported size is not reclaimable size. Images and build cache share layers, so a
total can be large while little is reclaimable on its own. Read the reclaimable
figure `docker system df` gives and report that, not the total.

Where the daemon stores its data in a virtual disk image rather than on the host
filesystem, as on macOS and Windows, the host's free space does not grow when
the daemon's usage falls. Report the daemon-side reclaim as what it is, and name
the host's own compaction step as a remaining action rather than claiming space
the host has not got back.

Close by listing what remains and why: in use, not ours, or awaiting a decision.
