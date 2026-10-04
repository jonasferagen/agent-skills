# Service foundation

Version: 0.1.0

Use this collection when designing a service boundary or changing how a service
runs. Begin with the project's current owners and operating choices. Install the
whole collection; load only the members needed by the task.

| Task | Guidance |
| --- | --- |
| Promote a spike to a maintained service | Read both [service boundaries](skills/service-boundaries/SKILL.md) and [runtime operations](skills/runtime-operations/SKILL.md); identify changed reliance, lifecycle and acceptance evidence in the project's existing owners |
| Change service ownership or an HTTP/MCP operation | [Service boundaries](skills/service-boundaries/SKILL.md) |
| Change startup, shutdown, readiness, process identity, credentials or recovery tooling | [Runtime operations](skills/runtime-operations/SKILL.md) |
| Install, update or check this collection | [Installation and maintenance](references/installation.md) |

A local service remains a service: localhost does not remove lifecycle or ownership
questions. Installing this collection does not select a process manager, hosting
provider, extra transport, container or database. Preserve explicit project choices
when applying member defaults; record a scoped difference in the project's owner.
A maintained service need not inherit a disposable preview's lifetime.

A literal text correction, browser styling edit or ordinary pure-function change
does not need service review unless it changes these boundaries. Follow its existing
owner directly. When a task crosses both service and runtime responsibilities, read
both members before implementation; do not stop at the first matching row.

Project policy, application internals, language conventions and test design retain
their project-selected guidance. Missing external guidance does not waive an
obligation or require loading a source catalog. Report the specific missing owner
and continue work that does not depend on it. Ordinary consumption does not require
the installation guide or the authoring repository.
