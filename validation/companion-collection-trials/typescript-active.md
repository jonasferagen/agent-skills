# Typed CLI command operation design

This is a design and verification plan only. No proposed child command, compiler, test suite, live service or installer was run. Local instruction files were read; no source repository or other trial fixture was inspected. No implementation or repository-wide refactoring is proposed here.

## Decision and ownership

The call-site problem is that a typed record still needs runtime validation, and a generic `exit 1` would erase whether the child exited, timed out, received a signal or never started. Use one explicit sequence: validate the record, make one immutable request, await one process invocation, return its tagged outcome.

`CommandOperation` is a stateless class with a static `execute` method. It owns validation and the single-invocation rule. Inputs and results remain passive contracts: these are one-shot DTOs, not reusable invariant-bearing domain objects. Validation helpers used only here stay private static methods. A CLI entry/composition class owns parsing external `unknown`, constructing the adapter, formatting diagnostics and choosing the CLI's exit status.

Declare the consumer-owned `CommandExecutor` port beside `CommandOperation`, using consumer-owned request/result types rather than Node's child-process types. It is a named semantic role: both the Node adapter and a checked test double satisfy it. Its contract includes exactly one child launch attempt per call, bounded capture, timeout policy, completion/cleanup ownership, and resolution for expected failures. An adapter must not secretly retry, probe the program with another launch or hand live process handles to the consumer.

`NodeCommandExecutor` owns child handles, timers, listeners and captured bytes. Its public static factory can construct a private per-invocation instance to keep scratch state off static method parameters. It delegates neither resource lifetime nor termination classification to the operation. A composition adapter can expose its static method as the port's checked object literal. The composition root supplies a known-valid working directory and an explicit environment snapshot under the application's policy; no invented environment sanitization policy is imposed by this design.

If implemented, each operation/adapter class gets a file named after its primary export. Start with contracts beside the consumer; move shared sibling contracts into `CommandTypes.ts` only when they escape that single class. No new barrel, dependency, framework, registry or generic pipeline is needed for this short fixed sequence. Preserve the existing strict compiler settings.

## Boundary contracts

Illustrative field names below describe a generic caller-selected command; they do not assert a repository product schema. Limits are explicit required fields because no local default policy was supplied.

```ts
interface CommandInput {
  readonly program: string;
  readonly args: readonly string[];
  readonly timeoutMs: number;
  readonly maxOutputBytes: number;
}

interface ValidationIssue {
  readonly field: keyof CommandInput | "input";
  readonly message: string;
}

interface CapturedOutput {
  readonly stdout: Uint8Array;
  readonly stderr: Uint8Array;
  readonly complete: boolean;
  readonly truncated: boolean;
}

type TerminationObservation =
  | { readonly kind: "exit"; readonly code: number }
  | { readonly kind: "signal"; readonly signal: string }
  | { readonly kind: "unobserved" };

type ProcessOutcome =
  | { readonly kind: "exited"; readonly code: number;
      readonly output: CapturedOutput }
  | { readonly kind: "timed_out"; readonly timeoutMs: number;
      readonly termination: TerminationObservation;
      readonly output: CapturedOutput }
  | { readonly kind: "signaled"; readonly signal: string;
      readonly output: CapturedOutput }
  | { readonly kind: "missing_program"; readonly program: string;
      readonly errorCode: "ENOENT"; readonly message: string }
  | { readonly kind: "output_limit"; readonly maxOutputBytes: number;
      readonly termination: TerminationObservation;
      readonly output: CapturedOutput }
  | { readonly kind: "start_error"; readonly errorCode?: string;
      readonly message: string }
  | { readonly kind: "io_error"; readonly message: string;
      readonly termination: TerminationObservation;
      readonly output: CapturedOutput };

type CommandResult = ProcessOutcome
  | { readonly kind: "invalid_input";
      readonly issues: readonly ValidationIssue[] };

interface CommandExecutor {
  readonly run: (request: CommandInput) => Promise<ProcessOutcome>;
}

interface CommandDependencies {
  readonly executor: CommandExecutor;
}

class CommandOperation {
  static async execute(
    input: CommandInput,
    dependencies: CommandDependencies,
  ): Promise<CommandResult> {
    const issues = this.validate(input);
    if (issues.length !== 0) return { kind: "invalid_input", issues };
    const request: CommandInput = { ...input, args: [...input.args] };
    return dependencies.executor.run(request);
  }

  // Design signature only; implementation must perform the checks below.
  private static validate(input: CommandInput): readonly ValidationIssue[];
}
```

