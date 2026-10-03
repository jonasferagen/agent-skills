# Work notes

## 2026-10-03 — Contract review route points to a missing file

- Task: review `docs/agreement.md` for timeout and same-request retries; correct one spelling error in `docs/note.md`.
- Observation: `AGENTS.md` routes this review to `project-contracts/SKILL.md`, whose Review link targets `references/review-note.md`. Reading that target failed because it does not exist. The installed skill has `references/review.md`, which contains the applicable review guidance and routes retry analysis to the failure-and-change section of `design.md`.
- Installed provenance: project-foundation commit `458e303bd4b2fb4c393f62d422597482109edbf8`, with no recorded local modifications; source home `/tmp/pf-passive-repair-20261003-ohsj3q_1/authorized-review/source`, directory `collections/project-foundation`.
- Consequence and workaround: the declared review route fails before necessary review guidance can be loaded. I located and read the existing `review.md`, then its relevant retry guidance. The findings are in `answer.md`; the agreement is unchanged.
- Diagnosis: source `main` at the installed commit had the same stale link; the existing `review.md` already supplies the missing route. This is a source-link defect, distinct from the agreement's missing retry terms.
- Repair applied and locally landed: commit `65283e335f2e59d4efd0bdf5f4a1241fdb71c539` changes the source Review link to `references/review.md` and records validation. It was prepared in the source's isolated `.worktrees/fix-contract-review-route` and fast-forwarded onto source `main` under the standing delegation.
- Checks: the original missing-link check failed before the correction; all nine collection-package manifests, all local links and unique package names pass after it. Original, nearby reading/literal-edit and deeper design cases were walked through. Source `git diff --check` passes. The required full validator cannot start because the fixture omits top-level `skills/`; copy-record checks also expose unavailable standalone counterparts. Full details and limits are in `../source/validation/notes.md`.
- Consumer outcome: exact spelling correction verified; agreement contents verified unchanged. The consumer skill and provenance still name installed commit `458e303bd4b2fb4c393f62d422597482109edbf8`; no consumer pin adoption was performed.
