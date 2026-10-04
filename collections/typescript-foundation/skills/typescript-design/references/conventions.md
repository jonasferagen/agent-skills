# Naming conventions

## Naming

### Files

- Use `PascalCase.ts` for classes, primary model/type exports and sibling
  `XTypes.ts` contract files. Match the filename to the primary exported class.
- Use `camelCase.ts` for class-free runtime modules: constants, data records,
  tokens, and hooks. Type-only modules inside a contract directory follow
  [naming and placement](naming-and-placement.md#file-naming).
- Use `kebab-case/` for directories, not TypeScript filenames.
- Follow [naming and placement](naming-and-placement.md#file-naming) for the
  domain/topic/role decision. A repository may gate export parity locally, but
  no mechanical check can choose the right domain name.

### Symbols

- `PascalCase` for types and enums.
- `camelCase` for variables and functions.
- `SCREAMING_CASE` for constants and enum members.

### Boundary Normalizers

When a helper converts an external shape into the project's internal shape,
name it `normalize...`, not a vague `clean` or `sanitize`. Use `parse...` /
`tryParse...` when the helper validates a grammar and returns a domain value.

```ts
function normalizeOptionalParam(value: string | null): string | undefined {
  return value ?? undefined;
}
```

The asymmetric signature names the boundary crossing between two absence
models.

### React, When Applicable

- Use `PascalCase.tsx` and `PascalCase` component names.
- Prefix hooks with `use`.

## Name And Type Cohesion

When a variable or parameter is an instance of a project-owned type, use the
type name as the default name in `camelCase`.

Examples:

- `billingPeriod: BillingPeriod`
- `gridCoordinate: GridCoordinate`
- `localeResolver: LocaleResolver`

Rename when the local role carries meaning the type cannot: `from`/`to`,
`current`/`previous`, `source`/`target`, or `fallback`/`primary`.

Third-party types are exempt because the project does not own their vocabulary:
`layoutGroup: Group` is clearer than `group: Group` when a vendor group plays a
domain role.

If many call sites use the same non-matching name for a project-owned type, the
type may be misnamed or a missing wrapper/domain concept may be hiding there.
The review-time diagnostic lives in
[review heuristics](review-heuristics.md#name-vs-type-cohesion).

## Boolean names

- Name boolean values so they read as predicates at the call site. Prefer `isX`
  for state or condition and `hasX` for possession or presence.
- Use `canX`, `shouldX`, `didX`, or another predicate verb when it carries the
  value's real modal or temporal meaning. Keep an externally owned field or an
  established domain term when adding `is` or `has` would misstate the contract;
  do not prefix a name only to advertise its type.

## Cross-References In Comments

When a comment points at a symbol, use a supported `{@link}` reference instead
of a handwritten file path. Prefer the symbol name, such as
`{@link InvoiceState}`, when the repository's editor or documentation tool can
resolve it.

Cross-module declaration-reference syntax and rename support vary by tool.
Follow the repository's proven syntax and verify that the link resolves; do not
assume a TypeScript `import(...)` expression is a portable TSDoc link. Keep a
path only when no symbol exists, such as a config file, asset, or route.
