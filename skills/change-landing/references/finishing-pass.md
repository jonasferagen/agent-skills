# The finishing pass

[`change-landing`](../SKILL.md) runs this pass at its merge boundary. Run it at
the end of non-trivial work and for **every tracked-path rename or deletion**,
even when the change is otherwise trivial. It answers one question: **is the
final state actually finished?** Intermediate commits may legitimately have left
things red where the plan named that red window.

## 1. Inspect scope and diff

Read the whole changed file list before any individual hunk, then apply what its
effects trigger.

| Change effect | Required action |
| --- | --- |
| Removed or renamed behavior | Update its tests, docs and every inbound reference |
| Refactored code paths | Check for dead code the refactor left behind |
| Substantially grown ownership surface | Consider a focused architecture review |
| One owner, policy or topology event touching several otherwise independent surfaces | Treat the spread itself as evidence about the structure, not only as work to do |

Preserve unrelated user edits. A rename or deletion notice is a **search cue**,
not automatically a finding.

## 2. Sweep stale references

Turn every renamed or deleted path into three searches over the current
checkout: the **old path**, the **basename** and the **stem**. Classify every hit,
and rerun any search that truncated. The results are advisory — a historical
reference can be intentional.

Add domain terms the filenames do not capture, and broaden shared names across
the checkouts this lane already has when ownership crosses them. Where a refactor
moved files between packages, treat a documentation review as required evidence:
file moves ripple into docs, agent-instruction files and inline comments.

**A sweep this wide is itself a finding.** When one renamed tree, service or port
turns up in dozens of files, the hand-sweep is the symptom: the name had no
registry entry or configuration token behind it, so nothing connected the
mentions to the thing. Fix the hits, say so in the hand-back, and route the
missing indirection to whoever owns those names. Doing the sweep and leaving the
name unregistered guarantees the next rename repeats it.

**The sweep stops at the checkout boundary** — a limit on the lane, not on
finishing. A hosted code search is not a substitute: it silently returns nothing
for a private repository it cannot index, which reads exactly like a clean tree.
So an unreachable citing repository is a deferred obligation with a named home.
Name the outbound citation left unverified and the vantage point that can settle
it, such as a session that already holds those repositories checked out side by
side. That licence is exactly "sweep the checkouts this lane demonstrably already
has", never an instruction to census a workspace or enumerate siblings looking for
more.

An outbound citation survives because it was **authored**, not because someone
found it later. When a rename moves or splits something another repository is
known to cite, what is owed here is that the concept stays reachable under the
name outsiders use for it — not a notification to them.

**A live environment is the same blind spot in the other dimension.** It is not a
tree you have, and static evidence that a route is unused is not evidence that
every environment stopped running it. So a change retiring a one-time route — a
bootstrap, a migration, a backfill — consults the environments themselves, and
whatever inventory of owed acts the project keeps, before deleting the lane.

**A change that deleted data is reconciled against its target, not against a
restore.** Show that the named target is gone and that nothing beside it went with
it. Whether a restore rehearsal is also owed depends on what the reading project
has declared it retains; authorizing a deletion and guaranteeing its recovery are
separate questions, and that project's policy settles both.

## 3. Synchronize documentation

Every doc describing the old shape gets updated to the new one — behavior, API,
architecture, commands and paths — **in the present tense.** A doc that narrates
the migration instead of describing the result is the next reader's confusion.

Fix a stale reference or broken link the moment you find it, in whatever change
you are making. A link pointing at a renamed heading or a moved file is a defect
with one correct answer, so it needs no report and no permission; where the
surrounding claim went stale with the link, correct the claim too.

**Burn down worklists.** Remove finished entries from any TODO-style list as the
work lands, rather than leaving them checked off or struck through. A checked box
is a fine temporary in-progress marker, but on merge the commit history is the
durable record, so completed entries — and any section their removal leaves empty
— come out of the file. Where the work completed something a forward-looking goals
document tracked, move the durable part into whichever document owns it and remove
the goal entry, instead of leaving a dated "landed" note under a still-active goal.

## 4. Run focused verification

Run the affected package's exact focused checks — typecheck, tests and any precise
package-owned static check already in its scripts. After a refactor, a rename or a
change touching several files, widen to the whole affected root unless there is a
clear reason not to. [verification.md](verification.md) holds what these results
do and do not establish, and why the merged tree still owes its own run.

## 5. Reconcile the tracker

This pass is the **backstop** for tracker work, not its first owner: each item
belongs to the session that did it. Fix what that session left, through the
project's own tracker conventions rather than inventing a comment form here.

- Close what is verified. Where only the landing is proven, say that instead of
  closing.
- Comment on the items this change affects.
- A plan with work in flight belongs in its active state, and a finished one gets
  closed rather than left mid-stage. Where its agreed steps landed and the
  remainder is deferred, re-home the remainder instead of leaving the plan active
  by default.
- **A rollout closes on an observation of the consuming environments, never on
  this change having landed.** Name the environments checked and any still behind.

Each item is conditional on its subject existing. An item with no subject — no
plan, no rollout obligation — is omitted from the hand-back, not reported as
`none`.

## 6. Capture what you are not doing

Flag anything outside the task's scope but worth tracking. **Do not silently
absorb adjacent cleanup into the finishing pass.**

Keep closeout cleanup separate from structural follow-up: land the mechanical
stale-reference and dead-path fixes that are already safe, and route one evidenced
root finding rather than one abstraction ticket per touched literal. Record where a
direct dependency stays cheaper and clearer than a new seam. A classified list
worth keeping is filed wherever the project tracks findings; report output is
scratch data and is not committed.

Where this change copied a helper instead of extracting it, name the copied files
somewhere durable now. Whether a landed duplicate must be filed is the reading
project's threshold to set, but an unrecorded copy is undiscoverable by
construction.

## 7. Stage and commit

Stage **explicit paths**, never a blanket add. Prefix a numbered plan step's
commit with its step number where the project works that way. Re-run the evidence
after the final commit.

Run `git status --short` in the repository that owns the touched files first. If
unrelated edits share a file, inspect the diff and commit only when the staged
hunk set is obviously yours; otherwise report that a clean commit is unsafe. Never
silently leave verified implementation or refactor work uncommitted — where a
clean commit is unsafe, or the user asked for no commit, say so plainly rather
than working around it.

**A project whose pre-commit hook re-stages what it rewrote must refuse a
partially staged target.** Otherwise the re-stage silently sweeps that file's
unrelated unstaged edits into the commit. Markdown formatters are the common case
rather than a special exception:

```bash
git status --short -- '*.md'
```

Run the equivalent check over every path class the hook can rewrite. On an `MM`
target, stop and report it, include both halves deliberately, or clear that file
from the index. Retrying the commit walks into the same hook.

## 8. Check the base checkout

For a change landing from a lane, this pass owns one check before the landing:
**the base checkout is clean and on the default branch. Report, never restore.**

An agent write that reached the base is the failure isolation exists to prevent,
and nothing else here would see it — the lane's own diff is clean, so the only
evidence sits in the other tree. Dirt there is not yours to discard either: the
user edits that tree, so a dirty base is not by itself evidence of agent drift.
Report the paths and the branch, and leave the decision about what that content is
to a deliberate one. The
[base-checkout repair](lane-identity.md#recovering-a-base-checkout-on-a-feature-branch)
covers the case where the base is also on the wrong branch.
