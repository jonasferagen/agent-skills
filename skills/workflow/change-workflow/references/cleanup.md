# Cleaning up a landed lane

Cleanup follows landing as a separate operation, and covers **only the lane this
session opened or resumed, and landed.** Other lanes, mismatches between Git
registrations and on-disk directories, orphaned directories, stale registrations
and unrelated local or remote refs are a population sweep: a different job, with
different evidence.
Do not widen this cleanup into one. [`change-workflow`](../SKILL.md) owns the
landing this cleanup follows.

**A discarding operation names its target from an observed location, never an
assumed one.** Before any `git checkout --`, `reset --hard`, worktree removal or
branch delete, establish the location: read it with `pwd`, or name it explicitly
with `git -C <path>`. A shell session's working directory can drift between
calls while file tools stay on absolute paths, so the two disagree silently and
every file you inspect still looks right. Status output matched against a
believed location is not evidence of which tree produced it.

## Containment is the only safety boundary

```bash
git rev-list --count <integration-branch>..<branch>   # 0 => fully contained
```

A `0` means every commit on the branch stays reachable from the integration
branch, so deleting the ref removes a name and no object. A count above `0` means
unique commits: retain the branch and report them, because discarding them is the
user's decision, not this pass's.

`git branch -vv` compares against an upstream tracking ref, which may be stale, and
`git branch -d` can therefore refuse a branch that is fully contained. **Neither an
upstream "ahead" count nor that refusal proves work is unmerged.** Names, issue
state and age prove nothing either. Try the normal removal first, then repeat the
containment test if it refuses:

```bash
git worktree remove <worktree>
git branch -d <branch>
```

`git branch -D <branch>` is for the contained case only, after a `0` has actually
been recorded against the integration branch.

## Order and rechecks

Clean up after landing, in this order:

1. Observe the remote integration branch containing the landed commit. If
   additional commits or uncommitted changes appeared during the landing,
   preserve that work before going on.
2. Inspect this worktree for uncommitted changes and its branch for commits not
   in the integration branch, and report either rather than discarding it.
   Decide whether the lane is retained, under the conditions below. A retained
   lane stops here: its processes keep running and nothing is removed.
3. Stop any process still rooted inside the worktree, deliberately.
4. Remove the worktree, then the branch. Git refuses to delete a branch that a
   worktree still has checked out, even with `-D`.
5. Recheck this lane's registration, directory and ref. The removals are
   separate operations that can fail or race independently, so one succeeding
   says nothing about the others.

This lane's published branch, below, depends only on step 1, not on the local
removals. The integration branch and its checkout are landing surfaces, never
cleanup candidates.

A process still rooted inside the worktree — a dev server, a watcher — is not
something Git checks for. `git worktree remove` checks the worktree's files and
lock, never its processes, so on Linux it deletes the directory while the
process runs. That is why step 3 stops it first.

Where a removal refuses for a reason you have not established, find out why
instead of forcing it: the force flags discard another lane's live work exactly
as easily as your own spent lane, which is why a project may keep some lanes
marked to be left alone.

**Retain and report the lane** when it is dirty, has unmerged commits, is still
needed for named follow-up or debugging, is held for visual or manual judgment, or
lacks containment evidence. A lane retained with its reason reported is a complete
terminal state; a lane retained silently is not.

## This lane's published branch

A direct landing can leave this lane's published branch on the remote; a
pull-request host may already have removed it. Inspect **only this lane's own
branch**, after observing the integration branch containing the landed commit.

Run it as one fail-closed block. It observes exact object IDs without relying on a
remote-tracking ref, accepts a later integration tip only when that tip contains
the landed commit, and treats an empty successful observation as already clean. A
failed remote read is unavailable evidence, never a missing head.

```bash
(
  set -euo pipefail

  landed_commit=$(git rev-parse <landed-commit>)
  integration_head=$(git ls-remote --heads \
    <integration-remote> refs/heads/<integration-branch>) || {
      echo "integration observation unavailable" >&2
      exit 1
    }
  test -n "$integration_head"
  observed_integration_tip=${integration_head%%[[:space:]]*}

  if ! git cat-file -e "$observed_integration_tip^{commit}" 2>/dev/null; then
    git fetch <integration-remote> refs/heads/<integration-branch>
    test "$(git rev-parse FETCH_HEAD)" = "$observed_integration_tip"
  fi
  git merge-base --is-ancestor "$landed_commit" "$observed_integration_tip"

  feature_head=$(git ls-remote --heads \
    <publish-remote> refs/heads/<branch>) || {
      echo "feature observation unavailable" >&2
      exit 1
    }
  if test -z "$feature_head"; then
    echo "remote feature branch already absent"
    exit 0
  fi
  observed_feature_tip=${feature_head%%[[:space:]]*}

  git fetch <publish-remote> refs/heads/<branch>
  test "$(git rev-parse FETCH_HEAD)" = "$observed_feature_tip"
  test "$(git rev-list --count \
    "$observed_integration_tip..$observed_feature_tip")" = 0

  git push \
    --force-with-lease="refs/heads/<branch>:$observed_feature_tip" \
    <publish-remote> :refs/heads/<branch>

  remaining_feature_head=$(git ls-remote --heads \
    <publish-remote> refs/heads/<branch>) || {
      echo "feature recheck unavailable" >&2
      exit 1
    }
  test -z "$remaining_feature_head"
)
```

`--force-with-lease` is what makes a concurrent advance of the feature branch fail
instead of deleting work the containment check never saw. There is no unguarded API
fallback: an API deletion cannot carry the expected-tip condition. Retain and report
a branch whose exact tip is not contained, that changes before deletion, that
cannot be fetched, that belongs to another lane, or that cannot be deleted.
