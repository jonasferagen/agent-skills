# Canonical project document homes

Project-foundation maintains governance, architecture, conceptual models,
process descriptions and handoff contracts in `project-docs/` at the repository
root. The collection owns their document types and default structures; the
responsible project or repository owns their meaning. Command-level operating
procedures, setup, implementation references, creative content and technical
evidence retain repository-declared homes outside this reserved directory.

## Document types and owners

| Document type | Canonical home | Maintaining workflow |
| --- | --- | --- |
| Foundation facts, including boundaries, overview and policy | `project-docs/foundation.md` | Bootstrap establishes; policy reconciles changed facts and obligations |
| Shared or local working agreements and skill routes | `project-docs/working-agreements.md` | Bootstrap establishes routes; affected workflows maintain them |
| Active outcomes, work queue and deferred choices | `project-docs/planning/README.md` | Project planning |
| Detailed plans for substantial bounded work | `project-docs/planning/<topic>.md` | Project planning; linked from the active plan |
| Durable governance decisions and policy exceptions | `project-docs/decisions/<topic>.md` | The workflow making the decision; policy reviews changed obligations |
| Completed planning records and governance change evidence | `project-docs/records/<topic>.md` | The workflow completing or reconciling the work |
| Repository internal design and its detail routes | `project-docs/design.md` | Project design |
| Architecture overview and navigation | `project-docs/architecture/README.md` | Project design; project documentation maintains routes |
| Architecture boundaries, information flows and documentation conventions | `project-docs/architecture/<topic>.md` | Project design; project documentation owns documentation conventions |
| Distinct architecture alternatives or unresolved designs | `project-docs/architecture/proposals/<topic>.md` | Project design; link from the architecture index |
| Architecture and handoff walkthroughs | `project-docs/architecture/examples/<topic>.md` | The workflow exercising the design; link from the architecture index |
| Conceptual model index | `project-docs/models/README.md` | Project documentation |
| Domain concepts, relationships and constraints | `project-docs/models/<topic>.md` | Project design |
| Process index | `project-docs/processes/README.md` | Project documentation |
| Named process entry: triggers, participants, decisions, interruptions and handoffs | `project-docs/processes/<process>/README.md` | Project design; the responsible repository maintains local meaning |
| Supporting explanations of that process | `project-docs/processes/<process>/<topic>.md` | Project design; linked from the process entry |
| Existing flat process descriptions, retained until deliberate migration | `project-docs/processes/<topic>.md` | Project design; the responsible repository maintains local meaning |
| Handoff contract index | `project-docs/contracts/README.md` | Project documentation |
| Exchange obligations, identity, acceptance and compatibility | `project-docs/contracts/<topic>.md` | Project contracts |

This is a closed set of document types. The collection owns this map; a task
must not add a new category or miscellaneous file to the reserved directory.
Propose a collection change when a genuinely new managed type is needed.
Documents outside these types belong in their repository-owned homes.

These are allowed homes, not a required set of files. Create a document only
when its type is needed and no existing owner serves it. A small task can remain
one item in the active plan with a short result; it does not need a task file,
decision record and report. Keep policy in the foundation's Policy table rather
than creating a competing `policy.md`. Use decision records only when the durable
reason or scoped exception warrants one.

README and AGENTS remain at their conventional repository entry points and link
to these owners. The installed collection stays at its selected dependency path;
project documents must remain outside the vendored skill files.

## Default structures

Start repository design pages from the [design template](../templates/project-docs/design.md),
conceptual models from the [model template](../templates/project-docs/model.md),
process entries from the [process template](../templates/project-docs/process/README.md),
and handoff contracts from the [contract template](../templates/project-docs/contract.md).
Use the [view template](../templates/views/view.md) for architecture views.
Each index links its owners with a brief reader question; it need not repeat
their changing status or definitions. A walkthrough identifies whether its case
is synthetic or observed and links the model or terms it exercises.

These are starting structures. Preserve an existing page that already supplies
purpose, scope, ownership, status, explanations, relevant constraints and evidence
or open questions. Omit irrelevant sections rather than inventing content. A
process, contract or model need not contain a diagram. Several identifiable views
can remain in one page. The templates establish readable associations; a parser
syntax, comprehensive structural validation and an operating-procedure template
require a separately selected scope.