The class snippet is illustrative API/pseudocode, not a claimed compilable implementation. At the CLI boundary, parse JSON or other external values as `unknown`, prove they form a record and narrow every field without `any`, non-null assertions or `as unknown as`. Do not cast external JSON to `CommandInput`. The operation rechecks semantics even for typed callers: a nonblank program with no NUL; an actual array whose elements are strings with no NUL; positive safe-integer timeout within Node's timer range; and a positive safe-integer byte cap within the application's feasible memory range. Choose/document that memory policy before implementation. Empty argument strings remain valid; do not trim arguments or paths and thereby change command meaning. Copy inputs before the asynchronous boundary so later caller mutation cannot alter the launch request. Invalid input produces diagnostics and zero runner calls.

Use `interface` for object contracts and `type` for unions. External Node `null` code/signal values are narrowed at the adapter boundary; internal absence uses `undefined` or a tagged `unobserved` observation. CLI presentation must switch exhaustively over `CommandResult` using a `never` guard, independent of compiler flags. Test doubles use ordinary annotations or `satisfies`, not casts.

## Process adapter policy

Use Node `spawn(program, args, { shell: false, stdio: ['ignore', 'pipe', 'pipe'], cwd, env })`. Argument vectors stay separate; there is no shell interpolation. Ignored stdin prevents accidental inherited input and children waiting for EOF. Attach child and stream error listeners immediately, and listen to both `error` and `close`: a program that never starts need not emit `exit`. Finalize normal capture on `close`, because `exit` can precede drained streams. Never turn `code === null` into exit zero.

Track a local primary stop cause (`timeout`, `output_limit` or `io_error`) separately from the final exit/signal observation. A nonzero numeric exit is still `exited`, carrying that exact code. A signal without a wrapper stop cause is `signaled`, carrying the actual signal. A deadline records `timed_out` even if subsequent teardown observes a numeric exit; retain that observation in `termination`. Do not infer a timeout merely from `killed` or from any occurrence of `SIGTERM`.

Start a deadline around the launch attempt, cancel it when completion is observed, and prevent a deadline firing after an observed exit from overwriting that exit. Record the first observable initiating stop cause once; later events add termination facts without replacing it. A startup error takes precedence over the later negative `close` code. For `ENOENT`, report `missing_program` with the requested program and actual error text; explain that the executable or its interpreter could not be found. A known-valid composition-owned cwd avoids conflating a missing cwd with a missing executable. Preserve permission errors such as `EACCES` as `start_error`, not `missing_program` or child exit 1.

Count raw bytes across stdout and stderr together, before decoding. Keep at most `maxOutputBytes` total, copying only the remaining allowance of an arriving chunk. At exactly the cap there is no overflow; the first byte beyond it records `output_limit`, marks truncation and initiates teardown. Continue draining or deliberately close streams without retaining more data. Collection order is not a promise of temporal interleaving between streams. UTF-8 presentation may replace an incomplete final character; the retained byte arrays are authoritative. Timeout, signal, overflow and IO-error captures are explicitly incomplete and must never be parsed as complete structured output.

On a wrapper stop, send a configured termination signal, then escalate after a fixed grace interval where supported. Document and enforce a final cleanup bound as well: a child or inherited pipe may not close promptly. At that bound, close owned streams, clear timers/listeners and settle once with `termination: { kind: 'unobserved' }` if no final termination was seen. This guarantees bounded waiting/capture, not universal process-tree termination. Retain/diagnose kill failures; do not claim that a launch was fully reaped when it was not. Direct-child termination and platform-specific escalation are the default scope; grandchildren require a separately specified process-group/job policy. Expected synchronous startup and asynchronous errors become result variants. Unexpected programmer faults are not silently converted to child exit failures.

The CLI prints a reason even when stderr is empty, for example “timed out after 5000 ms” or “program could not be found (ENOENT).” It reports retained output as partial when applicable. Preserve ordinary child exit codes where representable, use 128 plus the platform signal number for signal termination, and choose/document distinct policy statuses for timeout, invalid input, overflow and startup failure. Those numeric presentation choices do not replace the tagged result. Set `process.exitCode` and return so queued diagnostics drain; avoid immediate `process.exit()`.

## Verification plan — not executed

No test standard or existing test command is supplied by this fixture beyond strict TypeScript/Node design. Do not invent a passed project gate or install a runner. Implementation remains a prerequisite for all runtime checks.

