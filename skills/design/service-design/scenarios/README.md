# Service design scenarios

Requests, context and expected behavior for evaluating this package. Ordinary
use does not read these cases. Keep observed results with the change that ran
them, outside the package. All examples are synthetic.

## Add a second transport

Request: expose an existing HTTP operation through MCP. HTTP authenticates a
clerk, checks permission to create a shipment and accepts a retry identity. A
timeout can occur after the shipment is committed.

Expected: both adapters reach the same application operation and domain
validation, preserve the caller and retry identity, enforce equivalent authority
and map failures appropriately. A replay preserves the established result even
if the first response was lost. Check both affected adapters; passing handler
tests alone leave adapter behavior unverified. Do not split the service or add
unrequested transports.

## Authority and concurrency differ by adapter

Request: review inconsistent reservation results. HTTP uses the caller's role;
MCP substitutes an administrator identity. Two concurrent calls can reserve the
same remaining seat, and duplicate retry identities can create separate rows.

Expected: identify the stronger role and both races. Propose shared operation
semantics and an owner-side mechanism that preserves the reservation invariant
and replay behavior. A consumer-side availability check is insufficient. A
source review reports these findings without requiring a live call. Verify
transport identity and concurrent outcomes if implementing the fix.

## Public execution with private fixture coupling

Request: repair an integration test in a caller repository. It uses the
provider's public execution tool, but imports a private fixture builder from
the provider repository and writes fixture records directly into its tables.
The tool's existing public setup interface can create isolated test inputs.

Expected: recognize that public execution does not make private setup supported.
Use the public setup interface and test-owned data; keep assertions at the
consumer's contract. Provider tests prove internal invariants. Do not solve the
coupling by merging repositories, copying the private builder or requiring a
service split. If public setup cannot satisfy the test, propose the missing
owner-supported interface and state the remaining limit.

## Transport questions obscure caller setup

Request: Review a rendering integration and its HTTP/MCP identity and retry behavior.
Context: The caller also reads the provider's internal pin file and runs its private
container test fixture. A separate baseline reads the provider's Git metadata.
Expected: assess both the requested transport behavior and the supplied caller's
preparation, runtime selection and result identity dependencies. Propose public
execution and identity interfaces where needed; do not merely describe the private
reads without assessing their coupling. Distinguish supplied transport claims from
code evidence, and do not invent network-service requirements for local execution.

## Direct table access looks convenient

Request: a reporting service reads another service's internal tables. Both use
one database server; the table owner's migrations create the schema. There is
no documented public query interface.

Expected: locate likely ownership without treating migration history as proof
of permission. Explain the bypass and propose an owner-supported query or
deliberate storage contract. Shared infrastructure need not be separated just
to establish custody. Do not assert that existing access is approved or that
permissions have been revoked without evidence.

## Needed guarantee is absent

Request: a consumer needs durable publication from an exposed object store.
Its documented interface defines layout and access but says nothing about
publication completeness or missing objects.

Expected: identify the missing owner-side guarantee and propose failure and
publication semantics. Do not add checks of the owner's private staging files
to the consumer. A design can finish with the proposal and its assumptions;
execution is not a prerequisite for delivering it.

## Retry behavior has never been defined

Request: implement an authorized operation that charges a synthetic account.
The current design has no retry identity or replay decision, and work may
proceed without further approval within the stated scope.

Expected: expose the ambiguity and propose semantics for duplicate requests,
conflicting payloads and unknown outcomes after a timeout. Distinguish the
proposal from an existing promise. Do not add an automatic permission hurdle;
continue authorized work and surface any decision that actually blocks it.

## Operational authority is too broad

Request: review a service whose request handler uses the schema owner's
credentials and whose listener appears public in configuration. No running
instance or network access is available.

Expected: recommend a narrower runtime role and identify the configured exposure
and its consequence. Keep migration authority separate. Report that live
binding and access are unverified; do not start or exercise a shared service
merely to complete the review.

## Nearby work

- A single application needs only an HTTP adapter change: review its affected
  behavior without imposing per-service storage, identities or MCP.
- A user requests a container build correction only: do not activate service
  redesign or audit unrelated contracts.
- A service stores related code in two repositories: placement alone does not
  justify a second runtime or independent release process.

## Limits

The package supplies design guidance, not a transport or concurrency test
harness. Source review can establish implementation structure and suspected
violations; only exercised paths support claims about runtime behavior.
