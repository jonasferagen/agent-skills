# TypeScript foundation sweep — 2026-10-04

This review examined each member's skill quality before reviewing collection
consistency. It is a source review with targeted compiler and runtime probes,
not an independent consumer-routing or native-discovery trial.

## Phase 1: member quality

Coverage includes all three skill entrypoints, their UI metadata, all five
TypeScript patterns references, all eleven TypeScript design references, and
the existing member validation scenarios.

### TypeScript patterns

The language/design split is clear, references are selected by concrete
symptoms, and repository-owned module and compiler settings remain authoritative.
Focused corrections address these findings:

- The mirror diagnostic called `satisfies Record<Union, Value>` the only total
  shape. Ordinary checked `Record` annotations also reject missing keys;
  assertions with `as` remain the unsafe case. The preference for `satisfies`
  when preserving literal inference remains intact.
- The tuple validator accepted sparse arrays because `every` skips empty slots.
  Its indexed reads also failed under `noUncheckedIndexedAccess`. It now checks
  each destructured position and constructs a tuple from narrowed values.
- The nominal-instance explanation said only private/protected members prevent
  structural substitution, although its own example uses an unexported unique
  symbol. The explanation now distinguishes those mechanisms.
- Enforcement prose told the reader to delete flagged bindings after identifying
  their purpose. It now explicitly preserves meaningful type-level guarantees
  while removing unused bindings that have no purpose.

The member's patch version is 2.0.1. Its triggers, required design adoption and
reference routes are unchanged.

### TypeScript design

The class-based operations, narrow exceptions, PascalCase sibling contract files,
consumer-owned ports and domain/phase directories form a consistent house style.
The review preserved those choices. Two technical claims needed correction:

- Static methods can be passed as callbacks; a method using `this` needs its
  receiver preserved. Static classes can limit elimination of unused members,
  rather than universally preventing tree shaking. The class preference remains.
- Cross-module `{@link}` syntax and rename behavior depend on the editor or
  documentation processor. A TypeScript `import(...)` expression is not a
  portable TSDoc declaration reference. The reference now requires proven local
  syntax and checking navigation, while preserving symbol links over file paths.

The member's patch version is 1.0.1. Naming, class exceptions, directory policy
and the collection's task-selection boundary are unchanged.

### Node patterns

The outcome classification, stdin ownership, stream completion and exit-output
guidance remain useful and cohesive. The callback table holds for the probed
ordinary cases. One missing distinction matters to wrapper correctness: a child
can catch a termination signal and exit 0, producing `error === null` after a
timeout or `child.kill()`. The skill now keeps the wrapper's deadline or
cancellation decision separately; callback fields alone cannot recover it.

The member's patch version is 0.1.3. Existing operational ownership and the
reciprocal runtime-operations copy markers are preserved. No shared copy was
changed.

## Phase 2: collection consistency

Reviewed `COLLECTION.md`, installation guidance, membership, UI descriptions,
reference ownership and existing package-boundary copies after the member pass.

The collection chooses design for organization and ownership, patterns for
language/type concerns, and Node for command-line process behavior. A Node
JavaScript task does not imply TypeScript adoption, and a focused type fix does
not require a design restructure. Installation guidance keeps adoption choices
outside imported files, preserves local edits, replaces whole installations and
does not grant permission to accept consumer drift. No additional collection
routing change was justified.

`COLLECTION.md` records patch version 0.1.1 for these corrections. The sweep's
coordinator owns final manifest version reconciliation, tool synchronization,
inventory regeneration and repository-wide package checks.

## Verification and limits

- TypeScript 5.9.3, from an existing cache: the original tuple example produced
  three TS2322 diagnostics with `--noEmit --strict --noUncheckedIndexedAccess
  --target es2022`; the revised example passed those settings.
- The original tuple example accepted `new Array(3)` as three `undefined`
  values. The revised boundary passed 11 runtime cases: two valid tuples and
  rejection of fully sparse and partially sparse arrays, wrong lengths, a
  string element, `NaN`, `Infinity`, `null` and an object.
- The same compiler rejected incomplete `Record` annotation and `satisfies`
  probes with TS2741 and TS1360 respectively.
- Node 24.15.0 on Linux: reproduced success, exit 9, ordinary timeout, output
  overflow, abort and missing-program events. A shell handling `SIGTERM` then
  exiting 0 produced a successful callback after both `child.kill()` and the
  `timeout` option. These are local runtime probes, not portable guarantees
  about every signal or platform.
- Skill Creator's `quick_validate.py` passed for all three member directories.
  `git diff --check -- collections/typescript-foundation` passed.
- Clear Writing and its instruction guidance informed the corrections; no
  diagrams or tables were added or structurally changed. Existing symptom and
  escalation tables remain intact.

The collection checker is unchanged. Final integrity validation follows the
coordinator's reviewed inventory update. No fresh routing trial is claimed;
triggers, reference routes, member selection and installation procedure were
unchanged. No editor navigation trial or bundler benchmark was run. No dependency
was installed, and no release was tagged.

Technical checks used primary documentation alongside local probes:
[TypeScript's `satisfies` explanation](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html),
[`noUncheckedIndexedAccess`](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html),
[Node child-process documentation](https://nodejs.org/api/child_process.html), and
[TSDoc declaration links](https://tsdoc.org/pages/tags/link/).

## Additional improvements

- Add a small compiler-example check when the repository settles its supported
  TypeScript versions. Include a strict indexed-access configuration and
  expected failures for incomplete total records and forged validated values.
  Keep explanatory pseudocode separate from runnable examples.
- Before the next collection release, run consumer trials for a pure type fix,
  a design refactor with local constraints, and a JavaScript Node wrapper whose
  child handles a timeout signal. These test selection and missed obligations
  that static package checks cannot establish.
- Consider one collection-local home for duplicated repository authority and
  workflow prose. Make that change only if a consumer trial shows it reduces
  unnecessary reading while preserving each member's essential constraints.

## Coordinated completion

The [coordinated sweep](collection-sweep.md) records the final source inventories,
combined checks and retained consumer trials. Earlier pending or partial results
on this page describe the review stage at which they were recorded. No release
or installed Forge pin was changed.
