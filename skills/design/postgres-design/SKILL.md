---
name: postgres-design
description: "Design or review PostgreSQL schemas, migrations and transaction boundaries, including pooled connections. Use for keys, relationships, types, state and integrity; not for query tuning."
metadata:
  version: "2.1.0"
---

# Postgres design

Shape stored data around what identifies a record, what is known about it, and
which operations must preserve its meaning. Start with the project's domain
model, schema or migrations, access boundaries and verification instructions.
Inspect later migrations before treating an initial definition as current.

Apply these conventions to new application-owned PostgreSQL objects unless a
concrete domain, compatibility or operational requirement justifies a departure.
Record the reason beside the project's other database conventions, or in the
migration that departs, if no such document exists. Explicit project conventions
take precedence. Check the target PostgreSQL version before using newer features.
Adopting these conventions does not by itself call for renaming existing
objects, rewriting deployed migrations, changing access or deploying anything.
Examples below are synthetic.

## Naming

| Object | Default |
| --- | --- |
| Tables | English, lower-case `snake_case`, plural: `orders`. |
| Link tables | Subject first, singular prefix and plural related noun: `order_products`. Use a domain noun such as `order_items` when the relationship has its own meaning. |
| Columns | English, lower-case `snake_case`; singular for a single value. |
| References | Role followed by the referenced key name: `order_id`, `approver_id`. Distinguish multiple roles referring to the same table (`customer_id` and `approver_id` both referencing `people`). |
| Instants | PostgreSQL `timestamptz`, names ending in `_at`. |
| Calendar dates | `date`, with a domain name such as `valid_from` or `ship_on`. |
| Primary and foreign keys | Keep PostgreSQL-generated `_pkey` and `_fkey` names. |
| Checks | Explicit `<table>_<subject>_check`; name the rule. |
| Unique constraints | Explicit `<table>_<columns>_unique`. |
| Indexes | Explicit `<table>_<columns>_idx`, including standalone unique indexes. |

Use a clear subject for expressions, partial predicates or overly long names.
Respect the database's identifier limit; preserve generated key names that it
shortens. Naming communicates intent but does not enforce identity or access.

## Identity and relationships

Maintained entities need a stable local identity that survives corrections to
labels and external references. Use `id uuid PRIMARY KEY DEFAULT gen_random_uuid()`
for new entities (built in since PostgreSQL 13; older versions need the
`pgcrypto` extension). Keep UUIDs in the native `uuid` type. Use the project's chosen
generator when one is established. Before selecting a newer UUID algorithm,
check target-version support and the workload; switching does not require
rewriting existing identities.
Give every application table a primary key unless its integrity design requires
a documented exception. Natural keys can fit genuinely stable identities or
rebuildable projections; do not key a maintained entity by a mutable display
label or URL merely because it is unique today.

Simple links use the relationship's identifying columns as a composite primary
key. Give a relationship its own identifier when it needs independent references
or maintained context. A surrogate key still needs a domain uniqueness rule.
Include a role, capacity or other qualifier only when it distinguishes genuinely
different relationships. Lifecycle flags must not create duplicate identities.

When a uniqueness rule includes a nullable column or expression, decide whether
two unknown values count as duplicates. PostgreSQL's
`UNIQUE NULLS NOT DISTINCT`, where supported, can express that choice. An
unknown scope must not silently match every known scope.
Choose foreign-key deletion behavior from ownership and retention requirements;
do not cascade away independent records just because they are related.

Store external identifiers separately from the local identity and enforce
uniqueness within their real scope, including provider, account, list or other
namespace where needed.
Preserve opaque identifiers' case and contents unless the provider defines
normalization. Reject blank identifiers rather than treating them as identities.
Keep URLs that point at an external record separate from identity.

A link to the import source a record came from is provenance; it does not
identify the local entity. When several records can share one source, model
that as many-to-many; a repeated import must then name its target record or
reject ambiguous matches.
Cross-database references need an explicit rule for validation and for a
missing target; an identifier alone neither supplies a foreign key nor proves
the target exists.

## Types and missing values

Make required fields `NOT NULL`. Allow null when absence has a defined meaning;
use neither empty strings nor sentinel dates or IDs as substitutes. Defaults must
represent a valid domain choice, not hide missing input. Reject blank names and
codes when a value is required; `NOT NULL` alone permits empty text.

Use `text` unless a length bound is a domain rule. Use exact `numeric` with chosen
precision and scale, or integer minor units with currency, for monetary amounts.
Use typed columns and related tables for fields that need foreign keys, uniqueness
or stable query semantics. Reserve `jsonb` for genuinely variable payloads and
validate the structure the application relies on. Do not let a JSON object
become a way around relational integrity.

## Facts, state and time

Prefer underlying facts, relationships and explicit domain values over booleans
that duplicate lifecycle or conceal unknowns. Retain a boolean for a genuinely
binary property; define what false and unknown mean. This concerns stored domain
fields, not application control flow or booleans derived in views.

Keep lifecycle, real-world validity, visibility and confidence in imported data
distinct.
An archive timestamp describes visibility only if the domain defines it that way.
Decide separately whether links have their own lifecycle. Do not add validity
periods to every relationship or assume that an unknown end date proves activity.

Use a timestamp only when the instant is known. Use a date when only the day is
meaningful, and define the business timezone for rules involving "today". Do not
invent midnight timestamps or infer domain events from database bookkeeping.

Store explicit conditions and derive their current consequences. For example,
readiness can depend on a prerequisite and a date; storing another mutable
`is_ready` flag creates a second rule to maintain. Keep a condition after it is
satisfied if it may become unsatisfied again. A stored fact such as a signed
agreement or an approval date establishes permission only through the domain's
explicit rule.

