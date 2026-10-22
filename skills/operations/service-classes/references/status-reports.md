# Status reports

Everything here is a recommended default. A project that already has its own
status words, report format or exit codes keeps them and maps each word onto the
meanings below; a project without them can use these as they stand. What is not
optional is set in the skill itself: a scheduled service never reports readiness
and reports its last run instead, and a deliberately stopped service is not a
fault.

A project-wide report, one listing covering every declared service, is only read
if it can be scanned. A controller's own status output is written for someone
asking about that one service, so a report that prints all of it buries the
project in log lines.

So a service's status has two forms. Asked for a report, a controller prints one
machine-readable line per instance and nothing else. Asked without that, it
prints its full status, for the reader who is asking about that one service.
How a controller is asked for the report form, such as a `--report` option, is
the project's choice. The project's status command, or whatever command the
project uses to list its services, calls each controller's report form, renders
a row from each line, and falls back to the full form when a controller prints no
report line, so a service that has not adopted the report form still appears.
Without such a command, run each controller's report form by hand.

Each line carries the service, the checkout (the path of the working copy the
controller ran from) and one state, and the rest only when
they exist: the service's lifecycle class, an endpoint, a unit, a detail and an
attention. The service is the name it was discovered under, or a
service-and-instance pair where one service holds several named instances. The
detail says in one short line what the state does not, and the attention is what
a reader must act on, so a report can show what is owed without printing
everything. Both are bounded single lines; the long output stays with the
question about one service, which is what a reader asks next. The line's field
names and encoding are the project's choice.

## The state vocabulary

The default state vocabulary is closed, so a reader learns seven words once and
a consumer never guesses at an eighth. Mapping a project's own words onto it
keeps that property:

| State | Meaning |
| --- | --- |
| `ready` | A running instance that answers ready now |
| `scheduled` | An installed, active schedule; a run is intended and none is held. Exits 0 only when the last run succeeded |
| `stopped` | Known here and deliberately not running |
| `absent` | Nothing installed or provisioned here to run, including a schedule that was never installed |
| `elsewhere` | The named unit or instance belongs to another checkout |
| `failed` | It ran, or was asked to run, and did not succeed; for a scheduled service, its last run failed |
| `unknown` | The controller could not determine the state |

A running service's readiness is live, so an active unit whose instance will not
answer reports `failed` and not `ready`: it was asked to serve and does not. A
scheduled service never reports `ready`, because readiness is not a property it
has; an active schedule is `scheduled`, and what its row owes besides is the
durable record of the last success, as its detail and as an attention when there
is none. `elsewhere` applies only when a project runs several working copies of the same
service on one machine: the controller compares the running unit's working
directory with its own checkout path and, when they differ, reports `elsewhere`
rather than refusing, because a report is a reading and not an operation. A
project with one working copy per machine skips this state.

A service with no instance reports `absent` rather than inventing a default
instance, which would hide the instances that were actually started.

## Report without asserting health

By default, a controller's status exits 0 only when its service is doing its job now: a
running instance is `ready`, or a scheduled service's schedule is active and its
last run succeeded. Every other case exits nonzero with the reason in its
detail, including `stopped` and `absent`, so a nonzero exit from one service is
not by itself a fault.

A project-wide report therefore shows each service's exit code beside its row
and does not fold them into a verdict: folding them would report a healthy
project as broken whenever something is deliberately stopped, and teach the
reader to ignore the report. The report itself exits nonzero only when a
controller could not be run at all, which is the one condition a reader cannot
see in the rows.

## Read widely, change one service at a time

Reading may cover the whole project; starting and stopping name one service in
one checkout, so lifecycle changes stay explicit. Ask for status from the
checkout whose units and containers actually run, not from another working copy
that never started them, or the report shows instances that do not exist while
the real ones stay invisible. A checkout that was named deliberately and has no
services is reported as such rather than omitted, because a reader cannot tell
silence from a checkout that was skipped by accident.

## Declare what a bulk start may touch

A state says what a service is doing; it cannot say what the service is.
`absent` is what an unprovisioned environment, an instance that was never named
and a unit that was never installed all report, so nothing in a row tells a
reader which of them a "start everything" command should act on.

So, by default, a controller declares its lifecycle class, in a second closed
vocabulary, on its report line:

| Lifecycle | What it is | A bulk start |
| --- | --- | --- |
| `maintained` | A running service kept up continuously because others expect it to be available | starts and stops it |
| `environment` | Infrastructure that someone sets up on purpose, once, because it costs money, holds data or is shared, such as a database or a cloud deployment | leaves it alone, and says so |
| `scheduled` | A schedule, installed by its own start, that later runs unattended | leaves it alone |
| `on-demand` | A running service started only when someone asks, under a name they choose, such as a dev server | leaves it alone |

`maintained` and `on-demand` are both running services; they differ in who
decides when an instance exists. `scheduled` is the lifecycle of every scheduled
service. The word appears in both vocabularies on purpose, because an installed
schedule is both what the service is and what it is currently doing. A controller that declares nothing is
unclassified, and a bulk start skips it rather than guessing. A reader reduces a
value outside the vocabulary to unclassified for the same reason, keeping the row
and discarding only the claim.

Whether a project has a bulk start, and what it is called, is the project's
choice. If it has one, it lives with whatever already lists the project's
services together, reads each report line's lifecycle, and calls the own start of
each `maintained` service; no one service's controller starts another's.
