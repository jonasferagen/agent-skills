# Validation and alignment — Change Workflow

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation or a live run.

| Request and context | Expected outcome |
| --- | --- |
| A project has not adopted worktrees and authors on branches in one checkout | No worktree is imposed. The package states that isolation is a discipline a project opts into and that its own instructions win. |
| A one-line documentation fix in an adopting project | Still starts in a worktree. Size and file kind are explicitly not exceptions. |
| The agent judges a change too small to isolate | Refused: only a direct user instruction in the moment authorizes authoring in the base checkout, and "it is only a doc change" is not that instruction. |
| The session starts in a directory under `.worktrees/` that looks like a lane | The role is settled from the branch and `git worktree list --porcelain`, never from the path's name. |
| An existing lane matches the task by name | Not an authoring lane unless the user or the project's record of the work directs this session to resume it. |
| The base checkout is found on a feature branch | Treated as a defect to repair — switch the base back and re-add the lane — not as a usable lane; a base holding uncommitted work is reported before switching. |
| A branch has to be brought current | Merged, never rebased, with the reason given: the rewrite orphans the commit identifiers that plans, tracker threads, hand-backs and change records cite. |
| Tidying an unpublished branch's own commits before it lands | Named as a different operation from integrating, which the commit-identity reason does not reach — and handed to the reading project's policy on rewriting, so a flat "never rebase" rule stays intact. |
| A published branch is proposed for rebase | Refused outright; others may already have it. |
| Verification ran, then the base advanced before the merge | The evidence is stale. Synchronize and check the resulting tree again; two object IDs establish freshness and a second run of the same checks does not. |
| A conflict-free merge is offered as evidence | Refused: Git resolving the texts says nothing about the resulting behavior. |
| Focused branch checks are offered as merge evidence | Accepted as authoring evidence only; the merged tree still owes its own run. |
| A check rewrites tracked files and exits zero | The result is invalid: it describes the post-rewrite worktree, and the first run has made its own failure irreproducible. The rewrite is a defect to report in that project. |
| The project has no runnable check for the changed surface | Reported as friction to fix there. No substitute is guessed at and no scanner is invented for the occasion. |
| A rename or deletion is part of the change | The finishing pass is owed even when the change is otherwise trivial: three searches per path over the old path, the basename and the stem, every hit classified. |
| One rename turns up in dozens of files | The width of the sweep is itself reported as a finding: the name had no registry entry or configuration token behind it. |
| A citing repository is outside the checkout | Named as a deferred obligation with a named vantage point. A hosted code search is refused as a substitute, because an unindexed private repository reads exactly like a clean tree. |
| A change retires a one-time route | The live environments are consulted before the route's deletion lands; static evidence that it is unused does not prove every environment stopped running it. |
| A change deleted data | Reconciled against the target — gone, and nothing beside it — while whether a restore rehearsal is also owed defers to the reading project's retention policy. |
| A commit in the landing range carries a closing keyword | Surfaced before the merge, because a commit message is not part of a diff. Whether to amend it is the project's tracker convention; nothing is closed by accident. |
| A rollout is closed on the change having landed | Refused: a rollout closes on an observation of the consuming environments, with the environments checked and any still behind named. |
| A blanket `git add` is proposed | Refused; explicit paths only. |
| Unrelated user edits share a touched file | The diff is inspected, and a clean commit that is unsafe is reported as unsafe rather than worked around. |
| A pre-commit hook re-stages what it rewrote and a target is `MM` | Not committed as it stands: stopped and reported, both halves included deliberately, or the file cleared from the index. The re-stage would sweep that file's unrelated unstaged edits into the commit. |
| A trivial change without renames or deletions lands from a lane | The full finishing pass is not owed, but its staging and base-checkout steps are: explicit paths, the `MM` check, and a check that the base is clean and on the default branch. |
| The base checkout is dirty at the merge boundary | Reported, never restored. The user edits that tree, so dirt there is not by itself agent drift, and it is not this pass's to discard. |
| Unrelated dirty edits in the base at landing time | Not a stop sign. The merge is attempted where the touched paths do not overlap, and the blocking paths are reported when it refuses. |
| `git branch -d` refuses a branch | Not read as proof of unmerged work. Containment against the integration branch is recomputed, and `-D` is used only after a recorded `0`. |
| A worktree has a dev server running in it | The process is stopped deliberately; the directory is not pulled out from under it, and force flags are not reached for. |
| A lane is dirty, has unique commits, or lacks containment evidence | Retained and reported with the reason, which is a complete terminal state. |
| This lane's published remote branch is deleted after landing | Only under exact observed object IDs, containment against an integration tip that contains the landed commit, and `--force-with-lease`, so a concurrent advance fails instead of being discarded. |
| Another lane's branch or worktree turns up during cleanup | Out of scope: a population sweep is a different job with different evidence. |
| An ordinary change is handed back | Changed surfaces, verification, the commit id, follow-ups and friction. Stale terms, plan and rollout are omitted because they are empty by construction, not reported as `none`. |
| A change renamed a path and is handed back | The stale-terms field returns, because `git diff --name-status` shows an `R` entry. |
| A rename-free change of several commits is handed back | Each commit's net line delta is added; stale terms stay omitted. |
| A change carrying a rollout is handed back | The plan and rollout field names the environments checked and any still behind. |
| A verification report covering a subset of the suite | Names which subset. A check that could not run at all is a refusal, never a silent pass. |
| Visual or manual work is handed back with branch and worktree state | Incomplete: the report also owes a review surface, or a statement of which surface could not be supplied and why. |
| A stopped service's URL is offered as the review surface | Refused as worse than none — it reads as reviewable and is not. |
| Lane locks, leases, gate tiers or a merge train are proposed as the follow-up | Declined: the package holds judgment, and a project wanting automation on top owns it. |
| A pickup note for deferred work is asked for | Handed on: it orients a session that has not started, where a hand-back reports one that finished, and it lives wherever the project keeps work state. |
| Adopting the package into an existing project | No landing command, tracker, branch protection or authorization model is implied. Nothing here is a licence, and nothing is assumed disposable unless that project has said so. |

