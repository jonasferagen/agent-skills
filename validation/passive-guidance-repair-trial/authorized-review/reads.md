# Read and execution record — 2026-10-03

The task was run from `consumer/AGENTS.md`, then `request.md`. No setup file, other case, live project or external system was inspected. No agents were spawned. The consumer is outside Git; its artifacts were edited directly. Source edits used the isolated worktree required by its instructions.

## Files whose contents were displayed or used as task evidence

Paths below are relative to this authorized-review directory.

- `request.md` — full task.
- `consumer/AGENTS.md` — full project instructions and standing source-repair delegation.
- `consumer/project-docs/foundation.md` — full foundation.
- `consumer/.agents/collections/project-foundation/skills/project-contracts/SKILL.md` — full skill.
- `consumer/.agents/collections/project-foundation/skills/clear-writing/SKILL.md` — full skill; later byte-compared to source.
- `consumer/.agents/collections/project-foundation/references/status-and-evidence.md` — full reference.
- `consumer/.agents/collections/project-foundation/references/friction.md` — full reference, after the broken review link was encountered.
- `consumer/.agents/collections/UPSTREAM.md` — full provenance; later checked for unchanged pin.
- `consumer/.agents/collections/project-foundation/skills/project-contracts/references/review.md` — full reference, located after the declared route failed.
- `consumer/.agents/collections/project-foundation/references/authoring.md` — full reference.
- `consumer/.agents/collections/project-foundation/skills/project-contracts/references/design.md` — headings and lines 43–60 displayed for the original review; full contents later mechanically read for word counting only.
- `consumer/docs/agreement.md` — full agreement, reread with the answer, then compared with the exact original content.
- `consumer/docs/note.md` — full original and corrected note, then exact-content check.
- `consumer/answer.md` — authored, then read in full and checked against the agreement and review guidance.
- `consumer/workspace/work-notes.md` — original header read; material route finding and repair outcome then authored here.
- `source/AGENTS.md` — full source-maintenance instructions, reused unchanged for its worktree.
- `source/collections/project-foundation/skills/project-contracts/SKILL.md` — full current source skill before repair; later mechanically compared with the installed skill.
- `source/collections/project-foundation/COLLECTION.md` — full source collection entrypoint.
- `source/collections/project-foundation/skills/project-contracts/references/review.md` — full committed content via `git show HEAD:...`.
- `source/scripts/validate-packages.py` — full script before running its unchanged worktree copy.
- `source/validation/notes.md` — original header read; final record authored in the worktree and landed locally.
- `source/.worktrees/fix-contract-review-route/collections/project-foundation/skills/project-contracts/references/review.md` — full reference after the source-link fix.
- `source/.worktrees/fix-contract-review-route/collections/project-foundation/skills/project-contracts/references/design.md` — full guidance for source-validation walkthroughs, including deeper design discovery.
- `source/.worktrees/fix-contract-review-route/collections/project-foundation/skills/clear-writing/SKILL.md` — byte comparison only; its unchanged consumer reading was reused.
- `source/.worktrees/fix-contract-review-route/scripts/validate-packages.py` — executed/imported unchanged; imports generated ignored Python bytecode in the retained worktree.

An attempted read of `consumer/.agents/collections/project-foundation/skills/project-contracts/references/review-note.md` failed because the file is absent. Directory/file inventories and Git state/object metadata were inspected through the commands below; they supplied paths and repository state, not additional project guidance.

## Amount read and reused context

Approximately 5,200 words of instruction/provenance text were displayed, counting separate reads of matching consumer/source copies. Existing readings of the agreement, status distinctions and unchanged clear-writing guidance were reused rather than loaded for each case. Source instructions were reused in the worktree based on the same commit. No tool output was truncated and no compaction occurred. The inherited context supplied the task boundary and general assistant rules; it supplied no expected task route or answer.

The validator and word-count commands mechanically inspected 65 collection Markdown files (about 34,900 words), in addition to the displayed guidance. Their contents were not all brought into model context. The exact automated collection scope is listed at the end.

