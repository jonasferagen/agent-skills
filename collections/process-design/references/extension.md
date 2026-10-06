# Process-design extension

Process-design owns work records: the brief that commissions a bounded
assignment, the worklog that tracks progress, the report or study that retains
findings, and the handoff record that transfers a result. It can
be used with a project's own instructions or adopted as an optional
project-foundation extension. Its guidance and checker require no
project-foundation installation.

## Scope and document ownership

Adopt this convention where work is commissioned, performed and judged across
owners and the records of that need to be readable later. A project selects
which work qualifies; a routine fix, a literal correction or an item that the
active plan already tracks with a short result needs no brief merely because
this collection is installed.

The [record chain](record-chain.md) is authoritative for what each record means,
which owner keeps it and how findings route back to the thing that changed.
The [assignment contract](assignment-contract.md) owns assignment boundaries,
discoverable inputs and the requested return. The
[record format](record-format.md) is authoritative for the optional
`work-record/v1` metadata and its checker. The templates under
`templates/repository-docs/work-records/` are starting structures for the five
document purposes; omit sections rather than inventing content to fill them.

These are extension-managed documents with repository-owned content. The
project keeps intent, criteria, evidence and decisions; this collection supplies
their shape. Do not copy policy, architecture, responsibilities or a changing
work queue into a record.

## Select homes outside the reserved tree

Work records are content. Keep them with the work: the performing repository's
workspace for a report, study or worklog, the commissioning owner's workspace
for a cross-discipline brief. Where a project framework reserves a governed document
root, these homes stay outside it unless that framework's own map admits the
type.

A project may keep an existing home and filename when adopting this convention.
Changing where records live is a separate migration with its own inbound-link
repair; adoption alone moves nothing.

## Adopt in a project

Record this entrypoint, the affected repositories, the selected homes, any
project adaptations and the validation route in the existing instruction owner.
Record the complete collection's source pin in collection provenance using
[installation guidance](installation.md). A shared installation can serve
several repositories without adopting the convention in every one.

With project-foundation 5 or later, follow its extension-adoption convention
from the project's installed core. Other project systems can declare equivalent
explicit routes in their own instructions; no core parser or runtime import is
required.

Project policy and user decisions govern authority. These defaults do not
override project commitments, and a recorded disposition is not acceptance by an
owner who did not give it. Keep unresolved conflicts with their affected owner
and continue unrelated work.

## Discovery and checks

Discovery is bounded by the paths a project passes to the checker. There is no
crawl, no registry file and no automatic extension discovery. A consumer that
browses records implements and verifies its own discovery; this collection
defines the source format, not a viewer.

Run `python3 <process-design>/scripts/validate-work-records.py <path>...` when
changing selected records. It checks structure and identifier uniqueness without
resolving links, reading linked evidence or judging content. The
[record format](record-format.md) owns the exact limits. Collection installation
checks verify the distributed package, not a consumer's records.

A core document check makes no claim about these records, and this checker makes
no claim about core documents.

## Owned by the project framework

The named-process document type and its structured page format belong to the
consuming project's framework. Where that is project-foundation, its
`project-process/v1` reference, parser and template are the single owner, and
this collection supplies no second definition of them. The division follows the
document's home and subject, not a release boundary: a named process is a
standing explanation of how recurring work runs, kept in the framework's governed
document root; a work record is a dated document about one assignment, kept with
that work. Do not treat a process page as extension-managed and do not run this
checker over one.

Project-foundation's `review-feedback-section` template stays core's for the same
reason. It is a section pattern for an assessment placed inside the repository
document that already owns the subject. This collection's
[report](../templates/repository-docs/work-records/report.md) and
[worklog](../templates/repository-docs/work-records/worklog.md) are standalone
records that return findings to a commissioning owner. Their fields overlap, so
select by where the finding belongs rather than by which is newer. Both stay
defined; neither deprecates the other.

Earlier revisions recorded taking both over as this collection's next step. That
intention is withdrawn, so no reader needs a pending migration to interpret
either collection. Moving the process type here later would be a new decision in
both, with its own migration, deprecation path and version impact.

Project exchange contracts, policy, architecture, conceptual models and the
active plan retain their own owners. A brief links them; it never becomes their second home.