## Scope boundaries

Covers one change's path from isolation to a cleaned-up lane: the worktree, keeping
current, the finishing pass, what counts as merge evidence, the landing, cleanup by
containment, and the hand-back that reports it.

It does not decide a project's landing policy, own a landing command or gate, define
tracker conventions, or grant authorization for any operation. It carries no control
plane, no lane locking or leasing protocol, and no cross-repository coordination. A
pickup note for deferred work is a different subject and is deliberately out.

## Sources inspected

Merged from the owner's Forge Agent Kit `worktree` and `reconcile` skills at
`c98147a115a30f36b952df5faf1c869b54480c59` (2026-09-18) on 2026-09-29, reconciled
against Personal Atlas's `docs/change-workflow.md`, which is an independent and
newer reduced extraction of the same two skills.

The upstream packages were heavily coupled to the owner's Forge fleet. Removed
whole, not softened: the `./ops/land` and `./ops/verify` landing-door contract and
its conformance rules; the `git worktree lock` claim protocol, with its
stranger-readable lock reasons, reclaim procedure and lock-release rows; the
container model in which the integration lane is what the container runs from; the
fail-closed authorization matrix, whose rows were fleet-shaped standing grants; and
every reference to `ferraforge/forge-agents` and its control tracker. `authorization.md`
kept three transferable rules and lost the matrix: naming a discarding operation's
target from an observed location, the partially-staged formatter-hook case, and not
leaving verified work silently uncommitted.

Seven citations of the Forge Project Policy were redirected, because that policy
opens by declaring nothing is in production while both consuming projects are, each
with its own posture document. Four carried substance now stated in place:
correctness is owed at the merge boundary; a check that rewrites tracked content
does not verify its input; a verdict names what it measured; and authorizing a
destructive act is separate from guaranteeing its recovery. The other three defer to
the reading project's own policy — retention and restore evidence, the threshold at
which a landed duplicate must be filed, and whether landing is authorized without
asking. Upstream's licence that state nobody declared retention for is disposable was
inverted rather than imported: assume nothing is disposable unless the project has
said so.

`--force-with-lease` on the published branch was kept. It is ordinary Git safety on a
ref deletion — a concurrent advance fails instead of being discarded — and not part of
the lane-coordination lock and lease protocol that was removed.

References to nine sibling Agent Kit skills became descriptions of the boundary, since
each skill directory is the installable unit here and a cross-package path would break
when this one is installed alone. Three of those were the whole substance of an
upstream section — plan lifecycle stages, occupancy evidence for reclaiming a lane, and
capture-evidence rules for frames — and were reduced to the transferable rule or cut.

Three divergences between upstream and the Atlas extraction were resolved
deliberately:

- **Rebase.** Atlas forbids it absolutely, including a local branch; upstream gives the
  same commit-identity reason for integrating and then permits tidying an unpublished
  branch's own commits. The package states the absolute rule for integrating, with the
  reason, and names the tidy as a different operation the reading project's rewriting
  policy decides — because the reason genuinely only reaches commits something already
  cites, while a skill that granted the tidy would override a project that chose the
  flat rule.
- **The hand-back contract.** Upstream's newer rule is carried: a field empty by
  construction is omitted while a field that could have carried content reports `none`,
  and the terms-searched field is owed only when `git diff --name-status` shows an `R`
  or a `D`. Atlas's unconditional list makes a rename-free single-commit change report
  three absences, which is not evidence about the change.
- **Authoring in the base checkout.** Atlas's sharper formulation is taken — size and
  file kind are not exceptions, and a one-line doc fix counts — with upstream's single
  exception kept in the form that closes the loophole: the agent never grants it to
  itself, only a direct user instruction in the moment does.

Upstream's `handoff` skill was read and left out. Its subject is forward-looking
orientation for deferred work, which upstream itself contrasts with closing out what a
turn just did; its two touchpoints with landing are inbound citations of rules this
package already owns — a worktree before the first write, and bringing a resumed branch
current. It also carries a second opinionated planning model, including the control
tracker that had to be stripped anyway, and in both consuming projects work state is
homed outside the project that holds facts.

