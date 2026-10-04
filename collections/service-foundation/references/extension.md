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

Record this entrypoint, the affected repositories/capabilities, service home,
project adaptations and validation route in the existing instruction owner.
Record the complete collection's source pin in provenance using
[installation guidance](installation.md). A shared installation can serve several
repositories without adopting service definitions in every repository.

With project-foundation 5 or later, follow its extension-adoption convention from
the project's installed core. Earlier foundations or other project systems can
declare equivalent explicit routes in their instructions; no core parser or
runtime import is required. Project-foundation versions before 5 shipped this
service scaffold themselves. During migration, remove active routes to that copy
and select this collection as the single owner. Preserve current service paths,
controls, local adaptations, retained state and operating guarantees. Installation
does not start services or change hosting, exposure or automatic startup.

Project policy and user decisions govern authority. Extension defaults do not
override project commitments. Keep unresolved conflicts with their affected owner
and continue unrelated work; unavailable guidance does not waive requirements.

## Discovery and checks

For an adopted default home, `services/README.md` indexes immediate named service
directories; `services/<name>/README.md` owns each definition. The selected home
and index bound discovery. Supporting guides remain linked sources, not additional
service definitions. Do not follow symlinks or scan arbitrary directories for
possible services. Repositories without defined services need no empty home.

Run `python3 <service-foundation>/scripts/validate-services.py <service-home>`
when changing adopted definitions. It checks structure and index routes without
executing controllers. Python 3 is needed for the checker and dispatcher; runtime
prerequisites remain service-specific. The convention explains the exact check
limits and required operational review/evidence. Collection installation checks
verify the distributed package, not a consumer's service definitions.

This declaration supplies reading and validation routes. It does not install a
browser adapter, automatically register services or define a structured service
facts schema. Browsers retain their selected discovery until support is implemented.
