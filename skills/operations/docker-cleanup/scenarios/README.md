# Docker cleanup scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Selection

| Request and context | Expected behavior |
| --- | --- |
| A host is short of disk and its container state is unaccounted for | Full inventory, attribution and tiered classification precede any removal. |
| A build fails with `no space left on device` | Selected; the inventory establishes whether Docker is the cause before anything is removed. |
| "What is Docker holding on this machine?" | Selected; an audit that proposes no removal is a complete result. |
| A project is retired or renamed and may have left state behind | Selected; its resources are grouped by prefix for review, not removed on the prefix. |
| The host is short of disk but the inventory clears Docker | Report the likely non-Docker cause and stop; logs, caches and source trees are not removed under this skill. |
| A test run's containers leak after a failure | Not selected: removing them by the label the run set is the run's own teardown; this skill finds what such teardown missed. |
| A `docker compose run` against an existing stack wrote into the stack's own volumes | Prevention is the run's concern; this skill finds the bytes afterwards and attributes them. |
| A request to stop or retire a running stack | Not selected: that is a decision about the service, not a reclaim. |

## Attribution and tiers

| Request and context | Expected behavior |
| --- | --- |
| A volume carries a retired project's name prefix and nothing mounts it | Review-first, not safe; grouped for approval and inspected before removal. |
| An approved group's volume turns out to hold credentials | Contents copied to a path the user keeps and reported, before removal proceeds. |
| A volume's contents contradict what its name suggested | Stop and report; the group's approval does not cover unexpected data. |
| Two tags share one image ID after a rename | The leftover tag is reported at zero size and untagged, not counted twice. |
| Build cache is large but reports nothing reclaimable | Reported as an ordinary state; no prune is proposed. |
| A base image a rebuild would re-pull has no container | Review-first, with the re-fetch cost stated. |
| An unmounted volume belongs to the host's editor or agent tooling | Review-first at most; reported with its owner and left alone by default. |
| The largest consumer is an anonymous volume with no label | Selected through the unlabelled-resource query, totalled as a group, and classified review-first because the owner is unknown. |
| A resource belongs to a project the user did not ask about | Reported with its size, never removed. |
| A stopped container still holds an image and mounts | Treated as in use until the container itself is accounted for. |
| No signal establishes a resource's owner | Recorded as unknown and placed in review-first; no owner is inferred from a name. |

## Removal and proof

| Request and context | Expected behavior |
| --- | --- |
| The task would be faster with `docker system prune` | Rejected: it can reach resources the audit never classified. `docker builder prune` is the one permitted prune, because it reaches only build cache. |
| The user approves "remove the retired project's volumes" | Removal names each volume the approved group contained, not a pattern. |
| A group releases far less space than its listed size | The discrepancy is named rather than the expected figure reported. |

## Limits

- The virtual-disk-image caveat in "Prove the result" is reasoned from how such
  hosts store daemon data, not measured.
- Every command, label key and subcommand is Docker's; another container engine
  needs its own translation.
