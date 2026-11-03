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

## Check JavaScript through JSDoc

JSDoc types are checked only in files the checker includes with `checkJs` or
`// @ts-check`. Their syntax has traps that TypeScript syntax does not:

- A cast is `/** @type {T} */ (expression)`, and the parentheses are part of it.
  Without them, the comment is ignored: no cast and no diagnostic.
- JSDoc has no non-null `!`. Narrow with a check, or cast to the non-null type
  beside a comment that states the invariant.
- A destructured parameter with a `= {}` default is typed from its binding
  pattern. A binding element without a default value, such as `{ min, max } = {}`,
  is missing from that inferred type, so callers that pass it are rejected. Name
  the parameter in a `@param` with an options type instead.
- Reuse a type from another module with `/** @typedef {import('./owner.js').Name} Name */`.
  Write generics with `@template`.
- A `//` comment ends only at the line break. Placed inside a chained
  expression, it silently removes the rest of the line from the program.
  Put a long explanation above the statement.

```js
// @ts-check
/** @typedef {{samples?: number, seed?: number}} RunOptions */

/** @param {string} key @param {RunOptions} [options] */
export function run(key, { samples = 1024, seed } = {}) {
  return `${key}:${samples}:${seed ?? 'fixed'}`;
}

/** @param {unknown} raw */
export function rowCount(raw) {
  if (!Array.isArray(raw)) throw new Error('Expected rows');
  // The caller validated each row; this cast states that, it does not check it.
  const rows = /** @type {readonly {id: string}[]} */ (raw);
  return rows.length;
}
```

A typed alias, such as `const TABLE = /** @type {Record<string, Row>} */ (CATALOG)`,
works around a missing contract at each use site. When several files need the
same view, type the value where it is defined instead.

## Change strictness on evidence

For a new TypeScript boundary, `strict` is a useful starting point. For an
existing project, run a proposed flag against the affected code and inspect the
findings before changing its configuration. Flags such as
`noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` add distinct
obligations beyond `strict`. Do not turn on a flag repo-wide as a side effect of
a local fix, or disable it just to hide the fix's errors.

Count the findings per flag before choosing an order. Flags that mostly need
`null` handling can cost little, while `noImplicitAny` over untyped JavaScript
can cost far more. Type the shared contracts at their owners first: each one
types every caller at once, while casts at the call sites have to be redone
when the owner gains its type.

The compiler has no per-file flags. To adopt a stricter flag file by file, run a
second configuration that enables it and fail only on diagnostics in files that
have opted in. The project chooses how a file opts in. Keep the main
configuration authoritative for everything else. Imported files enter the
program, so attribute each diagnostic by its file rather than by the files you
listed. Run the main and the stricter check together so that typing a parameter
cannot break a caller unnoticed.

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

## Prove a type-only change

A change meant to add types should leave the executed program unchanged. Review
the diff for runtime edits that look like typing: an added `??`, `?.` or guard,
a changed default, a removed or reordered call, and code swallowed by a comment.
These change what runs, even when tests and the type check still pass. Where a
change is large, compare the old and new source after removing comments, type
annotations and the parentheses of casts. Every remaining difference should be
justified one by one, such as a split declaration or a local alias read
immediately. Tests and replay checks still owe evidence for the behavior itself.

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
