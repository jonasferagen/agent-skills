# Worked examples

**Read this when you know which form you need and want a model to copy.**
[Form selection](select.md) decides the form; [mermaid.md](mermaid.md) covers the syntax. Each
example below names the failure it replaces, so it is clear what the shape is
buying. ER-specific models live in [ER examples](er/examples.md);
data movement has [data-flow examples](data-flow/examples.md).

These are synthetic design examples. References to storage or delivery contracts
name illustrative documents, not supplied ones or verified systems. In a real
project, link the actual document before marking that detail as available
elsewhere.

## An overview and its detail, instead of one wide block

**Replaces:** one flowchart holding an authoring lane, a publish boundary, and a
delivery lane side by side — three altitudes in one block, which renders as
squeezed lanes with unreadable labels.

The overview keeps the complex part as a single node:

```mermaid
flowchart TB
  A["authoring surface"] --> B["publish boundary"]
  B --> C["delivery surface"]
  B -. "rejected: stale base" .-> A
```

The detail diagram opens that one node, in the doc that owns it. Its title
repeats the black box's label exactly, so a reader knows what they opened.

The publish boundary checks the candidate in this order.

```mermaid
flowchart TB
  subgraph Publish [publish boundary]
    direction TB
    P0["stale-base check"] --> P1["whole-corpus validation"]
    P1 --> P2["artifact rules"]
    P2 --> P3["immutable commit"]
    P3 --> P4["activation"]
  end
```

Each diagram now answers one question at full column width. The detail's opening
names the boundary; review the detail against its source when that boundary
changes.

## One overview fanning out to several owned details

**Replaces:** a black-box overview whose outbound links leave locally owned
components unopened, or one oversized diagram that mixes system ownership with
every component's internal flow.

The overview answers only which components meet at the artifact registry:

```mermaid
flowchart TB
  A["authoring service"] --> R["artifact registry"]
  R --> D["delivery service"]
  D --> E["edge router"]
```

Inventory every black box before drawing details:

| Overview box | Disposition | Reason or destination |
| --- | --- | --- |
| `authoring service` | compact detail here | this doc owns its validation boundary |
| `artifact registry` | canonical detail elsewhere | the storage contract owns its internals |
| `delivery service` | compact detail here | this doc owns its resolution boundary |
| `edge router` | intentionally atomic | only its public handoff matters at this altitude |

The two locally owned boxes each get a compact detail at the same altitude. The
exact overview label appears again, and only the immediate external seams are
redrawn.

The authoring service validates edits before handing them to the artifact registry.

```mermaid
flowchart TB
  U["author input"] --> A0
  subgraph Authoring [authoring service]
    direction TB
    A0["parse"] --> A1["validate"]
    A1 --> A2["package"]
  end
  A2 --> R["artifact registry"]
```

The delivery service resolves a published artifact for the edge router.

```mermaid
flowchart TB
  R["artifact registry"] --> D0
  subgraph Delivery [delivery service]
    direction TB
    D0["resolve pin"] --> D1["load artifact"]
    D1 --> D2["shape response"]
  end
  D2 --> E["edge router"]
```

The artifact registry would link to the real storage contract instead of being
redrawn, and the edge router stays closed for a stated reason. If the reader
also needs request order or retry behavior, draw a separate lifecycle diagram;
that question does not belong inside this ownership set.

## A multi-phase lifecycle split by stage-level question

**Replaces:** one lifecycle that expands every relevant input, optional build
step, and finalization state. No single subgraph has to be enormous for the
whole diagram to answer too many useful questions at once.

The stable-stage overview carries only the end-to-end order. Repeated inputs,
the optional branch's internals, and routine finalization states are collapsed:

```mermaid
flowchart TB
  I["candidate inputs"] --> P["candidate preparation"]
  P --> B["optional backend build"]
  P -. "build skipped" .-> F["set finalization"]
  B --> F
  F --> D["delivery"]
```

The black-box inventory applies just as it does to a component overview:

| Lifecycle stage | Disposition | Reason or destination |
| --- | --- | --- |
| `candidate inputs` | compact detail here | input fan-in and precedence matter |
| `candidate preparation` | intentionally atomic | its public outcome is enough here |
| `optional backend build` | compact detail here | the conditional lane has load-bearing order |
| `set finalization` | compact detail here | activation states and handoffs matter |
| `delivery` | canonical detail elsewhere | the delivery contract owns its internals |

Each focused detail answers one stage-level question and repeats the overview
label exactly.

Candidate inputs converge on candidate preparation. For this synthetic case,
authored values override imported values for the same candidate field; other
imported values remain. The arrows show fan-in; this sentence owns precedence.

```mermaid
flowchart TB
  subgraph Inputs [candidate inputs]
    direction TB
    A["authored candidate"] --> N["normalize"]
    M["imported candidate"] --> N
  end
  N --> P["candidate preparation"]
```

