# Project foundation

Install this directory as one dependency. It contains the bootstrap workflow,
project documentation and policy skills, source-of-truth, their authoring skills,
and the templates they interpret. Preserve the directory layout so relative
references work.

| Task | Entry point |
| --- | --- |
| Start the project foundation | [Project bootstrap](skills/project-bootstrap/SKILL.md) |
| Interpret policy facts and review changed circumstances | [Project policy](skills/project-policy/SKILL.md) |
| Organize and reconcile project documents | [Project documentation](skills/project-docs/SKILL.md) |
| Keep authoritative decisions and their consumers aligned | [Source of truth](skills/source-of-truth/SKILL.md) |
| Write clear prose | [Clear writing](skills/clear-writing/SKILL.md) |
| Choose and design visual explanations | [Diagrams and tables](skills/diagrams-and-tables/SKILL.md) |

Project work follows [foundation authority guidance](references/foundation-authority.md).
The project skills also use [shared authoring guidance](references/authoring.md).
Read only the guidance needed for the task; installation does not require loading
every entry point. Tool-specific references, including Mermaid rendering guidance,
remain with the visual skill and are loaded when needed.

The [templates](templates/README.md) hold project facts and decisions. Use them
through these skills. They deliberately omit the procedure for interpreting or
maintaining those facts. Blank cells mean unknown, never permission or a waiver.

For a project-local adoption, copy this whole directory to
`.agents/collections/project-foundation/`, record the source and full commit in
`.agents/collections/UPSTREAM.md`, and have bootstrap add explicit routes to the
entry points in the project's `AGENTS.md`. If using an uncommitted draft, identify
it as a draft and record its base revision and local changes. Do not claim it
matches a committed release.

This layout supports explicit file routing from project instructions; it does not
claim that a client automatically discovers nested skills. A user-wide adoption
can use its chosen location and equivalent routing. This task establishes the
collection; it does not install it globally.