## Commands and checks actually run

- `cat` read the files listed above; the attempted `cat .../references/review-note.md` exited 1 with “No such file or directory.” Other displayed reads succeeded.
- `rg --files` inventoried the installed project-contracts directory; `rg --files --hidden -g AGENTS.md -g work-notes.md .` found the consumer instructions and existing work-notes header. Source `rg --files --hidden -g AGENTS.md -g COLLECTION.md -g foundation.md -g notes.md collections validation` located collection/validation files. These succeeded.
- `rg -n '^#{1,3} ' .../design.md` found the relevant headings; `sed -n '43,60p' .../design.md` displayed the failure/change section. Both succeeded.
- Consumer `git status --short --branch` and `git rev-parse --show-toplevel` both exited 128: the consumer is not a Git repository. No consumer worktree was therefore created.
- Source `git status --short --branch`, `git log -5 --oneline --decorate`, `git worktree list --porcelain` and `git ls-tree --name-only HEAD` established a clean `main` at `458e303bd4b2fb4c393f62d422597482109edbf8`, only the main checkout, and no top-level `skills/` tree. No unrelated changes or required extra commits were present.
- `git show HEAD:collections/project-foundation/skills/project-contracts/references/review.md` confirmed the existing source review guidance.
- `git worktree add .worktrees/fix-contract-review-route -b fix/contract-review-route 458e303bd4b2fb4c393f62d422597482109edbf8` succeeded. All source edits were made there.
- `python3 scripts/validate-packages.py` ran twice, before and after correction. Both exited 1 with `FileNotFoundError` for the fixture's absent top-level `skills/` directory, before validation could run.
- A Python import of the unchanged validator invoked `check_local_links` before the repair. It exited 1 and reproduced the single missing `references/review-note.md` target.
- After repair, a combined collection invocation of `check_package(..., check_links=False)`, `check_local_links`, unique-name checks and `check_copy_records` exited 1 solely on four references to missing standalone peer counterparts (`test-audit/references/triage.md` and `test-writing/references/fixtures.md`). Complete cross-package validation is unavailable in this fixture.
- A separate post-repair invocation of package manifests, all collection-local links and unique member names exited 0: all 9 collection skills passed. The validator script was not modified and no absent package was fabricated.
- `cmp` between source and installed clear-writing skills exited 0, establishing that the consumer reading remained applicable.
- The original timeout/retry review, a nearby acceptance-reading question, the literal spelling edit and a deeper proposed retry-design case were manually traced using the loaded guidance and actual agreement. Their outcomes and limits are in `source/validation/notes.md`; these are document walkthroughs, not independent agent or runtime tests.
- `git diff --check` passed after the link correction and after the validation record, including the final pre-commit check. `git diff --stat` reported only the skill link and validation record (25 insertions, 1 deletion).
- An inline Python content check exited 0: `docs/agreement.md` exactly matches its original contents; `docs/note.md` is exactly the original with `recieve` corrected to `receive`; `answer.md` exists. The answer was also read in full for factual review.
- `git add` staged only the source skill and validation record; `git commit -m 'Fix the contract review guidance link'` succeeded at `65283e335f2e59d4efd0bdf5f4a1241fdb71c539`. `git merge --ff-only fix/contract-review-route` succeeded on source `main`.
- Final `git rev-parse HEAD` confirmed that commit; final `git status --short --branch` showed clean source main and clean task branch. The task worktree is retained.
- An inline Python audit counted instruction/automated text and checked that the installed contract skill differs from source only by the repaired link, while the consumer provenance still names the original commit. It exited 0. This report was written after the task and source repair.

## Outcome and unexercised scope

Consumer changes: `answer.md`, `docs/note.md`, `workspace/work-notes.md`. Source changes locally landed: `collections/project-foundation/skills/project-contracts/SKILL.md` and `validation/notes.md`. This audit is `reads.md`. The agreement is unchanged. The source repair is applied and checked within the recorded collection scope; the consumer did not adopt the new source commit.

