# Process design

Version: 0.1.0

Use this collection for the records that carry work between owners: the brief
that commissions a bounded assignment, the worklog or study that retains its
evidence, and the findings and disposition that close it. Start from the
project's existing owners and the work actually being done. This collection
works without a specific project framework, document root or viewer.

| Task | Entry point |
| --- | --- |
| Frame a bounded assignment, record its evidence or close it with a disposition | [Work records](skills/work-records/SKILL.md) |
| Understand which record owns intent, evidence, findings or a decision | [Work records](skills/work-records/SKILL.md), then its [record chain](references/record-chain.md) |
| Write or interpret record metadata, or run its checker | [Record format](references/record-format.md) |
| Adopt work-record homes and checks in a project | [Process-design extension](references/extension.md) |
| Install, update or check this collection | [Installation](references/installation.md) |

Reading or correcting an existing record follows that record directly; it needs
no route from here. A record is a document, not a database row: these are
reviewable contents and an optional field vocabulary, not a schema, a service or
an approval gate. Existing records stay valid; adopting this collection migrates
nothing on its own.

Project policy, architecture, planning and contracts retain their own owners. A
brief states intent and criteria for one assignment; it does not become a second
home for responsibilities, obligations or the active work queue. Report a missing
required owner with its consequence and continue unaffected work.

## Scope boundary and planned ownership

This release owns work records only. The named-process document type and its
structured page format remain with the consuming project's framework; where that
is project-foundation, its `project-process/v1` reference, parser and template
stay authoritative and this collection adds no second definition.

Transferring that type here is the recorded next step for this collection, taken
as a deliberate framework change with its own migration and version impact. Until
it lands, do not treat a process page as an extension-managed document, and do
not run this collection's checker over one.