### Named processes

For a new named process, use `project-docs/processes/<process>/README.md` and
link it from `project-docs/processes/README.md`. One process README is sufficient;
do not create supporting pages or empty directories in anticipation of future
work. Prose or numbered steps can explain the workflow without a diagram.

When one part needs its own explanation, add a direct `<topic>.md` page in that
process directory and link it from the entry. Keep one canonical process owner;
supporting pages elaborate it rather than restating its workflow. This is one
named directory level, not permission for nested stage directories or arbitrary
files. Commands, implementation artifacts and run records stay in their existing
repository-owned homes; contracts and models retain their mapped homes. Link them
where the process needs them.

Existing flat `processes/<topic>.md` pages remain valid until deliberate migration.
Do not keep both `processes/<name>.md` and `processes/<name>/README.md`: they create
ambiguous owners. A process's location describes its reader question, while its
status states whether the described work is proposed, adopted or evidenced. A
proposed process can use the same structure without implying implementation.

## Repository-owned documentation

Command invocations, controls, provider setup, executable API/schema references,
fixture details and creative briefs retain repository-selected homes, commonly
in `docs/`. Implementation evidence, run records and task handoffs use the
repository's declared work-record home. A policy impact record can link technical
evidence there without copying it into governance records.

Choose placement by the question the page answers. A process explains how work
moves between responsibilities and decisions; an operating procedure gives exact
commands or controls for carrying it out. Keep that process in its managed owner
and link the local procedure. A conceptual exchange contract owns what parties
can rely on; a generated API reference or an implementation-specific field/command
guide stays with implementation. A creative brief is content; the reusable model
connecting briefs to findings is a managed model. Split a mixed page only where
those meanings have separate owners. Preserve exact facts and evidence links.

A design proposal belongs beside its design owner; the task to resolve it belongs
in planning. A plan may link the proposal without reproducing it. A runtime
runbook remains implementation documentation even when policy requires it.

For a repository-owned message, record or package format, use the optional
[format-section template](../templates/repository-docs/format-section.md) when
it helps distinguish the representation from the steps that produce or consume
it. Place the section in the existing implementing guide. State its applicable
revision and scoped status beside the definition, link the governing process or
contract where one exists, and point to the operating procedure and evidence.
Keep an adequate existing section; the template adds no document type or required
headings. A linked format alone does not establish adoption or contract
conformance.

For a format used across repositories, identify the owner that decides its
representation. Consumer guides link that definition and explain their own
checks, adaptations or narrower support instead of maintaining another
complete field list. When one guide defines records with distinct identities
or uses, give each a directly linkable section and scoped status; this does
not require separate files. Use [source-of-truth](../skills/source-of-truth/SKILL.md)
if competing definitions have already appeared.

Before creating a document, identify its type and owner. Reuse the existing
owner when one exists. Within the reserved directory, use only the mapped files
and Markdown topic documents directly within the mapped subdirectories, including
the one named process level above. Keep technical attachments, generated output
and scratch outside it. Process and topic names use lowercase words separated by
hyphens, optionally prefixed by a date.
This restriction governs document placement, not permission to undertake work.

Run `python3 <collection>/scripts/validate-project-docs.py <project-docs-root>`
after changing the managed directory. It reads the allowed paths from the table
above, including the explicit `<process>` directory placeholder. It requires a
mapped parent index when a directory contains topic documents or named processes,
a README for each named process, and distinct flat and directory process names.
Symlinks, additional directory levels and non-Markdown artifacts are rejected.
This remains a path check: it does not enforce headings,
template fields, semantic completeness or browser input. Review content against
the type map as well; a filename check cannot tell whether a command guide was
misfiled as a process. Validate the foundation format separately when its facts
change.

## Shared projects

Each member keeps its local foundation in the canonical location and declares
inheritance from the shared owner. Shared working agreements, policy and plans
live once in that owner. Shared architecture, models, processes and contracts also
have one authoritative owner. Members define only their internal detail and link
shared processes and terms instead of maintaining copies. Shared planning links any delegated local queues;
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
