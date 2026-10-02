---
name: change-workflow
description: "Manage an adopted worktree workflow: start or resume a change, synchronize it, verify the landing tree, and clean up. Use at those lifecycle steps; the project owns authorization and landing policy."
metadata:
  version: "0.2.1"
---

# Change Workflow

**This describes a discipline a project opts into, not a universal rule.**
Whether changes are authored in isolated worktrees, how one reaches the default
branch, and who may land it are decisions the reading project makes in its own
instructions. Read those first. Where they are silent, this package supplies a
reliable default; where they disagree with something here, they win. A project
that authors on branches in one checkout is not doing it wrong.

Once a project has adopted it, the rule is:

**Before the first repository write bound for the default branch, create a
worktree and author there.** Anything Git would track counts, however small or
early: source, docs, configuration, generated files and status records alike.
Ignored dependencies and disposable output do not. Size and file kind are not
exceptions: a one-line doc fix counts.

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

Work whose success is visual or manual is not a fourth condition. Hold it back
from landing only when you cannot tell whether the rendered or manual outcome is
right; not knowing how to look at the outcome does not count as that
uncertainty. Either way, the report owes the review surface the judgment is
made on. Branch and worktree state locate a change, but they do not let anyone
review it.
[hand-back.md](references/hand-back.md#handing-back-visual-or-manual-work)
settles which surface applies.

## Workflow routing

Before starting or resuming a lane, read [the workflow](references/workflow.md)
and its lane-identity guidance. At synchronization or landing, read the relevant
steps there and [verification](references/verification.md). For a finishing
pass use [finishing-pass](references/finishing-pass.md); for removal use
[cleanup](references/cleanup.md). These references are selected by the current
step, not loaded as a checklist at the start of every task.

## Hand back

Report, in this order: the changed surfaces; the verification performed, with the
commands, their status and anything skipped together with the risk it leaves; the
commit identifiers; the stale terms searched; the plan and rollout state; the
remaining risk and surfaced follow-ups; and any tooling or structural friction
met along the way, where `friction: none` is a complete answer.

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

There is no control plane here, and building one — gate tiers, merge trains,
lane sidecars, per-lane databases, fleet boards, port allocation — is not the
follow-up to propose or build. What this holds is judgment: work in isolation,
integrate by merge, verify the tree that will actually merge, fail closed on
anything that discards work. A project that wants automation on top owns it.

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
