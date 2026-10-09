# Work-records extension

Work-records supplies reusable methods for bounded assignments, evidence and
scoped disposition. It works alone or alongside the project's document
conventions. It owns no concrete document shapes or templates.

## Scope and document ownership

Use this guidance where an assignment's intent, evidence or transfer needs to
survive the conversation. A routine fix or an adequate plan item with a short
result needs no separate brief. A brief can be a bounded item in the plan;
reports, studies and handoffs use the project's record shape, and worklogs
collect dated records.

The [record chain](record-chain.md) owns the semantic relationships and the
[assignment contract](assignment-contract.md) owns bounded commissions and
returns. The [record format](record-format.md) owns the optional
`work-record/v1` metadata and its checker. The project or its adopted framework
owns concrete shapes, filenames, placement and validation of those shapes.
Standalone use needs none of those installations: concise prose with reachable
inputs, completion criteria, identified evidence, limits and an actual disposition
is sufficient. For example, a task can ask for a comparison under named conditions
and receive one dated record of the observations and unresolved choice.

Project owners retain intent, domain specifications, active coordination and
actual decisions. Records organize that work and grant no authority. They do not
make an executor's recommendation into acceptance by another owner.

## Adopt in a project

Declare the affected repositories, selected record homes, local adaptations and
any optional validation route in existing project instructions. Reuse adequate
homes and records. Keep records with their work and link current policy, design
and recurring operations to their maintained owners; changing placement is a
separate migration that preserves links and assessed revisions.

Record the skill's source pin with other installed skill provenance. A shared
installation does not adopt its guidance in every repository. Existing task
systems may retain both coordination and dated evidence when their ownership
and assessed versions remain distinguishable.

## Discovery and checks

Use `python3 <work-records>/scripts/validate-work-records.py <path>...` only when
checking records that select `work-record/v1`. Discovery is bounded by the paths
passed; there is no registry, automatic crawl or framework dependency. Unselected
Markdown is skipped. The checker verifies the optional metadata and identifier
uniqueness, not document shape, links, evidence, acceptance or content adequacy.
The [format reference](record-format.md) states its exact contract and limits.

## Owned by the project framework

Standing specifications, governing documents, indexes and work definitions keep
the shapes selected by the project. This skill adds no process-page format or
competing review-feedback section. Its method can be used inside those existing
forms without making them extension-managed documents.

Version 1 removes the five bundled templates. Consumers upgrading from 0.x
replace live template routes with their selected project shapes; existing
records and the optional v1 metadata need no migration. Keep the old source pin
for historical references. No subtype taxonomy replaces the removed files.
