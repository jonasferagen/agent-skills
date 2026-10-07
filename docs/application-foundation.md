# Application foundation scope

> Design record from 4 October 2026. The collection described here was
> flattened on 7 October 2026: `application-design` is now a standalone skill
> under `skills/design/`, and the collection entry point, manifest and
> installation reference are history. Companion routing is the project's.


Status: initial draft package with bounded design trials, 3 October 2026.
No release tag or consumer adoption is claimed.

The [application-foundation collection](https://github.com/jonasferagen/agent-skills/blob/914aa01b1915d190ee0429d18a570e72c179fd5d/collections/application-foundation/COLLECTION.md)
connects an established workflow to application operations, state ownership,
dependency interfaces and verification boundaries. Its first member is
`application-design`; external integration mechanics are a conditional reference
inside that workflow.

## Responsibility boundary

The project's framework continues to own system responsibilities, conceptual models,
workflow and provider selection, handoff obligations, policy and document ownership.
Application-design opens an implementing application around a concrete operation.
An internal trace can expose a question for the shared architecture, but cannot
silently change that owner's decision.

Language-design skills own how those responsibilities appear in TypeScript or
Python. Service-boundaries retains its HTTP/MCP and service-ownership scope.
Runtime-operations owns its credential and process procedures. Verification-design
selects evidence; test-writing owns test and fixture construction. Service boundaries
and runtime operations ship together in service-foundation.
Python, TypeScript and verification guidance each ships as a complete companion
collection; task routing
selects the guidance the work needs.

| Guidance | First package treatment | Reason |
| --- | --- | --- |
| Application-design workflow | New collection member | Language-neutral internal design has a distinct trigger and outcome |
| External operation boundaries | Conditional reference | Provider mechanics refine the same operation trace |
| Language, service and test guidance | Separately pinned companion packages or collections | Existing tasks and installation units remain useful alone |
| The project's framework | Optional project-routed companion | Reuse established owners without copying the collection |
| Provider-specific commands and contracts | Consuming repository | Product facts and executable behavior need local owners |

## Packaging choice

The first collection is self-contained and has no mandatory companion dependency.
Its [installation route](https://github.com/jonasferagen/agent-skills/blob/914aa01b1915d190ee0429d18a570e72c179fd5d/collections/application-foundation/references/installation.md)
uses independently pinned companions and explicit project-owned paths. This works
within the current package validator's installation-unit containment rule; it adds
no resolver and does not settle mandatory dependency packaging for data-foundations.

One core member is deliberate: packaging establishes an extensible installation
boundary without initially moving existing standalone skills or inventing another workflow
merely to populate a collection. Add a member only when a separate recognizable
task needs its own outcome. Required shared resources can then remain inside this
installation unit.

A project may hold one shared installation for several repositories. This
source change does not install or update any consumer.

## First trials

Three isolated consumers exercised project-instruction discovery with copied
installations and synthetic inputs: provider execution representative of
a tool repository, local candidate receipt representative of an asset repository, and a literal
wording edit. The two designs preserved their different state and dependency needs;
the wording edit left application-design unopened. The provider trial used the
core without reading the project's framework; receipt also used contract and authoring
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
