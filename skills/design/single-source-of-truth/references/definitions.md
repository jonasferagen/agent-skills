# Choosing an authoritative definition

## Name the concept

Name the concept with one question the system answers. For example: which
statuses may an order have? What shape does an identifier have? Which address
does this deployment select for a service? If the question needs an "and", it
may combine concepts that need different owners.

The question determines what counts as an appearance. Similar strings can
answer different questions: the publisher's supported protocol version and a
consumer's adopted version have different owners. Do not unify them merely
because their values happen to match.

## Find the homes

Search the relevant owned tree and declared inputs for each way the concept is
expressed. Values may appear with different quoting, separators, case or display
labels. Include schemas, configuration, build files, tests and prose. A document
that lists a vocabulary can guide behavior just as code does.

Trace declared provenance across a repository boundary. Use the publication or
contract that the consumer actually adopts; inspecting publisher internals may
help an authorized source investigation, but is not a prerequisite for ordinary
consumer work. A sibling checkout's presence does not make it an input.

History can reveal drift: an extension that updated only one maintained copy
shows a missed obligation. A consumer pinned before that extension may instead
be behaving correctly for its adopted revision. Establish which happened before
proposing a fix.

## Decide which prose claims to keep

Before consolidating a changing claim, ask whether the reader needs it. Omit
incidental status from maintained prose rather than maintaining a more accurate
copy. An overview may explain how to find releases without saying whether one
exists. If availability matters, link the release listing directly with enough
context to use it; do not add a chain of summaries.

Keep limitations and uncertainty that qualify the contract the reader uses.
Distinguish a required guarantee from observed support. A dated report retains
its assessed revision and conditions even after the current answer changes.

For necessary prose maintained by hand, identify its owner, scope and update
triggers. If ownership is unknown, state that gap and propose the owner of the
contract it describes. Keep the maintained set small enough to update reliably.
Supporting documents explain their own subject and point to the appropriate
home or selected revision rather than maintaining another inventory.

## Choose the home that decides

Identify who may change the rule and how it reaches consumers. Within one
application, the deciding mechanism may be a database constraint, a schema or the
configuration a process reads. Application code that filters stored values is
downstream of the mechanism that admits them.

Across independently released repositories, distinguish three decisions:

- The **publisher** owns the definition and publishes a supported contract or
  artifact. Its private implementation is not automatically that contract.
- The **consumer** selects an immutable revision and owns when to adopt another.
  Its lock or equivalent declaration records the source, revision and artifact
  identity; record transformations and local modifications as well.
- The **integration owner** selects participants and checks that the versions and
  deployed settings work together. This may impose a compatibility requirement
  without requiring every participant to use the publisher's latest head.

A pin or imported publication with provenance is deliberate derivation, not a
second authority over the upstream rule. A consumer-specific extension or subset
is a separate policy with its own owner. An unrecorded local edit to an imported
contract creates ambiguity about which rule the consumer implements.

For shared settings and external identifiers, follow
[one owner for a shared value](authoritative-values.md). Ownership includes
precedence, interpretation and requiredness, not just the literal.

Validation stricter than a storage rule may be a deliberate boundary policy.
State that policy and its reason; do not present it as an exact mirror. Do not
choose a convenient copy as the home while leaving the deciding owner unchanged.

## Derive instead of restate

Prefer the least costly option that preserves ownership, dependency direction,
release independence and required behavior. Consider these rungs in order;
a higher rung is unsuitable when it would cross a private boundary or make an
independent release depend on a moving source.

1. **Remove the restatement.** Read the owned declaration through an allowed
   dependency or receive its resolved value as an explicit input.
2. **Derive at build or publication time.** Generate or import from a selected
   source revision. Publish a self-contained artifact with provenance; consumers
   can pin it and verify their installed copy without reading the source tree.
3. **Derive at start time.** Read an agreed configuration or published interface
   and validate the process's assumptions. Use this when availability and
   version compatibility are part of the startup contract.
4. **Derive at request time.** Deliver the needed definition with the data or
   through a public interface. Define versioning and unknown-value behavior.
5. **Check agreement in the responsible gate.** Compare maintained appearances
   with the definition at the selected revision. The publisher checks generation,
   the consumer checks adoption, and integration checks explicit compatibility.
   Apply [check design](check-design.md).
6. **Record manual coordination.** If reuse, derivation and automated checking
   are impractical, name the copies, owners, update triggers and failure risk.

Rungs 1 to 4 reduce independent maintenance; they do not automatically establish
semantic correctness. A generator can be wrong, a publication can omit required
facts and a runtime dependency can be unavailable. Check those consequences
where they are owned. A pin prevents unreviewed updates; it does not prove
compatibility with an arbitrary newer deployment.

## Give machine consumers a structured contract

Reuse an existing structured contract. If none exists, keep machine facts in a
small versioned schema or data format and generate their human view. Prose
layout, table headings and explanatory wording should not become a domain API.
Moving a table to JSON alone does not establish ownership.

If a formal document must remain authoritative, compile its explicit fields into
a structured publication. Validate extraction against the selected document
revision, record provenance and check deterministic generation whenever source
or generator changes. Consumers depend on their adopted artifact; a new document
revision does not silently change that adoption.

Behavior tests may read the structured contract, while document checks verify
rendering or extraction. Preserve independently authored examples and literal
expectations as oracles. Generating an expected answer with the implementation
under test cannot establish that implementation's correctness. Tests of document
syntax or authoring rules still read the document itself.

## Beware the fallback

An unknown value can silently become plausible output through a default, a
filter that fails to match or a catch-all branch:

    // An unhandled code renders as empty, with no error.
    const label = labels[code] ?? '';

Where the adopted contract requires completeness, use exhaustive handling or
explicit failure. Compiler exhaustiveness can catch a missing case at build
time. It proves coverage of the declared type, not that labels mean the right
thing.

A fallback is appropriate for an open vocabulary or a versioned protocol whose
consumer must tolerate new values. State that obligation and test the unknown
case. A consumer that ignores a stored value and always states a fixed answer
can silently lie; prefer an accurate less specific answer when available.

## What is not a second home

Before unifying similar definitions, check these cases:

- **A selected publication.** A pinned artifact answers which revision the
  consumer adopts. A newer upstream publication does not invalidate it.
- **A policy over a vocabulary.** A list selecting some members for special
  treatment answers a different question. A list meant to mirror all members
  still needs derivation or checking against its adopted vocabulary.
- **An independent test oracle.** A literal expected result can check behavior;
  deriving it from the implementation would remove that evidence.
- **Two things sharing a shape.** Similar port lists or identifier patterns may
  have different owners and meanings. Compare their questions first.
- **Repeated uses inside one home.** Several uses of one constant are not
  independently maintained definitions.

Keep separate declarations when unification would create a harmful dependency,
such as importing server machinery into a browser or reading another service's
private tables. Use a published contract, explicit input or proportionate check
rather than making private internals a shared interface.

## Rank by how it fails

Set effort according to the consequence of disagreement:

- Silent false output is harder to detect than a rejected write or failed build.
- Appearances across languages and media are harder to find with one search.
- Growing vocabularies need more care than values fixed for a system's lifetime.
- A complete mirror needs coverage; a deliberate subset needs a clear policy.
- A stale untracked copy differs from an intentionally selected older revision.
  Evaluate the latter against its support and compatibility obligations.

One growing concept copied across media with silent failure deserves more
attention than many uses of a stable constant.
