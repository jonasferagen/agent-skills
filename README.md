# Jonas’s agent skills

Jonas's reusable, project-agnostic agent skills. Every skill is a standalone
package at `skills/<area>/<name>/`, installed by its name and complete in its
own directory. Areas group skills by their main task for browsing; they do not
require loading every skill in the group, and they are not installation units.
A skill marked (draft) is a first version whose scope is still settling: expect
its contract to change, and read its scenarios for what it is evaluated against.

A package may carry `scenarios/README.md`: the requests, context and expected
behavior it is evaluated against. Ordinary use of a skill does not read it.

A consuming project may install several skills from here together. It owns
its own selection, lock, checks and upgrade rules; this repository supplies the
packages and their versions.

## Authoring

| Skill | Use it for |
| --- | --- |
| [clear-writing](skills/authoring/clear-writing/SKILL.md) | Express facts and instructions clearly without changing their meaning. |
| [diagrams-and-tables](skills/authoring/diagrams-and-tables/SKILL.md) | Choose and verify useful visual explanations of relationships and comparisons. |

## Design

| Skill | Use it for |
| --- | --- |
| [repository-design](skills/design/repository-design/SKILL.md) | Define repository ownership, public commands and boundaries, external references, handoff contracts and independent verification. |
| [single-source-of-truth](skills/design/single-source-of-truth/SKILL.md) | Give each rule a home and derive or check its other appearances. |
| [application-design](skills/design/application-design/SKILL.md) | Shape application operations, internal boundaries, state ownership, injected dependencies and recovery. |
| [service-design](skills/design/service-design/SKILL.md) | Define runtime ownership, public interfaces, caller identity, retry behavior and storage custody. |
| [relational-modeling](skills/design/relational-modeling/SKILL.md) (draft) | Structure known entities around retrieval questions and revise relationships through synthetic scenarios. |
| [postgres-design](skills/design/postgres-design/SKILL.md) | Designing and reviewing PostgreSQL schemas: identity, types, state, timestamps and integrity boundaries, and transactions on pooled connections. |

Repository-design applies to content, library, application and infrastructure
repositories. Application-design and service-design specialize the decisions
inside applications and across running services; each package works alone.
Boundary contract review and external-reference discovery are part of
repository-design. Consumer adoption remains explicit and pinned.

## Operations

| Skill | Use it for |
| --- | --- |
| [service-classes](skills/operations/service-classes/SKILL.md) (draft) | Decide whether a capability is a service and whether it is running or scheduled, what evidence each class owes, and what a status report may claim. |
| [database-migrations](skills/operations/database-migrations/SKILL.md) | Preserve migration history, review baselines and verify database bootstrap and upgrades. |
| [docker-cli](skills/operations/docker-cli/SKILL.md) | Write or review a single container or image command: ports, secrets, mounts, labels, identity and the cleanup of what it created. |
| [docker-compose-cli](skills/operations/docker-compose-cli/SKILL.md) | Write or review a compose command and the file it reads: project selection, inherited environment, borrowed definitions and project-scoped teardown. |
| [docker-cleanup](skills/operations/docker-cleanup/SKILL.md) | Audit a Docker host's accumulated images, volumes, networks and build cache, and reclaim space by attributed owner and tier. |

Service homes, document shapes, control commands and their checks are the
consuming project's own, and service-classes states only what a
service and its status owe. Promotion from a spike to maintained service use
selects service-design for runtime boundaries and service-classes for
classification, as the work requires.

The three Docker packages split one tool by the moment it is used: assembling a
command, driving a project of containers, or accounting for what a host has
accumulated. Each is standalone and carries its own copy of the identity,
label-over-pattern and prune-refusal rules they share. The outcomes a project's
containers must meet — lifecycle, state custody, image pinning, composed sets —
are project decisions rather than CLI usage and belong to the consuming
project.

## Verification

| Skill | Use it for |
| --- | --- |
| [repository-maintenance](skills/verification/repository-maintenance/SKILL.md) | Review structural and semantic drift across a repository's responsibilities, instructions, implementation, checks and open work. |
| [verification-design](skills/verification/verification-design/SKILL.md) | Choose evidence for a change or milestone and consolidate checks by the failures they detect. |
| [test-writing](skills/verification/test-writing/SKILL.md) | Writing unit tests, integration tests and their fixtures, with made-up data and state each test owns. |
| [test-audit](skills/verification/test-audit/SKILL.md) | Auditing a settled test suite for brittleness, coverage asymmetry, weak assertions, mock drift and non-determinism. |

Choose by the requested task; new regression work does not require a suite audit.
Repository-maintenance assesses an existing repository's coherence; it does not
own project governance, maintenance scheduling or local document shapes.

## Languages and runtimes

| Skill | Use it for |
| --- | --- |
| [node-patterns](skills/languages/node-patterns/SKILL.md) | Preserving child-process outcomes, exit status and output in Node scripts, command-line tools and test harnesses. |
| [python-patterns](skills/languages/python-patterns/SKILL.md) | Python types, runtime boundaries, numerical comparisons, defaults, exceptions, resource cleanup and async tasks. |
| [python-design](skills/languages/python-design/SKILL.md) | Python program structure: responsibilities, phase contracts, state ownership, shared interfaces and naming. |
| [bash-patterns](skills/languages/bash-patterns/SKILL.md) | Preserving arguments, command failures, query results and cleanup ownership in Bash scripts. |
| [godot-gdscript](skills/languages/godot-gdscript/SKILL.md) (draft) | Typed Godot scripts, headless probes, imports and scene measurements. |

The Python patterns and design skills pair naturally; each works alone.

## Using a skill

[Install and pin a complete package](docs/packages.md#using-a-skill) through the
consuming project's normal review process. During ordinary use, follow the
installed skill and project instructions; source maintenance guidance is for
editing, upgrading or investigating the source.

## Maintaining this repository

Read [AGENTS.md](AGENTS.md) before editing. Select the guide for your task;
inspect headings in a long guide and read the relevant sections, including their
prerequisites and required references.

<a id="selection"></a>
<a id="adding-a-skill"></a>
<a id="maintenance-checks"></a>
<a id="where-a-package-keeps-its-checks"></a>
<a id="evaluating-a-skill-against-its-scenarios"></a>
<a id="discovery-and-routing"></a>
<a id="routing-quality"></a>
<a id="routing-trial-method"></a>
<a id="skill-releases"></a>
<a id="release-review"></a>
<a id="authoring-skills"></a>
<a id="origins"></a>
<a id="attribution"></a>
<a id="moves-and-retirements"></a>
<a id="current-maintenance-notes"></a>

| Task | Authoritative guidance |
| --- | --- |
| Add or change a package, its name or selection trigger | [Package authoring](docs/packages.md#adding-a-skill) and [selection](docs/packages.md#selection) |
| Run the source gate | [Maintenance checks](docs/verification.md#maintenance-checks): Python 3.11+, Node 24, `python3 scripts/check.py` and `git diff --check` |
| Change entrypoints, triggers, shared guidance or packaging | [Routing acceptance and fresh-agent trials](docs/verification.md#routing-quality) |
| Evaluate a skill's scenarios | [Scenario evaluation](docs/verification.md#evaluating-a-skill-against-its-scenarios) |
| Version or tag a skill | [Releases](docs/releases.md), including the applicable release review |
| Upgrade a retired or moved skill, or inspect attribution | [Origins and replacements](docs/origins.md) |
