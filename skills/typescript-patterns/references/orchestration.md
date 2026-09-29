# Orchestration And Pipelines

## Contents

- [Lifecycle orchestrators](#lifecycle-orchestrators)
- [Intentional centrality](#intentional-centrality-versus-service-location-pressure)
- [Sequential pipeline](#sequential-pipeline)
- [Nested pipelines](#nested-pipelines)
- [Standardizing pipelines](#standardize-the-pipeline)

## Lifecycle Orchestrators

A lifecycle orchestrator owns the creation, replacement, and teardown order of
a cohesive collaborator set. It is a stateful shell, not a home for each
collaborator's domain behavior.

### Rules

- Construct dependencies in dependency order and dispose them in the reverse
  order unless the domain requires an explicit exception.
- Keep long-lived roles as named fields; keep transient workflow objects local
  to the operation that uses them.
- Delegate behavior to focused collaborators. The orchestrator says when and in
  what order, not how each domain operation works.
- Make replacement symmetric: unsubscribe and dispose the old collaborator
  before publishing the new one.
- Keep event subscription ownership visible and pair registration with teardown.
- Expose the smallest public lifecycle: usually start/load/update/dispose rather
  than every inner service.

### Why

- One owner makes lifetime and teardown order reviewable.
- Collaborators remain independently testable.
- Replacement and failure cleanup stop being scattered call-site concerns.

### When To Use

Use an orchestrator when work creates several long-lived collaborators, owns
subscriptions or resources, replaces a running session, or must guarantee
cleanup after partial failure.

### When Not To Use

- A pure transformation has no lifetime; use a stateless operation.
- A short fixed sequence with only local intermediate values is a
  [sequential pipeline](#sequential-pipeline).
- A class that merely forwards unrelated services is a service locator, not an
  orchestrator.

## Intentional Centrality Versus Service-Location Pressure

Some nodes are intentionally central: an application shell, request context,
or composition root may have high fan-in because it owns the lifecycle. The
question is whether consumers take named capabilities or reach through the
central object for arbitrary services.

Pressure toward a service locator shows up when:

- new features add a field, constructor argument, and forwarding method to the
  shell as one repeated pattern;
- consumers receive the shell only to call one inner service;
- testing a small feature requires constructing most of the application graph;
- teardown ownership becomes unclear because any consumer can fetch a service.

Keep the composition root central, but pass narrow roles to consumers. Group
collaborators into a named sub-composition only when they share a real lifetime
or domain boundary—not merely to reduce constructor length.

## Sequential Pipeline

A sequential pipeline makes a fixed multi-step transformation read top to
bottom while one context carries intermediate state.

```ts
interface BuildContext {
  readonly input: SourceDocument;
  tokens?: readonly Token[];
  output?: CompiledDocument;
}

class DocumentCompiler {
  static compile(input: SourceDocument): CompiledDocument {
    const context: BuildContext = { input };
    this.tokenize(context);
    this.validate(context);
    this.emit(context);
    return this.outputOf(context);
  }
}
```

### Rules

- Keep the entry method as the narrative: one line per meaningful phase.
- Name steps for domain decisions, not implementation verbs such as `process`.
- Use a local context when intermediate values genuinely span steps; do not
  turn every local variable into context state.
- Let each step either mutate a clearly owned context or return a value. Avoid
  a mixture that hides data flow.
- Validate phase preconditions at the phase boundary and fail with the domain
  fact that is missing.
- Keep a fixed pipeline explicit. A generic step registry is justified only
  when steps are truly data-driven or extensible at runtime.

### Why

The entry reads as the workflow, private steps own branch policy, and tests can
pin phase behavior without duplicating the entire operation.

### When Not To Use

- Two or three straight-line expressions are clearer inline.
- Independent stages do not share state and already have honest public
  contracts; compose them directly.
- The workflow is dynamic by contract; model its step data rather than hiding it
  in a fixed method sequence.

## Nested Pipelines

Use a nested pipeline when one phase of a larger workflow is itself a meaningful
ordered process with its own vocabulary and tests. The parent keeps the phase as
one step; the child opens it at the next altitude.

```ts
class ReportBuilder {
  static build(input: ReportInput): Report {
    const rows = RowPipeline.build(input.records);
    return this.assemble(input, rows);
  }
}
```

### Rules

- Split only when the nested sequence answers a coherent question on its own.
- Repeat the seam name in both levels so readers can follow the handoff.
- Pass a narrow input/result across the seam. Do not share the parent's mutable
  context wholesale.
- Keep error ownership with the phase that can explain it best; add parent
  context only when it changes the meaning.

### When Not To Use

Do not mint a class merely to hide line count. If the child has no vocabulary,
contract, or independent test surface, keep named private steps on the parent.

## Standardize The Pipeline

Several pipelines with the same lifecycle can share a small protocol only after
their phase meanings have stabilized.

### Rules

- Stabilize one exemplar before extracting the common shape.
- Standardize the lifecycle seam—input, result, error, cleanup—not every private
  method name.
- Prefer a shared interface or base operation only when consumers benefit from
  substituting implementations.
- Keep domain-specific phases on their owners; a framework full of callbacks is
  harder to read than a few explicit pipelines.
- Delete the duplicated old shape in the same change once the shared contract
  wins.

### When Not To Use

- The resemblance is only "several methods run in order."
- Pipelines have different failure or resource ownership semantics.
- A generic abstraction requires casts or optional hooks for most members.
