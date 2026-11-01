# TypeScript patterns scenarios

Requests, context and expected behavior for evaluation. Ordinary use reads the
skill and the references selected by the task, not these expectations. Record
observed results with the change that ran them.

## Language guarantees

| Request and context | Expected behavior |
| --- | --- |
| Saved JSON is asserted to a domain type | Validate unknown input and consequential invariants; carry the checked type inward without requiring a new schema library. |
| A type predicate only checks a tag but promises nested payloads | Check the whole claimed contract or narrow the promise. |
| A generic loader returns caller-selected `T` without a validator | Require a source for that type relationship; do not hide the cast in a generic helper. |
| Two string ID namespaces can be swapped | Consider validating brands if the mix-up is plausible; keep the cast at the factory and use it in fixtures. |
| A class with only public instance fields has a private constructor | Do not claim the constructor makes its instance type nominal; preserve a necessary instance marker when clearing unused findings. |
| A status has optional payloads that only make sense in one variant | Model the relationship with a discriminated union; do not require classes. |
| A closed-union `void` switch omits a newly added variant | Make the complete handling claim checkable; keep an intentional subset consumer distinct. |
| An external protocol deliberately permits future variants | Preserve its compatibility fallback at the parsing boundary. |
| A catalogue must cover every union member but uses `satisfies readonly Kind[]` | Identify membership versus completeness; derive from the owner or use a checked total record. |
| A fresh literal must preserve its exact value types | Choose `satisfies` when useful; distinguish it from annotation, assertion and runtime validation. |
| A value with extra properties is assigned through a variable | Do not claim structural typing or `satisfies` universally rejects all extra properties. |
| A setting of zero triggers the default | Preserve zero with an absence check or `??`; retain deliberate blank normalization where its contract requires it. |
| A patch distinguishes omission, null and explicit undefined | Preserve the wire meanings and account for `exactOptionalPropertyTypes`. |
| An indexed read or `Map.get` uses repeated `!` | Put a real cardinality guarantee on the producer, guard the lookup or use the owning required accessor. |
| A sparse array passes `every` before being cast to a triple | Check every position and construct a tuple; exercise holes and non-finite values. |
| A tuple is mapped into an array and then assumed to retain cardinality | Check the transformed type; preserve the intended return contract explicitly. |
| A branded quantity is incremented | Recheck the result's numerical invariant; a brand does not survive arbitrary arithmetic as proof. |
| A readonly snapshot shares a nested array with its caller | Explain the shallow guarantee and copy the owned mutable levels if independence is promised; exercise the original alias. |
| A heterogeneous registry separates a schema from its handler and casts the handler | Preserve the pairing before erasure, for example with a typed closure; reject mismatched input/handler types. |
| A generic key lookup widens every result to the union of values | Preserve the key/value relationship and verify more than one key. |

## Scope and toolchain

| Request and context | Expected behavior |
| --- | --- |
| Convert only a simulation engine; a browser UI and a dice renderer remain JavaScript | Preserve that boundary and current behavior, check engine and consumers, and do not spread TypeScript adoption or DOM dependencies into other parts. |
| Fix a type in one package with inherited compiler settings | Read applicable inherited settings; do not impose a repo-wide strictness migration. |
| A selected JavaScript boundary needs checking during migration | Distinguish allowJs inclusion from checkJs or per-file checking; account for imported files without inferring a whole-project conversion. |
| A transpilation build passes while a type error remains | Find the actual type-check command and its included files; report execution separately. |
| An emitted Node ESM package and a bundler app use different import spellings | Follow each execution path; no universal extension or alias rule. |
| Native Node runs a TypeScript source file | Do not call that a type check or assume it reads tsconfig aliases. |
| A lint exemption silences both a valid idiom and a real bug | Probe both and narrow the single rule; report the uncovered defect class. |
| Asked to reorganize operation classes or rename directories | Follow adopted design guidance; language patterns do not prescribe the structure. |
| A JavaScript child-process wrapper loses signal status | Select Node patterns without inferring TypeScript adoption. |
| Asked only to restyle a JavaScript screen | Do not select this skill or convert the screen. |

## Evidence limits

The package's compiler-example tests check selected relationships and runtime
examples, not arbitrary consumer behavior. They require Python 3.11+, Node 24
and TypeScript 5.0+ (`tsc` on PATH). Install the source repository's pinned
compiler for its maintenance gate. The examples do not establish a project's
replay parity, performance, bundler compatibility or migration completeness.
