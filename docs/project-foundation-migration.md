# Project foundation repository migration plan

This is the retained preparation plan. Execution began after project-foundation
1.5.0 and its declaration hardening landed at
`9093cfca4ffa93df1be35b1bb7ebffaef0baac65`. The
[extraction record](../validation/framework-extraction.md) owns actual results;
the destination repository owns current framework maintenance and release rules.
The steps below preserve the original proposal and its preparation baseline.
Private cross-repository CI uses locked artifact checks; local adoption and
release checks also compare the imports with actual upstream Git objects.

## Preparation status

Prepared on 4 October 2026 against local agent-skills commit
`71b6aa0bea6b72517eff908a2f355fb3ed1f4183`. At inspection, `main` was clean and 18
commits ahead of `origin/main`. Use the local landed history when choosing the
migration base; cloning the remote alone would miss required commits.
The collection at this preparation baseline is unreleased version `1.4.0`.
These facts describe preparation, not the eventual migration baseline.

The isolated preparation branch is `prep/project-foundation-migration`, in
`.worktrees/project-foundation-migration`. It contains this plan and a read-only
inventory command. It does not alter the collection, its inventory, or main.
The next iteration's completed commit must be selected explicitly before moving
source files. An inventory run against a new commit does not establish that
the iteration has finished.

## Ownership after migration

| Source home | Owns |
| --- | --- |
| New project-foundation repository | Foundation format and authority, document homes, templates, bootstrap, project design, planning, contracts, policy, project documentation, their shared routes and framework validators |
| agent-skills | Clear-writing, diagrams-and-tables, source-of-truth, specialist collections and skills, and the shared collection installation checker |
| Forge and other consumers | Their actual policies, project facts, architecture, processes, contracts, working agreements and evidence |

Use `project-foundation` as the working name for the new repository. Its final
remote URL and access settings are selected when creating it. Keep the name
and scope independent of Forge. This preparation creates no remote repository
and publishes no release.

For the first migration, preserve the installed collection path, skill names,
foundation format, document homes and interpretation rules. Within the new
repository keep `collections/project-foundation/` so its internal relative
layout and consumer entry routes remain recognizable. Treat the three imported
skills as dependencies in the distributed collection, rather than native source
owned by this repository. Source ownership and bundled membership are different:
the checked installation can still contain all nine entrypoints.

## Make the generic dependency packages complete

Before cutting over, establish canonical, self-contained packages in agent-skills.
Proposed source paths are `skills/authoring/clear-writing/`,
`skills/authoring/diagrams-and-tables/` and `skills/design/source-of-truth/`.
Keep their skill names. Review the applicable version changes after the landed
iteration has been compared; do not assign versions from today's draft.

All three currently link to project-foundation's shared friction reference.
Source-of-truth additionally links to the collection entrypoint, foundation
authority, project-policy and shared authoring guidance. Moving directories
alone would leave incomplete standalone packages and reverse dependencies.
Make generic guidance use the consuming project's declared authority and capture
routes where those are relevant. Keep framework-specific interpretation in
project-foundation's owning references and route to it from the project workflow.
Preserve consequential unknowns, evidence distinctions and the observed-problem
capture trigger. A generic authoring request must work without installing
project-foundation; an actual project policy question must still reach its owner.

Do this in source and test the changed routes before importing the new packages.
Do not patch vendored copies to achieve independence. Preserve package-local
references, examples and UI metadata. Update agent-skills' AGENTS, catalog,
self-conformance review and current validation routes to the new source homes.
It should continue using its locally owned authoring skills.

## Import dependencies with explicit pins

Use checked, committed source revisions for the three generic packages. Import
complete directories into their existing collection destinations:
`collections/project-foundation/skills/<name>/`. Native skills and the shared
authoring reference can keep their local routes to those destinations.
Consumers receive one complete installation with its dependencies already
present; ordinary use needs no checkout of agent-skills or network resolution.

Introduce a small dependency lock owned by the new repository. For each import,
record source repository, source directory, full source commit, package version,
selected tag when present, and destination. Verify destination bytes and modes
against that selected source before regenerating the combined collection
inventory. The inventory also covers the lock if it ships with the collection.
Keep a dependency source checkout available to CI at the recorded pin; local
checks may use an equivalent already available checkout. Never track `main`
implicitly or use inventory regeneration to bless changed imports.

