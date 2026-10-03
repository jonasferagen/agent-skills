# Canonical project document homes

Project-foundation maintains project governance and coordination documents in
`project-docs/` at the repository root. Repository-specific technical documentation
remains in `docs/` or another repository-declared technical home, outside that
reserved directory. Using a writing or diagram skill on a technical document does
not make it a managed project document.

## Document types and owners

| Document type | Canonical home | Maintaining workflow |
| --- | --- | --- |
| Foundation facts, including boundaries, overview and policy | `project-docs/foundation.md` | Bootstrap establishes; policy reconciles changed facts and obligations |
| Shared or local working agreements and skill routes | `project-docs/working-agreements.md` | Bootstrap establishes routes; affected workflows maintain them |
| Active outcomes, work queue and deferred choices | `project-docs/planning/README.md` | Project planning |
| Detailed plans for substantial bounded work | `project-docs/planning/<topic>.md` | Project planning; linked from the active plan |
| Durable governance decisions and policy exceptions | `project-docs/decisions/<topic>.md` | The workflow making the decision; policy reviews changed obligations |
| Completed planning records and governance change evidence | `project-docs/records/<topic>.md` | The workflow completing or reconciling the work |

This is a closed set of document types. The collection owns this map; a task
must not add a new category or miscellaneous file to the reserved directory.
Propose a collection change when a genuinely new managed type is needed.
Repository-specific documents belong in their repository-owned homes.

These are allowed homes, not a required set of files. Create a document only
when its type is needed and no existing owner serves it. A small task can remain
one item in the active plan with a short result; it does not need a task file,
decision record and report. Keep policy in the foundation's Policy table rather
than creating a competing `policy.md`. Use decision records only when the durable
reason or scoped exception warrants one.

README and AGENTS remain at their conventional repository entry points and link
to these owners. The installed collection stays at its selected dependency path;
project documents must remain outside the vendored skill files.

## Repository-owned documentation

Architecture, domain definitions, API contracts, design explanations, operating
procedures and setup instructions retain repository-selected homes, commonly
elsewhere in `docs/`. Implementation evidence, run records and handoffs use the
repository's declared work-record home. A policy impact record can link technical
evidence there without copying it into governance records.

Choose placement by the document's purpose. A technical design proposal belongs
beside its design owner; the task to resolve it belongs in planning. A plan may
link the proposal without reproducing it. A runtime runbook remains technical
documentation even when policy requires that procedure.

Before creating a document, identify its type and owner. Reuse the existing
owner when one exists. Within the reserved directory, use only the mapped files
and Markdown topic records directly within the three mapped subdirectories;
keep technical attachments, generated output and scratch outside it. Topic names
use lowercase words separated by hyphens, optionally prefixed by a date.
This restriction governs document placement, not permission to undertake work.

Run `python3 <collection>/scripts/validate-project-docs.py <project-docs-root>`
after changing the managed directory. It checks allowed paths and requires the
active plan index when detailed plans exist. Review content against the type map
as well: a filename check cannot tell whether a technical manual was misfiled as
a plan. Validate the foundation format separately when its facts change.

## Shared projects

Each member keeps its local foundation in the canonical location and declares
inheritance from the shared owner. Shared working agreements, policy and plans
live once in that owner. Members add local documents only for their own facts or
delegated responsibilities. Shared planning links any delegated local queues;
keep each item's changing status and next action in one home.

## Adoption and migration

Use these homes for new foundations. An existing installation keeps its declared
routes until a deliberate migration; upgrading the collection alone must not
silently move files or leave consumers pointing at missing owners. Record the
existing layout as transitional when adopting this convention, with migration
work in the active plan. An explicit user-selected exception must be declared in
working agreements with the same document-type mapping; do not select a different
root independently for each task.

For migration, inventory current owners and their inbound links first. Map each
document by purpose, preserve unique facts and historical evidence, and update
entry points, relative links, foundation bindings, inheritance anchors and
validators that use the old paths. Land shared owners before member consumers;
use a temporary route if the authorized landing sequence requires one. Check
main-checkout and task-worktree access. Remove superseded active routes only when
their consumers have moved. Report what was migrated and what remains transitional.
