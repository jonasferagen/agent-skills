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
  public/shared identity, such as a canonical export whose prefix is part of
  the package's public API; prevents a real ambiguity; or names a concept used
  widely outside the directory (`console/ConsoleCommands`, `admin/AdminBoot`).
  A consumer's import line names the directory once; the prefix names the
  domain at every later use.
- If the prefix-free name would clash with another exported identifier in the
  same file, rename one of them. A collision is not a reason to keep the
  prefix.
- If the prefix is the only thing tying some siblings together, the directory
  holds unrelated files. Split the directory instead of keeping the prefix.

### Why

- The prefix is noise at every read site within the directory and at the import
  statement.
- Cross-directory consumers usually import through the barrel, whose path names
  the directory, so most classes need no prefix even there.
- Mixed prefixes leave no clear convention for the next file added.

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
  parent until a second sibling justifies the subdirectory, unless the
  subdirectory is a known growth area whose next files are planned.
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

- A top-level `types/` directory that is genuinely the home for cross-cutting
  passive contracts. Even there, prefer named subgroups once the file count
  grows past a handful. A top-level `utils/` gets no such exemption: split its
  files by domain or concept, as for `helpers/`.

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
  in a named sequence** (good) or a **kind of object** (bad). `compile/` and
  `parse/` are fine; `parsers/` is not, even when every file is a parser.

### Why

- A concept or phase folder makes the next file's home predictable; a role folder
  accretes anything that shares a suffix.
- The folder list narrates the domain — or the pipeline — when every entry is a
  concept or a phase, and stops narrating anything the moment a role bucket
  appears beside them.

### When Not To Use

- A `types/` subdirectory of passive contracts is named for what it owns:
  nothing in it runs. A role folder such as `parsers/` does not qualify.

## Type-Only Files In Directory Shapes

A directory's shape decides where passive type-only modules go.

| Directory shape | Family | Subsystem |
| --- | --- | --- |
| What it holds | Homogeneous: every file is a peer in the same vocabulary family, such as values, events, materials, vectors, or wire payload atoms | Mixed responsibility: an owning runtime concept plus support contracts, helpers, adapters, or nested families |
| Type-only modules | Family members live beside class-bearing peers | Support modules go in a `types/` subdirectory when the subsystem needs one |
| Why | The directory itself is the contract surface | The root stays focused on primary runtime concepts |
| Do not | Add a `types/` subdirectory just because a file is passive | Scatter support contracts through the root when a `types/` subdirectory would make their role clearer |

The same [type-placement
tiers](naming-and-placement.md#type-placement-three-tiers) still apply: promote a
type only when its scope justifies the new home.
