# Checks that survive restructuring

A consistency check can become another restatement if it copies the structure
it examines. Build it around the claim and declared inputs identified in
[check design](check-design.md). The
[rung ladder](definitions.md#derive-instead-of-restate) helps decide whether a
check earns its maintenance cost. Examples are synthetic.

## Compute from the selected inputs

Read structural facts from their declarations when the check runs. For
publisher generation parity, compare output with the selected source and
transformation. For consumer adoption, compare the installed artifact with the
pin and integrity record. For integration, compare or exercise the explicitly
selected participants. Name those revisions in the result.

- **Breaks:** a scanner compares a fresh file count with a committed expected
  count that must be updated for every legitimate restructure.
- **Holds:** a check derives the expected file set from the build manifest and
  compares the resulting artifact; a consumer verifies an installed package
  against the digest recorded for its selected immutable publication.

A hand-maintained structural snapshot meant to follow current inputs is a
fragile golden. A pinned dependency is an adoption decision; a publication newer
than the pin does not make it stale by definition. Do not turn consumer checks
into live-head equality gates. Check provenance and integrity, then test the
consumer's obligations under its adopted contract.

Independent literal behavioral expectations are valid oracles. A test that
states the result an operation should produce can catch a mistake shared by the
implementation and generator; generating that expectation from the same logic
would lose the evidence.

A **shrink-only ledger** is a bounded exception: it names known debt in its own
repository, rejects new or increased violations and may only get shorter. It is
not a moving baseline to update whenever structure changes.

## Anchor to the owned tree or explicit input

A check must not inherit its subject accidentally from the caller's working
directory. Resolve the repository containing the check from its own location,
or accept a declared root as an explicit input. Scope inventory queries to that
root: commands such as `git ls-files` otherwise return a caller-relative set.
Report the root and set measured so a partial scan cannot appear to cover the
whole tree.

- **Breaks:** a check measures a subdirectory and reports whole-repository
  success; a test assumes a fixed path to a real sibling checkout.
- **Holds:** a local check anchors to its owning module and resolves its inputs
  through its manifest; an integration check receives participant locations and
  revisions through explicit environment configuration.

Repository-relative paths and declared artifact inputs are valid. Guessing
another repository's host path from a familiar workspace layout is not.

## Read the declaration rather than copying it

Each structural fact has an owner. Read the selected manifest, configuration or
published contract rather than retyping its directory list, member list or
count into several scripts.

- **Breaks:** four scripts hand-maintain the same build-directory list, or a
  parity test adds a third literal vocabulary instead of reading both inputs.
- **Holds:** the check reads the same selected manifest as the build, or reads
  the consumer's dependency declaration and verifies the installed bytes.

A check still needs an independent oracle when its claim concerns behavior
rather than equality of representations. Reading the declaration establishes
the selected contract, not whether its promises are correct or useful.

## Fabricate the fixture

Tests of a check create isolated fixtures and control the external commands or
interfaces they exercise. They should not depend on optional checkouts, running
services or unlisted host tools.

- **Breaks:** a local checker test reads a real neighboring repository or queries
  another service's private database to obtain its expected values.
- **Holds:** the test builds a temporary tree, installs a synthetic pinned
  publication and stubs required commands. It exercises both agreement and a
  representative disagreement without touching real consumer data.

An integration test can provision selected services and exercise their public
interfaces when that is its stated subject. Declare that environment and report
its evidence separately; fixtures alone do not establish deployed integration.

## Report an absent dependency as absent

Distinguish "could not run" from "ran and disagreed." Name missing prerequisites
at the boundary responsible for providing them.

If a required local or integration check needs an artifact, tool or service,
absence prevents acceptance. Fail with that explanation rather than interpreting
empty output as drift or reporting success. Fix the provisioning obligation
where it is owned.

If a check is genuinely optional in the current environment, it may exit with a
prominent notice that it did not run. Report the resulting coverage gap; do not
count that skip as evidence of agreement. A missing live publisher is irrelevant
to a local check whose declared inputs are available pinned artifacts.

- **Breaks:** a missing tool produces an empty inventory that is reported as
  contract disagreement; an optional integration check silently skips.
- **Holds:** a prerequisite check identifies the missing required tool, or an
  optional check clearly reports that integration was not measured.

## Keep enforcement with the owner

Put repository-local checks in the repository whose obligation they protect.
Derive its file set from version control and declared build inputs. A scanner
that hard-codes workspace topology must change whenever an unrelated checkout
moves, so it cannot establish repository independence.

The publisher owns checks of its generated publications. Consumers own checks
of their selected dependencies and their use of those contracts. An integration
owner can keep an explicit environment and compatibility suite across selected
participants. Do not make those three responsibilities depend on a universal
scan of private source trees.

A check required before merge or publication prevents a covered defect only
when it runs for all affected inputs. Manual checks and reports can still guide
a decision; name their reader and action, and do not describe them as an
unconditional gate. Demonstrate the retained check's detection by causing a
representative failure and reverting it.
