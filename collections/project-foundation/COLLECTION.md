# Project foundation

Start with the project's instructions and existing document routes. Use this
entrypoint when choosing a workflow.
Its source repository's catalog and release/authoring rules are not prerequisites
for consumption. Follow provenance to the source only when the task needs source
maintenance, an upgrade or investigation of a concrete source issue.

For a project spanning repositories, read [multi-repository foundations](references/multi-repository.md)
before selecting document owners or installation locations.

Install this directory as one dependency. It contains the bootstrap workflow,
Git worktree guidance, project design and contracts, documentation and policy skills, source-of-truth,
their authoring skills and the templates they interpret. Preserve the directory
layout so relative references work.

| Task | Entry point |
| --- | --- |
| Interpret foundation declarations and inherited values | [Foundation format](references/foundation-format.md) |
| Start the project foundation | [Project bootstrap](skills/project-bootstrap/SKILL.md) |
| Shape architecture, responsibilities, workflows and integration choices | [Project design](skills/project-design/SKILL.md) |
| Read, apply, design or review handoff obligations | [Project contracts](skills/project-contracts/SKILL.md) |
| Start or resume edits and preserve repository work | [Git worktrees](skills/git-worktrees/SKILL.md) |
| Set phase-appropriate scope and review policy changes | [Project policy](skills/project-policy/SKILL.md) |
| Organize and reconcile project documents | [Project documentation](skills/project-docs/SKILL.md) |
| Keep authoritative decisions and their consumers aligned | [Source of truth](skills/source-of-truth/SKILL.md) |
| Write clear prose | [Clear writing](skills/clear-writing/SKILL.md) |
| Choose and design visual explanations | [Diagrams and tables](skills/diagrams-and-tables/SKILL.md) |
| Record an observed obstacle during work | [Friction capture](references/friction.md) |

Design selects responsibilities and relationships. Contracts define what participants
can rely on at a selected handoff. Diagrams and tables supplies the visual form for
either task. These are separate entry points, not a mandatory sequence; use only
the guidance the question needs.

Project work follows [foundation authority guidance](references/foundation-authority.md).
Edits in Git repositories use task worktrees unless repository-local instructions
explicitly opt out. Work outside Git proceeds directly. Bootstrap puts this rule
and the [Git worktrees route](skills/git-worktrees/SKILL.md) in project instructions
so it is visible before the first edit; installation alone does not activate it.

For a question about an existing document, consult its owner and relevant terms.
A literal wording edit that preserves meaning needs a focused edit check. Neither
task needs an authoring workflow merely because it involves prose. A replacement
that changes a decision or obligation still needs its governing workflow.

Use [shared authoring guidance](references/authoring.md) when composing or
restructuring explanations and instructions. Read only what the task needs;
installation does not require loading every entry point. Tool-specific references,
including Mermaid rendering guidance, are conditional on the selected work.

The [foundation template](templates/docs/foundation.md) has five fixed tables:
References, Inheritance, Boundaries, Overview and Policy. The
[format and interpretation](references/foundation-format.md) reference owns their
meaning; foundation files contain data only. The [README template](templates/README.md)
links the foundation.
Members declare inheritance and keep only local differences. Use the templates
through these skills. They deliberately omit the procedure for interpreting or
maintaining those facts. Blank cells mean unknown, never permission or a waiver.

For a project-local adoption, copy this whole directory to
`.agents/collections/project-foundation/`, record the source and full commit in
`.agents/collections/UPSTREAM.md`, and have bootstrap add explicit routes to the
entry points from the project's `AGENTS.md`, through its local foundation when
using a shared installation. If using an uncommitted draft, identify
it as a draft and record its base revision and local changes. Do not claim it
matches a committed release.

This layout supports explicit file routing from project instructions; it does not
claim that a client automatically discovers nested skills. A user-wide adoption
can use its chosen location and equivalent routing. This task establishes the
collection; it does not install it globally.
