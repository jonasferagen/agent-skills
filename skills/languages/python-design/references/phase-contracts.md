# Phase contracts

## State what each handoff guarantees

For each meaningful stage, identify its input assumptions, output guarantees,
expected failures and effects. A parser may validate a wire representation;
resolution may establish identities and references; construction may produce
objects ready to serialize. Name the actual guarantees in the program rather
than copying a fixed list of stage names.

Return a representation that downstream callers can use without reconstructing
how it became valid. Carry the result of validation forward instead of parsing
and validating the same input again in each stage. Keep revalidation at a real
trust boundary or after mutation that invalidates the earlier guarantee.
Annotations alone do not establish runtime validity.

A separate record is useful when a handoff establishes materially different
invariants. It is unnecessary for every helper or pass. When alternatives have
different required fields, use explicit variants or distinct records rather
than an object whose optional fields mean different things at different times.
Do not assume a frozen record protects nested mutable data.

## Make mutation and evidence ownership explicit

A builder may accumulate mutable working state efficiently. Keep that state
with its owner and expose the result only when the promised invariants hold.
If a stage intentionally changes a shared object in place, make the required
state and mutations visible in its API; avoid invisible dependence on a previous
call having filled a field.

Keep source identity and diagnostic locations through transformations when
callers need to explain failures or audit output. Build evidence should describe
the produced result and its source, rather than requiring consumers to inspect
a partly populated internal builder.

Separate computation from publication or other irreversible effects where that
enables validation before effects. Validate encoded or persisted representations
when conversion can invalidate an in-memory guarantee. The domain decides
which invariants and precision limits matter.

## Preserve differences between versions

Select a format-specific frontend at a clear entry boundary. Share downstream
representations only where their semantics agree; do not erase distinctions
between missing, explicit and inferred values to force one universal model.
Keep compatibility adaptation visible and preserve provenance through it.

For a fixed pipeline, ordinary function calls and explicit results are usually
enough. Registries, plugins or a workflow engine need an actual extension or
scheduling requirement, not just multiple stages.

## Plan a conversion around observable contracts

Start a replacement plan with the public behaviours and artifacts that must
remain compatible, the known defects to correct, and the acceptance evidence.
Characterize successful inputs and refusals, including diagnostic meaning.
Compare old and new results at those boundaries, using semantic comparisons
when byte identity is not required. The old implementation is useful evidence,
not an oracle for behaviour already known to be wrong.

Identify the smallest useful path through the new implementation and the
conditions under which callers can switch. Name who owns routing during any
coexistence, what happens on failure and when the old path can be retired.
Use incremental replacement when stable seams exist; a parallel implementation
can be clearer when the representations change substantially. Do not require
permanent adapters, dual writes or silent fallback to the old implementation.

Keep the plan distinct from execution. State unresolved contract decisions and
the checks needed to resolve them; do not invent commitments, schedules or a
rewrite mandate from an architectural review.
