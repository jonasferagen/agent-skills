# Module imports

<!-- Package-boundary copy: typescript-design/references/imports-and-barrels.md (Module And Path Syntax) is checked against this authoritative passage by the source-maintenance gate. -->

## Module And Path Syntax

The repository owns ESM/CommonJS policy, file-extension conventions,
`moduleResolution`, aliasing, and lazy-loading rules. Follow those local facts;
do not infer a universal import spelling from this canon. Prefer `import type`
for type-only dependencies when the toolchain supports it, and keep dynamic
imports for genuine lazy or conditional loading.
