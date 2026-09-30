# Design review heuristics

Diagnostic prompts to apply when reviewing code — your own work in progress, or
a colleague's. None of these are enforced rules; they are questions worth
asking when the relevant signal shows up. Their value is in the violations they
surface, not in following them mechanically.

This package supplies the prompts, not a review workflow. When the task is to
review a tree, branch, pull request, or diff, follow the repository's review
workflow and use these prompts inside it.

If a prompt fires repeatedly across the codebase, the underlying pattern may
be stable enough to belong in the focused pattern docs. Some entries
below already cross-reference a constructive form there.

## Name vs Type Cohesion

Default: when a parameter or variable is an instance of a project-owned type,
the name follows the type. See
[Name And Type Cohesion](conventions.md#name-and-type-cohesion).
Renames are allowed and useful when they carry meaning the type cannot
(`target: Player`, `from`/`to`, `current`/`previous`).

**Diagnostic:** when many call sites accept the same project-owned type and _every_ parameter is renamed the same way, ask:

- Is the type misnamed? Maybe the class name should follow what callers naturally write.
- Is a missing wrapper or domain concept hiding here? Callers may all be talking about a higher-level concept that the existing type is only the implementation of.
- Or is the rename genuinely contextual at each site? Then leave it.

Third-party types are exempt: naming a vendor `Group` parameter `layoutGroup`
is descriptive, not divergent—the project does not own `Group`, so there is no
project type to rename in response.

The constructive forms of this rule are
[Parameter Objects](utilities-and-data.md#parameter-objects) for
call-site clarity and
[Parameter Bundling](utilities-and-data.md#parameter-bundling) when
parameters travel together as a unit.


## Passive Type Carrying Behavior

Interfaces, type aliases, and DTOs describe shapes; they should not force every
caller to rediscover how that shape becomes valid domain data.

**Diagnostic:** when a call site builds the same object shape with conditional
spreads, optional-field checks, merge/defaulting logic, derived min/max or
dimension calculations, or "complete enough to become X" tests, ask whether the
type should be a class or value object.

**Action prompt:** classify the shape before suggesting a fix: runtime domain
data, wire DTO, passive boundary contract, or conversion boundary. Runtime
domain data usually wants the class/value-object path described in
[Classes and Managers](class-shape.md#classes-and-managers).
Wire DTOs and passive contracts stay passive, but construction/defaulting
behavior should still have a named owner.


## Bare Function For An Operation

When a module `export function`s a stateless verb-on-data operation (engrave,
resolve, compute, extract, total), it reads as an exemption from the class-shape
rule — but purity is not the test.

**Diagnostic:** an exported bare function that _does_ something to data, and
falls under none of the narrow exceptions
[Classes and Managers](class-shape.md#classes-and-managers) lists, is an
operation in the wrong shape — even a pure geometry/math kernel.

**Action prompt:** an operation is a class, `Domain.operation()`, per that same
section. Flag the exported bare operation and name the owning class.


## Compatibility Shims

Compatibility shims need a named external consumer or guarantee. Without one,
they cost documentation, surface area, and time new contributors spend asking
why they exist. Check the repository's deployed consumers and compatibility
guarantees. When every consumer can change in the same release, update the
surface and its call sites together. Keep a transition only when a named live
consumer or published contract requires it, with a clear removal condition.

**Diagnostic:** when changing a shim, check whether a live consumer still
justifies it. If not, delete it with the old surface.

Example smell: an empty compatibility subclass with no remaining consumers earns
nothing; delete it instead of preserving the old name as a facade.


## Stale Cross-References In Comments

A comment that names another part of the code with an explicit file-path string
(`see client/input/KeyBindings.ts`) goes stale the moment that file moves — no
tool updates it.

**Diagnostic:** when a comment references a symbol by hand-written path instead
of `{@link Symbol}`, flag it. Use the symbol link, which resolves and survives
renames. A path is only acceptable when there is no symbol to target (a config
file, asset, or route). Constructive form:
[Cross-References In Comments](conventions.md#cross-references-in-comments).


## Accretion On A Shell Or In-File Family

Accumulated file state is easy to miss because a large shell is built from many
locally tidy edits. Two visible signs predict that growth reliably.

**Diagnostic:** the change adds the _Nth near-identical sibling_ to a family
inside one file—another panel, handler, or adapter cloned from the previous one.
The second or third sibling is the extraction point: mint the
shared helper per
[Sibling Families](class-shape.md#sibling-families-a-list-not-a-class-per-instance),
and ask whether a family worth a helper is worth its own module.

**Diagnostic:** the change adds a **field + constructor wiring + a public
method** to a long-lived shell or orchestrator in one change. That trio is a
collaborator being inlined. The feature likely belongs as (or inside) a class
beside the shell, per
[Lifecycle Orchestrators](orchestration.md#lifecycle-orchestrators).
Inline `emitter.on(...)` registrations carrying real behavior in a constructor
are the same smell in event-subscription form, and they tend to skip the
symmetric dispose a named subscription owner would provide.

A repository may use a warn-level file-size check to catch growth these prompts
miss. Treat it as a signal to apply these prompts, not as a limit to get under
by moving lines into an arbitrary helper.
