# Project Docs

A reusable skill for understandable, maintainable repository documentation:
shared vocabulary, clear ownership, useful relationship diagrams and focused
project instructions.

The installable unit is [skills/project-docs](skills/project-docs/SKILL.md).
It supports establishing a documentation set, reviewing an existing one, and
reconciling it after changes. Its references cover
[structure](skills/project-docs/references/structure.md),
[diagrams](skills/project-docs/references/diagrams.md), and a
[synthetic worked example](skills/project-docs/references/worked-example.md).

## Use and adoption

Example requests after installation:

- “Use $project-docs to establish documentation for this repository.”
- “Use $project-docs to review our glossary, architecture diagrams and instructions.”
- “Use $project-docs to reconcile the docs after this release.”

For a repository-local import, copy the complete `skills/project-docs/` directory
to the target's `.agents/skills/project-docs/` through its normal review process.
Record this repository URL and the exact source commit in the target's provenance
notes. On updates, review the diff and preserve any documented local adaptations.
Keep target-specific instructions outside the imported directory where practical.

Creating this repository does not install the skill globally or into another
project. Adoption into Personal is a separate next step.

## Scope

This skill adapts to the project's existing documentation. It does not prescribe
a technology stack, access model, Git merge policy, deployment procedure or fixed
folder tree. It does not publish documents or operate external services.

## Origin and validation

Developed from a documentation review and cleanup in Personal on 2026-09-19.
The reusable guidance is newly written; no account details, credentials, service
identifiers or private domain records are included. The worked example is synthetic.
The source project credited Forge Agent Kit and Diátaxis as earlier influences;
this package contains no copied upstream skill files.

See [validation scenarios](validation/scenarios.md) for the intended behavior and
scope boundaries. The first version still needs experience in a second real project.
