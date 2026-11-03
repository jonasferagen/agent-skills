# Modules and surfaces

## Give an internal API a cohesive home

Group related TypeScript exports by a responsibility callers can name and a
reason to change. A module can contain functions, records and a class together;
neither one export per file nor a fixed directory depth is required. Match
existing naming and file conventions. A helper with one caller may stay local;
a separate test file or a line count does not by itself justify a public API.

When several callers reach into an owner's implementation, decide whether they
need a shared operation, a small stable value contract or different behavior.
Make that boundary explicit rather than simply exporting every helper. Avoid
creating a miscellaneous helper bucket or a central types module with unrelated
contracts. A one-consumer interface can live beside its consumer. Closely
related consumers can share a cohesive contract module when neither should
import the other's implementation.

A type-only module should represent a real contract owner. Do not create a
parallel hierarchy of `types` files that forces a reader to open two files for
every small implementation. Conversely, do not make a low-level consumer import
a large implementation just to name the small value it receives.

When several modules handle the same record, such as a participant or a state
that every adapter extends, give its type one owner. Variants that add fields
should extend it, as in `Base & { extra: T }`, not restate it. Decide that owner
before typing work is split by file or by worker. Otherwise each part tends to
invent its own near-copy, and the copies drift until someone has to reconcile
them. A near-duplicate type found during review usually means a contract is
missing at its owner.

## Treat exports as a supported surface

Use a barrel when it supplies a useful subsystem or package entrypoint, not
because every directory needs one. Direct imports within an owning area can be
clearer. Prefer explicit exports at a supported boundary when wildcard exports
would expose internal helpers. Type exports are public contracts too: changing
them can break consumers even though they emit no JavaScript.

Do not use an area's public barrel from its own implementation by default: it
can pull unrelated siblings and initialization back into the dependency graph.
Trace the actual graph before changing a working import. Internal direct
imports and external supported entrypoints serve different callers; respect
an existing boundary instead of bypassing it for convenience. A local module
refactor does not authorize changing a package's distribution contract.

## Separate type edges from runtime edges

Type-only imports can remove an unnecessary runtime edge. They do not establish
that the underlying responsibilities are sensibly divided. For a cycle, trace
which module reads a runtime value during initialization, which only names a
type, and who should own the shared contract. Move a neutral contract to its
cohesive owner, invert the dependency through an explicit input, or use a
supported entrypoint as the actual design requires. Dynamic imports should
serve deliberate deferred loading, not disguise a structural dependency.

Keep importing a reusable module free of application startup: opening clients,
reading browser storage or launching work belongs at an explicit entry or
composition boundary. This is especially useful for code shared by a CLI and
a browser adapter. Some plugins deliberately register on import; preserve that
contract where it is intentional and keep the effect discoverable to callers.

Module syntax, extension spelling, ESM/CommonJS and emitted paths follow the
project's runtime and compiler setup. A structural cleanup should not silently
switch the module system. Check imports against the emitted or bundled artifact
when execution depends on the changed surface; a type-only check cannot prove
initialization behavior.

Primary references: [TypeScript module execution model](https://www.typescriptlang.org/docs/handbook/modules/theory.html)
and [type-only import/export syntax](https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html).
