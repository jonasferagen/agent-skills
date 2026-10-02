# Validation — Git worktrees

Date: 3 October 2026. Unreleased version 0.1.0 in project-foundation.

## Contract

Edits in Git repositories use task worktrees unless repository-local instructions
explicitly opt out. A deliberately single-agent project can record that policy.
Work outside Git proceeds directly. Bootstrap puts the rule and the installed
skill link in AGENTS so the default is visible before the first edit.

The skill owns location selection and preserving work. It does not import the
retired change-workflow package's merge strategy, mandatory publishing, tracker
procedures or report format.

## Behavioral scenarios

| Case | Expected result |
| --- | --- |
| Small edit in a Git repository, with unrelated work in the base | Edit in a separate task worktree; preserve unrelated changes. Being the only active agent is not an exception. |
| Worktree already assigned to the task | Reuse it after inspecting its Git state; do not create nested worktrees. |
| Repository specifies a worktree location | Follow that convention when creating a worktree. |
| No repository location convention, with a tool-configured location | Use the tool's configured location. |
| Repository instructions explicitly choose the main checkout for a single-agent project | Follow that exception and preserve it during foundation updates. |
| Spike in a directory outside Git | Edit there without initializing Git to satisfy the workflow. |
| A subdirectory inside a repository | Discover the parent repository and apply its policy. |
| New Git repository with no commit | Use a task worktree, including an unborn branch when supported; do not invent a main-checkout exemption. |
| Move existing task changes away from unrelated edits | Transfer only the task's files or hunks and verify them before removing originals. |
| Worktree holds needed ignored state or unpreserved commits | Preserve that state or retain the worktree; clean status alone is insufficient. |
| Read-only question | Answer without creating a worktree or entering a full Git procedure. |

## Evidence

The installed Git is 2.53.0. An isolated empty repository accepted
`git worktree add --orphan -b foundation <path>` and registered the task worktree
on an unborn branch. This matches [Git's documented orphan option](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---orphan).
No initial-commit exception is needed on this version. Other Git versions were
not tested.

## Consumer routing trials

Temporary fixtures were created outside the authoring repository at
`/tmp/foundation-git-routing-9te5c2jd`. Each received the complete draft collection,
provenance and project instructions. The Git fixtures also had an unrelated
uncommitted owner note. The request was a literal README spelling correction;
the default case explicitly said the agent was working alone on a small edit.
No expected route was supplied beyond each project's normal instructions.

| Case | Observed behavior | Instruction reads |
| --- | --- | --- |
| Default, fresh context | Created a task branch and sibling worktree. Corrected only its README; the main checkout's README and owner note were preserved. | AGENTS: 54 words; Git worktrees: 327 words, each once. |
| Local policy exception, a separate fresh context | Followed the explicit main-checkout exception. Corrected README on main and preserved the owner note. No task branch or worktree was created. | AGENTS: 80 words; Git worktrees: 327 words, each once. |
| Outside Git, following the exception case in reused context | Established that the directory was outside Git and edited directly. Created no repository. | This project's AGENTS: 54 words; no new skill read. |

Both Git results passed `git diff --check`; an exact readback verified the
non-Git edit. Independent inspection confirmed all three results, preservation
of the owner note and unchanged Git membership. No trial committed, merged or
published its change. There were no questions or task obstacles.

Counts are approximate whitespace words displayed from instruction files, not
total context use. Project README reads added seven unique words per case; each
agent also reviewed the output. No authoring workflow, source catalog, source
repository or external reference was loaded. The default agent identified about
160 words of the short skill covering cases it did not exercise; these did not
trigger additional reading. The non-Git case reused the first case's skill text
and is not an independent cold-entry trial.

Detailed temporary ledgers were `default-evidence.md` and
`exceptions-evidence.md` under the fixture root. These observations preserve the
material results without requiring those temporary files. They show the routes
working in two fresh contexts and one reused context; they do not establish
reliability across clients or repositories.

## Bootstrap integration

A further agent used the supplied Project bootstrap skill to establish a
synthetic personal tool foundation in an empty Git repository. The new bootstrap
route led it to Git worktrees. It created the sibling
`empty-bootstrap-foundation` on unborn branch `task/bootstrap-foundation` and
wrote the foundation there; the original checkout remained clean on unborn main.

The generated AGENTS includes the worktree default, installed Git skill link,
reuse of the assigned worktree, repository-local exceptions, and the non-Git
case. It states that this fixture has no exception. Five foundation documents
and the complete 39-file collection were produced. The collection matched the
supplied trial source; 32 project links/anchors and whitespace checks passed.
No application, database, remote, commit, merge or publication was introduced.
Independent inspection confirmed the generated rule and worktree locations.

This bootstrap agent reused context from an earlier foundation experiment. It
received the new package and raw brief without an expected result, but this is
not a fresh-context bootstrap trial. Freshness applies only to the two consumer
cases identified above. The other scenario rows remain author-reviewed
expectations, including cleanup of ignored state and relocation of mixed edits.

The bootstrap agent reported about 6,300 words across 15 supplied files: Project
bootstrap, Git worktrees, COLLECTION, UPSTREAM, project-policy, project-docs,
shared authoring, foundation authority, all four templates, Clear Writing, its
instruction reference and project-docs' structure reference. It then reviewed
about 1,400 words of generated documents. Each supplied file was read once in
this trial without truncation; several guidance files repeated earlier-session
context. No source authoring repository or unrelated fixture was opened. The
temporary `bootstrap-evidence.md` records the detailed ledger; these estimates
exclude platform context and mechanical reads and are not total context usage.

## Package checks

- `python3 scripts/validate-packages.py`: 23 skill entries in standalone packages
  and one collection validated after replacing the retired package.
- Skill Creator's `quick_validate.py`: Git worktrees and Project bootstrap passed.
- All 369 inline local Markdown links and heading anchors across 123 source
  Markdown files resolved. External URL availability was outside that scan.
- `git diff --check`: passed; new files also receive the staged whitespace check.
- Remaining old-package mentions are retirement notes, provenance or dated
  evidence. No active catalog entry or installed instruction links to its deleted
  source directory.

These checks cover the source draft. No release tag or existing downstream
installation was changed. Trial fixtures included the complete collection; a
final source reflow in COLLECTION.md changed line wrapping only.

## Location fallback correction

The sibling-directory fallback was replaced with the tool's configured location
when the repository has no location convention. Review covered both location
cases and reuse of an assigned worktree. Package validation, Skill Creator's
validator and whitespace checks passed. No fresh client-level placement trial
was run; the sibling locations in earlier trials reflect the previous wording.

## Authoring

Skill Creator and Pattern capture informed the narrow scope and preservation
rules. Clear Writing and its instruction guidance kept the default, exceptions
and authorization distinct. Diagrams and Tables informed the scenario table;
no diagram is needed. The former package's history remains in
[its retirement record](change-workflow.md).