## Controlled vocabularies

Use stable English `snake_case` codes for roles, capacities and types; keep
display labels, translations and qualifications outside the code. For a small
fixed vocabulary, prefer text with a named check constraint. Follow existing
enum conventions when established; use a referenced table when values have
their own maintained data or lifecycle. Add a value only when an actual domain
case needs it, not in anticipation of one.

Define null explicitly when it means unknown. A check constraint on a nullable
column does not itself require a value. Enforce valid combinations as well as
allowed individual values: typed relationships may require exactly one target,
and a completion state may require its event timestamp. Keep these rules in the
database, where every writer must obey them.

## Bookkeeping and history

Every new mutable application-owned table, including link tables, has:

```sql
created_at timestamptz NOT NULL DEFAULT now(),
updated_at timestamptz NOT NULL DEFAULT now()
```

Reuse existing columns. These defaults handle insertion only. Attach a shared
row-level `BEFORE UPDATE` trigger that sets `NEW.updated_at = clock_timestamp()`
on every update, including no-op updates, and preserves `OLD.created_at`: one
function per schema (for example `<schema>.set_updated_at()`), one trigger per
table named `<table>_set_updated_at`, unless the project already has one.
Keep this database-managed so every write path follows the same rule. A project
may choose meaningful-change-only tracking, but must define and test that exception.
Database defaults can be overridden by supplied values; decide at the write
boundary whether callers may supply historical timestamps for imports.

`now()` is transaction-start time; `clock_timestamp()` is wall-clock time at the
call. These timestamps are bookkeeping, not commit order, a monotonic revision
number or an optimistic concurrency token. Use an explicit version when a write
must reject stale state. `timestamptz` stores an instant; retain a separate timezone
identifier when the original or recurring local timezone matters.

Backfilled timestamps mark when tracking began, unless evidence supports older
values. They cannot establish original creation or modification dates.
Deleting and recreating a link creates a new row and new bookkeeping timestamps.
Platform-owned tables and append-only logs need their own conventions; immutable
events generally need an occurrence or recording time rather than update tracking.

An update timestamp is not a revision history. If audit or domain events are
required, define coverage, actor attribution, payload exclusions and retention
separately. Emit required events atomically with the change and protect immutable
history through the access model. Avoid copying credentials or unnecessary
sensitive payloads into logs. The project decides which tables need coverage
and which mechanism records it (triggers, application events); if it has
decided neither, ask the user rather than auditing everything.

## Integrity and access

Put application-owned objects in named schemas, each holding one application's
or concern's objects, not in `public` or a platform-managed schema (one the
hosting provider or an extension owns, such as `auth`, `storage` or
`extensions`). Preserve the project's exposure model, meaning which roles,
APIs or schemas it already exposes to which callers; a schema name alone
provides no access protection.
Schema-qualify objects at trust boundaries and review the privileges of functions
and views as well as tables. Separate runtime authority from schema ownership.
Domain membership or an organisation relationship does not imply database access.

Review indexes alongside foreign keys. PostgreSQL creates indexes for primary
keys and unique constraints, but does not automatically index the referencing
columns of a foreign key. Add an index when joins, lookups or referenced-row
updates/deletes need it; check whether an existing composite index covers that
access before adding another. A link's `(left_id, right_id)` primary key may still
need an index for access by `right_id`.

Use constraints for row and relationship invariants. For changes spanning rows,
commands, retries or workers, read [operations](references/operations.md).
Work within the project's existing write boundary: a restricted record writer
(application code that may insert and update rows directly under a narrow role)
and a command-only API (writes happen only through named operations, such as
functions or endpoints, that enforce the rules) have different responsibilities. If the project
designates no write path, treat the application's existing data-access code as
that boundary and say so. Do not grant direct table writes merely to make a
generic convention easier to apply.

When application code runs transactions through a connection pool under
restricted roles, read [pooled transactions](references/pooled-transactions.md).
It covers binding each transaction to a role, read-only transactions, refusing a
commit after a failed statement, and resetting a connection before reuse. It
describes the contract such code must meet; write a new runner only when the
project has none and the task includes application code.

## Development lifecycle

For a new database implementation or an environment change, include the operating
lifecycle in the design: isolated development storage (a database or container
owned by the checkout, shared with no other environment), canonical migrations and a
repeatable synthetic seed routine, even if automated tests come later. A
request to review the conceptual model answers only that question and does not
start this lifecycle work. Implement setup, migrations and
seeds with the migration tool the project already uses; if it has none, propose
one, state the choice and ask the user before adding it.

Treat development and a shared validation environment such as staging as
separate environments with separate purposes. State which environments exist and
which are only planned; do not provision a second environment merely to complete
a pair. Adding or repurposing one calls for reviewing credentials, external
effects, retained data and recovery as well as configuration; raise it with the
user before doing so.

## Review and verification

Review identity, nullable uniqueness, valid state combinations, deletion behavior,
time semantics and access against concrete domain cases. For migrations, check
existing data and backfill meaning as well as the empty-schema result. Keep
deployed migrations immutable and follow the project's migration conventions.

Use the project's relevant checks: catalog assertions can cover naming, required
columns and trigger coverage; behavioral checks should cover rejected invalid
states, duplicates, allowed and denied operations, and concurrent writes where
they affect correctness. English names and domain meaning still need review.
Report what was inspected or tested and what remains unverified.

## PostgreSQL references

Check the documentation for the target major version when implementation details
matter: [UUID generation](https://www.postgresql.org/docs/current/functions-uuid.html),
[date and time](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT),
[constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) and
[date/time types](https://www.postgresql.org/docs/current/datatype-datetime.html).
