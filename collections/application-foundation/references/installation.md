# Install application foundation

Copy the complete collection, retaining its relative layout, into the project's
chosen collection location, normally `.agents/collections/application-foundation/`.
Select a source commit and record its repository URL, source directory, full SHA,
collection version and any release tag in the project's provenance file. A draft
can be pinned by commit without a release tag. Compare the complete installed copy
with that revision when installing or updating it.

Route from project instructions to `COLLECTION.md` for application-design tasks,
or directly to `skills/application-design/SKILL.md` when that owner is known.
The installation does not itself register native client discovery. Use the
client's supported discovery mechanism or an explicit project-instruction route.
For several repositories, one accessible, pinned installation may serve all of
them; each repository retains its own implementation and decision owners.

## Companion guidance

The collection has no required dependency on another collection or skill. All
required references are included. Project instructions can route to separately
installed companions when their tasks apply:

| Task | Companion candidates |
| --- | --- |
| Project responsibilities, handoffs and document ownership | project-foundation |
| Language-specific implementation | typescript-design and typescript-patterns, or python-design and python-patterns |
| Shared behavior across HTTP and MCP, or service ownership | service-boundaries |
| Runtime credentials, processes and service controls | runtime-operations |
| Evidence selection and writing tests | verification-design and test-writing |

Pin each selected installation independently in project provenance. Give it a
concrete local route in project instructions; do not put cross-installation
relative links inside this collection. Missing companions do not block the core
workflow, but project-required guidance remains required by that project. The
project's scope determines whether an unavailable dependency blocks a particular
implementation task.

Updates replace the complete collection and reconcile its project routes. This
scheme uses explicit installations and project routing; it provides no automatic
dependency resolution, version compatibility solver or tracking of upstream main.
