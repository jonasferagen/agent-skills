# Repository services pilot — 2026-10-04

Project-foundation 1.4.0 adds a conditional repository-service convention, index
and guide templates, and an executable dispatcher. Project design and bootstrap
route named-runtime work to it. Service-foundation retains boundary/runtime
ownership; the source change selects no process manager or deployment. The
convention was exercised with Forge's maintained docs browser and a design trace
of Game's explicitly launched preview.

## Scope and checks

The dispatcher discovers executable regular `services/<name>/control` files,
validates service/action selection and replaces itself with that controller,
forwarding `--root` and its exit status. Five isolated process-boundary tests
exercise another working directory, explicit checkout, unknown service/path,
unsupported action and unfinished/symlinked controller discovery. A disposable
mutation substituting the checkout failed both checkout-forwarding checks.

The complete source checker passed 87 tests across five suites, zero skipped,
plus package validation: 27 skills in six collections. Node 24 and the pinned
TypeScript dependency were present; npm installed the dependency from its cache
with scripts disabled. Initial sandboxed checks failed because GnuPG and Node
child execution lacked host permissions; the complete rerun with local execution
access passed. Inventory and diff checks passed. These results do not establish
live service behavior or native client discovery.

## Fresh-context routing trials

Four read-only trials used synthetic consumer fixtures outside this repository,
with installed project/service collections and an AGENTS hook. They executed no
controls and inspected no authoring repository. Counts below cover instruction,
source and template content reads, excluding file inventories and count-only
output. No read was truncated.

| Request | Content words | Observed outcome |
| --- | ---: | --- |
| Locate an existing reader's status command | 1,496 | Followed its guide; reported documented PID/checkout readiness without claiming a live check |
| Design a managed graphical preview | 10,218 | Reached design, service and runtime routes; kept scene readiness distinct from process existence |
| Classify a finite thumbnail command | 1,851 | Kept the command outside services; read an unnecessary boundary skill |
| Repeat finite-command classification after the route clarification | 1,467 | Same correct boundary; avoided the boundary skill, but still read an unnecessary service collection entry |

The existing-reader trial read AGENTS, foundation, project/service collection
entries, reader guide and status/evidence. The finite-command trials read AGENTS,
foundation, project collection, repository-services and service collection; the
first additionally read the reader guide and service-boundaries. Required
convention/owner reads supported their answers. Service design guidance was
unnecessary for the finite-command answer; the route now explicitly permits
stopping after inventory/classification. The remaining extra collection read is
a routing limitation, not evidence of selection reliability.

The preview trial read AGENTS, foundation, project collection/design,
repository-services, service collection/boundaries/runtime, reader guide,
status/evidence, authoring, project-policy/phase-and-scope, project-planning/next-step,
clear-writing, design/workflows, friction and the service installation reference
and manifest. It read targeted helper matches and then serviceControl.py in full.
Credential/backup material in runtime-operations was irrelevant to the preview.
The fixture omitted preview implementation, detailed architecture/planning owners,
phase facts and provenance, so the result remained a bounded proposal with those
limits. Source-home lookup did not leave the installed fixture.

The installed transient helper requires a TCP port and HTTP health; it cannot
manage graphical-preview readiness unchanged. Forge's Game candidate records
that limitation and calls for suitable process ownership and scene/session
readiness evidence. No HTTP endpoint was added merely to fit the helper. The
convention remains compatible with an independently implemented controller.

These exercised routes preserve current operating choices and keep finite jobs
out of the service scaffold. They establish the tested routes and helper limits,
not automatic client discovery or a verified Game preview. No release tag or
remote publication is part of this pilot.
