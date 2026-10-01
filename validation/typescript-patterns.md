# Validation scenarios — TypeScript patterns

These scenarios cover the language package from 2.0.0. The class-based design
scenarios now live in [TypeScript design](typescript-design.md). Earlier records
below describe the combined 1.x package under its historical name and paths.

| Request and context | Expected outcome |
| --- | --- |
| A cast is unavoidable at an opaque browser or vendor boundary | Keep it local and explained; do not invent a false type proof. |
| A total label table uses `satisfies readonly State[]` | Explain that membership is not completeness; derive the vocabulary from its owner or use a total record. |
| A closed-union switch returns a value with no default | Require the documented compiler settings before claiming missing cases will fail compilation. |
| A generic preserves the type relationship between an input and output | Use the generic; avoid a framework for a one-site helper. |
| A strictness check reports an unread nominal marker | Preserve the type guarantee and inspect the marker's purpose before removing it. |
| A lint exemption hides both a valid idiom and a real defect | Narrow the one rule's scope and document the unverified portion. |
| A project asks about import extensions or module resolution | Follow project configuration; no universal spelling or barrel policy is inferred. |
| A request only concerns filename case or class-based operation organization | Language guidance does not prescribe that choice; select adopted design guidance separately. |
| Asked to add tests or run a review workflow | Follow the consuming repository's conventions. |
| Local docs contradict this package | Report the contradiction with both passages; edit neither owner to settle it. |

## Split into language and design — 2026-09-30

The split is based on main at `4755a78`. It preserves the reference rules and
examples while changing selection and ownership. The scope reduction makes `typescript-patterns` 2.0.0;
consumers seeking the former full contract must adopt both packages.

### Reference ownership

| Former reference | Current home |
| --- | --- |
| `class-shape.md`, `dependency-ports.md`, `directories.md`, `domain-primitives.md`, `orchestration.md`, `utilities-and-data.md` | Moved unchanged to `typescript-design/references/` |
| `naming-and-placement.md`, `resolution.md` | Design; mirror links now reach a local completeness summary |
| `imports-and-barrels.md` | Design; its short module-syntax rule is also available in patterns' `imports.md` |
| `typescript.md` | Patterns; naming, boolean naming and comment links moved to design's `conventions.md` |
| `types-and-generics.md` | Patterns; name/type cohesion moved to design's `conventions.md` |
| `review-heuristics.md` | Split into type questions in patterns and design questions in design |
| `enforcement.md` | Patterns, unchanged; remains a conditional reference |

Both entrypoints retain repository authority, the focused workflow and output
expectations. The shape-escalation table belongs to design. Short shared
constraints have reciprocal source comments: repository authority/workflow,
module syntax and total registries. Neither package requires the other to be
installed or links outside its own directory.

### Review basis and limits

Clear writing was applied to the new entrypoints, scope descriptions and
migration guidance. Existing rule strength, exceptions and code examples were
preserved. Diagrams and tables guidance selected symptom tables and the mapping
above; no diagram is needed for this two-package selection decision.

The scenarios are reviewed statically against their routed references. This
is not an independent agent evaluation or evidence of host skill discovery.
No consumer installation, release tag, Python skill or Bash change is included.

### Measured checks

- `python3 scripts/validate-packages.py`: passed for all 14 packages.
- Skill creator's `quick_validate.py`: passed for each TypeScript package.
- Each package was copied alone into a separate temporary root and passed the
  repository validator's manifest, local-target and containment checks.
- `remark` CLI with `remark-validate-links --frail --no-stdout`: passed across
  README, AGENTS, every skill Markdown file and every validation page. The
  temporary runner needed an absolute plugin path because npm's ephemeral
  installation was not resolvable from the worktree; no dependency was added.
- A comparison against the source found all 19 fenced examples byte-for-byte
  unchanged. Six moved design references and the retained enforcement reference
  are also byte-for-byte unchanged.
- `git diff --check`: passed.
- Rendered both entrypoints, the current validation tables, reference mapping
  and catalog in external Chrome at an 830 px content width. Tables wrap and
  remain readable without horizontal clipping. This used temporary HTML,
  not a committed renderer or a host-specific discovery test.

Stale-reference review covered the moved paths, their basenames and stems,
old design invocation examples and both skill names. Current catalog links and
invocations follow the new owners; older validation and provenance records
retain the historical package name. Consumer pins are outside this change.

## Historical validation of the combined package

## Initial checks — 2026-09-29

Structure validated against the skill-creator conventions: an 80-line `SKILL.md`,
and a table of contents on `references/typescript.md`, the one reference page
over 300 lines. Every relative link and heading anchor resolves inside the
package, with none pointing outward. No references to companion skills remain
after the decoupling, and the frontmatter description was rewritten to list
call-site symptoms rather than advertise testing.

The author reviewed the instructions against the cases above. No independent
behavioral evaluation has been run, and the package has not yet been exercised
in a real project since testing left its scope.

## Release 1.0.0 — 2026-09-29

Added manifest version metadata for the per-skill release and commit pinning
convention. The TypeScript description is quoted so its colon parses as YAML. The instruction body and references are unchanged.
The manifest validator passes, and all 119 internal links and heading anchors
resolve. Behavioral scenarios remain the review basis above; this packaging
release does not claim a new independent behavioral evaluation.

## Release 1.0.1 — 2026-09-29

Removed three leftover dependencies on the source project's policy. Compatibility
guidance now checks actual deployed consumers and published contracts instead of
assuming nothing is in production. Enforcement guidance states its own rationale.
The manifest validator and all 119 local links/anchors pass. A package search
finds no remaining source-project policy references.

