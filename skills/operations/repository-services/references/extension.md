# Service extension

Repository-services owns repository service definitions and their documentation
and control conventions. It can be used with a project's own instructions or
adopted as an optional extension of the project's framework. Its tools and
guidance require no framework installation.

## Scope and document ownership

Adopt this convention for repositories that define named runtimes needing
explicit lifecycle controls. The project selects which capabilities qualify;
finite jobs, editors and ordinary commands need no service definition merely
because this skill is installed. Existing service guides remain the entry for
ordinary operation. Boundary and runtime design belong to the
`service-boundaries` and `runtime-operations` skills.

The [repository service convention](convention.md) is authoritative for the
default `services/` home, its index, per-service guide, controller interface,
templates and required explanations. These are extension-managed documents with
repository-owned content. Guides can link additional repository-defined operating
procedures and evidence. Project architecture retains responsibilities and
interfaces; the service guide retains the exact operational definition. Do not
copy policy, architecture or changing facts into a second owner.

## Adopt in a project

The project system owns how any extension is adopted: what to record, where, and
which authority survives it. Follow its adoption convention when it has one,
which then owns the declaration contents, the shared-installation rule and the
authority boundary; otherwise declare equivalent explicit routes in the project's
own instructions. This skill requires no core parser or runtime import, and
nothing here repeats that contract.

What this extension contributes to such a declaration is service-specific: the
capabilities selected as services, the chosen service home, local adaptations to
the layout in the convention, and the validation route in
[discovery and checks](#discovery-and-checks). Record the skill's source pin in
the project's skill provenance.

Where a project framework once shipped its own copy of this scaffold, remove
active routes to that copy during migration and select this skill as the single
owner. Preserve current service paths, controls, local adaptations, retained
state and operating guarantees. Installation does not start services or change
hosting, exposure or automatic startup.

## Discovery and checks

The [repository service convention](convention.md) defines the adopted home, its
index, the per-service guide and the controller interface. This declaration adds
only what bounds them: the selected home and its index bound discovery,
supporting guides are linked sources rather than further service definitions,
symlinks are not followed, arbitrary directories are not scanned for possible
services, and a repository with no defined services needs no empty home.

The validation route is
`python3 <repository-services>/scripts/validate-services.py <service-home>`, run
when adopted definitions change. Python 3 is the only prerequisite this extension
adds; runtime prerequisites stay service-specific. The convention owns the exact
check limits and the operational review and evidence that a structural pass
cannot replace. Package checks verify the distributed skill, not a consumer's
service definitions.

A repository whose controllers import the `runtime-operations` Python helpers
deploys that skill's loader and names the interface version it was written
against; its runtime-helpers reference owns that contract. Discovery of the
installed directory stays with the project's existing route.

The optional [structured definition](service-definition.md) adds versioned facts
inside the owning guide. This skill owns its format and parser; a browser
adapter selects adopted homes explicitly and projects these sources. Installation
alone does not register services or establish runtime readiness.
