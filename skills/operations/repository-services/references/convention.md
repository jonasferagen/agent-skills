# Repository service definitions

Use this convention when a project needs predictable discovery and operation of
named runtimes. Read the project's selected service owners and operating choices
first. For an existing service, follow its operating guide directly. A nearby
command, test or editor does not need promotion into a service merely to fit the
layout.

For discovery or inventory, use the existing service guide or the boundary criteria
below. Stop when the question is answered. Load service/runtime design guidance
only when defining or changing a service boundary or its controls.

## Choose the boundary

Start from a concrete capability that a person or another runtime needs to start,
stop and inspect as an identified instance. State its owner, inputs, outputs and
lifetime. A continuously maintained reader and an explicitly launched preview
can both have service definitions; they need different lifecycle and readiness
evidence. Interactive authoring tools retain their command workflows unless a
managed-instance requirement justifies a service boundary.

Two classes of service need different evidence, and a definition states which it
is. A **running** service holds a process while it serves: its readiness is a live
property, and `status` can ask the instance whether it is ready now. A
**scheduled** service holds no process between runs: a schedule is what is
installed, and each run is a finite job that finishes. A finite job alone is still
a command workflow; it becomes a scheduled service when the schedule itself has to
be started, stopped and inspected as an identified instance.

For a scheduled service, readiness is not a live property and must not be
reported as one. An installed schedule proves only that a run is intended, never
that one happened, so its evidence is the last run's durable outcome. The five
actions keep their names and apply to the schedule rather than to a run: `start`
installs and starts the schedule, `stop` stops and disables it without undoing
completed runs, `restart` re-applies it, `logs` shows the runs, and `status`
reports the schedule, the last run and the durable record of the last success
together. Reporting an active schedule without that record is the failure this
class invites, because an operator reads an active timer as a working backup.

A scheduled service is the one case where starting a service means it will later
act unattended. That follows from its class and needs no local exception; what
each guide owes instead is what an unattended run is allowed to touch, which
the `runtime-operations` skill owns.

A scheduled service also owns its own schedule units. The shared runtime helper
binds a running service: its `start` operates an installed unit without ever
installing one, and its `status` asks an instance whether it is ready now. For
this class `start` is what installs the schedule and readiness does not exist, so
a scheduled controller implements its own units rather than binding that helper.
That is the expected shape of the class, not a departure a guide must justify.

This skill owns this convention, templates, checks and documentation routes.
The [extension declaration](extension.md) defines adoption and discovery. Use the
`service-boundaries` and `runtime-operations` skills for boundary and runtime
design. Read both for a maintained-service transition; a narrow change follows
the relevant skill.
If that guidance is unavailable, report the missing owner and continue only work
that does not depend on it. This convention selects no process manager, transport,
hosting, database or automatic startup.

## Reuse the project's implementation conventions

When a project defines multiple services, select and record their common
implementation conventions in the existing architecture or repository-design
owner: stack, runtime controls, health/readiness interface and application
responsibility boundaries. Read that owner before implementing another service
and reuse its selected conventions. Explain departures and their concrete reason
in the affected design; similar services should not acquire separate control
implementations merely because they have different data sources.

Keep each service's identity, lifetime, dependencies and state explicit. Installed
and explicitly started services may use the same control machinery with different
settings. Application operations, transport adapters and startup have distinct
responsibilities; coherent small implementations need no identical file tree.
Use the project's installed service, application and language guidance for their
mechanics. This convention adds no universal stack, framework or health schema.
Existing services migrate through a scoped task that preserves their consumers
and operating guarantees; adding a service is not a project-wide rewrite trigger.

## Use a small home

Default to repository-relative `services/`:

```text
services/
  README.md
  control
  <name>/
    README.md
    control
```

`services/README.md` lists defined services and links their operating guides.
Each `services/<name>/README.md` owns its purpose, operational definition and
command route. Use lowercase names separated by hyphens. Use
`./services/control <name> start|stop|restart|status|logs` as the common entry point. `./services/control status`
without a name reports the whole project: this checkout and each checkout named in
the foundation References that has its own dispatcher, with `--scope checkout` to
narrow it to one. A declared member with no service home is reported as such rather
than omitted. Starting, stopping, restarting and logs always name one service, so
lifecycle changes stay explicit.

Reading is project-wide; starting and stopping stay checkout-local. A bare status
asks the installed checkout, found through the common Git directory, because a task
worktree owns no units or containers: its controllers would report instances that
were never created while the real ones run in the installed checkout. An explicit
`--root` still selects a checkout, and the mutating actions still run against the
checkout the command was invoked from.

