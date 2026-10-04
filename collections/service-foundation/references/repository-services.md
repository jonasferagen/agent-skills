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
evidence. Finite jobs and interactive authoring tools retain their command
workflows unless a managed-instance requirement justifies a service boundary.

Service-foundation owns this convention, templates, checks and documentation
routes. The [extension declaration](extension.md) defines adoption and discovery.
Use [service boundaries](../skills/service-boundaries/SKILL.md) and
[runtime operations](../skills/runtime-operations/SKILL.md) for boundary and runtime
design. Read both for a maintained-service transition; a narrow change follows
the relevant member.
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
`./services/control <name> start|stop|restart|status|logs` as the common entry point. The [dispatcher template](../templates/repository-docs/services/control)
finds executable `services/<name>/control` files and replaces itself with the
selected controller, forwarding the action and `--root`. Both entry points must
be executable. Each service controller accepts those five actions and an expected
checkout through `--root`; a mismatch must be visible before changing runtime
state. The controller implements the project's selected mechanism and language
and can delegate to existing controls. Keep application code in its existing home
unless a separate implementation decision moves it. Add runtime configuration or deployment
files only when the service needs them. Credentials and generated state retain
their declared external or ignored homes.

Copy and adapt the [index](../templates/repository-docs/services/README.md) and
[service guide](../templates/repository-docs/services/service/README.md) when no
adequate guide exists. Remove prompts and unneeded sections. The templates contain
no service-specific controller: implement and verify the selected mechanism
rather than shipping stub commands that appear operational. Do not create empty service trees
in repositories that have no defined services.

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

## Check an adopted service home

Run the bundled structural validator after creating or changing service definitions:

```sh
python3 <collection>/scripts/validate-services.py <service-home>
```

Select a home that adopts this convention, normally `services/`. Each immediate
subdirectory is a service definition. The check requires its guide and executable
controller, the index and executable dispatcher, lowercase hyphenated names and
inline Markdown index links targeting each service’s `README.md`. Symlinked
service entries are rejected, matching dispatcher discovery. An explicitly selected
missing or empty home fails; projects without selected services need no invocation
or empty tree. Existing layouts adopt this check only when they adopt the convention.

Exit 0 means these structural checks passed; exit 1 reports findings or unavailable
inspection. Findings identify the affected path. The checker never invokes controls,
reads credential sources or follows links to external roots. It checks only direct
inline index-to-guide routes, not reference-style links, anchors or arbitrary guide
links. Guide wording, action support, checkout enforcement, readiness and recovery
still need the selected review and runtime evidence above. Adapted guides need no
fixed headings, and a structural pass cannot establish operational compliance.
