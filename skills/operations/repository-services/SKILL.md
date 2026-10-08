---
name: repository-services
description: "Define, document and check a repository's named services: the services/ home, per-service guides, the control dispatcher and the structural validator. Use when adopting the service convention, adding a service definition or its scheduled class, or reporting project-wide status; boundary and runtime design are separate skills."
metadata:
  version: "0.3.1"
---

# Repository services

Give a project predictable discovery and operation of its named runtimes. Read
the project's selected service owners and operating choices first. For an
existing service, follow its operating guide directly; a nearby command, test or
editor does not need promotion into a service merely to fit the layout.

| Task | Guidance |
| --- | --- |
| Adopt service document homes and their checks in a project | [Service extension](references/extension.md) |
| Choose whether a capability is a running or scheduled service, and define its guide and controls | [Repository service convention](references/convention.md) |
| Report one line per instance project-wide, or read the state vocabulary | [Report one line per instance](references/convention.md#report-one-line-per-instance) |
| Declare which services a project-wide launch may start and stop | [Declare what a project-wide launch may touch](references/convention.md#declare-what-a-project-wide-launch-may-touch) |
| Opt a guide into comparable structured facts | [Structured service definition](references/service-definition.md) |
| Check an adopted service home | `python3 scripts/validate-services.py <service-home>` |

Copy and adapt the [index](templates/services/README.md),
[service guide](templates/services/service/README.md) and
[dispatcher](templates/services/control) when no adequate guide or entry point
exists. Remove prompts and unneeded sections. The templates contain no
service-specific controller: implement and verify the selected mechanism rather
than shipping stub commands that appear operational.

A local service remains a service: localhost does not remove lifecycle or
ownership questions. A scheduled service is a service too: having no listener
removes readiness, not lifecycle or ownership. This skill selects no process
manager, hosting provider, transport, container or database, and installing it
starts nothing.

Use the `service-boundaries` skill to decide service ownership and shared
behavior across transports, and the `runtime-operations` skill for credentials,
lifecycle controls, the Python helpers a controller imports and the rules an
unattended run follows. Read both for a maintained-service transition; a narrow
change follows the relevant skill. If that guidance is unavailable, report the
missing owner and continue only work that does not depend on it.

A literal text correction or ordinary pure-function change does not need service
review unless it changes these boundaries. Project policy, application internals,
language conventions and test design retain their project-selected guidance.
