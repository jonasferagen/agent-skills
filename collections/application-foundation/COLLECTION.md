# Application foundation

Version: 0.1.1

Design the inside of an application from a concrete operation: behavior, state,
dependencies and the boundaries that need verification. Start from project
instructions and existing architecture. This collection works without a specific
language, framework or companion collection.

| Task | Entry point |
| --- | --- |
| Turn a workflow into application operations, or change their responsibilities | [Application design](skills/application-design/SKILL.md) |
| Design an operation that calls an external provider | Application design, then its [external integration reference](skills/application-design/references/external-integrations.md) |
| Install or update this collection and select companion guidance | [Installation](references/installation.md) |

Use existing document owners for questions and literal wording edits; they need
no application-design pass. Project-wide responsibilities and handoff agreements
remain with the project's architecture and contract workflows. Language-specific
code conventions and deployment procedures enter when the task reaches them.

Read only the route needed by the task. Installation and source-maintenance
material are not prerequisites for ordinary use.

When an application task introduces a service boundary, lifecycle controls or
maintained service use, follow the project's service-guidance route before
implementation. If that route or installation is missing, identify the gap and
its consequence; do not silently treat core application design as service/runtime
coverage. Pure application logic and literal edits do not need this route.
