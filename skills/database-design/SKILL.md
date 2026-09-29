---
name: database-design
description: Design or review relational database naming, identity, relationships, state, timestamps and integrity boundaries, with PostgreSQL conventions. Use for schema and migration design; query tuning and database operations follow the project's own guidance.
---

# Database design

Shape stored data around what identifies a record, what is known about it, and
which operations must preserve its meaning. Start with the project's domain
model, schema or migrations, access boundaries and verification instructions.
Inspect later migrations before treating an initial definition as current.

These are defaults for new design. Preserve explicit project conventions and
document deliberate departures in the project's owning guide. Adoption alone
does not call for renaming existing objects, rewriting deployed migrations,
changing access or deploying anything. Examples below are synthetic.

## Naming

| Object | Default |
| --- | --- |
| Tables | English, lower-case `snake_case`, plural: `projects`. |
| Link tables | Subject first, singular prefix and plural related noun: `project_people`. Use a domain noun when the relationship has its own meaning. |
| Columns | English, lower-case `snake_case`; singular for a single value. |
| References | Role followed by the referenced key name: `project_id`, `reviewer_id`. Distinguish multiple roles referring to the same table. |
| Instants | PostgreSQL `timestamptz`, names ending in `_at`. |
| Calendar dates | `date`, with a domain name such as `valid_from` or `review_on`. |
| Primary and foreign keys | Keep PostgreSQL-generated `_pkey` and `_fkey` names. |
| Checks | Explicit `<table>_<subject>_check`; name the rule. |
| Unique constraints | Explicit `<table>_<columns>_unique`. |
| Indexes | Explicit `<table>_<columns>_idx`, including standalone unique indexes. |

Use a clear subject for expressions, partial predicates or overly long names.
Respect the database's identifier limit; preserve generated key names that it
shortens. Naming communicates intent but does not enforce identity or access.

## Identity and relationships

Maintained entities need a stable local identity that survives corrections to
labels and external references. Prefer UUID `id` keys for these entities unless
the project has another stable key convention. Natural keys can fit genuinely
stable identities or rebuildable projections; do not key a maintained entity by
a mutable display label or URL merely because it is unique today.

Simple links use the relationship's identifying columns as a composite primary
key. Give a relationship its own identifier when it needs independent references
or maintained context. A surrogate key still needs a domain uniqueness rule.
Include a role, capacity or other qualifier only when it distinguishes genuinely
different relationships. Lifecycle flags must not create duplicate identities.

For nullable components of uniqueness, decide whether two unknown values count
as duplicates. PostgreSQL's `UNIQUE NULLS NOT DISTINCT`, where supported, can
express that choice. An unknown scope must not silently match every known scope.
Choose foreign-key deletion behavior from ownership and retention requirements;
do not cascade away independent records just because they are related.

Store external identifiers separately and enforce uniqueness within their real
scope, including provider, account, list or other namespace where needed.
Preserve opaque identifiers' case and contents unless the provider defines
normalization. Reject blank identifiers rather than treating them as identities.
Keep evidence URLs separate from identity.

A source association can be provenance without identifying the local entity.
Model many-to-many provenance when several records can share one source; a
capture retry must then use an explicit target or reject ambiguous matches.
Cross-database references need an explicit validation and missing-target policy;
an identifier alone neither supplies a foreign key nor confers authority.

## Facts, state and time

Prefer underlying facts, relationships and explicit domain values over booleans
that duplicate lifecycle or conceal unknowns. Retain a boolean for a genuinely
binary property; define what false and unknown mean. This concerns stored domain
fields, not application control flow or booleans derived in views.

Keep lifecycle, real-world validity, visibility and evidence confidence distinct.
An archive timestamp describes visibility only if the domain defines it that way.
Decide separately whether links have their own lifecycle. Do not add validity
periods to every relationship or assume that an unknown end date proves activity.

Use a timestamp only when the instant is known. Use a date when only the day is
meaningful, and define the business timezone for rules involving "today". Do not
invent midnight timestamps or infer domain events from database bookkeeping.

Store explicit conditions and derive their current consequences. For example,
readiness can depend on a prerequisite and a date; storing another mutable
`is_ready` flag creates a second rule to maintain. Retain conditions that may
become unsatisfied again. An answer, evidence match or review date establishes
permission only through the domain's explicit rule.

## Controlled vocabularies

Use stable English `snake_case` codes for roles, capacities and types; keep
display labels, translations and qualifications outside the code. For a small
fixed vocabulary, prefer text with a named check constraint. Follow existing
enum conventions when established; use a referenced table when values have
their own maintained data or lifecycle. Add values for actual domain needs.

Define null explicitly when it means unknown. A nullable check does not itself
require a value. Enforce valid combinations as well as allowed individual values:
typed relationships may require exactly one target, and a completion state may
require its event timestamp. Keep these rules in the database where every writer
must obey them.

## Bookkeeping and history

For mutable application-owned tables, including links, default to required
`created_at` and `updated_at` values generated by the database. Reuse existing
columns. Defaults handle insertion; a shared row-level update trigger can cover
all write paths. Define whether no-op updates advance `updated_at`. PostgreSQL
`now()` uses transaction time; `clock_timestamp()` records wall-clock time at the
call. Preserve `created_at` on update.

Backfilled timestamps mark tracking from the backfill unless older values have
evidence. They cannot establish original creation or modification dates.
Deleting and recreating a link creates a new row and new bookkeeping timestamps.
Platform-owned tables and append-only logs need their own conventions; immutable
events generally need an occurrence or recording time rather than update tracking.

An update timestamp is not a revision history. If audit or domain events are
required, define coverage, actor attribution, payload exclusions and retention
separately. Emit required events atomically with the change and protect immutable
history through the access model. Avoid copying credentials or unnecessary
sensitive payloads into logs. Project policy decides which tables need coverage.

## Integrity and access

Use named, bounded schemas when the platform supports them. Preserve the
project's exposure model; a schema name alone provides no access protection.
Schema-qualify objects at trust boundaries and review the privileges of functions
and views as well as tables. Separate runtime authority from schema ownership.
Domain membership or an organisation relationship does not imply database access.

Use constraints for row and relationship invariants. For changes spanning rows,
commands, retries or workers, read [operations](references/operations.md).
Choose the existing write boundary: a restricted record writer and a command-only
API have different responsibilities. Do not grant direct table writes merely to
make a generic convention easier to apply.

## Review and verification

Review identity, nullable uniqueness, valid state combinations, deletion behavior,
time semantics and access against concrete domain cases. For migrations, check
existing data and backfill meaning as well as the empty-schema result. Keep
deployed migrations immutable and follow the project's migration workflow.

Use the project's relevant checks: catalog assertions can cover naming, required
columns and trigger coverage; behavioral checks should cover rejected invalid
states, duplicates, allowed and denied operations, and concurrent writes where
they affect correctness. English names and domain meaning still need review.
Report what was inspected or tested and what remains unverified.