Bare status reports and does not assert health. A service that is deliberately not
running, such as an unprovisioned environment or one that starts when asked, exits
nonzero while nothing is wrong, so each service's own exit code is shown and not
folded into a verdict. The aggregate exits nonzero only when a controller could not
be run at all, which is the one condition a reader cannot see in the rows. Action words are
therefore reserved and cannot name a service. The [dispatcher template](../templates/services/control)
finds executable `services/<name>/control` files and replaces itself with the
selected controller, forwarding the action and `--root`. Both entry points must
be executable. Each service controller accepts those five actions and an expected
checkout through `--root`; a mismatch must be visible before changing runtime
state. The controller implements the project's selected mechanism and language
and can delegate to existing controls. Keep application code in its existing home
unless a separate implementation decision moves it. Add runtime configuration or deployment
files only when the service needs them. Credentials and generated state retain
their declared external or ignored homes.

Copy and adapt the [index](../templates/services/README.md) and
[service guide](../templates/services/service/README.md) when no
adequate guide exists. Remove prompts and unneeded sections. The templates contain
no service-specific controller: implement and verify the selected mechanism
rather than shipping stub commands that appear operational. Do not create empty service trees
in repositories that have no defined services.

## Report one line per instance

A project-wide status is only read if it can be scanned. A controller's own `status`
output is written for someone asking about that one service, so an aggregate that
prints all of it buries a project in journals: one timer's status was forty-one
lines of the forty-six in a whole project's report.

So `status` has two forms. Asked with `--report`, a controller prints
`service-report/v1` lines, one per instance, and nothing else. Asked without it, it
prints what it has always printed, for the reader who is asking about that service.
The dispatcher asks for reports, renders a row from each, and asks again without the
flag when a controller reports nothing, so a partial adoption still appears. Its own
`--report` emits the lines instead of rows, for a consumer that is not a person.

Each line carries the service, the checkout, one state, and the rest only when they
exist: `endpoint`, `unit`, `detail`, `attention`. `service` is the name the
dispatcher discovered, or `service:instance` where one service holds several named
instances. `detail` is one short line, and `attention` is what a reader must act on,
so an aggregate can show what is owed without reading everything. Both are bounded
single lines; the long output stays with `status <name>`, which is what a reader asks
for next.

The state vocabulary is closed, so a reader learns seven words once and a consumer
never guesses at an eighth:

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
scheduled service never reports `ready`, because readiness is not a property it has;
an active schedule is `scheduled`, and what its row owes besides is the durable
record of the last success, as a `detail` and an `attention` when there is none. A
unit a reader might mistake for this checkout's reports `elsewhere` rather than
refusing, because a report is a reading and not an operation.

A service with no instance reports `absent` rather than inventing one. Assuming a
default instance is the failure this shape invites: one preview service reported a
unit that had never been created while its only started instance stayed invisible.

The `runtime-operations` skill owns the helper that builds and parses these lines, and the state a running service's unit maps to. A
controller that implements its own units builds its own line, and the helper
validates it.

## Connect the owners and evidence

Link the service index from the repository README and affected foundation or
design owner. Architecture decides responsibility and interfaces; the service
guide owns exact operating commands. Keep candidates explicitly proposed in their
design or planning owner, with the concrete need and next evidence required.
Adoption of this layout does not establish runtime readiness or authorize a
candidate's activation.

For each implemented definition, explain dependencies and checkout selection,
configuration, read and write locations, instance identity, readiness, logs and
failure recovery. Expose start, stop, restart, status and logs through its selected
controls. Startup and installation are separate actions. Follow the project's
runtime guidance for safe process ownership, timeout and cleanup behavior.

Exercise discovery from the repository entry point, an ordinary start/status case,
and a failure relevant to that instance. A successful unrelated listener or a
process that merely exists is insufficient readiness evidence. Report what was
exercised and what remains unverified. Existing layouts retain their routes until
deliberately migrated; preserve consumers and retained state when adopting this
default.

## Structured definitions

Projects can opt individual guides into [service-definition/v1](service-definition.md)
when they need comparable facts and browser inspection. Keep these facts in the
same guide and link the operating details and evidence. Unversioned guides remain
valid and discoverable; they have not adopted the structured format. The extension
owns the format; each repository owns its values and additional local documentation.

## Check an adopted service home

Run the bundled structural validator after creating or changing service definitions:

```sh
python3 <repository-services>/scripts/validate-services.py <service-home>
```

Select a home that adopts this convention, normally `services/`. Each immediate
subdirectory is a service definition. The check requires its guide and executable
controller, the index and executable dispatcher, lowercase hyphenated names that are not action words, and
inline Markdown index links targeting each service’s `README.md`. Symlinked
service entries are rejected, matching dispatcher discovery. An explicitly selected
missing or empty home fails; projects without selected services need no invocation
or empty tree. Existing layouts adopt this check only when they adopt the convention.

Exit 0 means these structural checks passed; exit 1 reports findings or unavailable
inspection. Findings identify the affected path. The checker never invokes controls,
reads credential sources or follows links to external roots. It checks only direct
inline index-to-guide routes, not reference-style links, anchors or arbitrary guide
links. Guide wording, action support, checkout enforcement, readiness and recovery
still need the selected review and runtime evidence above. Unversioned guides need no fixed headings. Declared structured definitions must
pass their format checks, including unique identities within the selected home.
A structural pass cannot establish operational compliance.
