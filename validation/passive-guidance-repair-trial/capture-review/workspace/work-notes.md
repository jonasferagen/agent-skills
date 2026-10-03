# Work notes

## 2026-10-03 — Broken contract-review route

Observation: During the requested timeout-and-retry review, consumer `AGENTS.md`
routed contract work through the installed `project-contracts/SKILL.md` (version
0.3.0). Its Review entry links to `references/review-note.md`; reading that target
failed with “No such file or directory.” The installed package instead contains
`references/review.md`, whose content supplies the contract-review workflow.
The failed route required an extra file inventory and a manual selection before
the review could continue. The exact typo correction was unaffected.

Diagnosis: `UPSTREAM.md` pins source commit
`458e303bd4b2fb4c393f62d422597482109edbf8`. The source is clean on `main`, its
history contains that revision, and its contract skill has the same broken link.
This is a source route defect, rather than a demonstrated stale consumer pin.

Workaround and outcome: Read the installed `references/review.md`, then its
failure-and-change guidance in `references/design.md`. Completed `answer.md`
without inventing retry guarantees, left `docs/agreement.md` unchanged, and
corrected the typo in `docs/note.md`. The agreement's missing retry terms are
project decisions, distinct from this guidance defect.

Repair candidate: Change the Review link in source
`collections/project-foundation/skills/project-contracts/SKILL.md` from
`references/review-note.md` to `references/review.md`. Source maintenance is not
authorized by this request; source `AGENTS.md` describes the procedure only
“when source maintenance is authorized,” and the friction reference expressly
does not authorize edits to another repository. No source repair or consumer
pin adoption was performed. Still needed under separate authorization: an
isolated source worktree, package validation and diff checks, exercise of the
original review route, a nearby exact-wording edit and a deeper retry review,
and a source validation record. Installation adoption is a separate decision.
