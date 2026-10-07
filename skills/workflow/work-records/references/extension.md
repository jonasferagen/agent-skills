# Work-records extension

Work-records owns the brief that commissions a bounded assignment, the worklog
that tracks progress, the report or study that retains findings, and the handoff
record that transfers a result. It can be used with a project's own instructions
or adopted as an optional extension of the project's framework. Its guidance and
checker require no framework installation.

## Scope and document ownership

Adopt this convention where work is commissioned, performed and judged across
owners and the records of that need to be readable later. A project selects
which work qualifies; a routine fix, a literal correction or an item that the
active plan already tracks with a short result needs no brief merely because
this skill is installed.

The [record chain](record-chain.md) is authoritative for what each record means,
which owner keeps it and how findings route back to the thing that changed.
The [assignment contract](assignment-contract.md) owns assignment boundaries,
discoverable inputs and the requested return. The
[record format](record-format.md) is authoritative for the optional
`work-record/v1` metadata and its checker. The templates under
`templates/repository-docs/work-records/` are starting structures for the five
document purposes; omit sections rather than inventing content to fill them.

These are extension-managed documents with repository-owned content. The
project keeps intent, criteria, evidence and decisions; this skill supplies
their shape. Do not copy policy, architecture, responsibilities or a changing
work queue into a record.

## Select homes outside the reserved tree

Work records are content. Keep them with the work: the performing repository's
workspace for a report, study or worklog, the commissioning owner's workspace
for a cross-discipline brief. Where a project framework reserves a governed
document root, these homes stay outside it unless that framework's own map
admits the type.

A project may keep an existing home and filename when adopting this convention.
Changing where records live is a separate migration with its own inbound-link
repair; adoption alone moves nothing.

## Adopt in a project

The project system owns how any extension is adopted: what to record, where,
and which authority survives it. Follow its adoption convention when it has one;
otherwise declare equivalent explicit routes in the project's own instructions.
No core parser or runtime import is required.

What this extension contributes to such a declaration: this entrypoint, the
affected repositories, the selected homes, any project adaptations and the
validation route below. Record the skill's source pin in the project's skill
provenance. A shared installation can serve several repositories without
adopting the convention in every one.

Project policy and user decisions govern authority. These defaults do not
override project commitments, and a recorded disposition is not acceptance by an
owner who did not give it. Keep unresolved conflicts with their affected owner
and continue unrelated work.

## Discovery and checks

Discovery is bounded by the paths a project passes to the checker. There is no
crawl, no registry file and no automatic extension discovery. A consumer that
browses records implements and verifies its own discovery; this skill defines
the source format, not a viewer.

Run `python3 <work-records>/scripts/validate-work-records.py <path>...` when
changing selected records. It checks structure and identifier uniqueness without
resolving links, reading linked evidence or judging content. The
[record format](record-format.md) owns the exact limits. Package checks verify
the distributed skill, not a consumer's records.

A core document check makes no claim about these records, and this checker makes
no claim about core documents.

## Owned by the project framework

The named-process document type and its structured page format belong to the
consuming project's framework, and this skill supplies no second definition of
them. The division follows the document's home and subject, not a release
boundary: a named process is a standing explanation of how recurring work runs,
kept in the framework's governed document root; a work record is a dated
document about one assignment, kept with that work. Do not treat a process page
as extension-managed and do not run this checker over one.

A framework's section pattern for review feedback placed inside the document
that already owns the subject stays the framework's for the same reason. This
skill's [report](../templates/repository-docs/work-records/report.md) and
[worklog](../templates/repository-docs/work-records/worklog.md) are standalone
records that return findings to a commissioning owner. Their fields may overlap
with such a pattern, so select by where the finding belongs rather than by
which is newer. Both stay defined; neither deprecates the other.

Earlier revisions recorded taking the process type over as a next step. That
intention is withdrawn, so no reader needs a pending migration to interpret
either owner. Moving the process type here later would be a new decision in
both, with its own migration, deprecation path and version impact.

Project exchange contracts, policy, architecture, conceptual models and the
active plan retain their own owners. A brief links them; it never becomes their
second home.
