# Inventory and attribution

Use this reference while taking the inventory, attributing resources and
reporting the result. Each command below assumes a Docker daemon the caller can
reach; check that first, because every listing is empty when it is unavailable
and an empty inventory reads as a clean host.

## Take the inventory in one pass

Collect the whole state before classifying anything. A partial inventory invites
a removal that a later listing would have blocked.

```sh
docker system df                     # totals, and the reclaimable figure per type
docker system df -v                  # per-resource sizes, including each volume
docker ps -a --format '{{.Names}}\t{{.Image}}\t{{.State}}\t{{.Status}}'
docker images --format '{{.Repository}}:{{.Tag}}\t{{.ID}}\t{{.Size}}'
docker volume ls --format '{{.Name}}'
docker network ls --format '{{.Name}}'
```

Read `docker system df` first and keep its reclaimable column beside the totals.
The size of a type and the part of it that removal would free are different
numbers, and only the second one answers the question being asked.

A build cache of tens of gigabytes with nothing reclaimable is an ordinary
state, not an error: every entry backs an image that still exists. Report it
that way instead of proposing a prune that would free nothing.

## Establish what is in use

Containers hold the only authoritative statement of use. Derive it from them
rather than from the `TOTAL`/`ACTIVE` counts.

```sh
docker ps -a --format '{{.Image}}' | sort -u                # images in use
docker ps -aq | xargs -r docker inspect \
  --format '{{range .Mounts}}{{.Name}} {{end}}' | tr ' ' '\n' | sort -u
```

Compare each list against the inventory. An image or volume absent from these
lists has no container; that makes it a candidate for a tier, not a candidate
for removal.

A stopped container still holds its image and mounts. Treat its resources as in
use until the container itself is accounted for.

## Attribute each resource

Prefer the strongest signal that applies:

| Signal | Read it with | Strength |
| --- | --- | --- |
| Compose project label | `docker inspect`, `com.docker.compose.project` | Authoritative |
| Run or project label | `docker volume ls --filter label=<key>` | Authoritative |
| Held by a container | the container's image and mount lists | Authoritative |
| Name prefix | the inventory listing | Grouping only |

Two tags sharing one image ID are one image under two names. Compare IDs across
the image listing: a leftover name from a rename occupies no additional space,
and the inventory should say so rather than counting its size twice.

Record an owner that no signal establishes as unknown. Do not infer an owner
from a name that merely resembles another resource's.

## Find what carries no label at all

The resources hardest to attribute are the ones with no label, and they are
often the bulk of the reclaim: an anonymous volume gets a hash for a name, so
nothing about it says which command created it or when.

There is no filter for the absence of a label, so subtract instead. List every
volume, list the ones each known owner claims, and treat the remainder as
unlabelled:

```sh
docker volume ls --quiet | sort > /tmp/all
docker volume ls --quiet --filter label=com.docker.compose.project | sort > /tmp/claimed
comm -23 /tmp/all /tmp/claimed          # repeat --filter per owning label in use
```

Repeat the claimed listing for every label key the host's projects use, so the
remainder shrinks to what genuinely carries none. A 64-character hex name is a
strong hint that Docker generated it, but confirm with
`docker volume inspect` rather than by the shape of the name.

To total a group, read the per-volume sizes from `docker system df -v` and sum
the group's rows; the summary line gives no per-group figure. Report the total
and the count together, because one 5 GB volume and five hundred 10 MB volumes
need different decisions.

Unlabelled does not mean unowned. A running container can mount an anonymous
volume, which makes it in use whatever its name looks like, so the in-use
listing above still comes first.

## Read a volume before removing it

Mount the volume read-only into a throwaway container and list it. The container
must carry no mount that could be written to by mistake other than the
destination for a copy.

```sh
docker run --rm -v <volume>:/src:ro <small image> find /src -maxdepth 2
```

Copy out what is not reproducible before the volume goes:

```sh
docker run --rm -v <volume>:/src:ro -v <destination>:/out <small image> \
  tar czf /out/<volume>.tar.gz -C /src .
```

Choose a destination the owner keeps and names in the result. A session's
temporary directory is not such a place.

What the listing shows decides the next step, not what the name suggested. A
volume named for a catalog can hold a database's data directory; a volume named
for a cache can hold the only copy of a token.

## Report in groups

Present findings as one table, grouped by owner and tier, so an approval can
name a group rather than a resource:

| Column | Holds |
| --- | --- |
| Group | The owner and tier, such as "retired `<project>` volumes" |
| Items | The count, and the names when few enough to read |
| Size | The group's reclaimable size, zero where removal frees nothing |
| Note | The action proposed, or the reason the group is untouched |

Name the resources that need a decision of their own outside the table, with
what the inspection found in each. A group's size tells the owner what is at
stake; the individual note tells them what they would lose.

After acting, report the measured reclaim per group and the state that remains.
