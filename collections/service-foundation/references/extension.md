# Service extension

Service-foundation owns repository service definitions, their documentation and
control conventions, and service boundary and runtime guidance. It can be used
with a project's own instructions or adopted as an optional project-foundation
extension. Its tools and guidance require no project-foundation installation.

## Scope and document ownership

Adopt this convention for repositories that define named runtimes needing
explicit lifecycle controls. The project selects which capabilities qualify;
finite jobs, editors and ordinary commands need no service definition merely
because this collection is installed. Existing service guides remain the entry
for ordinary operation. Boundary and runtime design follow the task routes in
[the collection](../COLLECTION.md).

The [repository service convention](repository-services.md) is authoritative for
the default `services/` home, its index, per-service guide, controller interface,
templates and required explanations. These are extension-managed documents with
repository-owned content. Guides can link additional repository-defined operating
procedures and evidence. Project architecture retains responsibilities and
interfaces; the service guide retains the exact operational definition. Do not
copy policy, architecture or changing facts into a second owner.

## Adopt in a project

The project system owns how any extension is adopted: what to record, where, and
which authority survives it. With project-foundation 5 or later, follow its
adopted-extensions convention from the project's installed core, which owns the
declaration contents, the shared-installation rule and the authority boundary.
Another project system declares equivalent explicit routes in its own
instructions. This collection requires no core parser or runtime import, and
nothing here repeats that contract.

What this extension contributes to such a declaration is service-specific: the
capabilities selected as services, the chosen service home, local adaptations to
the layout below, and the validation route in
[discovery and checks](#discovery-and-checks). Record the complete collection's
source pin through [installation guidance](installation.md).

Project-foundation versions before 5 shipped this service scaffold themselves.
During migration, remove active routes to that copy and select this collection as
the single owner. Preserve current service paths, controls, local adaptations,
retained state and operating guarantees. Installation does not start services or
change hosting, exposure or automatic startup.

## Discovery and checks

The [repository service convention](repository-services.md) defines the adopted
home, its index, the per-service guide and the controller interface. This
declaration adds only what bounds them: the selected home and its index bound
discovery, supporting guides are linked sources rather than further service
definitions, symlinks are not followed, arbitrary directories are not scanned for
possible services, and a repository with no defined services needs no empty home.

The validation route is
`python3 <service-foundation>/scripts/validate-services.py <service-home>`, run
when adopted definitions change. Python 3 is the only prerequisite this extension
adds; runtime prerequisites stay service-specific. The convention owns the exact
check limits and the operational review and evidence that a structural pass
cannot replace. Collection installation checks verify the distributed package,
not a consumer's service definitions.

A repository whose controllers import the bundled Python helpers deploys the
collection's loader and names the interface version it was written against;
[runtime helpers](runtime-helpers.md) owns that contract. Discovery of the
installed directory stays with the project's existing route.

The optional [structured definition](service-definition.md) adds versioned facts
inside the owning guide. Service-foundation owns its format and parser; a browser
adapter selects adopted homes explicitly and projects these sources. Installation
alone does not register services or establish runtime readiness.
