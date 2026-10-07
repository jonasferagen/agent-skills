# Use the runtime helpers

[Runtime operations](../SKILL.md) ships Python helpers
that service controllers import: `serviceControl`, `serviceHealth`,
`credentialStore` and `databaseBackup`. They are files in an installed
skill directory, not an installed package, so a consumer must put their directory on
`sys.path` before importing them. This reference owns how, what a project binding
supplies once they are importable, and what the skill guarantees across an
update.

## Who owns what

The project owns **discovery**: which installed copy of this skill a repository
uses and how it finds that directory. A repository that holds the installation can derive
it from its own root. A repository using another repository's installation
resolves that owner through its existing declared route, and keeps that route in
the owner it already uses for cross-repository paths. The skill selects no
workspace layout and reads no project document.

Resolve a declared relative route against the document that declares it, not the
working directory a controller happens to run from. A route that works from the
repository root and fails from a service directory is the same defect either way,
and an absolute declared target hides it until someone makes the target relative.

The skill owns **admission**: rejecting an unusable directory and refusing
an interface the caller was not written against. Copy
[the loader](../templates/service_runtime.py) into the
repository that runs services and give it the resolved directory:

```python
from service_runtime import load

load(runtime_operations, major=1)
import serviceControl
```

Deploy it verbatim, as with the services dispatcher; keep the project's
discovery in its own function or module so a later refresh replaces only the
loader. Each consumer then performs the same check instead of its own.

## What the two numbers mean

[The declaration](../scripts/runtimeApi.py) states the
interface the installed helpers offer. Its **major** number changes when a module
name, a function signature or a `Service` field changes incompatibly. Its
**minor** number rises when compatible surface is added. A consumer names the
version it was written against: one written against 1.0 keeps working on 1.3,
and one written against 1.3 refuses 1.0, because the surface it needs is absent.

This installation offers `runtime-operations/1.1`, so a consumer written against
it calls `load(runtime_operations, major=1)`. A consumer that reports its status needs
`minor=1`, which is where `Service.name`, `Service.endpoint` and the reporting
`status` arrived. [The declaration](../scripts/runtimeApi.py)
remains authoritative and a refusal names both sides; a bundled test keeps this
sentence and that file from disagreeing.

This interface is versioned separately from the skill's `metadata.version`. Prose guidance and importable surface change for
different reasons; a clarified paragraph is not an interface event, and a new
helper argument is not a guidance event.

A refusal raises before `sys.path` changes, naming both the installation's
interface and the caller's requirement. That ordering is the point: a failed
check must not leave an import path behind for a later `import serviceControl`
to succeed against. An installation predating this declaration is reported as
such and must be re-pinned before use rather than imported hopefully.

## Bind a service

A project binding supplies a `serviceControl.Service` and calls `control(service,
action)`. Which fields it sets is the binding's whole design, because an omitted
field is a choice rather than a default:

| Field | Set it | Leaving it out selects |
| --- | --- | --- |
| `unit` | Always. The user unit name, qualified so it cannot collide in the operator's manager. | Nothing; it is required. |
| `command` | For a transient service the control launches itself, as an argument vector. | An installed unit: control delegates to `systemctl --user` and never installs, enables or upgrades it. |
| `directory` | Always, as the expected checkout. | No checkout comparison, so a unit belonging to another checkout is operated as if it were this one. |
| `port` | For an HTTP service. | Readiness means only that the named unit is active. |
| `health_service` | For an HTTP service, as the name its `/health` must report. | The plain-PID probe, kept for bindings not yet migrated. |
| `environment` | Non-secret settings a transient command needs. | An inherited environment. It is passed only when launching a transient unit, never to an installed one. |
| `ready_seconds` | When 60 seconds is wrong for this service. | 60 seconds. It must be positive and finite. |
| `before_start` | When a prerequisite must be running first. | No prerequisite step. It does not run when `start` finds the service already active. |
| `name` | To report in the project-wide view, as the name the dispatcher discovered. | A binding that cannot report: `control(..., reporting=True)` refuses rather than inventing a name. |
| `endpoint` | When a reader would open an address, as that address. | A report row that points at the unit instead. |

A non-empty `command` requires a `port` between 1024 and 65535, and
`health_service` requires `directory`. Setting `health_service` on an installed
unit that is not loaded makes `start` report that the service is not installed,
rather than attempt a launch that cannot succeed. Keep secrets out of `environment` and `command`: the launcher passes
nothing to systemd, and each command fetches its own.

The actions behave as the operator contract requires, not as thin wrappers.
`status` prints the unit's state and checkout, adds an HTTP readiness line when a
port is set, and exits non-zero when the service is not ready, so a script can
depend on it. `control(service, 'status', reporting=True)` prints one
`service-report/v1` line instead of those, for the project-wide view, and keeps
the same exit status; only `status` reports, and
the `repository-services` skill owns the contract and its states.
A unit held by another checkout reports `elsewhere` there rather than refusing,
because a report is a reading, and an active unit that will not answer readiness
reports `failed` rather than `ready`. `start` on an already-active service waits for readiness and
reports without replacing or stopping that instance. `stop` on a unit that is not
loaded succeeds. Every action returns an exit status for the controller to pass
on, and reports a failure by raising rather than by returning one. A failed start or readiness timeout stops only the selected
unit, and a failure during that cleanup is reported separately so the original
error survives. A checkout mismatch is refused before anything changes state.

## Limits

The loader performs no discovery, installs nothing, and starts no service. It
does not verify the skill's source pin; the project's provenance record
owns that, and a passing version check is not evidence that the intended
revision is installed. It admits a Python import path only: helpers remain files
in a vendored directory, and a non-Python controller calls its own commands.

Because an update replaces the whole installed directory, every consumer importing these helpers is re-pointed at once. The version check
makes an incompatible replacement fail at the importing controller, with a
message naming both sides, instead of failing later inside a helper call. It
cannot make such a replacement safe: review the consumers a major change affects
and exercise each affected controller.
