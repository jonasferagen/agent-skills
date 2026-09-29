---
name: change-workflow
description: "Land a repository change safely: isolate it in a worktree before the first write, keep it current by merge, reconcile and verify the tree that will actually merge, then land it and clean up by containment. Use before the first write bound for the default branch and again at the merge boundary — when a branch has to be brought current, when a rename or deletion needs a stale-reference sweep, when deciding whether verification evidence is still fresh, when a worktree or branch is about to be removed, or when writing the hand-back that reports the result. Reach for it when a change is \"done\" but nothing has said what was verified. Describes a discipline a project opts into; the reading project owns its own landing policy, tracker conventions and authorization."
metadata:
  version: "0.1.0"
---

# Change Workflow

**This describes a discipline a project opts into, not a universal rule.**
Whether changes are authored in isolated worktrees, how one reaches the default
branch, and who may land it are decisions the reading project makes in its own
instructions. Read those first. Where they are silent, this package supplies a
lane that holds; where they disagree with something here, they win — and a
project that authors on branches in one checkout is not doing it wrong.

Once a project has adopted it, the rule is:

**Before the first repository write bound for the default branch, create a
worktree and author there.** Anything Git would track counts, however small or
early: source, docs, configuration, generated files and status records alike.
Ignored dependencies and disposable output do not. Size and file kind change
nothing — a one-line doc fix counts.

The base checkout stays on the default branch as the merge target. That is what
keeps parallel agents and live user edits out of one working tree, and it keeps
the base reliably available for verifying a merged result.

The trigger is the first write rather than the commit, because a pre-commit
reminder cannot catch an untracked file when no commit is attempted, and cannot
catch a read taken from the wrong tree at all.

