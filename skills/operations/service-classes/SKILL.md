---
name: service-classes
description: "Decide whether a capability is a service and whether it is running or scheduled, and what each class owes as evidence: live readiness for one, the last run's durable outcome for the other. Use when promoting a command or job into a service, deciding what a scheduled service's status must report, or reading a status report that covers many services and looks like a failure; document homes, control commands, transports and runtime mechanics are not chosen here."
metadata:
  version: "1.1.0"
---

# Service classes

Decide whether a capability is a service, which class it belongs to, and what
that class owes as evidence. Follow the project's service conventions; if none
are documented, infer them from its compose files, unit files and scripts, state
the assumption and ask the user. For a service that already exists, follow its
operating guide directly.

This skill selects no process manager, hosting provider, transport, container or
database, and installing it starts nothing.

**Rules and defaults.** The rules are the distinctions themselves: a running
service and a scheduled service are different classes; a running service proves
live readiness, a scheduled service proves its last run's outcome and never
reports readiness; and a deliberately stopped service is not a fault. The state
words, lifecycle words, report-line fields and exit codes in this skill and in
[Status reports](references/status-reports.md) are recommended defaults. When a
project already has its own status vocabulary, keep it and map each of its words
onto these meanings; use these defaults only where it has none.

Terms used here:

- A **checkout** is one working copy of a repository on one machine; services
  started from it read its files.
- A **service definition** is whatever declares a service and how it runs, such
  as a compose service entry, a systemd unit, or a script with its guide. Where
  the project has none written down, infer it from those files and say so.
- A **controller** is the command that starts, stops, restarts and reports the
  status of one service, such as a script with `start`, `stop` and `status`
  subcommands, or the compose or systemctl commands its guide names. If no
  controller exists, say so and ask the user before writing one.
- An **instance** is one identified, separately started copy of a service, such
  as a dev server started under a name.
- A **unit** is whatever the host's process manager installs to run an instance
  or a schedule, such as a systemd unit or a container.
- A **project-wide report** is one status listing that covers every service the
  project declares, possibly across several repositories.
- A **recorded status** is a written field, in a service's guide or the project's
  list of services, saying what kind of readiness the service has (live, or none)
  and how far it has got: *proposed* (described, not built), *implemented* (built
  and runnable, not yet relied on) or *adopted* (the project depends on it). If
  the project keeps no such record, do not create one unasked; ask the user where
  it should live if one is needed.
- The **durable record of the last success** is something a scheduled job writes
  only when a run succeeds and that outlives the run, such as a timestamp file or
  a log line with the finish time.

| Task | Guidance |
| --- | --- |
| Decide whether a capability deserves a service definition | [Decide whether it is a service](#decide-whether-it-is-a-service) |
| Decide which class a service belongs to and what it must prove | [Two classes, two kinds of evidence](#two-classes-two-kinds-of-evidence) |
| Report one line per instance, or read the state and lifecycle vocabularies | [Status reports](references/status-reports.md) |
| Judge what a start, a status or an adoption has established | [Evidence a service owes](#evidence-a-service-owes) |

## Decide whether it is a service

Start from a concrete capability that a person or another runtime needs to start,
stop and inspect as an identified instance. State its owner, inputs, outputs and
lifetime. A nearby command, test or editor does not need promotion into a service
merely because the project has services, and interactive tools such as an editor or a
REPL keep their command workflows unless a managed-instance requirement justifies a service
boundary.

A finite job on its own is still a command workflow. It becomes a scheduled
service when the schedule itself has to be started, stopped and inspected as an
identified instance.

A local service remains a service: localhost does not remove lifecycle or
ownership questions. A continuously maintained documentation server and an
explicitly launched dev server can both be services; they owe different lifecycle and readiness
evidence.

To list a project's services, use its existing service guide or these criteria,
and stop when the question is answered.

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

A scheduled service's status exits 0 only when its schedule is active and its
last run succeeded. When the last run failed, it reports the state `failed`, a
detail saying when and why, and an attention giving the time of the last success
(or that there is none), and exits nonzero. An active schedule that has not yet
succeeded reports `scheduled` with that attention and exits nonzero. A schedule
that was never installed reports `absent`; one installed and then stopped
reports `stopped`. These are the default words and exit codes; the
full defaults are in [Status reports](references/status-reports.md).

A scheduled service is the one case where starting a service means it will later
act unattended; its class already implies that. What
each scheduled service owes instead is a written statement, in its guide or
definition, of what an unattended run may read, write, spend and delete, and
which preconditions it cannot check for itself; if the project has no place for
it, ask the user where it goes. A precondition only a person can guarantee, such
as an agreed maintenance window, stays out of the unattended run.

A scheduled service also owns its own schedule units. Controls written for a
running service operate an already installed unit and ask an instance whether it
is ready now. For a scheduled service, starting it is what installs the schedule
and readiness does not exist, so its controller implements its own units. That is
the expected shape of the class, not a departure a guide must justify.

## Reuse existing control conventions

When a project already has services, reuse its stack, runtime controls and
readiness interface for the next one, and explain any departure and its concrete
reason in the affected design. Keep each service's identity, lifetime,
dependencies and state explicit.

## Evidence a service owes

For each implemented service, explain its dependencies and which checkout it
runs from, its configuration, read and write locations, instance identity,
readiness, logs and failure recovery. Say how it is started, stopped, restarted,
inspected and read, and keep installation distinct from ordinary control.

A process that merely exists is not readiness evidence, and neither is a
successful unrelated listener. Check that the service can be found from where the
project lists its services (its README, service list or status command), then
exercise an ordinary start and status case and a failure relevant to that
instance.
Report what was exercised and what remains unverified.

Writing a guide or a definition establishes no readiness and starts nothing; a
proposed service stays proposed until that evidence exists.

Keep a recorded status separate from live readiness: a recorded status is a
statement about implementation and adoption, never an inferred health claim. A
scheduled service has no live readiness, so record its readiness as none, not
unknown, and report its last run instead. (`unknown` is a report state meaning
the status could not be determined; it is never a recorded value.) Do not invent evidence to fill a field.

## Neighbouring decisions

Service ownership and interfaces, shared behavior across transports, credentials and lifecycle
controls follow the project's own boundary and operating guidance; the
service-design skill covers service interfaces and storage ownership, and where
it is not installed those decisions are the project's. If a necessary
operating contract is unavailable, report that gap and continue work that does
not depend on it. A literal text correction or an ordinary pure-function change
does not need service review unless it changes these boundaries.
