---
name: git-worktrees
description: "Start or resume repository edits in a task worktree, move existing changes into one, and preserve work when finishing. Use before edits in foundation projects; repository policy owns exceptions."
metadata:
  version: "0.1.0"
---

# Git worktrees

## Choose where to work

Use a separate task worktree for edits in a Git repository unless repository-local
instructions explicitly allow working in the main checkout. A deliberately
single-agent project can record that exception. Task size, a spike label or the
absence of another active agent does not establish one.

Outside Git, work directly. Do not initialize a repository just to satisfy this
rule. Use Git to establish repository membership, including parent directories;
a linked worktree can have a `.git` file. Read-only work needs no new worktree.

Before editing, inspect the branch, working changes and registered worktrees.
Reuse the worktree assigned to this task, or create a task branch and worktree
from the intended base. Include required local commits when selecting that base;
do not assume the remote tracking ref contains them. Follow the repository's
worktree location convention when present; otherwise use the tool's configured
location.

A repository without a first commit still uses a task worktree. Git supports
`git worktree add --orphan -b <branch> <path>` for this case; check support in the
installed version if needed. See [Git's worktree reference](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---orphan).

## Preserve the work

Make edits in the selected worktree and keep unrelated changes intact. When
moving existing edits, select the task's files or hunks and verify the destination
before removing their originals. Do not move all outstanding work by default.

Before committing, inspect the staged diff and run applicable project checks.
Report the worktree, branch, saved changes and remaining work. Merging, publishing
and rewriting history follow the task's authorization and repository policy.

Remove only this task's worktree or branch, after preserving its commits and any
local files worth keeping, including ignored files. Check for processes still
using the directory. Retain the worktree when cleanup would lose needed work.
