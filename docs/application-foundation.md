# Application foundation scope

Status: initial draft package with bounded design trials, 3 October 2026.
No release tag or consumer adoption is claimed.

The [application-foundation collection](../collections/application-foundation/COLLECTION.md)
connects an established workflow to application operations, state ownership,
dependency interfaces and verification boundaries. Its first member is
`application-design`; external integration mechanics are a conditional reference
inside that workflow.

## Responsibility boundary

Project-foundation continues to own system responsibilities, conceptual models,
workflow and provider selection, handoff obligations, policy and document ownership.
Application-design opens an implementing application around a concrete operation.
An internal trace can expose a question for the shared architecture, but cannot
silently change that owner's decision.

Language-design skills own how those responsibilities appear in TypeScript or
Python. Service-boundaries retains its HTTP/MCP and service-ownership scope.
Runtime-operations owns its credential and process procedures. Verification-design
selects evidence; test-writing owns test and fixture construction. These remain
standalone packages, selected when the task needs them.

| Guidance | First package treatment | Reason |
| --- | --- | --- |
| Application-design workflow | New collection member | Language-neutral internal design has a distinct trigger and outcome |
| External operation boundaries | Conditional reference | Provider mechanics refine the same operation trace |
| Language, runtime, service and test guidance | Separately pinned companions | Existing tasks and installation units remain useful alone |
| Project-foundation | Optional project-routed companion | Reuse established owners without copying the collection |
| Provider-specific commands and contracts | Consuming repository | Product facts and executable behavior need local owners |

## Packaging choice

The first collection is self-contained and has no mandatory companion dependency.
Its [installation route](../collections/application-foundation/references/installation.md)
uses independently pinned companions and explicit project-owned paths. This works
within the current package validator's installation-unit containment rule; it adds
no resolver and does not settle mandatory dependency packaging for data-foundations.

One core member is deliberate: packaging establishes an extensible installation
boundary without moving existing standalone skills or inventing another workflow
merely to populate a collection. Add a member only when a separate recognizable
task needs its own outcome. Required shared resources can then remain inside this
installation unit.

For Forge, a future shared installation belongs in Primary alongside its pinned
project-foundation collection. Members can use the same shared-access mechanism
and task routes. This source change does not install or update any consumer.

## First trials

Three isolated consumers exercised project-instruction discovery with copied
installations and synthetic inputs: provider execution representative of
forge-tools, local candidate receipt representative of forge-assets, and a literal
wording edit. The two designs preserved their different state and dependency needs;
the wording edit left application-design unopened. The provider trial used the
core without reading project-foundation; receipt also used contract and authoring
guidance. The [validation record](../validation/application-design.md) retains the
actual proposals, reading evidence and remaining coverage limits.

The useful guidance fits one application-design workflow with conditional provider
detail. The trials supplied no evidence for a second member, a generic provider
framework or moving existing specialist packages into this collection.

Further adoption can pin this complete draft in a consuming project and exercise a
real implementation slice after its brief and operating prerequisites are known.
Provider-specific claims need current official evidence. A supplied contract
supports reasoning about the design; it does not establish live provider behavior. Package checks establish
installation structure, not runtime behavior or reliable automatic discovery.
