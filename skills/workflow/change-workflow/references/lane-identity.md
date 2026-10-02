# Lane identity

Read this before the first read taken to guide authoring, again when a lane has
to be named, and when the base checkout is found on the wrong branch.
[`change-workflow`](../SKILL.md) owns the lane the roles below belong to.

## Which lane is this

A session starts where the host put it. That is usually the base checkout on the
default branch, and from the inside it can look like a task lane: an ordinary
path, a clean `git worktree list --porcelain` entry.

| Role | What identifies it | What it permits |
| --- | --- | --- |
| Base checkout | the main working tree, on the default branch | the merge target; lifecycle and service commands run here, nothing is authored here |
| Task lane | a sibling worktree under `.worktrees/`, on its own branch, that this session opened or was directed to resume | authoring |
| Pin | a detached `HEAD` | a comparison basis, not an authoring lane |

**The branch decides, never the path's name.** A directory under `.worktrees/`
proves nothing by itself. The facts, in the order that settles it:

```bash
git rev-parse --show-toplevel                          # this checkout
git rev-parse --path-format=absolute --git-common-dir  # which repository
git worktree list --porcelain                          # branch, registration, detached
```

Where the project provides a command that derives the role, run it before
authoring and use its answer. An unavailable command is unknown role evidence,
never permission to author.

If you find yourself in the base checkout, open a task lane from the default
branch and author only there. A lane this session did not open is an authoring
lane only when the session was directed to resume it, by the user or by the
project's record of the work naming the branch. A matching name or path is not
that direction.

## Naming a lane

The name becomes the directory, the branch, and how every later command, comment
and tracker reservation refers to this line of work, so it is settled once and
reused rather than re-derived. A project with its own convention wins over the
shapes below.

| Shape | When | Example |
| --- | --- | --- |
| `<kind>-<issue>-<topic>` | tracker-anchored work | `fix-535-materials` |
| `<kind>-<topic>` | shaped work without an issue | `spike-seeded-readonly` |
| `<topic>` | ad hoc | `fov-editor` |
| `plan-<n>[-<topic>]` | plan-owned | `plan-610-seeded-lane` |

`kind` is an open vocabulary; `fix`, `docs`, `test`, `tool`, `spike`, `chore` and
`plan` are the common values.

Keep them short and kebab-case. A project may derive other identifiers from the
name — a container, a database, a port label — and long names have overflowed
downstream limits.

A name cannot carry a slash, so a bare number in one is read as the lane's own
repository's tracker. Where the work answers to another repository's tracker,
still keep only the bare number in the name, and write the fully qualified
`<owner>/<repo>#<number>` in the text that cites the work, such as the tracker
reservation or pull request.

**A name grants nothing.** No kind, topic, issue number or project-specific shape
is evidence that a lane is active, important, disposable or safe to remove, and
none of them authorizes retention or deletion. Use the observed ownership,
liveness and containment evidence instead.

## Recovering a base checkout on a feature branch

Switching the base checkout onto a feature branch reintroduces exactly the
intermingling that isolation prevents, and leaves the base useless for verifying
a merged result. This is a repair, not part of the lifecycle. Check for
uncommitted work first, and switch only if the status is empty:

```bash
git -C <base-checkout> status --short
git -C <base-checkout> switch <integration-branch>
git -C <base-checkout> worktree add .worktrees/<name> <branch>
```

The branch's commits are preserved, so this restores rather than loses anything
committed. Uncommitted work is another matter. Git refuses the switch when an
uncommitted file also differs between the two branches, and otherwise carries
every uncommitted change onto the default branch while the lane opens without
it. So if the status check shows anything, do not switch: report the paths and
the branch, and leave where that work belongs to a deliberate decision.
