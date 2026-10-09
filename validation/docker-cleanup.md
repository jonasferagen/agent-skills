# Validation — Docker cleanup

## Initial package — 9 October 2026

Version 0.1.0 draws its method from an actual cleanup on the author's
development host, performed by hand before the package existed. That host had
run a retired project (Forge) and two unrelated ones, and held 40 images,
34 volumes, 29 networks and 428 build-cache entries across about 110 GB.

The rules below were derived from what that pass got right and from the two
places it nearly went wrong. No generated housekeeping run has been evaluated
against the written instructions yet.

### What the originating pass established

- Attribution, not age, decided every removal. The host's retired-project
  resources were grouped by name prefix for review and then removed by explicit
  name, one group at a time, after the owner approved each group.
- Two image tags shared one ID after a project rename. Counting the leftover
  tag's reported size would have overstated the reclaim by 3.61 GB; the
  inventory recorded it as zero and proposed untagging.
- Build cache fell from 428 entries and 24.8 GB to 87 entries and 10.46 GB as a
  side effect of removing images, and its reclaimable figure then read 0 B. The
  total alone would have suggested a prune worth 10 GB.
- Three of 22 volumes in an approved group held material the group was not
  understood to hold: a credential directory, a 798 MB release tree with a
  `desired.json`, and a 259 MB tree that proved to be a PostgreSQL 18 data
  directory rather than the expected catalog dump. Inspecting each before
  removal produced two small rescued copies at a path the owner keeps.
- The volume measured at 31.67 GB, the largest single item, belonged to the
  host's editor rather than to any project. It was reported and left alone.

### Rules that follow from it

The safe tier is limited to resources whose removal loses no data: untagged
images with no container, a tag sharing an ID with a tag in use, build cache,
and an unattached network of a retired project. Everything holding data —
every named volume, every image a rebuild would re-fetch, and every resource of
unknown ownership — is review-first.

Blanket prune commands are refused, with `docker builder prune` the single
exception, because it reaches only build cache. This matches the rule
`containerization` states for a test run's own resources, reached from the
opposite direction: that package forbids prune because it can reach resources
the run did not create, and this one because it can reach resources the audit
never classified.

### Checks

Repository package validation and `git diff --check` passed. No automatic
discovery trial has been run for the new trigger; the routing acceptance
requirement applies before a release tag.

## Behavioral scenarios

These scenarios define expected behavior for the initial package. The author
reviewed the instructions against them.

| Request and context | Expected outcome | Evaluation status |
| --- | --- | --- |
| A host is short of disk and its container state is unaccounted for | Full inventory, attribution and tiered classification precede any removal | Performed by hand before the package |
| A build fails with `no space left on device` | Selected; the inventory establishes whether Docker is the cause before anything is removed | Author review only |
| "What is Docker holding on this machine?" | Selected; an audit that proposes no removal is a complete result | Performed by hand before the package |
| A project is retired or renamed and may have left state behind | Selected; its resources are grouped by prefix for review, not removed on the prefix | Performed by hand before the package |
| The host is short of disk but the inventory clears Docker | Report the likely non-Docker cause and stop; logs, caches and source trees are not removed under this skill | Author review only |
| A test run's containers leak after a failure | Not selected: the run's own label-based teardown belongs to containerization | Author review only |
| State a borrowed service definition wrote into a service-owned location | Prevention belongs to containerization; this skill finds the bytes afterwards and attributes them | Author review only |
| A request to stop or retire a running stack | Not selected: that is a decision about the service, not a reclaim | Author review only |
| A volume carries a retired project's name prefix and nothing mounts it | Review-first, not safe; grouped for approval and inspected before removal | Performed by hand before the package |
| An approved group's volume turns out to hold credentials | Contents copied to a path the owner keeps and reported, before removal proceeds | Performed by hand before the package |
| A volume's contents contradict what its name suggested | Stop and report; the group's approval does not cover unexpected data | Reproduced: a catalog-named volume held a database data directory |
| Two tags share one image ID after a rename | The leftover tag is reported at zero size and untagged, not counted twice | Performed by hand before the package |
| Build cache is large but reports nothing reclaimable | Reported as an ordinary state; no prune is proposed | Performed by hand before the package |
| A base image a rebuild would re-pull has no container | Review-first, with the re-fetch cost stated | Author review only |
| An unmounted volume belongs to the host's editor or agent tooling | Review-first at most; reported with its owner and left alone by default | Performed by hand before the package |
| A resource belongs to a project outside the task's scope | Reported with its size, never removed | Performed by hand before the package |
| The task would be faster with `docker system prune` | Rejected: it can reach resources the audit never classified | Author review only |
| An owner approves "remove the retired project's volumes" | Removal names each volume the approved group contained, not a pattern | Performed by hand before the package |
| A group releases far less space than its listed size | The discrepancy is named rather than the expected figure reported | Author review only |
| A stopped container still holds an image and mounts | Treated as in use until the container itself is accounted for | Author review only |
| No signal establishes a resource's owner | Recorded as unknown and placed in review-first; no owner is inferred from a name | Author review only |

## Trigger conditions — 9 October 2026

Version 0.1.0 names the selecting symptoms in the description and in the
entrypoint's own section, after the first draft carried only the task
("audit and reclaim") and a scope note. The symptoms were chosen because each
one was a plausible way the originating cleanup could have started: a failed
build, an unexplained usage total, a direct question about what Docker holds,
or a project's retirement.

Two trigger decisions are worth recording:

- A question expecting the answer "nothing is reclaimable" selects the skill.
  The originating pass found a 10.46 GB build cache with 0 B reclaimable and a
  31.67 GB volume belonging to the editor. Both were correct results, and a
  trigger that fired only on an intent to delete would have missed them.
- Host disk pressure that is not Docker's is an explicit non-trigger. Naming it
  prevents the skill from being selected for log, cache or source-tree cleanup
  it has no rules for, while still asking for the observation to be reported
  when the inventory clears Docker.

The near-neighbour that most needs separating is `containerization`: a leaked
test resource and an unattributed host resource look alike once the run is
over. The boundary is stated from both sides — that package prevents the leak
and owns the run's teardown, this one finds what already escaped. No automatic
discovery trial has distinguished them yet.

The name changed from `container-housekeeping` to `docker-cleanup` before any
release, because every command, label key and subcommand in the package is
Docker's and the engine-neutral name claimed a portability the package had not
earned. The engine-neutral claim was removed with it; the entrypoint now says
the method would translate and that no other engine has been tried.

## Limits

The package has been exercised once, by its author, on one Linux host with one
Docker daemon. No scenario above has been evaluated against an independent
agent following the written instructions, and no trial has tested whether a
realistic request selects this package rather than `containerization`.

The virtual-disk-image caveat in "Prove the result" is reasoned from how such
hosts store daemon data, not measured: the originating host writes to the host
filesystem directly, so no compaction step was needed or observed.
