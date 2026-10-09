# Status reports

A project-wide status is only read if it can be scanned. A controller's own
status output is written for someone asking about that one service, so an
aggregate that prints all of it buries a project in journals: one timer's status
was forty-one lines of the forty-six in a whole project's report.

So a service's status has two forms. Asked for a report, a controller prints one
machine-readable line per instance and nothing else. Asked without that, it
prints what it has always printed, for the reader who is asking about that one
service. An aggregate asks for reports, renders a row from each, and asks again
for the plain form when a controller reports nothing, so a partial adoption still
appears.

Each line carries the service, the checkout and one state, and the rest only when
they exist: the service's class, an endpoint, a unit, a detail and an attention.
The service is the name it was discovered under, or a service-and-instance pair
where one service holds several named instances. The detail says in one short
line what the state does not, and the attention is what a reader must act on, so
an aggregate can show what is owed without printing everything. Both are bounded
single lines; the long output stays with the question about one service, which is
what a reader asks next.

The `service-report/v1` line's field names and encoding belong to the report
producer's interface contract, which the `runtime-operations` skill states. What
each state and each class means is owned here, and source maintenance checks the
two tables below against that producer.

## The state vocabulary

The state vocabulary is closed, so a reader learns seven words once and a
consumer never guesses at an eighth:

| State | Meaning |
| --- | --- |
| `ready` | A running instance that answers ready now |
| `scheduled` | An installed, active schedule; a run is intended and none is held |
| `stopped` | Known here and deliberately not running |
| `absent` | Nothing installed or provisioned here to run |
| `elsewhere` | The named unit or instance belongs to another checkout |
| `failed` | It ran, or was asked to run, and did not succeed |
| `unknown` | The controller could not determine the state |

A running service's readiness is live, so an active unit whose instance will not
answer reports `failed` and not `ready`: it was asked to serve and does not. A
scheduled service never reports `ready`, because readiness is not a property it
has; an active schedule is `scheduled`, and what its row owes besides is the
durable record of the last success, as its detail and as an attention when there
is none. A unit a reader might mistake for this checkout's reports `elsewhere`
rather than refusing, because a report is a reading and not an operation.

A service with no instance reports `absent` rather than inventing one. Assuming a
default instance is the failure this shape invites: one preview service reported
a unit that had never been created while its only started instance stayed
invisible.

## Report without asserting health

An aggregate status reports and does not assert health. A service that is
deliberately not running, such as an unprovisioned environment or one that starts
when asked, exits nonzero while nothing is wrong. So each service's own exit code
is shown and not folded into a verdict: folding them would report a healthy
project as broken every day and teach the reader to ignore the report. The
aggregate exits nonzero only when a controller could not be run at all, which is
the one condition a reader cannot see in the rows.

## Read the project, mutate one checkout

Reading is project-wide; starting and stopping stay checkout-local. A status
asked for the whole project is asked of the checkout that actually holds the
instances, not of the task worktree the command was run from: a worktree owns no
units or containers of its own, so its controllers would report instances that
were never created while the real ones run in the installed checkout. Starting,
stopping and restarting always name one service, so lifecycle changes stay
explicit. A checkout that was named deliberately and has no services is reported
as such rather than omitted, because a reader cannot tell silence from a checkout
that was skipped by accident.

## Declare what a project-wide launch may touch

A state says what a service is doing; it cannot say what the service is. `absent`
is what an unprovisioned environment, an instance that was never named and a unit
that was never installed all report, so nothing in a row tells a reader which of
them a "bring the project up" command should act on. Starting all of them is
wrong in three different ways: an environment is provisioned deliberately by its
own guide's words, an instance cannot be started without a name, and a schedule
is installed once and then means unattended runs.

So a controller declares its class, in a second closed vocabulary, as the
`lifecycle` key on its report line:

| `lifecycle` | What it is | A project-wide launch |
| --- | --- | --- |
| `maintained` | Kept running because the project expects it available | starts and stops it |
| `environment` | Provisioned deliberately, by its own guide's words | leaves it alone, and says so |
| `scheduled` | A schedule, installed once by its own start | leaves it alone |
| `on-demand` | An instance that cannot be started without a name | leaves it alone |

`scheduled` appears in both vocabularies deliberately: an installed schedule is
both what that service is and what it is currently doing. A controller that
declares nothing is unclassified, and a launch skips it rather than guessing. A
reader of these lines reduces a value outside the vocabulary to unclassified for
the same reason, keeping the row and discarding only the claim. This is how a
partial adoption stays visible instead of becoming wrong.

A project-wide launch is not an action on one repository's own controls. Reading
is project-wide and mutation is checkout-local, and a project-wide start would
contradict that, besides giving every repository authority over the others'
runtime state. A project that wants one command to bring its maintained set up
builds it where the repositories are already declared together, and composes the
named, checkout-local starts each repository already provides. The declared class
is what such a composer reads.
