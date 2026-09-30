# Imports And Barrels

Barrels are opt-in API boundaries, not a file every folder needs. Use one when a
package entry point, subsystem, or sibling directory needs a stable import
surface; otherwise direct imports inside the owning area are fine.

## Barrel Policy

- Files are internal by default. Export only the surface you intend consumers
  to use.
- A directory barrel exports siblings only; it does not reach into parents,
  cousins, or deep descendants.
- An aggregator exports sibling files and immediate child barrels.
- A package-public barrel lists the intended public names explicitly when
  `export *` would leak internal helpers.
- Type exports and value exports are equally public. Use `export type` when the
  distinction improves generated output or dependency clarity.
- Follow the [one-primary-export shape](naming-and-placement.md#export-shape) for
  ordinary production modules.

## Barrel Levels

| Surface             | Purpose                                                                              |
| ------------------- | ------------------------------------------------------------------------------------ |
| Directory barrel    | One folder's intentional API, from sibling files                                     |
| Aggregator barrel   | Immediate child barrels gathered into a larger boundary                              |
| Package entry point | Explicit surface for external consumers                                              |
| Bridge barrel       | Rare transitional/public surface whose consumer and removal condition are documented |
| Internal module     | Implementation absent from boundary barrels                                          |

Use aggregators sparingly. A bridge that has no live consumer provides no
compatibility; it is dead surface.

## Choosing An Import Boundary

- Import from the nearest stable boundary matching the dependency you intend to
  take.
- Use direct sibling imports inside one directory.
- Use a directory barrel for cross-folder imports only when the directory is a
  real subsystem boundary.
- Direct cross-folder imports are acceptable inside one tightly owned feature
  area when no boundary exists.
- Use package entry points for external consumers and true package boundaries.
- Do not bypass an existing appropriate boundary to reach a concrete file.
- Flatten a thin subdirectory when its files mostly reach back into the parent.
  Widening the parent barrel to keep such a subdirectory separate hides that it
  is not a real boundary.

## External Dependency Boundaries

Isolate a third-party runtime, platform API, persistence client, or optional
adapter behind the area that owns it. Domain modules should depend on
project-owned contracts and values; boundary modules adapt them to concrete
external types.

Keep the boundary name honest. A directory named for a dependency may import
that dependency and project-owned values. Neighboring domain directories remain
free of it unless their public purpose is to expose that external surface.

<!-- Package-boundary copy: typescript-patterns/references/imports.md (Module And Path Syntax). Keep both passages aligned. -->

## Module And Path Syntax

The repository owns ESM/CommonJS policy, file-extension conventions,
`moduleResolution`, aliasing, and lazy-loading rules. Follow those local facts;
do not infer a universal import spelling from this canon. Prefer `import type`
for type-only dependencies when the toolchain supports it, and keep dynamic
imports for genuine lazy or conditional loading.

## Prohibited Shapes

- Do not import through a barrel from within the same directory.
- Do not use re-export declarations in an ordinary implementation module unless
  it intentionally owns a documented public wrapper.
- Do not import from a package's public root from inside that package unless its
  architecture explicitly sanctions the dependency direction.
- Do not deep-import another directory's file when that directory already
  exposes the capability you need.
- Do not add barrels or exports solely to silence a checker; first decide
  whether the boundary should exist.

## Align Policy Before Cleanup

A repository-owned checker models policy; it does not create policy. When a
diagnostic conflicts with the documented or exported surface, fix the model and
pin that distinction in the checker's own tests before rewriting legal imports.
Then treat the remaining findings as review input.

A durable checker derives current package surfaces from authoritative export
maps or configuration instead of carrying a hardcoded inventory of filenames.
Keep exceptions small, named, and justified; an exception list is not a place to
park violations you mean to fix later.