| Claim / observable failure | Cheapest proposed check | Prerequisite / cost |
| --- | --- | --- |
| Invalid records never launch | Checked fake executor with call counter; invalid semantic values and CLI `unknown` shapes produce field diagnostics and zero calls | Implementation; cheap in-process |
| Valid record launches exactly once after validation | Fake records arguments; assert exact vector, bounds, immutable snapshot and one call; no retry on any variant | Implementation; cheap in-process |
| Result consumers retain every distinct outcome | Fake returns every union member, including exit 0 and nonzero, timeout with exit observation, external signal and ENOENT; exhaustive compile-time consumer check | Existing strict compiler, implementation; cheap |
| Real process status is correctly classified | Later local Node child fixtures for exit 0, exit 7, a nonexistent absolute executable, permission denial, external signal and timeout; inspect exact kind and diagnostic | Authorization to execute processes, supported platform; integration |
| Capture is bounded by bytes, not characters or stream count | Adapter collector checks at cap−1, cap, cap+1, multibyte UTF-8 and mixed stdout/stderr; later real fixture writes beyond cap and keeps writing | Implementation; unit plus distinct real-stream evidence |
| Lifecycle cannot settle twice or hang | Deterministic event/timer traces: startup error then close; exit then deadline; timeout then close; overflow then timeout; late stream error; failed kill; streams staying open until cleanup bound | Implementation with controlled event/time seam; cheap |
| OS teardown works within documented scope | Real child ignoring graceful termination and supported escalation; validate final deadline and unobserved cleanup reporting, not an unsupported process-tree guarantee | Platform/process execution; integration |
| CLI diagnostics survive slow output consumers | Later built CLI writes more than a pipe buffer to a delayed reader; compare bytes/count against file output, and check exit status; invoke from another cwd/path containing spaces | Built artifact, process execution; slower distinct output/packaging boundary |

Do not substitute fake-runner success for Node lifecycle evidence. Keep pure event ordering tests deterministic and independent; retain integration checks because they observe a different boundary. Once implemented, record exact existing project commands, environment, denominators and outcomes. Here all checks are planned and unrun; there is no verification or compilation claim.

## Instruction-read record

Counts below are approximate whitespace-separated words (`wc -w`), excluding tool wrappers and shell startup warnings. Every file is inside this trial. Required means selected by the local router/task; useful means contextual supporting detail. No irrelevant instruction file was deliberately loaded. Installation guides, unrelated language guidance, enforcement changes, generic-type/import references, test-writing and settled-suite test-audit skills were not loaded because this task requests design and a verification plan only.

| Instruction file actually read | Words | Classification / contribution |
| --- | ---: | --- |
| `AGENTS.md` | 26 | Required: local routing and scope |
| `project.md` | 51 | Required: local-only, existing strict TypeScript/Node, no install/refactor |
| `.agents/collections/typescript-foundation/COLLECTION.md` | 223 | Required: TypeScript and Node selection |
| `.agents/collections/verification-foundation/COLLECTION.md` | 222 | Required: verification-plan routing |
| `.agents/collections/typescript-foundation/skills/typescript-design/SKILL.md` | 662 | Required: class-based operation and ownership method |
| `.agents/collections/typescript-foundation/skills/typescript-patterns/SKILL.md` | 451 | Required: boundary and discriminated type decisions |
| `.agents/collections/typescript-foundation/skills/node-patterns/SKILL.md` | 1,484 | Required: child outcomes, stdin, events, bounded output, CLI draining |
| `.agents/collections/verification-foundation/skills/verification-design/SKILL.md` | 535 | Required: evidence boundary and unrun prerequisites |
| `.agents/collections/typescript-foundation/skills/typescript-design/references/class-shape.md` | 1,722 | Required: static entry and private per-invocation adapter state |
| `.agents/collections/typescript-foundation/skills/typescript-design/references/dependency-ports.md` | 886 | Required: consumer role, lifetime semantics, checked doubles |
| `.agents/collections/typescript-foundation/skills/typescript-design/references/orchestration.md` | 931 | Useful: retain short direct sequence; keep lifecycle in adapter |
| `.agents/collections/typescript-foundation/skills/typescript-design/references/utilities-and-data.md` | 1,255 | Useful: parameter object and passive one-shot inputs |
| `.agents/collections/typescript-foundation/skills/typescript-design/references/naming-and-placement.md` | 1,247 | Useful: contract placement and one primary class per file |
| `.agents/collections/typescript-foundation/skills/typescript-patterns/references/typescript.md` | 1,939 | Required: unknown narrowing, interface/union split, exhaustiveness |

Unique instruction load: approximately **11,634 words** across **14 files**. One batched tool response was truncated globally (individual reads were not locally truncated), obscuring portions of `orchestration.md` and `utilities-and-data.md`; both were re-read once in full, adding approximately **2,186 repeated words**. Approximate requested read volume including repetition: **13,820 words**. The count-only pass did not re-display their contents. Some sections within the loaded references (sibling class families, token helpers, fail-closed discovery, tuples/brands) were irrelevant to this operation; they were not applied or expanded into additional reads.

Constraints preserved: work confined to this fixture; no source/other-fixture inspection; no live services, secrets, network, dependency installation or proposed program execution; existing strict compiler settings retained; no repository-wide refactoring; no unrelated documentation correction; typed record validated before exactly one launch; consumer/adapter ownership and cleanup explicit; ordinary exit, timeout, signal, ENOENT, overflow and other failures retained distinctly; verification presented as a plan with unavailable evidence marked.