The optional backend build completes before set finalization.

```mermaid
flowchart TB
  P["candidate preparation"] --> B0
  subgraph Build [optional backend build]
    direction TB
    B0["load source"] --> B1["build revision"]
    B1 --> B2["package artifact"]
  end
  B2 --> F["set finalization"]
```

Set finalization commits and activates the selection before delivery.

```mermaid
flowchart TB
  P["candidate preparation"] -. "build skipped" .-> F0
  B["optional backend build"] --> F0
  subgraph Finalize [set finalization]
    direction TB
    F0["commit inactive"] --> F1["compare-and-swap activation"]
    F1 --> F2["selected set"]
  end
  F2 --> D["delivery"]
```

Every node from the oversized version can still be relevant. The split moves
each ordering fact to the diagram whose question needs it; it does not discard
those facts or introduce a third altitude.

## Before / after as parallel vertical lanes

**Replaces:** a paragraph saying "today the response is rendered per request;
afterwards it resolves a pinned artifact instead" — true, but the reader has to
hold both flows in their head to see where they diverge.

```mermaid
flowchart TB
  subgraph Before [today: render per request]
    direction TB
    B0["request"] --> B1["render on demand"]
    B1 --> B2["serve response"]
  end
  subgraph After [target: prebuilt artifact]
    direction TB
    A0["request"] --> A1["resolve pinned artifact"]
    A1 --> A2["serve response"]
  end
```

The two unconnected subgraphs request vertical internal flows. Their placement
and width still need a rendered check. If the pair does not fit, stack it using
[the Mermaid guidance](mermaid.md#side-by-side-lanes-and-how-to-stack-when-they-do-not-fit).

The lanes are **comparable on purpose**: three stages each, identical first and
last node, so the single differing stage is the change. A before lane drawn in
six nodes against an after lane of three would hide exactly what it exists to
show.

## A layered overview with separate detail

**Replaces:** one left-to-right chart of a content platform's outer dependency
map with every node drawn. Cross-group edges in a left-to-right chart can make
internal nodes form wide rows, even with `direction TB` inside each group.

At overview level, show the three dependency groups as single nodes. Each arrow
means that at least one part of the first group depends on a part of the next;
it does not claim every member connects to every other member.

```mermaid
flowchart LR
  Surfaces["client surfaces"] -->|"depend on"| Services["services"]
  Services -->|"depend on"| Backbone["stores"]
```

Open those groups in a separate detail view when the particular dependencies are
the question. This representative slice keeps the cross-group fan-out; the
architecture document owns the complete inventory. Use top-to-bottom layout here
to keep the individual nodes and labels legible in a document column. Web app,
content browser and mobile app are client surfaces. Static host, read API and
write API are services; catalog and files are the stores. The ungrouped nodes
keep each dependency's endpoint visible.

```mermaid
flowchart TB
    E0["web app"]
    E1["content browser"]
    E2["mobile app"]
    S0["static host"]
    S1["read API"]
    S2["write API"]
    B0["catalog"]
    B1["files"]
  E0 --> S0
  E0 --> S1
  E1 --> S0
  E1 --> S1
  E2 --> S1
  S1 --> B0
  S1 --> B1
  S2 --> B0
  S2 --> B1
```

The overview and detail answer different questions. Do not switch the detailed
view to `LR` on the assumption that inner directions preserve vertical lanes;
external node links override those directions. Verify the actual render and
split further if the detail stops fitting the reader's column.


## A coverage matrix

**Replaces:** a section describing each surface in turn. Prose can cover all
three surfaces honestly and still never reveal that one of them answers nothing.

| Surface | Validates on write | Emits audit event | Owns rollback |
| --- | --- | --- | --- |
| editor UI | yes | yes | no — delegates to publish |
| publish API | yes | yes | yes |
| bulk importer | **unknown** | no | **none** |

The importer row is the finding. Two cells nobody could fill are worth more than
the seven that were easy, and they are visible at a glance — which is the whole
argument for the matrix over the paragraph.

## A decision matrix

**Replaces:** three paragraphs arguing for the chosen option. The matrix makes
the runners-up legible enough to be argued *against*, which is what a keystone
decision needs.

| Option | Effort | Reversible | Cost when wrong |
| --- | --- | --- | --- |
| **render at publish** (chosen) | medium | yes — republish | stale artifacts until the next publish |
| render per request | low | yes | latency on every read, permanently |
| render nightly | low | no — batch window is fixed | a day of stale reads before anyone notices |

Prose then carries only what the table cannot: *why* reversibility and the
cost of being wrong outrank effort here. Effort is paid once; an irreversible
choice, or one that charges every read, keeps costing after the work is done.
