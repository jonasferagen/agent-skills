# Proposed data-foundations collection

Status: scope proposal, 2 October 2026. A
[relational-modeling draft](../skills/design/relational-modeling/SKILL.md) has completed
a bounded document trial with explicitly supplied dependencies. This does not establish an
Atlas model or implement the proposed collection. See
[trial evidence](../validation/relational-modeling.md).

## Starting situation

The project has a rough brief, known entities and retrieval questions. The next
task is to structure their relationships and database representation. In the Atlas
example, PostgreSQL is chosen, retrieval comes before CRUD, there is no UI, and
the application language and stack remain deferred. Future container packaging
informs choices but does not require a container implementation now.

“Read-only” describes application behavior. Schema migrations and synthetic seed
loading have separate write responsibilities to address when their work begins.
Choosing PostgreSQL does not settle local connection policy, provisioning or runtime
credentials; record those choices when needed rather than inferring them.

## Proposed responsibilities

| Task and trigger | Guidance | Treatment |
| --- | --- | --- |
| Turn known entities and retrieval questions into a relational model; revise an ambiguous relationship | `relational-modeling` | New workflow candidate. Own the iteration, open questions and readiness for implementation. |
| Choose PostgreSQL representation: keys, types, constraints, naming and data lifecycle | Existing `postgres-design` | Reuse relevant guidance. Separate design conventions from the broader modeling workflow; review its current migration/transaction scope before packaging. |
| Explain entities, roles, cardinalities and optionality | Existing visual selection and ER reference | Reuse `diagrams-and-tables` and its `references/er/` guidance. The model owns semantics; diagram guidance owns representation and checking. |
| Plan schema bootstrap, baselines or upgrades | Existing `database-migrations` | Load when migration strategy or implementation is in scope, not merely because a model contains tables. |
| Choose synthetic cases that expose model behavior | A scenario/seed reference supporting modeling | Begin with a reference. Dataset design is distinct from test-framework fixtures and from loading data into a running database. |
| Establish database document homes and terminology | Existing `project-docs`, `clear-writing`, `source-of-truth`; domain-modeling ideas | Reuse foundation authoring. Adapt useful domain-modeling guidance without inheriting fixed glossary paths or mandatory ADRs. |

## The new workflow's boundary

`relational-modeling` would start with a brief and end with a model whose decisions
can be implemented or whose blocking questions are explicit. Its useful work is:

1. Connect each retrieval question to the information and relationships needed.
2. Examine identity, roles, ownership, cardinality, optionality and lifecycle.
3. Separate domain meaning from PostgreSQL representation and record assumptions.
4. Challenge the model with small synthetic cases, including missing, multiple
   and conflicting relationships where relevant.
5. Reconcile the model, glossary and retrieval scenarios; identify what remains
   undecided before SQL, migration or application work.

An ER diagram alone is not the outcome. Conversely, a coherent model does not
prove that migrations run, permissions hold or a retrieval performs adequately.
The workflow should support both an initial model and a focused change to one
relationship without forcing a full review of every entity.

## Document responsibilities to exercise later

| Project artifact | Owns |
| --- | --- |
| `docs/database/README.md` | Orientation, status and routes once there is enough material to need them |
| `docs/database/model.md` | Intended entities, relationships, invariants and the canonical ER view |
| `docs/database/scenarios.md` | Retrieval questions and synthetic cases used to reason about the model |
| `docs/project/glossary.md` | Domain meanings that need an explicit shared definition |
| `docs/database/migrations.md` | Agreed bootstrap/upgrade approach when addressed |
| `docs/database/seeds.md` | Dataset purpose, coverage and loading approach when addressed |

These are proposed homes, not a requirement to create six empty documents. Keep
scenario design and model review small. SQL will own the executable schema once
implemented; the model document owns intended semantics and unresolved gaps.

## Organization and dependency boundary

Use `data-foundations` as the provisional working name for this group of skills.
The project's framework supplies policy and authority; `clear-writing`,
`source-of-truth` and `diagrams-and-tables` supply authoring and visual
guidance. Avoid copying those skills into a second independently maintained
home.

Collection-to-collection dependency resolution is not implemented: today's package
validator permits references only within an installation unit. Before packaging,
choose how complete dependencies are installed, pinned and routed. For the next
design trial, supply the existing guidance explicitly and record that setup;
do not claim a working collection dependency mechanism.

Keep container runtime setup, application patterns/languages, API transports,
query tuning and broad operational audits outside the initial modeling route.
Select them when a concrete task reaches those subjects.

## First bounded experiment

The [trial record](../validation/relational-modeling.md) covers an initial model,
a relationship correction and a nearby wording task. The documents stayed aligned
while keeping unresolved decisions visible. The initial reading cost exposed a
broad visual-guidance route; the record proposes a focused comparison before
changing it.

The trial did not implement a database or validate an environment. PostgreSQL
representation, migrations, seed loading and runtime setup remain later work.
