## Workflow

Resolve the remote roles once, from the project's documentation and Git
configuration: `<integration-remote>` carries the `<integration-branch>` this
lane synchronizes with and lands into, and `<publish-remote>` receives the
feature branch. They are often one remote, but neither is reliably named
`origin`. Reuse the resolved identities for the rest of the lane.

### 0. Identify the lane you are in

A session starts where the host put it, usually the base checkout on the default
branch — and from the inside, that can look like a task lane. Before the first
read taken to guide authoring, settle the role from the branch and the Git
registration, never from the path's name.
[lane-identity.md](lane-identity.md) holds the roles, the facts that
decide between them, and the repair when the base is on the wrong branch.

### 1. Create

Name the lane once, before any Git state exists: the name becomes the directory,
the branch, and how every later command and comment refers to this line of work.
[lane-identity.md](lane-identity.md#naming-a-lane) holds the shapes.

```bash
git fetch <integration-remote>
git worktree add .worktrees/<name> -b <branch> \
  <integration-remote>/<integration-branch>
```

Lanes live at `.worktrees/<name>` inside the base checkout, a project-owned
directory beside the tracked tree. **The ignore entry belongs in the project's
tracked ignore file, not `.git/info/exclude`.** An untracked exclude is local to
one machine, and the failure shows up far from its cause: without the entry, the
first worktree makes the base checkout dirty, and whatever refuses to land on a
dirty base then refuses for no visible reason. Do not put lanes under
tool-control directories such as `.agents/` or `.codex/`, which a host may
protect as read-only; where a convention names a protected path, use
`.worktrees/` and fix the convention in the same authorized change.

Then move into the worktree, **re-read the files there**, and run the project's
documented setup or dependency-install step before running anything else. Every
fresh worktree starts without gitignored dependency state, so setup is owed per
worktree even when the base checkout looks ready. Reads taken in the base may
already be stale, and will diverge further as other work lands.

### 2. Resume, if the line of work already exists

Resume a lane this session did not open only when the user or the project's
record of the work directs it; a matching name is not that direction. For a
paused branch or a stacked phase, **bring it current before adding edits.**
Conflicts are cheapest before new work is layered on them, and a dirty paused
branch can otherwise stay stale indefinitely.

```bash
git -C <worktree> status --short
git -C <worktree> rev-list --left-right --count \
  <integration-remote>/<integration-branch>...HEAD
git -C <worktree> merge <integration-remote>/<integration-branch>
```

Commit or stash uncommitted work before the merge. Do not sweep it into a merge
nobody asked for.

### 3. Keep current by merge, never rebase

```bash
git merge <integration-remote>/<integration-branch>
```

**Never rewrite history to integrate**, not even on a local unpushed branch,
where rebasing looks free. It is not: a rebased tree is no better verified than
a merged one, while the rewrite orphans the commit identifiers that plans,
tracker threads, hand-backs and change records cite.

A published branch must never be rebased at all — others may already have it.
Publishing early is cheap and worth doing: once the branch is on the remote, the
work survives whatever happens locally.

```bash
git push -u <publish-remote> <branch>
```

Tidying an unpublished branch's own commits before it lands is a different
operation, and the reason above does not apply to it, because nothing cites a
commit nobody has seen. It is still history rewriting, so **the reading
project's policy decides whether it is allowed**; a project with a flat "never
rebase" rule has already ruled it out. The operation includes establishing that
the branch is unpublished and that only its own commits are rewritten; do not
assume either.

### 4. Reconcile and verify the tree that will merge

**Correctness is owed at the merge boundary.** In-branch a lane may be red, built
out of order and full of spikes; what merges is green, with its docs synchronized
and its history readable. In exchange for that latitude, non-trivial work runs
a real finishing pass before the merge rather than an improvised checklist.
[finishing-pass.md](finishing-pass.md) owns that pass. It is also
owed for **every tracked-path rename or deletion** even when the change is
otherwise trivial, and its staging and base-checkout steps apply to every change
that lands from a lane.

Synchronize before the final verification, and run the checks the change calls
for on the resulting tree. [verification.md](verification.md) holds
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

Use `--no-ff` regardless of size, so the branch stays legible in history.
**Merge and push are one operation, not two decisions**: do not leave a
completed merge only in the local checkout. Unrelated dirty edits in the base
do not by themselves block the merge. Git refuses if local edits would be
overwritten, so attempt the merge when the touched paths do not overlap. If Git
refuses, report the blocking paths; do not treat a dirty status by itself as a
reason to stop.

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

When nothing matches, grep exits non-zero, so guard its status where this runs
inside a failing-fast script. A hit is not automatically wrong; it is a closeout
nobody reviewed. Whether the message gets amended or the close is intended is
the project's tracker convention to settle, and closing an item stays a
deliberate, verified act either way.

Where the project's commits carry trailers, ask Git for them rather than
reimplementing paragraph parsing. Git reads trailers only from the last
paragraph, so a trailer separated from that block by a blank line still renders
on the host but is invisible to `git interpret-trailers --parse`. Report how
many commits carried a trailer at all, so a range that measured nothing says so
instead of passing.

### 6. Clean up the landed lane

Successful landing ends authoring in the lane; further changes start in a new
lane from the current integration branch. After observing the remote integration
branch containing the landed commit, remove **only this session's** worktree and
branch, and only against a containment count:

```bash
git rev-list --count <integration-branch>..<branch>   # 0 => fully contained
```

Never substitute a name, an issue state, an age or `git branch -d`'s refusal for
that count. [cleanup.md](cleanup.md) holds why the refusal proves
nothing, the order the removals go in, this lane's published branch, and the
conditions that retain a lane instead.

