# The runtime helpers contract

A service controller does not drive a process manager directly. It binds one
service and asks for one action, through a small set of Python modules the
project's framework deploys: `serviceControl`, `serviceHealth`, `serviceReport`
and `credentialStore`, with a `runtimeApi` declaration beside
them. They are files in a deployed directory, not an installed package, so a
consumer must put that directory on `sys.path` before importing them.

This reference owns the contract and nothing else: how a consumer admits the
modules, what the two version numbers mean, what a project binding supplies, how
the actions behave, and what survives an update. The modules themselves are
deployed with the project's framework, which also chooses the process manager
and the secret store they bind. Read this contract instead
of inferring the surface from a deployed module's source, and treat it as what a
conforming deployment must offer.

## Who owns what

The project owns **discovery**: which deployed copy of these modules a repository
uses and how it finds that directory. A repository that holds the deployment can
derive it from its own root. A repository using another repository's deployment
resolves that owner through its existing declared route, and keeps that route in
the owner it already uses for cross-repository paths. This contract selects no
workspace layout and reads no project document.

Resolve a declared relative route against the document that declares it, not the
working directory a controller happens to run from. A route that works from the
repository root and fails from a service directory is the same defect either way,
and an absolute declared target hides it until someone makes the target relative.

The deployment owns **admission**: rejecting an unusable directory and refusing
an interface the caller was not written against. It ships one loader, which every
consuming repository copies verbatim next to its other tools and hands the
resolved directory:

```python
from service_runtime import load

load(runtime_operations, major=1)
import serviceControl
```

Deploy that loader verbatim and keep the project's discovery in its own function
or module, so a later refresh replaces only the loader. Each consumer then
performs the same check instead of writing its own. The loader must:

- accept either the directory the modules live in or the deployment root that
  contains it;
- refuse a missing directory, a file where that directory belongs, and a symbolic
  link at either the directory or the declaration;
- refuse a deployment that carries no declaration, naming it as predating this
  contract and requiring a re-pin rather than importing it hopefully;
- refuse an expected version that is not two integers, as a type error rather
  than by interpreting it;
- raise before it changes `sys.path`, so a failed check leaves no import path
  behind for a later `import serviceControl` to succeed against;
- name both the deployment's interface and the caller's requirement in a refusal;
- admit a Python import path and nothing else: it performs no discovery, installs
  nothing and starts no service.

## What the two numbers mean

The declaration states the interface the deployed modules offer, as a name and
two integers. Its **major** number changes when a module name, a function
signature or a `Service` field changes incompatibly. Its **minor** number rises
when compatible surface is added. A consumer names the version it was written
against: one written against 1.0 keeps working on 1.3, and one written against
1.3 refuses 1.0, because the surface it needs is absent.

A deployment declares those numbers where it ships the modules, and carries this
reference beside them. This installation offers `runtime-operations/1.2`, so a
consumer written against it calls `load(runtime_operations, major=1)`. A consumer
that reports its status needs `minor=1`, which is where `Service.name`,
`Service.endpoint` and the reporting `status` arrived, and `minor=2` to declare a
class, which is where `Service.lifecycle` arrived. The declaration remains
authoritative and a refusal names both sides; the deployment owns the check that
this sentence and that file do not disagree.

This interface is versioned separately from the skill's `metadata.version`. Prose
guidance and importable surface change for different reasons; a clarified
paragraph is not an interface event, and a new helper argument is not a guidance
event. Skill 3.0.0 moved the modules, the loader and their tests out of this
package to the framework that deploys them. The interface did not move with them:
it remains `runtime-operations/1.2`, no signature or field changed, and a
consumer already written against `major=1` needs no code change. What such a
consumer must revisit is discovery — the directory it resolves now belongs to the
deployment rather than to an installed copy of this skill.

## Transient argument compatibility

A transient `Service.command` is a literal argument vector, never a string for a
shell to parse. A service manager can expand expressions such as `${NAME}` in
that vector even where no shell runs, so a conforming deployment selects literal
handling at that boundary and verifies the values the child received. Where the
installed client cannot make that selection, starting or restarting a transient
service fails with setup guidance; there is no fallback that changes argument
interpretation. Check that capability before running a prerequisite, stopping an
existing instance or launching a unit. Status, stop, logs, an already-active
`start` and installed-service controls do not require it.

Which client capability that is, and which release introduced it, belongs with
the deployment, as does whatever escaping or literal-execution mode a project's
installed-service generators require; these modules generate none. An explicit
shell command retains the shell's own interpretation contract. A successful
import proves neither host capability nor live-service readiness. Keep secrets
out of command arguments and service definitions.

## Bind a service

A project binding supplies a `serviceControl.Service` and calls `control(service,
action)`. Which fields it sets is the binding's whole design, because an omitted
field is a choice rather than a default:

