---
name: project-bootstrap
description: "Bootstrap a new project or a fresh repository with project boundaries, policy and a project overview, plus a README that links them. Use when establishing this starting foundation; ordinary implementation and documentation maintenance belong to their own workflows."
metadata:
  version: "3.0.0"
---

# Project bootstrap

Establish a small project foundation from the user's intent and available
evidence. The outcome is a repository ready for its next design or implementation
decision, with known scope and unresolved choices visible.

## Establish the starting point

Resolve the target directory and read applicable project instructions. Inspect
existing files and Git state before writing. A fresh start does not imply copying
an earlier implementation or adopting its technology and obligations. Use prior
projects as evidence only to the extent the user intends.

Use [Git worktrees](../git-worktrees/SKILL.md) before editing in a Git repository.
Outside Git, work directly unless repository creation is part of the task. If
creating a repository, initialize it and select a task worktree before writing
the foundation; the Git skill covers repositories without a first commit.
Honor an explicit repository-local worktree exception, including one for a
deliberately single-agent project. Do not infer an exception from the task's size.

Create a local Git repository when requested or included in the bootstrap scope.
Check whether the target already belongs to a repository before initializing one;
clarify an unintended nested repository. Preserve existing work. Select ignore
rules for the files actually expected, including local credentials. Configure a
remote, install dependencies or add a runtime only when the task calls for it.

## Establish the foundation

Determine whether this is an independent project, a shared foundation owner or
one of its members. Bootstrap each repository's entry point; members use
[multi-repository foundations](../../references/multi-repository.md) to declare
the parent, reference binding and local scope.

The default starter is `docs/foundation.md` with three sections, each containing
a compact table, plus a `README.md` that links it:

| Section | Owns |
| --- | --- |
| Boundaries | Purpose, responsibilities, exclusions and ownership |
| Overview | Current environment, resources, application choices and unresolved options |
| Policy | Concise operating facts and adopted decisions by axis |

Adapt the [foundation](../../templates/docs/foundation.md) and
[README](../../templates/README.md) templates. Preserve existing document homes
unless restructuring is requested; the three sections can also route to established
owners. Add a glossary only when ambiguous terminology needs its own home.
Merge useful routes into an existing README rather than replacing it.

A shared owner or independent project records its decisions in all three tables.
A member declares section inheritance and keeps only local rows; retain a header-only
table with “No local differences” when all values inherit. Remove unused template
rows from members: a present unknown is not the same as an omitted inherited row.
Keep detailed role assignments in their existing architecture owner and reference
them from boundaries. State the repository or environment scope of technical
choices so a shared owner's own implementation is not inherited by every member.

Keep the title, date/revision and section scope comments. Boundaries may add a
concise project-specific table when needed for actual ownership. Overview keeps
current choices and open options; policy keeps operating facts and adopted
constraints. Put procedures, work queues, skill routes, impact records and evidence
in their existing owners. The foundation may declare references and inheritance;
it does not contain the procedure for interpreting policy.

Policy owns operating facts and adopted constraints. Overview owns the
chosen mechanisms and open implementation options. For example, put a no-network
constraint in policy and a selected local database in overview, linking to the
constraint when relevant. A possible future mechanism does not adopt the policy
for that future use. Keep detailed architecture elsewhere once it is needed.

Fill from established decisions. Distinguish adopted scope, proposals and unknowns
where that difference matters. For a consequential unknown, explain what depends
on it and when it needs a decision. Ask now only if the current work depends on
the answer. A short statement that the subject is undecided is sufficient when
there is little evidence. Remove template prompts, example rows and unused
sections from the project output.

Keep implementation status separate from intended behavior. A local repository
does not establish local-only deployment, synthetic data or disposable state.
Keep existing obligations in force. Avoid inventing requirements, domain terms,
setup commands, architecture or a work queue to fill the template.

## Establish the collection and its routes

Use the complete [project-foundation collection](../../COLLECTION.md). The
scaffold and its interpreting skills are one dependency. A member may route to an
accessible shared installation; do not require a copy per repository. For a new project-local
adoption, copy the whole collection as described there; use an existing complete
installation when one is already selected. Preserve the user's chosen installation
scope and existing project instructions.

Read the [shared authoring guidance](../../references/authoring.md) and use
[project-policy](../project-policy/SKILL.md) to assess the initial facts and
[project-docs](../project-docs/SKILL.md) to establish reader routes. Keep the
initial result small: explicit unknowns are valid where facts are not known.
Do not reproduce those skills' instructions in the documents.

Merge a short foundation section into the project's `AGENTS.md`, routing through
the local foundation to the chosen installation and project files.
For external owners, bind a named reference once and use it as specified in the
multi-repository guidance. Keep the local entry link usable without that owner.
Include the consultation and
conflict rules from [foundation authority](../../references/foundation-authority.md):
keep a short operating summary visible, consult the relevant foundation owner
when a task depends on it, and check affected decisions before completion. Keep
proposals and implementation evidence distinct from adopted requirements.
It must also route:

- Before edits in a Git repository, use a task worktree and consult
  [Git worktrees](../git-worktrees/SKILL.md). Put the default itself in `AGENTS.md`,
  alongside the installed-skill route (through the local reference when shared).
  Only repository-local instructions
  can opt out; link any existing exception in those instructions instead of
  overwriting it.
  State that work outside Git proceeds directly and needs no repository merely
  to satisfy this rule. An upgrade must add or reconcile this hook explicitly.
- Initial scaffolding to this skill and document organization to project-docs.
- Prose and visual explanations to the collection's shared authoring guidance.
- Changes to purpose, responsibilities, terminology or operating circumstances to
  project-policy for a review of affected foundation decisions and consequences.
- Relevant facts and decisions to overview, boundaries and policy, with links
  from each operating-summary statement to its authoritative owner.
- Repeated definitions, inconsistent consumers and drift checks to source-of-truth.
- Observed obstacles or repeated workarounds to [friction capture](../../references/friction.md)
  at a natural checkpoint, using existing project notes. Ordinary successful work
  needs no capture pass. Put this trigger in project instructions so it is visible
  before the reference is loaded.

These routes are part of bootstrap's output: the sparse documents rely on the
skills to interpret them. Review triggers apply during authorized project work;
they do not start a watcher, scheduled task or full-project audit on every edit.

## Verify and hand back

Check the generated files for unsupported claims, leftover prompts and duplicate
owners. For members, verify reference resolution, inherited changes, explicit
unknowns, local scope, conflicts and missing authority as described in the
multi-repository guidance. Verify local links and run applicable documentation
checks, including
`git diff --check` when Git is available. Review the actual staged files before
any initial commit; include only the bootstrap's intended content.

Report the project path, files established, Git state, checks and next unresolved
decision. Report the collection location and verify the project instruction links to it. Do not describe the
scaffold as a working application or the documented requirements as verified
implementation.
