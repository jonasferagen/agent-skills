---
name: service-classes
description: "Decide whether a capability is a service and whether it is running or scheduled, and what each class owes as evidence: live readiness for one, the last run's durable outcome for the other. Use when promoting a command or job into a service, deciding what a scheduled service's status must report, or reading a project-wide status that looks like a failure; document homes, control commands, transports and runtime mechanics belong to other owners."
metadata:
  version: "1.0.0"
---

# Service classes

Decide whether a capability is a service, which class it belongs to, and what
that class owes as evidence. Read the project's own service owners and operating
choices first. For a service that already exists, follow its operating guide
directly.

Where service documents live, what the controls are called and how a project-wide
report is invoked are the consuming project's claims, not this skill's. This
skill selects no process manager, hosting provider, transport, container or
database, and installing it starts nothing.

| Task | Guidance |
| --- | --- |
| Decide whether a capability deserves a service definition | [Decide whether it is a service](#decide-whether-it-is-a-service) |
| Decide which class a service belongs to and what it must prove | [Two classes, two kinds of evidence](#two-classes-two-kinds-of-evidence) |
| Report one line per instance, or read the state and class vocabularies | [Status reports](references/status-reports.md) |
| Judge what a start, a status or an adoption has established | [Evidence a service owes](#evidence-a-service-owes) |

## Decide whether it is a service

Start from a concrete capability that a person or another runtime needs to start,
stop and inspect as an identified instance. State its owner, inputs, outputs and
lifetime. A nearby command, test or editor does not need promotion into a service
merely because the project has services, and interactive authoring tools retain
their command workflows unless a managed-instance requirement justifies a service
boundary.

A finite job on its own is still a command workflow. It becomes a scheduled
service when the schedule itself has to be started, stopped and inspected as an
identified instance.

A local service remains a service: localhost does not remove lifecycle or
ownership questions. A continuously maintained reader and an explicitly launched
preview can both be services; they owe different lifecycle and readiness
evidence.

For discovery or inventory, use the existing service guide or these criteria, and
stop when the question is answered.

## Two classes, two kinds of evidence

A service definition states which of two classes it is, because the two owe
different evidence.

A **running** service holds a process while it serves. Its readiness is a live
property, so its status can ask the instance whether it is ready now.

A **scheduled** service holds no process between runs. A schedule is what is
installed, and each run is a finite job that finishes. Readiness is not a live
property for this class and must not be reported as one. An installed schedule
proves only that a run is intended, never that one happened, so its evidence is
the last run's durable outcome.

The same operations apply to a scheduled service, against the schedule rather
than against a run. Starting it installs and starts the schedule. Stopping it
stops and disables the schedule without undoing completed runs. Restarting it
re-applies the schedule, its logs show the runs, and its status reports the
schedule, the last run and the durable record of the last success together.
Reporting an active schedule without that record is the failure this class
invites, because an operator reads an active timer as a working backup.

A scheduled service is the one case where starting a service means it will later
act unattended. That follows from its class and needs no local exception. What
each scheduled service owes instead is a statement of what an unattended run may
touch, which the `runtime-operations` skill owns.

A scheduled service also owns its own schedule units. A control binding written
for a running service operates an installed unit without ever installing one, and
its status asks an instance whether it is ready now. For a scheduled service,
starting it is what installs the schedule and readiness does not exist, so its
controller implements its own units rather than binding that helper. That is the
expected shape of the class, not a departure a guide must justify.

## Keep one set of control conventions

When a project defines several services, reuse the implementation conventions it
has already selected: stack, runtime controls, the health or readiness interface,
and the boundary between application responsibility and startup. Read the owner
of those choices before implementing another service. Explain a departure and its
concrete reason in the affected design; similar services should not acquire
separate control implementations merely because they have different data sources.

Keep each service's identity, lifetime, dependencies and state explicit.
Installed and explicitly started services may use the same control machinery with
different settings. Application operations, transport adapters and startup have
distinct responsibilities, and coherent small implementations need no identical
file tree. Existing services migrate through a scoped task that preserves their
consumers and operating guarantees; adding a service is not a project-wide
rewrite trigger.

## Evidence a service owes

For each implemented service, explain its dependencies and checkout selection,
configuration, read and write locations, instance identity, readiness, logs and
failure recovery. Say how it is started, stopped, restarted, inspected and read,
and keep installation distinct from ordinary control.

A process that merely exists is not readiness evidence, and neither is a
successful unrelated listener. Exercise discovery from the project's entry point,
an ordinary start and status case, and a failure relevant to that instance.
Report what was exercised and what remains unverified.

Adopting a layout, writing a guide or installing this skill establishes no
runtime readiness and authorizes no candidate's activation. Keep a candidate
service explicitly proposed, with the concrete need and the next evidence
required, until that evidence exists.

Where a project records a service's facts so that several services can be
compared, keep a documented status separate from live readiness: a recorded
status is a scoped statement about implementation and adoption, never an inferred
health claim. Record a scheduled service's readiness as none rather than unknown,
because readiness is not a property this class has; none is the honest value
there, not a gap to be filled. Route each fact to the owner that already holds
the detail instead of copying commands, and do not invent evidence to fill a
field. The format such a record takes is the consuming project's claim.

## Neighbouring owners

Service ownership, shared behavior across transports, credentials and lifecycle
controls follow the project's adopted boundary and operating guidance. A
maintained-service transition needs evidence for the relevant responsibilities;
a narrow change follows only the guidance its behavior touches. If a necessary
operating contract is unavailable, report that gap and continue work that does
not depend on it.

A literal text correction or an ordinary pure-function change does not need
service review unless it changes these boundaries. Project policy, application
internals, language conventions and test design retain their project-selected
guidance.
