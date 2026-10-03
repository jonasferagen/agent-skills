# Run records

Use this reference when an operation needs retained evidence of what it consumed,
which stages completed and what it published. A read-only function returning a
value does not need a receipt system. Choose fields from the actual recovery and
handoff questions; no common schema or helper library is required.

## Record what happened

Identify the attempt separately from the input revision and result. For stages
whose partial completion matters, distinguish not started, running, passed and
failed. An interrupted running stage has an unknown outcome until reconciled;
absence of a failure record does not mean success. Preserve relevant diagnostics
and earlier attempts. Record technical completion separately from acceptance.

When byte identity matters, record SHA-256 and byte length for the bytes actually
consumed, with paths relative to an identified input root. Include relevant
configuration and tool versions. If hashing parsed/canonical data, state that
representation separately from the original file hash. A digest identifies bytes;
it does not establish their provenance, safety or suitability.

## Publish at a defined boundary

A temporary sibling file followed by replacement can prevent readers seeing a
partially written record. It does not make several file replacements one
transaction, prevent competing writers or by itself guarantee power-loss durability.
Choose the publication boundary for outputs and their record together: a staged
revision, transaction, or an explicit recovery procedure may fit. State the writer
model and retain enough evidence to reconcile interruption at that boundary.

Do not publish completion before required output identities and completeness are
checked. Define what repeating an attempt or reusing a revision with changed
inputs means; an unchanged result must still satisfy the checks its caller relies
on. External submissions also need the uncertainty handling in
[external integrations](external-integrations.md); a local receipt cannot make a
remote effect atomic or safe to retry.

## Verify preservation where promised

If source must remain unchanged, define the comparison scope and exclusions.
Identify the copied bytes and check for changes during capture; compare relevant
source state after the operation, including failure paths where possible. Record
unknown when either observation is unavailable. Equal before/after hashes show
matching observed states, not that no intermediate mutation occurred. A difference
alone does not attribute the edit to this operation. Stronger isolation needs an
appropriate snapshot or writer-control mechanism.

Exercise the consequential gap: interrupt publication, change an input during
capture, or repeat a revision with conflicting content. Verify both the record
and the outputs, then state which recovery and concurrency guarantees remain
untested. Surface a demonstrated gap in the owning work record; do not expand a
small operation into a general job framework without a current need.
