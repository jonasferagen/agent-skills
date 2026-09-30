# Directory Patterns

## Contents

- [Directory carries the prefix](#directory-carries-the-prefix)
- [Cohesive directory](#cohesive-directory)
- [Concept or phase, not bare role](#concept-or-phase-not-bare-role)
- [Type-only files in directory shapes](#type-only-files-in-directory-shapes)

## Directory Carries The Prefix

When a class lives in a directory whose name already disambiguates it, drop the
redundant prefix from the filename and the class name.
`billing/tax/RateResolver.ts` reads more clearly than
`billing/tax/BillingTaxRateResolver.ts`—the directory already supplies the
billing-tax domain. The same holds for sibling names such as `RateTable` and
`RatePolicy`.

This is the directory side of the
[`{Domain?}{Topic}{Role?}` filename grammar](naming-and-placement.md#file-naming):
the path is already part of the name readers see at import sites and in editor
search, so a domain prefix needs a specific reason to be in the name.

### Rules

- Drop the prefix when the directory name encodes the same namespace.
- Rename the file and the class together. The file is named after the class,
  and consumers import by class name; both should follow the same convention.
- Apply uniformly across the directory in one pass. Mixed prefixes inside a
  single folder are the visible drift that triggers the cleanup.
- Co-located type aliases follow the class.
- Prefer a bare topic plus role (`RateResolver`, `InvoiceBuilder`) when
  the directory supplies the domain. Keep a domain prefix only when it is a
  public/shared identity, prevents a real ambiguity, or signals a concept that
  travels meaningfully outside the directory. A class imported from outside
  its folder qualifies (`console/ConsoleCommands`, `admin/AdminBoot`): the
  import site loses the path context, so only the prefix names the domain
  there.

### Why

- The prefix is noise at every read site within the directory and at the import
  statement.
- Cross-directory consumers usually import via the barrel, so the directory
  name appears at the call site exactly when the prefix would have been
  informative.
- Mixed prefixes leave no clear convention for the next file added.

### When Not To Use

- Name collision: if the prefix-free name would clash with another exported
  identifier in the same file, rename one of them rather than keeping the
  prefix on the other.
- The class is the canonical export of a domain contract where the prefix is
  part of the public API consumed downstream of the package.
- The directory holds genuinely unrelated files where the prefix is the only
  thing tying related siblings together. That is a sign the directory needs
  splitting, not a sign to keep the prefix.

## Cohesive Directory

A directory's contents should share one concept that a single short sentence
can describe. When the honest one-line description needs an "and also" clause,
split the directory.

### Rules

- The directory's name and one-line description should cover every file without
  "and also."
- An orchestrator that consumes from multiple sibling directories belongs at
  the parent level, not nested inside one of its dependencies' folders.
- A one-file subdirectory is over-fragmentation. Flatten the file into the
  parent until a second sibling justifies the subdirectory.
- Bridge re-exports across directories need an explicit public-surface reason.
  Otherwise, move the directory so the bridge is unnecessary or drop the bridge.

### Why

- A directory of unrelated files is the visible end-state of accretion.
  Splitting when the contents first drift from one concept is cheaper than
  splitting after another year of additions.
- Directory names are part of the namespace at every import site.
- Orchestrators buried inside a dependency's folder mislead readers about
  ownership.

### When Not To Use

- Top-level catch-all directories like `utils/` or `types/` that are genuinely
  the home for cross-cutting helpers. Even there, prefer named subgroups once
  the file count grows past a handful.
- A subdirectory holding two or three files today but in a known growth area.

## Concept Or Phase, Not Bare Role

A directory name answers one of two questions: **"what domain lives here?"** or,
in a genuine pipeline, **"which phase?"** A concept noun like `billing`,
`delivery`, or `identity` answers the first; a stage in a documented sequence,
like `compile` or `emit`, answers the second. The directory must not be named
for a generic technical role that could hold anything, such as `producer/`,
`parsers/`, `handlers/`, or `helpers/`.

This sharpens [Cohesive Directory](#cohesive-directory) with an explicit
concept-vs-role test. A concept or phase folder has a one-line invariant with no
"and also"; a role folder's only invariant is "things that happen to be this kind
of unit." `billing/` can mean "owns invoices, payments, and their policy";
`handlers/` means only "things that happen to handle something"—that is the
smell.

### Rules

- Name a directory for the concept it owns or the pipeline phase it represents,
  never for the kind of unit its files happen to be.
- A role word in a directory name is the signal to split by concept, or to rename
  the folder to the phase its files actually share.
- In a pipeline or compiler the _phases are the domain_, so phase-named folders
  like `compile/` and `emit/` are correct and desirable — a reader should see the
  pipeline by scanning the folder list. The test is whether the name is a **step
  in a named sequence** (good) or a **kind of object** (bad). `compile/` is fine;
  `parsers/` holding non-parsers is not.

### Why

- A concept or phase folder makes the next file's home predictable; a role folder
  accretes anything that shares a suffix.
- The folder list narrates the domain — or the pipeline — when every entry is a
  concept or a phase, and stops narrating anything the moment a role bucket
  appears beside them.

### When Not To Use

- A folder whose concept genuinely _is_ a unit kind — a `types/` contract surface
  or a `fixtures/` test-support family — is named for what it owns, not for an
  accreting role. The smell is a role name holding mixed concepts, not any folder
  that happens to share a suffix.

## Type-Only Files In Directory Shapes

A directory's shape decides where passive type-only modules go.

**Family directories** are homogeneous: every file is a peer in the same
vocabulary family, such as values, events, materials, vectors, or wire payload
atoms. Type-only family members live beside class-bearing peers because the
directory itself is the contract surface.

**Subsystem directories** are mixed-responsibility: they hold an owning runtime
concept plus support contracts, helpers, adapters, or nested families. Type-only
support modules go in a `types/` subdirectory when the subsystem needs one, so
the root stays focused on primary runtime concepts.

Do not add a `types/` subdirectory to a family just because a file is passive.
Do not scatter support contracts through a subsystem root when a `types/`
subdirectory would make their role clearer. The same
[type-placement tiers](naming-and-placement.md#type-placement-three-tiers) still
apply: promote a type only when its scope justifies the new home.