**Never grant yourself the exception.** Only a direct user instruction in the
moment authorizes authoring in the base checkout, and "it is only a doc change"
is not that instruction — the file-kind excuse is the one that actually gets
taken. A base checkout found sitting on a feature branch is a defect to repair
rather than a lane to use;
[lane-identity.md](references/lane-identity.md#recovering-a-base-checkout-on-a-feature-branch)
is the repair.

## Landing is the default terminal state

Isolation opens the lane; landing closes it. Work bound for the default branch is
not finished when its branch is clean and verified — it is finished when it has
reached the default branch and the lane is either cleaned up or deliberately
retained with its reason reported.

Whether an agent may land without asking is the reading project's policy, and
nothing here grants it. What this package does say is that an undecided branch is
not the cautious outcome it looks like: a green branch handed back with no
decision leaves the lane open, the work unlanded, and the next session guessing.
Follow the project's rule and report the result — do not invent a confirmation
step it does not ask for, and do not skip one it does.

Three conditions stop short of landing:

| Stop condition | Report | Continue when |
| --- | --- | --- |
| A real merge conflict, or dirty paths in the base that overlap the merge | Branch and worktree state, and the blocking paths | The blocker clears |
| The user directed a stop or a branch hand-back | Branch and worktree state, with the hand-back below | The user authorizes landing |
| The project lands through review, or a coordinator owns integration | Publish the branch; return its reference and the verification, leaving the lane intact | The reviewer or coordinator lands it |

Work whose success is visual or manual is not a fourth condition. Hold it only
when you cannot tell whether the rendered or manual outcome is right; not knowing
how to look at the thing is not that uncertainty. Either way the report owes the
surface the judgment is made on — branch and worktree state locate a change, they
do not let anyone review it.
[hand-back.md](references/hand-back.md#handing-back-visual-or-manual-work)
settles which surface applies.

## Workflow

Resolve the remote roles once, from the project's documentation and Git
configuration: `<integration-remote>` carries the `<integration-branch>` this
lane synchronizes with and lands into, and `<publish-remote>` receives the
feature branch. They are often one remote, but neither is reliably named
`origin`. Reuse the resolved identities for the rest of the lane.

### 0. Identify the lane you are in

A session starts where the host put it, usually the base checkout on the default
branch — and from the inside, that can look like a task lane. Settle the role
from the branch and the Git registration, never from the path's name, before the
first read taken to guide authoring.
[lane-identity.md](references/lane-identity.md) holds the roles, the facts that
decide between them, and the repair when the base is on the wrong branch.

### 1. Create

Name the lane once, before any Git state exists: the name becomes the directory,
the branch, and how every later command and comment refers to this line of work.
[lane-identity.md](references/lane-identity.md#naming-a-lane) holds the shapes.

```bash
git fetch <integration-remote>
git worktree add .worktrees/<name> -b <branch> \
  <integration-remote>/<integration-branch>
```

Lanes live at `.worktrees/<name>` inside the base checkout, a project-owned
directory beside the tracked tree. **The ignore entry belongs in the project's
tracked ignore file, not `.git/info/exclude`.** An untracked exclude is local to
one machine and the symptom lands far from the cause: the first worktree makes
the base checkout dirty, and whatever refuses to land on a dirty base then
refuses for no visible reason. Do not put lanes under tool-control directories
such as `.agents/` or `.codex/`, which a host may protect as read-only; where a
convention names a protected path, use `.worktrees/` and fix the convention in
the same authorized change.

Then move into the worktree, **re-read the files there**, and run the project's
documented setup or dependency-install step before running anything else. Every
fresh worktree starts without gitignored dependency state, so setup is owed per
worktree even when the base checkout looks ready. Reads taken in the base may
already be stale, and will diverge further as other work lands.

### 2. Resume, if the line of work already exists

For a paused branch or a stacked phase, **bring it current before adding edits.**
Conflicts are cheapest before new work is layered on them, and a dirty paused
branch can otherwise stay stale indefinitely.

```bash
git -C <worktree> status --short
git -C <worktree> rev-list --left-right --count \
  <integration-remote>/<integration-branch>...HEAD
git -C <worktree> merge <integration-remote>/<integration-branch>
```

Commit or stash first. Do not sweep uncommitted work into a merge nobody asked
for.

### 3. Keep current by merge, never rebase

```bash
git merge <integration-remote>/<integration-branch>
```

**Rewriting history to integrate is never the lane**, and that holds even for a
local unpushed branch, where rebasing looks free. It is not: a rebased tree is no
better verified than a merged one, while the rewrite orphans the commit
identifiers that plans, tracker threads, hand-backs and change records cite.

A published branch must never be rebased at all — others may already have it.
Publishing is worth doing early as cheap insurance: once the branch is on the
remote, the work survives whatever happens locally.

```bash
git push -u <publish-remote> <branch>
```

Tidying an unpublished branch's own commits before it lands is a different
operation, and the reason above does not reach it — nothing cites a commit nobody
has seen. It is still history rewriting, so **the reading project's policy
decides whether it is allowed**, and a project that says never rebase, flatly,
has settled it. Establishing "unpublished" and "its own commits only" is part of
the operation, not an assumption to make about it.

### 4. Reconcile and verify the tree that will merge

**Correctness is owed at the merge boundary.** In-branch a lane may be red, built
out of order and full of spikes; what merges is green, with its docs synchronized
and its history readable. What that latitude costs is a real finishing pass
before the merge rather than an improvised checklist —
[finishing-pass.md](references/finishing-pass.md) owns it, and it is owed for
**every tracked-path rename or deletion** even when the change is otherwise
trivial.

Synchronize before the final verification, and run the checks the change calls
for on the resulting tree. [verification.md](references/verification.md) holds
what counts as merge evidence, what only looks like it, and how freshness is
established when time passes between the checks and the merge.

### 5. Land

Use the project's documented landing command, or its established pull-request or
direct-merge convention. For a direct land, synchronize, run the project's checks
on the resulting tree, confirm that neither the candidate nor the integration
branch moved since, then:

```bash
git -C <base-checkout> merge --no-ff <branch>
git -C <base-checkout> push <integration-remote> <integration-branch>
```

`--no-ff` regardless of size, so the branch stays legible in history. **Merge and
push are one operation, not two decisions** — a completed landing is not left
sitting local. Unrelated dirty edits in the base do not by themselves block the
merge: Git refuses if local edits would be overwritten, so attempt it when the
touched paths do not overlap, and report the blocking paths rather than reading
any dirty status as a stop sign.

**Check the landing range's commit messages, not only its diff.** On hosts that
act on closing keywords, such a keyword on any commit reaching the default branch
closes the item it references at merge — and a commit message is not part of a
diff, so review never sees one.

```bash
# nine keyword inflections, anywhere in the message, only when a reference
# follows; do not simplify it
git log <integration-branch>..<branch> --format='%B' \
  | grep -inE '\b(close[sd]?|fix(es|ed)?|resolve[sd]?)[[:space:]]+(([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)?#[0-9]+|https://github\.com/[^ ]+/issues/[0-9]+)'
```

No match exits non-zero, so guard the status where this runs inside a failing-fast
script. A hit is not automatically wrong; it is a closeout nobody reviewed.
Whether the message gets amended or the close is intended is the project's
tracker convention to settle, and closing an item stays a deliberate, verified
act either way.

Where the project's commits carry trailers, ask Git for them rather than
reimplementing paragraph parsing: Git reads only the last paragraph, so a trailer
separated from that block by a blank line still renders on the host and is
invisible to `git interpret-trailers --parse`. Report the denominator — how many
commits carried one at all — so a range that measured nothing says so instead of
passing.

### 6. Clean up the landed lane

Successful landing ends authoring in the lane; further changes start in a new
lane from the current integration branch. After observing the remote integration
branch containing the landed commit, remove **only this session's** worktree and
branch, and only against a containment count:

```bash
git rev-list --count <integration-branch>..<branch>   # 0 => fully contained
```

Never substitute a name, an issue state, an age or `git branch -d`'s refusal for
that count. [cleanup.md](references/cleanup.md) holds why the refusal proves
nothing, the order the removals go in, this lane's published branch, and the
conditions that retain a lane instead.

## Hand back

Report, in this order: the changed surfaces; the verification performed, with the
commands, their status and anything skipped together with the risk it leaves; the
commit identifiers; the stale terms searched; the remaining risk and surfaced
follow-ups; and any tooling or structural friction met along the way, where
`friction: none` is a complete answer.

**A field that is empty by construction is omitted; a field that could have
carried content and did not is reported as `none`.** An omitted field says the
question never arose; a `none` says it arose and the answer was nothing. A change
that renames nothing and answers to no plan reports neither, because "stale
terms: none, plan: none" is the absence of two questions rather than evidence
about the change.

**A verification report names what it measured.** A run that covered a subset
says which subset, and a check that could not run at all is a refusal rather than
a silent pass.

[hand-back.md](references/hand-back.md) holds the field-by-field conditions,
including the diff that makes the stale-terms field owed, and the review surface
a visual or manual result has to carry.

## What this package is not

There is no control plane here, and building one — gate tiers, merge trains, lane
sidecars, per-lane databases, fleet boards, port allocation — is not the
follow-up. What this holds is judgment: work in isolation, integrate by merge,
verify the tree that will actually merge, fail closed on anything that discards
work. A project that wants automation on top owns it.

Three neighbouring subjects belong elsewhere:

- **Tracker conventions.** How an item is claimed, commented on and closed is the
  project's; this package only refuses to close one by accident and reconciles
  what a session left behind.
- **A pickup note for deferred work** is the opposite of a hand-back: it orients a
  session that has not started, where a hand-back reports one that finished. It
  lives wherever the project keeps work state.
- **Authorization.** Which operations an agent may perform without asking, and
  what recovery evidence a destructive one owes, are the project's calls. Nothing
  here is a licence, and assume nothing is disposable unless the project has said
  so.