## Review limits

- No independent agent evaluation has run against these scenarios.
- **The package is prepared, not adopted.** It is registered in no consuming project,
  and neither consumer was changed. Whether a project uses worktrees is that project's
  policy decision.
- Not exercised as a package: the lane it describes was followed by hand while
  authoring it, but no session has read this `SKILL.md` and landed a change from it.
- The stale-reference sweep and the containment checks are the best-worn parts, since
  both consuming projects already run reduced versions of them. The gate-freshness
  comparison and the published-branch recipe are the least worn: neither consuming
  project has a composite named check command, and neither routinely publishes feature
  branches, so the two-object-ID window and the `--force-with-lease` deletion have been
  reasoned about rather than run.
- The Markdown link-check recommendation is untested here. This repository has no
  package manifest and validates links by inspection.
- One divergence resolution deliberately leaves a decision open rather than settling
  it: whether tidying an unpublished branch is allowed now depends on the reading
  project's policy, so a project with no rewriting policy gets no answer from the
  package.

## Clear writing pass — 2026-09-30

Version 0.1.1 revises the manifest and all five references; see the [package
sweep](clear-writing.md#package-sweep--2026-09-30). Figurative uses of the
defined terms "lane" and "land" were replaced where they clashed with the
definitions, such as "a lane that holds" and "is never the lane". The
description is unchanged. Review found rule strength, authorization boundaries,
stop conditions and the order of Git steps unchanged; three wording corrections
followed, and one edit was reverted to the original.

Left unresolved, because each answer changes behavior:

- `finishing-pass.md` has a change retiring a one-time route consult the
  environments "before deleting the lane"; the scenario above says before the
  route is deleted.
- `lane-identity.md` says a bare number in a lane name always refers to the
  lane's own repository's tracker, then keeps the bare number for work that
  answers to another repository's tracker.
- `lane-identity.md` accepts a lane "this session opened or deliberately
  resumed", but rejects one "this session did not open and the project does not
  name".
- In the base-checkout repair, Git carries uncommitted edits across a switch
  when the changed files do *not* overlap, which is the case the check approves.

## Diagrams and tables pass — 2026-09-30

No change; see the [package
pass](diagrams-and-tables.md#package-pass--2026-09-30). The five existing tables
are complete and grounded. A table of when each hand-back field is owed was the
strongest candidate, but it would have to settle the hand-back contradiction
recorded above.

Newly found: the manifest says `cleanup.md` gives "the order the removals go
in", but it gives only a partial order; and the plan and rollout fields in
`hand-back.md` are missing from its ordered field list.

## Resolutions — 2026-09-30

Version 0.2.0 carries these changes.

The owner accepted every proposed resolution of the contradictions recorded
above, together with four findings not recorded there. Each line gives what was
contradictory and what the text now says.

- One-time route: `finishing-pass.md` said to consult the environments "before
  deleting the lane", which follows landing; it now says before the deletion
  lands, and the scenario matches.
- Bare number: `lane-identity.md` said a bare number "always" means the lane's
  own tracker, then kept one for another tracker's work; it is now the default
  reading, and the qualified reference goes in the text that cites the work.
- Resuming a lane: the roles table accepted a "deliberately resumed" lane that
  the prose rejected. Owner decision: a session authors in a lane it did not
  open only when the user, or the project's record of the work naming the
  branch, directs it to resume; a matching name or path is not that direction.
  Cleanup now covers the lane this session opened or resumed, and landed.
- Base-checkout repair: the check approved switching when uncommitted files do
  not overlap the branch difference, which is the case where Git carries them
  onto the default branch. The repair now switches only a clean base, and
  reports uncommitted work first.
- Removal order: the manifest promised an order that `cleanup.md` gave only in
  part; `cleanup.md` now numbers it, with the worktree removed before the
  branch, as Git requires.
- Plan and rollout: the hand-back treated them as fields its ordered list
  lacked; the list and the manifest now carry a plan and rollout field.
- Full list: this is the hand-back contradiction the diagrams pass cites but no
  earlier section records. "The full list returns" for any multi-commit or
  unlanded change conflicted with field 4's `R` or `D` condition; each
  condition now brings back only the field it triggers.
- Finishing-pass scope: the manifest implied the pass on every lane, the
  reference on non-trivial work and renames. Owner decision: the manifest now
  scopes it the same way, and the staging checks in step 7 (explicit paths and
  the `MM` check) and the base-checkout check in step 8 apply to every change
  that lands from a lane.
- Formatter hook: "a project … must refuse" left the actor unclear; the agent
  now does not commit a partially staged target as it stands.
- Process in a worktree: `cleanup.md` said a running process blocks removal,
  but `git worktree remove` checks files and locks, not processes, so on Linux
  it deletes the directory under a running process. Stopping it first is kept,
  with that reason. The step 2 resume now carries the same direction rule as
  `lane-identity.md`.
