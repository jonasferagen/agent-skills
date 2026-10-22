# Derivation across boundaries

A boundary changes how a consumer obtains a definition. It does not remove the
need for ownership, nor require access to private internals. Choose an option
from the [rung ladder](definitions.md#derive-instead-of-restate) that preserves
the boundary and the relevant release contract. Examples are synthetic.

## The repository and release boundary

An independently released consumer adopts a published interface, package,
schema or other artifact at an immutable revision. Its local build and behavior checks use declared artifacts and toolchain
inputs without requiring the publisher's checkout or live service. Operations
and integration checks that need a running service declare that prerequisite.

Available: a pinned publication or generated artifact with source revision and
integrity information (rung 2), or a versioned runtime interface when the system
intentionally depends on one (rungs 3 or 4). Record any local transformation or
modification. Let adoption changes follow the consumer's review process.

The publisher verifies that a publication matches its selected authoritative
source. The consumer verifies the artifact it adopted and its behavior against
that contract. A separate integration check selects both participants and
verifies compatibility. A local gate comparing a consumer pin with an upstream
moving head would erase the consumer's adoption decision; do not use it as a
generic drift check.

Reading sibling source can help a source investigation or coordinated change
when authorized. It is not a hidden prerequisite for consumer validation.
Declare any deliberately coordinated release or integration environment and
report its results separately from checks of each repository.

## The language boundary

A rule written in one language may need a different representation in another.
For example, one URL parser may expose brackets around an IPv6 host and another
the bare address. Copying identical strings would not establish identical
meaning.

Available: generate each representation from a selected structured source
(rung 2), consume an agreed data file at startup (rung 3), or deliver the needed
facts through a public interface (rung 4). Validate conversions with independent
examples, including cases where normalization differs.

When manual representations remain, compare them after their stated
normalization (rung 5). The consistency check reads each representation; a
third literal list cannot establish parity. Independently authored behavioral
expectations still have value as oracles.

## The bundle boundary

A browser import can pull in a server's validation library or database driver.
Preserve the dependency direction rather than importing private machinery just
to remove duplicate text.

Available: a dependency-free published module (rung 1 or 2), a generated client
artifact (rung 2), or delivery through the request interface (rung 4). A type-only
declaration may be erased from the runtime bundle, but its build-time dependency
must still be declared and obey the release boundary. Check which facts the
consumer actually needs.

## The process boundary

Shared code receives deployment-specific values through explicit inputs rather
than guessing them. The deployment or configuration owner selects addresses,
schedules and other settings; neither process's private configuration becomes a
public discovery interface merely because another process needs the value.

Available: pass the resolved setting at the edge (rung 1), have both processes
consume an agreed configuration source (rung 3), or use an intentional discovery
interface (rung 3 or 4). Define precedence, validation and availability where the
setting is owned.

If two declarations must agree for a deployment, the deployment's integration
check reads the explicitly selected inputs. If a shared settings source is out
of scope, compare those inputs (rung 5) or record the coordination risk (rung 6).
Do not make every local repository check inspect another process's live config.

## The schema and data-ownership boundary

A database constraint cannot consult arbitrary application code. Some integrity
mechanisms also limit what they can read: for example, a PostgreSQL check
constraint cannot use a subquery. Turning a vocabulary into referenced rows is a
schema design change, not a duplication-only refactor.

Within a service that owns both schema and application, derive from its selected
schema or verify parity there. Follow the project's migration rules: a deployed
migration normally changes through a new migration rather than rewriting
history. Do not infer authorization for a schema change from this guidance.

Across services, consume the owner's published schema or API contract, emitted
events or an explicit export. Reading another service's private tables or
constraints makes those internals a dependency; it is not the default remedy
for drift. An integration test may provision the selected service versions and
exercise their public interfaces when its environment is explicitly declared.

## Make disagreement fail

A retained consistency check needs a named relation and inputs:

- **Read both sides at the selected revisions.** Compare a generated publication
  with its source at publication time, an installed artifact with its adoption
  declaration in consumer checks, or selected participants for integration.
  These are different claims; report which one was checked.
- **Run where the obligation is owned.** A required gate covers changes to its
  relevant inputs and the check itself. An optional or manual check supplies
  evidence when run but leaves that gate coverage absent.
- **Demonstrate detection.** Introduce a representative disagreement, observe
  the expected failure, then undo the mutation. A passing run alone does not
  show that the check detects drift.
- **Prefer direct enforcement when appropriate.** Compiler exhaustiveness,
  database constraints and validated inputs can avoid separately maintained
  checks. They still prove only the properties they enforce.

Use [durable checks](durable-checks.md) when implementing a retained check. When
automated agreement is impractical, record the manual relationship, its owners
and what happens if an update is missed. Do not label intentional version
selection as an unprotected duplicate merely because live upstream is absent.