Keep the existing shared installation checker owned by agent-skills. Its shipped
copy is already in the collection. Record its source pin and verify it against
the canonical file when updating it. In the new repository, use that pinned
checker as the implementation for installation checks; avoid establishing a
second independently edited canonical copy. Synchronization in agent-skills
continues to affect only the collections it owns.

The package validator needs to distinguish native and imported source. For an
import, verify its exact pin and check recorded paired-rule counterparts in that
pinned agent-skills source. Keep checks of native rules strict. Source-of-truth's
paired rules with test-writing and test-audit remain owned together in
agent-skills, but their imported comments must still be accounted for in new-repo
validation. Do not remove the comments, skip the requirement, or install the
verification collection merely to make a source check pass.

This is explicit vendoring of three packages and one helper. A general dependency
resolver, automatic client discovery and independent publishing of every shared
reference are outside the migration.

## Refresh the inventory when the iteration lands

Run the preparation helper from this branch with the selected source checkout
and an explicit landed commit. It resolves the ref once, reads committed Git
objects, and prints JSON. Redirect stdout to a report outside the source checkout.
For example, from the preparation worktree, substitute the landed full SHA for
the sample ref before running:

```sh
python3 scripts/prepare-project-foundation-migration.py \
  --repo ../.. \
  --ref LANDED_FULL_COMMIT_SHA > /tmp/project-foundation-landed-inventory.json
```

The report records payload hashes, source owners, source-reference mentions,
links crossing the proposed ownership boundary, paired rules, supporting file
candidates and working-copy status. It rejects committed manifest drift and
symlink payloads. Working-copy changes are reported and excluded. It does not
copy files, execute source helpers or change either repository.

Compare this report with the preparation baseline. Review additions or changes
to membership, shared references, templates, validators, service scaffolding,
installation guidance and validation records. Every candidate outside the
collection needs a move, retained-history, imported-tool or rewritten-link
disposition. Literal searches cannot discover every symbolic or dynamic route.

## Perform the migration in order

1. **Select and preserve the landed base.** Inspect status and worktrees in the
   authoring repository. Record the full commit and the preceding consumer pins.
   Preserve required local commits, unrelated changes and ignored dependencies.
   Create fresh isolated task worktrees from that landed history; do not use the
   preparation branch's old payload as the migration source.

2. **Prepare the generic packages in agent-skills.** Establish the three source
   homes above, remove their hard-coded dependency on project-foundation, and
   validate standalone use plus the project-specific routes that replace it.
   Keep these source changes reviewable alongside the coordinated removal of
   native project-foundation source so the catalog has no duplicate package names
   or competing current owners. Commit that coordinated migration branch and use
   its full commit as the initial import pin. Keep the branch off main until the
   new repository is accessible. Publishing it is ordered below.

3. **Build the new repository locally.** Use a disposable clone of the landed
   local history and a reviewed path allowlist for project-owned source,
   authoring documentation and framework-specific validation. Prefer retaining
   relevant history through filtering. Preserve earlier source paths in the
   allowlist where needed; filtering only today's collection directory loses
   history from before grouping. Exclude canonical generic skill directories
   from the new native source and import their committed packages at the pin
   selected in step 2. Filtering rewrites commit identities: record the original
   baseline and mapping, and retain the original repository as the historical
   authority. Do not reuse published tag names for different commits.

4. **Give the new repo its own maintenance entrypoints.** Create README and
   AGENTS for the framework scope; carry its authoring convention, release and
   routing requirements, scoped self-conformance review, helper tests, CI and
   dependency lock. Adapt source tools to the actual layout and imported-source
   rules. The current runner requires Node 24, TypeScript and GnuPG for other
   collections: require them here only if retained tests need them. Preserve
   nonempty suite discovery and fail skipped or incomplete required suites.

5. **Move validation by ownership.** Framework-specific cases and their inputs
   follow the new repo. Generic writing, diagrams and source-of-truth validation
   stay with agent-skills. Split mixed collection-sweep and self-conformance
   material into current requirements and historical evidence. Historical
   records retain the names and SHAs they actually exercised, with explicit
   links to the original source. Supporting-file candidates are an inventory
   for review, not an automatic move list.