| Field | Set it | Leaving it out selects |
| --- | --- | --- |
| `unit` | Always. The name the process manager knows this service by, qualified so it cannot collide in the operator's manager. | Nothing; it is required. |
| `command` | For a transient service the control launches itself, as an argument vector. | An installed service: control delegates to the process manager and never installs, enables or upgrades it. |
| `directory` | Always, as the expected checkout. | No checkout comparison, so a service belonging to another checkout is operated as if it were this one. |
| `port` | For an HTTP service. | Readiness means only that the named service is active. |
| `health_service` | For an HTTP service, as the name its `/health` must report. | The plain-PID probe, kept for bindings not yet migrated. |
| `environment` | Non-secret settings a transient command needs. | An inherited environment. It is passed only when launching a transient service, never to an installed one. |
| `ready_seconds` | When 60 seconds is wrong for this service. | 60 seconds. It must be positive and finite. |
| `before_start` | When a prerequisite must be running first. | No prerequisite step. It does not run when `start` finds the service already active. |
| `name` | To report in the project-wide view, as the name a reader and that view know this service by. | A binding that cannot report: `control(..., reporting=True)` refuses rather than inventing a name. |
| `endpoint` | When a reader would open an address, as that address. | A report row that points at the unit instead. |
| `lifecycle` | To declare which class the service belongs to, as one of the report vocabulary's declared values. | An unclassified row: a consumer composing a project-wide launch skips it rather than guessing. |

A non-empty `command` requires a `port` between 1024 and 65535, and
`health_service` requires `directory`, because comparing the checkout is half of
what the probe proves. Setting `health_service` on an installed service that is
not loaded makes `start` report that the service is not installed, rather than
attempt a launch that cannot succeed. Keep secrets out of `environment` and
`command`: the launcher passes nothing to the process manager, and each command
fetches its own.

The actions behave as the operator contract requires, not as thin wrappers.
`status` prints the service's state and checkout, adds an HTTP readiness line
when a port is set, and exits non-zero when the service is not ready, so a script
can depend on it. `control(service, 'status', reporting=True)` prints one report
line instead of those, for the project-wide view, and keeps the same exit status;
only `status` reports. A service whose unit is held by another checkout reports
`elsewhere` there rather than refusing, because a report is a reading, and an
active service that will not answer readiness reports `failed` rather than
`ready`. `start` on an already-active service waits for readiness and reports
without replacing or stopping that instance. `stop` on a service that is not
loaded succeeds. Every action returns an exit status for the controller to pass
on, and reports a failure by raising rather than by returning one. A failed start
or readiness timeout stops only the selected service, and a failure during that
cleanup is reported separately so the original error survives. A checkout
mismatch is refused before anything changes state.

## Answer readiness

For an HTTP service, set `Service.health_service` and expose `/health` using
`serviceHealth`'s `service-health/v1` JSON envelope: `schema`, `service`, `pid`,
`checkout`, `status` and `details`. Return HTTP 200 for `ready` and 503 for
`degraded`, and include only bounded, non-sensitive diagnostics; the application
owns the meaningful dependency checks and its own detail fields. A response is
bounded, and an oversized body is refused rather than parsed.

The controller verifies the service name, the ready status, the reported process
identity against the manager's record for that service, membership of that
service's process group, and both the reported and the configured checkout. This
establishes readiness of the named instance at that moment, and not continuous
availability. A binding without `health_service` keeps the plain-PID probe until
it is deliberately migrated.

## Report one line

`control(service, 'status', reporting=True)` prints one line of the project's
declared service-report schema: the service as a reader and the project-wide view
know it, the checkout, one state, and `lifecycle`, `unit`, `endpoint`, `detail`
and `attention` where they exist. A binding that has not set `name` is refused
rather than given an invented one, and `detail` and `attention` are each held to
one bounded line. A controller that implements its own services, as a scheduled
service does, builds its line with the same module so the same validation
applies.

That schema and its closed state and lifecycle vocabularies have one owner
outside this contract: the `service-classes` skill, which states what each
state means and which class a project-wide launch may touch. Validate every
value against that owner; a controller may not invent a state or a class that
every consumer would then have to guess at.

## Limits

The loader performs no discovery, installs nothing, and starts no service. It
does not verify the deployment's source pin; the project's provenance record owns
that, and a passing version check is not evidence that the intended revision is
deployed. It admits a Python import path only: the modules remain files in a
deployed directory, and a non-Python controller calls its own commands.

Because an update replaces the whole deployed directory, every consumer importing
these modules is re-pointed at once. The version check makes an incompatible
replacement fail at the importing controller, with a message naming both sides,
instead of failing later inside a call. It cannot make such a replacement safe:
review the consumers a major change affects and exercise each affected
controller.

This contract states a surface, not an implementation. Which process manager
and secret store the deployed modules bind is the framework's
choice, and that choice carries its own prerequisites: a client capability, a
running manager, an installed credential tool, a container runtime. A conforming
deployment documents them where it ships the code, and keeps its own tests with
it, because this contract cannot establish that a deployment satisfies it.
