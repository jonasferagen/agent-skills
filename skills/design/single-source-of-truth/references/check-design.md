# Designing a consistency check

## Choose the claim and owner

Name the failure the check protects, its responsible owner and its declared
inputs before implementing it. Consistency checks commonly protect different
claims:

- **Publication:** a generated or exported artifact matches the authoritative
  source revision selected by its publisher.
- **Consumer adoption:** the installed artifact matches the consumer's immutable
  pin, and the consumer satisfies the contract it adopted.
- **Integration:** explicitly selected participants and settings are compatible.

Do not replace these with equality to a live upstream head. A consumer can
correctly use an older supported contract. Its normal check uses declared
artifacts rather than discovering sibling checkouts or private services.
A compatibility or support policy may require an upgrade; name that separate
policy and the evidence it needs.

## Keep the check durable

A retained check must:

- Protect a named consequence at a proportionate cost.
- Read each structural fact from its owning declaration or selected publication.
- Record enough revision and integrity information to reproduce its comparison.
- Resolve local inputs from its own location or an explicit declared root.
- Give its tests isolated fixtures rather than requiring a neighboring checkout.
- Distinguish disagreement, missing prerequisites and unmeasured behavior.

For parity within one selected revision, compute the answer from those inputs
when the check runs. Avoid a hand-maintained golden that merely copies current
file sets, member lists or counts. A pinned published contract is different: it
records a dependency selection, and remains valid until adoption changes.
Independent literal behavioral expectations are also legitimate oracles.

| Ask of the check | Response |
| --- | --- |
| Is there no concrete consequence to protect? | Do not add it until that consequence is clear. |
| Can cheaper evidence observe the same consequence? | Use that evidence. |
| Can unrelated changes make it fail? | Narrow the trigger or explain the proxy's cost. |
| Does it repeat a list or count already declared by an input? | Read that declaration at the selected revision. |
| Does it require live sibling internals for a local claim? | Replace that dependency with the adopted publication or move the claim to explicit integration verification. |
| Does it depend on where the caller launched it? | Resolve its own location or accept an explicit root and report it. |
| Does a missing prerequisite look like drift? | Report the absence at the boundary that owes it; do not assert parity from empty output. |
| Does it only report findings? | Identify who acts on them and when; do not claim required prevention without a gate. |

Read [checks that survive restructuring](durable-checks.md) when implementing
the check. Verify a representative failure as well as the passing case.
Generation parity and contract conformance do not prove the contract is correct;
retain independent behavioral evidence for the consequences that matter.
