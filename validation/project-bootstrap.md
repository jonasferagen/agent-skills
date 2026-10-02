# Validation — Project bootstrap

## Git worktree default — 3 October 2026

Unreleased version 2.0.0 applies the collection's Git worktree rule before
repository edits and installs the rule and skill link in generated instructions.
Existing repository-local exceptions remain authoritative. A directory outside
Git does not acquire a repository unless creating one is within the task.

The [Git worktrees validation](git-worktrees.md) records the shared behavior and
practical trials. Earlier bootstrap results below predate this default.

## Collection adoption — 2 October 2026

The current entry point belongs to the project-foundation collection. See
[collection validation](project-foundation-collection.md) for the shared templates,
required authoring guidance and policy review behavior. Earlier standalone-package
and template-copy results below describe the previous structure.

## Draft scope — 2 October 2026

The first draft captures starting a local repository and establishing three
project definitions, with a README linking them. The package location and bundled
templates are the maintained home. User-wide installation and reorganization of the
companion skills remain separate decisions.

The assets are copied from the local `project-foundation` repository's
`templates/` tree at commit `800398dbddb09d80ce2b0cc4275becb2b5e4c691`.
On 2 October 2026 the owner authorized retiring the source repository after
verification of the port. All four template files matched byte for byte. The
source's template directory was removed and its README now points here. Its Git
history, adoption review, project-docs trial and Atlas sample remain as historical
evidence in the retired repository. Maintain reusable templates in this package.

## Responsibilities to review

Bootstrap owns the starting layout and coordinates available guidance.
Project-policy retains the requirements workflow; project-docs retains document
organization and reconciliation. Clear-writing and diagrams-and-tables remain
general authoring skills. Their presence is optional for this package.

The policy asset is an initial profile and unknowns scaffold. The fuller
project-policy template remains useful for that skill's independent operation;
using both skills must populate one project policy owner. Whether to consolidate
template maintenance belongs in the subsequent packaging review.

The existing repository instructions recommend project-local imports. This draft
leaves installation scope to the user's request and changes no installation.

## Behavioral scenarios

| Request and context | Expected outcome |
| --- | --- |
| Bootstrap a new project with only a name and target directory | Establish the requested foundation with explicit unknowns; invent no stack or product scope. |
| Apply the foundation to a fresh repository that already has a README and initial commit | Preserve history and useful README content; add the definitions and routes. |
| Target directory is inside another repository | Establish whether a separate nested repository is intended before initializing it. |
| Earlier implementations exist beside the target | Treat them as references within the requested scope; copy no application or private data automatically. |
| Bootstrap is installed without its companions | Produce an honest initial foundation from bundled resources, without broken external links or claims of specialist review. |
| Bootstrap and project-policy are both available | Establish one policy at the chosen path; avoid a competing root policy file. |
| User requests README only | Honor the narrower output; do not impose three additional files. |
| User requests foundation plus selected project-local skill imports | Import complete packages from known revisions with provenance; keep project decisions outside them. |
| User mentions possible user-wide installation later | Keep that as a pending decision; do not install globally. |
| Fix a typo in an established README | Use ordinary editing guidance; do not bootstrap the project again. |

## Evidence and limits

Author review applied clear-writing, including its instruction guidance, to keep
defaults distinct from requirements and selection distinct from installation.
Diagrams-and-tables guidance informed the file ownership and companion tables.
No diagram was needed. Pattern-capture informed the scope: this has its own
starting-project trigger, while existing specialist workflows retain their homes.

Checks run on 2 October 2026:

- Repository package validation passed for all 21 packages.
- The skill-creator manifest validator passed for project-bootstrap.
- An isolated copy contained the four expected files and four working local
  links. It matched the source templates byte for byte, staged cleanly in a
  temporary Git repository and passed the staged whitespace check.
- `git diff --check` passed for the authoring repository.

Behavioral scenarios above are expectations, not independent agent trials.
The Atlas repository has not adopted the foundation as part of this skill draft.

## Policy output scope — 3 October 2026

Author review: the policy scaffold retains a scope comment and a single blank
axis table. Bootstrap now routes interpretation to project-policy and assigns
working rules and impact records to their own homes. Forge provided the observed
failure: working rules and three transition reports accumulated despite the sparse
template. This change does not constitute a fresh independent bootstrap trial.

## Boundary output scope — 3 October 2026

Author review against Forge: preserve the core template table and its local
ownership table; remove earlier-work narrative and duplicated lifecycle/status
prose. Current Library uncertainties belong in overview; source-preservation and
import rules already have policy and instruction owners. A new project receives
only the core table and a scope comment, with no mandatory historical section or
Forge-specific ownership rows. This is a focused editorial review and package
check, not an independent bootstrap trial.

## Overview output scope — 3 October 2026

Focused author review against Forge: overview retains six technical-choice rows;
next-task details move to workspace notes, skill routes stay in AGENTS, and the
existing workspace index locates evidence. The scaffold no longer includes First
useful slice, which invited a work queue into the definition. Unknown technical
options remain valid table content; a next implementation task belongs elsewhere.
Package/link checks apply; no independent behavioral trial was run for this edit.