6. **Finish the agent-skills source change.** Remove its current native
   project-foundation collection and its exclusive current authoring document.
   Link the catalog to the new canonical repo. Reconcile active AGENTS, catalog,
   validation, tests and planned-companion routes. Preserve historical releases
   and evidence; label old source paths as historical rather than rewriting
   them to imply they tested the new repository. Validate the remaining
   collections with their existing checks and pins.

7. **Validate the repositories and staged distribution.** Meet the acceptance
   cases below. Compare project-owned rules with the landed baseline, accounting
   for every changed obligation or route. Do not combine the split with policy
   changes, a documentation migration or unrelated specialist reorganization.

8. **Publish in dependency order.** Make the committed agent-skills dependency
   source accessible on its migration branch first, leaving main's existing
   source available. Publish the checked new repository next, then merge the
   source retirement/catalog change. If later maintenance edits changed an
   imported package or helper, refresh its pin and repeat import verification
   before publishing the new repo. Select the
   first new-repo collection version after reviewing the landed and migration
   changes; retain release history and perform the required self-conformance
   review before tagging. A source move alone is not a consumer upgrade.

9. **Adopt in Forge as a separate change.** Stage a complete new collection,
   verify it against the selected new-repo source, and replace the installation
   with rollback available. Update provenance to the new source URL, directory,
   full commit, collection version and any tag, including imported dependency
   pins. Existing project routes should continue to resolve. Validate Primary
   and the Assets, Tools and Game members through their declared access routes.
   Leave their project facts and document homes as adopted. Other consumers
   keep their old pins until separately selected for adoption.

## Acceptance cases

| Case | Required evidence |
| --- | --- |
| Generic skills used alone | Each selects its own task and works without project-foundation; no missing shared routes or resources |
| Exact dependency import | Each imported directory and helper matches its locked source pin; a temporary changed import fails verification |
| Complete framework installation | One staged collection passes source comparison, link containment and bundled helper suites; missing or stale files fail |
| Native and imported paired rules | Counterparts remain checkable at their actual source pins; no requirement disappears because its source moved |
| Framework reading and application | Narrow foundation, documentation and contract questions preserve the existing task scope and relevant obligations |
| Framework design and review | Policy impact, inheritance, new document placement and contract adequacy still reach deeper owning guidance |
| Nearby generic task | A wording or visual explanation task uses its generic dependency without loading project bootstrap or policy |
| Forge shared access | Primary and all three members resolve the new complete installation and inherited owners from their declared contexts |
| agent-skills maintenance | Catalog, AGENTS, package checks and maintained suites work after native project-foundation is removed |

Mechanical checks establish structure and helper behavior. Practical routing
trials and the collection's self-conformance review establish separate evidence;
inventory matches alone do not establish those claims. Record actual checks,
findings, dispositions and unavailable evidence against the commits exercised.

## Rollback and handoff

Keep the original landed SHA, source retirement commit, new-repo commit, dependency
pins, first release identity and each consumer's preceding import pin in the
migration record. Preserve the original source history. Revert a consumer adoption
by replacing the complete collection with its preceding checked copy and restoring
provenance and affected routes together. Preserve local modifications first.
Never move a published tag or delete the source history to roll back.

Preparation is complete when this plan and the tested inventory helper are
available. Migration remains pending until the next iteration finishes, the
landed inventory is reviewed, and the extraction and acceptance cases run.
No background monitor or automatic consumer upgrade is established by this plan.

## Preparation verification

The preparation inventory matches the committed `1.4.0` manifest: 89 files,
nine bundled skills, six proposed native project skills and three generic skills
retained in agent-skills. The literal scan found 48 links crossing proposed source
ownership and eight current paired-rule references across the old collection
boundary. With all three generic skills retained, those paired-rule source
owners stay together in agent-skills. The import-side validation requirement
described above remains.

The five new CLI integration tests passed with synthetic temporary repositories.
They cover the immutable commit pin, source preservation with dirty files, a
newly selected ref, dependency links and paired rules, committed manifest drift,
symlink rejection and missing revisions. A temporary mutation that read working
files instead of committed blobs failed the commit-pin test for inventory drift.
The same baseline report was produced under the default and ASCII locales.

The repository's required `python3 scripts/check.py` passed: package validation
plus 92 tests across five maintained suites, with zero skips. `git diff --check`
also passed. These checks verify preparation and the unchanged current source;
the migration acceptance cases have not run.