## Clear writing pass — 2026-09-30

Version 1.0.2 revises the prose of the manifest and twelve reference pages;
`types-and-generics.md` needed no change. See the [package
sweep](clear-writing.md#package-sweep--2026-09-30). The description's "blurring"
became "becoming unclear", matching the symptom table. Review found one changed
causal claim about where a total mirror's compile error appears and one clarity
regression; both were corrected with the other wording notes. Code, links and
heading anchors are unchanged. No behavioral trial was run.

Left unresolved, because each answer changes behavior:

- The manifest calls a contradiction with local docs drift "to reconcile"; the
  scenario above says to surface it.
- `directories.md` says an import from outside a folder loses the path context,
  while its rationale says such consumers import through the barrel, whose path
  names the directory.
- `directories.md` forbids `parsers/` as a role name, then implies a folder
  holding only parsers is acceptable.
- `review-heuristics.md` applies its prompts to reviewing a colleague's code,
  then says reviewing a diff is a separate task.
- `dependency-ports.md` uses "conduit" both for a class that only forwards a
  dependency and for an opaque external boundary.
- `enforcement.md` never defines the "both directions" in which a rule can fail.

## Diagrams and tables pass — 2026-09-30

See the [package pass](diagrams-and-tables.md#package-pass--2026-09-30). Three
passages became tables: the shape-escalation steps in the manifest, the family
and subsystem cases in `directories.md`, and the closed-union shapes in
`review-heuristics.md`. Review corrected one changed quantifier, "the other two
fail open" for "two shapes fail open". The tables were rendered at 830 px in
both themes. The version stays 1.0.2, which is unreleased.

Left unresolved:

- Filename case for type-only and contract modules has three answers: a
  lowercase domain noun in `naming-and-placement.md`, camelCase for class-free
  contract modules, and PascalCase in `DeliveryTypes` and `XTypes.ts`.
- `review-heuristics.md` says the safe closed-union shape triggers TS2366
  without the compiler-settings caveat that `typescript.md` gives.

## Resolutions — 2026-09-30

Version 1.1.0 carries these changes.

The owner accepted every recommendation below. The version stays 1.0.2 until
release.

- Drift with local docs: "reconcile" versus the scenario's "surface". The
  manifest now says to report it to the user, quoting both passages, and to
  edit neither side. Owner decision: report.
- Type-module filename case: three answers. Owner chose PascalCase
  `{Topic}Types.ts` for sibling contract files, a lowercase noun only inside a
  contract directory, and camelCase for class-free runtime modules, in
  `naming-and-placement.md` and `typescript.md`.
- Prefix versus barrel: "the import site loses the path context" versus
  importing through the barrel. A prefix now stays for concepts used widely
  outside the directory, because it names the domain at every later use.
- `parsers/`: forbidden, then implied acceptable. It is now a role folder even
  when every file is a parser; only a `types/` contract folder is exempt.
- Prefix-rule "When Not To Use": two items were not exceptions. They are now
  rules; the public-API item joined the public-identity condition.
- "Two or three files … known growth area": exempted no rule. It is now an
  exception to the one-file flattening rule. Owner decision.
- Review heuristics: authoring-only versus reviewing a colleague's code. The
  page now supplies prompts for use inside the repository's review workflow,
  and its diagnostics say "the change" instead of "the diff".
- TS2366: the safe closed-union shape lacked a settings caveat. Both pages now
  require a declared return type without `undefined` under `strictNullChecks`
  (TS2366), or `noImplicitReturns` (TS7030). Tested with TypeScript 5.9.3 (no
  error by default) and 7.0.2 (TS2366 by default; none with `--strict false`).
- "Conduit": a forwarding class and an external boundary. The external sense
  is now "boundary", matching the vendor-cast scenario.
- Enforcement "both directions": undefined. The probe now checks that the idiom
  stops being reported and the defect is still reported.
- Smaller slips: "constraint" became "type parameter" in
  `types-and-generics.md`; `class-shape.md` names the costs it compares; the
  lifecycle list in `dependency-ports.md` no longer calls keeping the concrete
  dependency a port; its contents list gains the provider-types section;
  `resolution.md` says "the ledger" for "it".
- Testing leftovers removed: the fixture-module naming sentence in
  `naming-and-placement.md` and `fixtures/` in `directories.md`.

`utils/` (owner decision, resolved after the list above): `directories.md`
exempted a top-level `utils/` catch-all, while `naming-and-placement.md` says to
avoid `Utils`, the concept-or-phase rule forbids `helpers/`, and
`utilities-and-data.md` says utility is no exemption → only a top-level `types/`
of passive contracts stays exempt; `utils/` is split by domain or concept like
`helpers/`. Fewer exceptions to maintain was the reason.

Filename casing (owner decision, reaffirmed): a parallel branch proposed an
export-parity rule, under which a `Types` bundle is camelCase (`orderTypes.ts`)
because no export carries its name. The owner kept option A above,
`{Topic}Types.ts` in PascalCase, as the simpler rule; the export-parity commit
is not part of this package.

## Discovery routing — 2026-09-30

The discovery review shortened the 1.1.1 description before the language/design
split. Version 2.0.0's description was written for the split and has 30 words, so
the review's measurements for this skill describe 1.1.1, not 2.0.0. See [the
discovery review](discovery.md) for the measured sizes, scope and verification.
Earlier behavioral results do not establish the new discovery behavior.
