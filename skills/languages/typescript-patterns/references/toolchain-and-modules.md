# Toolchain and modules

## Inspect what actually checks the code

Read the affected package's scripts, inherited configuration and supported
runtime before choosing syntax or imports. Distinguish checking from execution:
`tsx`, Babel, bundlers and native type stripping may transform or execute code
without type checking. Confirm the project's separate type-check path and which
source, tests and callers it includes. `tsc` can emit despite errors unless
configured otherwise; output files are not proof the check passed.

`allowJs` allows JavaScript files in the TypeScript program; it does not by itself
enable error checking in them. `checkJs` enables checking across the included
JavaScript files; `// @ts-check` opts in a single file. For a selected JavaScript
boundary, keep the checking configuration scoped and account for imported files
that enter the program. Neither option requires converting those files to
TypeScript.

An explicit public return type can expose unintended inference changes; local
values often read better with inference. Use the project's conventions rather
than annotating every expression. A `.d.ts` file describes a contract but does
not implement or validate it. A broad declaration hiding an untyped JavaScript
module is not evidence that the implementation meets the declaration.

## Change strictness on evidence

For a new TypeScript boundary, `strict` is a useful starting point. For an
existing project, run a proposed flag against the affected code and inspect the
findings before changing its configuration. Flags such as
`noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` add distinct
obligations beyond `strict`. Do not turn on a flag repo-wide as a side effect of
a local fix, or disable it just to hide the fix's errors.

A checker can establish an assignment or an exhaustive union; it cannot decide
whether an operation has the right owner or whether a fallback matches the
product contract. Use the compiler for type guarantees, a focused lint rule for
an appropriate syntactic defect, and review for intent. When a lint exemption
is needed, probe a valid idiom and a real defect together. Narrow that rule's
scope rather than suppressing the whole ruleset, and report the remaining gap.

For type regressions, compile valid callers and deliberately invalid ones with
the supported compiler and relevant flags. `@ts-expect-error` fails when its line
stops producing a diagnostic; keep the expression small so an unrelated error
cannot satisfy it. Runtime tests still owe evidence for parsing, failure and
mutation behavior. A compiler upgrade can change diagnostics and the contents
of `strict`; review it as its own dependency change.

## Match imports to the execution path

The project owns ESM/CommonJS, aliases, import spelling and build boundaries.
Use type-only imports for erased dependencies, and preserve side-effect imports
when execution needs them. Do not infer a universal extension rule:

- Emitted Node ESM commonly uses `.js` specifiers in TypeScript source so the
  emitted files resolve. Check the actual Node mode and package type.
- Bundler resolution follows the bundler's supported contract, which may accept
  spellings Node does not. Do not export those assumptions into an unbundled
  library consumer.
- Direct TypeScript execution follows the runner's extension and syntax rules.
  Native Node type stripping does not type-check and does not apply `tsconfig`
  path aliases. Check the supported Node version before selecting features that
  require JavaScript generation, such as enums or parameter properties.

When migrating a selected JavaScript boundary, preserve its consumers and
execution path. Use scoped checking or interop where appropriate; do not
silently port the UI, require a framework, or change package exports. Browser,
server, worker and environment-neutral source can need distinct checking
configurations. The `lib` and ambient types determine which globals the checker
accepts, not which the runtime provides. Accidentally accepting `document` in a
headless module does not make that module portable.

Primary references: [module configuration](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html),
[`allowJs`](https://www.typescriptlang.org/tsconfig/allowJs.html),
[`checkJs`](https://www.typescriptlang.org/tsconfig/checkJs.html),
[`strict`](https://www.typescriptlang.org/tsconfig/strict.html),
[`verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html),
[`noEmitOnError`](https://www.typescriptlang.org/tsconfig/noEmitOnError.html),
and [Node TypeScript execution](https://nodejs.org/api/typescript.html).
