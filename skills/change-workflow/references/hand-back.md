# The hand-back

What a finished change reports, and what it must not pad.
[`change-workflow`](../SKILL.md) states the contract; this page holds the
field-by-field conditions.

## Fields, in this order

1. **Changed surfaces.**
2. **Verification performed** — the commands run, their status, and anything
   skipped together with the risk it leaves unproven.
3. **Commit identifiers.** Add each commit's net line delta **when the range holds
   more than one commit, or when the branch is handed back rather than landed**;
   on a single landed commit the diff the reviewer already has carries the scale.
4. **Stale terms searched** — owed when the change renamed or deleted a tracked
   path, which `git diff --name-status <base>..HEAD` answers by showing an `R` or a
   `D` entry.
5. **Remaining risk and surfaced follow-ups.**
6. **Friction** — any tooling or structural friction met along the way. That is
   signal about the repository rather than noise, and `friction: none` is a
   complete answer.

## Omitted versus `none`

**A field that is empty by construction is omitted; a field that could have
carried content and did not is reported as `none`.** The difference is what the
reader gets: an omitted field says the question never arose, a `none` says it
arose and the answer was nothing.

Writing "stale terms: none, plan: none, rollout: none" on a change that renames
nothing and answers to no plan reports the absence of three questions, which is
not evidence about the change.

**An ordinary change** — one that renames and deletes nothing, answers to no plan
or rollout obligation, and lands from a single commit — hands back the changed
surfaces, the verification, the commit id, the remaining follow-ups and the
friction, and omits the rest. The full list returns the moment the change renames
or deletes a tracked path, carries a plan step or a rollout, spans more than one
commit, or is handed back unlanded. Every one of those conditions is readable from
the lane you are standing in: a `git diff --name-status`, a commit count, or a
reference the branch already carries.

## Handing back visual or manual work

Read this whenever the user is asked to look at something: a landed change whose
success is visual or manual, or a hold taken because you cannot tell whether the
outcome is right.

The user is being asked to judge the work, so the report owes the surface that
judgment is made on. Branch and worktree state locate the change; they are not a
review surface, and a report carrying only them leaves the reviewer to assemble
one. Both go back together, with the first surface below that applies.

| Review surface | Supply it when | What the hand-back names |
| --- | --- | --- |
| A live URL | a served page can safely be kept up across the review window | the exact route, the state needed to see the thing, the tree identity the page is serving, and that the service is still running |
| A captured set | nothing is served, or the page would not survive the review window | where the frames are, and the evidence needed to interpret them: what was rendered, from which tree, at what size |
| Neither | both routes are unavailable | which surface could not be supplied, and why |

**A URL for a service stopped before the hand-back is worse than none** — it reads
as reviewable and is not. Either keep the service up across the review window and
say so, or fall to the captured set.

The third row is a stated result, never a silent omission. Naming the surface that
could not be supplied is what lets the user ask for it, run the thing themselves,
or accept the branch knowing what went unseen.

**Prefer an assertion to a capture.** A change some test can observe owes no
pixels — report the check that proved it. Reach for a capture only where no test
surface can observe the outcome: rendered output, layout, audio, or a manual smoke
step the task names by hand. Not knowing how to look at the thing is a reason to
write the assertion, not a reason to capture.
