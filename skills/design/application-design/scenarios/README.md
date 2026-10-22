# Application design scenarios

Requests, context and expected behavior this skill is evaluated against. Ordinary
use of the skill does not read them. Record observed results with the change that
ran the evaluation, not here. Names and systems below are synthetic.

## Shared operation and private helpers

Request: Review a CLI, UI handler and maintenance command that each select inputs,
validate and publish a report. The maintenance command calls the CLI's private
selection and publication helpers and reimplements its validation.

Expected behavior: Compare the rules and effects across the entrypoints. Propose
one owned operation and thin adapters; convenience workflows call or compose that
operation. Preserve legitimate caller differences. Do not merely export the
helpers or add a workflow framework. Explain which tests observe the shared rules
and which check each adapter's translation.

## Importing a dependency's private models

Request: A scheduling application imports `Planner` and `Preview` source classes from
a separate simulation component to evaluate an arrangement. A changed private
constructor broke the application. Its published evaluator accepts a scenario
record and returns a score with warnings.

Expected behavior: Identify the application's need as evaluation, and the
supported scenario-and-result seam as the dependency interface. Inject an adapter
that calls it and maps the result into application terms; keep consequential
warnings. Trace one application behavior with a local double and one separate
interoperability check against the published evaluator. Do not reconstruct the
provider's evaluation rules locally, assume a reachable source tree is a public
API or prescribe repository consolidation from this application question.

## Saved checkpoints whose meaning changes

Request: A puzzle editor saves a checkpoint with a board identifier and piece
coordinates. The next release changes board geometry and movement rules. Its
loader accepts the old JSON, and a proposed cleanup would drop the old board
revision because the schema has not changed.

Expected behavior: Trace an old checkpoint under the new interpreter and identify
the lost meaning. Keep the board and rule revision needed to interpret saved
state, then choose an explicit compatibility check, migration, retained
interpreter or rejection from the product obligations. Preserve recoverable
original state. Parsing and a valid schema do not establish semantic compatibility;
a version field alone does not prove migration correctness.

## Ordinary tests need a provider checkout

Request: Make report-generation unit tests work without checking out a provider's
repository. They currently import its private result classes, and no external
calls run during these tests. The provider publishes an API and a client package.

Expected behavior: Test application decisions using representative public inputs
and a supplied double at the dependency seam. Adapt the real client at construction
and keep provider-specific result objects there. Keep a separately identified
interoperability check against an actual supported client/API version. Do not
claim that mocks establish compatibility, replace the public client with copied
provider rules or make an ordinary application test fetch a source checkout.

## External lookup with hidden effects

Request: Design an availability lookup that a provider labels as preflight.
Its actual contract says each call uploads the supplied document and consumes
quota, while the proposed design treats it as a free local validation.

Expected behavior: Check the operation's real contract and effects even though
it returns no retained output. Expose the transmission and quota use, separate
local preparation from that call and preserve the authorized scope. Do not
require the full submission recovery workflow for an ordinary lookup.

## External submission with a lost response

Request: Design one operation that submits a rendering job to an external API and
retains its deliverable. A timeout can occur after submission but before a job ID
is saved.

Expected behavior: Reach external operation guidance. Keep retained local intent
and attempt identity distinct from proof of provider receipt. Treat the lost
response as unknown; use supported reconciliation and avoid hidden automatic
resubmission. Verify supported lookup, idempotency, cancellation and output
retrieval before relying on them. Retain output bytes and companion files before
claiming custody; quality acceptance remains with the receiving owner. Separate
design, application tests and evidence from real provider execution.

## Local publication and acknowledgement

Request: Design an operation that receives uploaded files into a local directory
and acknowledges them. Repetition and an interrupted write are possible.

Expected behavior: Define completeness, publication and acknowledgement without
adding provider job mechanics or a quality judgment. Publish bytes and their
record before acknowledging; handle repetition and conflicting content under one
identity, and establish how competing writers are prevented. Select the actual
storage and recovery guarantees and identify evidence still needed.

## Saving, previewing and accepting

Request: Simplify an editor that requires manual export before every preview and
a passing preview before saving. Its catalog uses one `valid` flag for checksum
integrity, remote storage confirmation and runtime admission.

Expected behavior: Distinguish coherent preview input, durable draft and derived
output; consider direct preview input and saving independently from preview while
preserving product obligations and useful interchange export. Share lookup and
storage mechanisms while keeping integrity, custody and admission guarantees
separate. Execution success does not establish acceptance or downstream adoption.

## Nearby work and evidence limits

- A literal sentence change in an application's README needs no internal design
  pass. A repository ownership decision or transport-specific error mapping needs
  its own scope; this package does not choose it through application abstraction.
- An example resolving a relative path is evidence of that example, not adoption
  of a general path-resolution rule. Identify the missing rule before depending
  on it.
- These synthetic cases can expose inconsistent design. They cannot establish
  actual interoperability, storage durability or provider retry guarantees.