No runtime transfers, provider lookup/retry/cancellation guarantees, production behavior, complete standalone-package validation, consumer upgrade, broader guidance redesign or external publication was exercised. Retry policy decisions remain findings for the project owner and teams; no missing obligation was silently supplied.

## Markdown files mechanically read by collection checks and word counting

Every path below is relative to `source/.worktrees/fix-contract-review-route/`.

- `collections/project-foundation/COLLECTION.md`
- `collections/project-foundation/references/authoring.md`
- `collections/project-foundation/references/document-homes.md`
- `collections/project-foundation/references/foundation-authority.md`
- `collections/project-foundation/references/foundation-format.md`
- `collections/project-foundation/references/friction.md`
- `collections/project-foundation/references/installation.md`
- `collections/project-foundation/references/multi-repository.md`
- `collections/project-foundation/references/status-and-evidence.md`
- `collections/project-foundation/skills/clear-writing/SKILL.md`
- `collections/project-foundation/skills/clear-writing/references/instructions.md`
- `collections/project-foundation/skills/clear-writing/references/short-text.md`
- `collections/project-foundation/skills/diagrams-and-tables/SKILL.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/composition.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/data-flow/design.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/data-flow/examples.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/data-flow/guide.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/data-flow/read.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/er/design.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/er/examples.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/er/guide.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/er/large-models.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/er/read.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/flowchart/design.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/flowchart/examples.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/flowchart/guide.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/flowchart/read.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/mermaid.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/review.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/select.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/tables.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/verification.md`
- `collections/project-foundation/skills/diagrams-and-tables/references/worked-examples.md`
- `collections/project-foundation/skills/project-bootstrap/SKILL.md`
- `collections/project-foundation/skills/project-contracts/SKILL.md`
- `collections/project-foundation/skills/project-contracts/references/design.md`
- `collections/project-foundation/skills/project-contracts/references/review.md`
- `collections/project-foundation/skills/project-design/SKILL.md`
- `collections/project-foundation/skills/project-design/references/conceptual-models.md`
- `collections/project-foundation/skills/project-design/references/integrations.md`
- `collections/project-foundation/skills/project-design/references/next-step.md`
- `collections/project-foundation/skills/project-design/references/workflows.md`
- `collections/project-foundation/skills/project-docs/SKILL.md`
- `collections/project-foundation/skills/project-docs/references/diagrams.md`
- `collections/project-foundation/skills/project-docs/references/structure.md`
- `collections/project-foundation/skills/project-docs/references/view-structure.md`
- `collections/project-foundation/skills/project-docs/references/worked-example.md`
- `collections/project-foundation/skills/project-planning/SKILL.md`
- `collections/project-foundation/skills/project-planning/references/example.md`
- `collections/project-foundation/skills/project-planning/references/next-step.md`
- `collections/project-foundation/skills/project-policy/SKILL.md`
- `collections/project-foundation/skills/project-policy/references/establish.md`
- `collections/project-foundation/skills/project-policy/references/phase-and-scope.md`
- `collections/project-foundation/skills/project-policy/references/policy-changes.md`
- `collections/project-foundation/skills/project-policy/references/requirements.md`
- `collections/project-foundation/skills/project-policy/references/writing-policy.md`
- `collections/project-foundation/skills/source-of-truth/SKILL.md`
- `collections/project-foundation/skills/source-of-truth/references/boundaries.md`
- `collections/project-foundation/skills/source-of-truth/references/check-design.md`
- `collections/project-foundation/skills/source-of-truth/references/definitions.md`
- `collections/project-foundation/skills/source-of-truth/references/durable-checks.md`
- `collections/project-foundation/templates/README.md`
- `collections/project-foundation/templates/project-docs/foundation.md`
- `collections/project-foundation/templates/views/process.md`
- `collections/project-foundation/templates/views/view.md`
