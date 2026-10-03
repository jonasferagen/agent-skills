# Isolated foundation consumer trial

Fixture root: `/tmp/foundation-reference-trial-ffc9fnpk`. Artifact paths below
are relative to that retained local fixture; this file records the trial evidence.

Date: 2026-10-03. Draft collection, base 4770b35c4276ba9c6002d23709ebea5cb3d7efbe. All work stayed in this fixture. No source repository, browser, account, application runtime, package service or live system was used.

## Outcome

Bootstrapped Orchard (shared coordination owner), Renderer, independent Pebble and a synthetic Catalog sibling. Each has one `docs/foundation.md`, README and AGENTS. Orchard and Pebble each carry the complete installed collection with draft provenance. Members route to Orchard through one named binding. Initial Git changes used orphan bootstrap task worktrees; later edits used actual nested task worktrees. Git logs preserve staged project diffs and checks. These are documentation fixtures, not working applications.

The actual route/read harness passed 94 checks, including binding-only relocation, local files and section anchors, inherited shared policy changes from main and nested worktrees, local isolation, explicit Blender-version uncertainty and unavailable parent behavior. See `exercise-results.json` for every check and programmatic read. This harness explicitly resolves a known fixture binding. It is not a shipped or general Markdown resolver.

## Artifacts and cases

- `orchard/docs/foundation.md`: coordination/shared owner; local development, retain originals, no public hosting, recovery undecided, delegated member stacks.
- `renderer/docs/foundation.md`: relocated binding only; Renderer responsibility and local Blender choice, unknown version; shared policy axes omitted so they inherit.
- `renderer/.worktrees/tasks/routing/`: actual nested Git task worktree, with reviewed local changes and proposal assessment in `docs/hosting-proposal.md`.
- `orchard-relocated/`: local clone for relocation. The Renderer reference binding was the only content changed for relocation; README, AGENTS and skill suffixes did not need edits. All symbolic skill routes and section anchors resolved from both actual main and nested checkouts.
- Shared change: isolated Orchard requirement to edit working copies while retaining originals was authored in its nested policy worktree and landed in its fixture main. Reads through Renderer main and task bindings observed it. Member summary reconciled in the task worktree. `orchard-relocated/docs/task-notes.md` records impact and missing implementation evidence.
- Local choice: Renderer selects Blender background rendering as a local interface choice; byte comparisons establish Catalog and Pebble foundations stayed unchanged. They contain no Blender adoption.
- Explicit unknowns: Blender version stays unknown; source sensitivity and ownership remain unknown; recovery targets stay undecided. Omitted shared axes inherit prohibition and source retention. No blank value or omission was interpreted as permission.
- Hosting exception: proposal only. It conflicts with shared policy and boundaries; no adoption occurred. The proposal records missing reason, decision authority and review/expiry condition, affected owners, required reviews, acceptance evidence and gates for public use.
- Missing parent: renamed the relocated parent directory, checked the dependency was unavailable, read the local missing-owner rule, deferred hosting-dependent decisions, made an unrelated README wording edit, then restored the directory. No stale snapshot was substituted.
- Nearby wording edit: README “boundaries, overview and policy” became “project boundaries, overview and policy”. This preserves meaning; focused content/link/diff checks sufficed.

## Routes activated

Bootstrap → multi-repository guidance, Git worktrees, foundation authority, policy, docs, authoring, clear writing and instruction writing, structure/ownership, and templates. Binding ownership and coordinated shared changes → source-of-truth and definitions. Proposed hosting transition → project-policy and policy-changes. The literal nearby wording edit did not trigger bootstrap, full policy reconstruction, diagrams or authoring rereads. Friction capture was consulted for the actual harness/tool setbacks. No visual, Mermaid, tool discovery, source authoring or release routes were needed.

## Constraints, shortcomings and limits

Preserved all requested substantive constraints: separate independent Pebble, single foundation per repo, shared ownership and local implementation scope, originals retained, recovery undecided, public-hosting prohibition, proposal/adoption distinction and unavailable-authority deferral. No scenario constraint was knowingly missed.

Operating summaries remain manually maintained derived copies. The shared-change exercise updated Renderer task instructions; its main summary still has the older shorter source-retention wording until those pending changes are landed. It is compatible with the tighter rule but is not automatic synchronization. Catalog deliberately remains bound to the original Orchard fixture, so policy propagation was verified for relocated Renderer only. Local choice isolation uses foundation byte comparison, not runtime effects. Absolute filesystem binding worked in these Linux worktrees; relative bindings, remote URL content/revision policies, Windows, cycles and independently absent shared collection access were reviewed conceptually, not exercised. No rendering, restore, deployment, authentication or operational compliance was tested.

The fixture harness had two corrected setup errors: `python` was absent, so `python3` was used; its first exercise run lacked a helper and stopped after clone creation. The helper was added and the complete successful run followed. No product data or real repository was affected. These were harness errors, not evidence of collection defects.

## Reading cost

Consumer source files actually read are listed below. Approximate words use whitespace counts. Full files were returned without truncation. First-pass reading was batched and reused from context for subsequent routes; no authoring/source repository documents were read. A few source-of-truth and policy-change references were loaded in advance of their known later cases, rather than waiting for each action. Those routes were subsequently used; no unused specialist reference was identified.

Initial instruction/collection reading: 10,918 words across 19 files.

- `AGENTS.md`: approximately 14 words.
- `installed/UPSTREAM.md`: approximately 12 words.
- `installed/project-foundation/COLLECTION.md`: approximately 496 words.
- `installed/project-foundation/references/multi-repository.md`: approximately 871 words.
- `installed/project-foundation/references/foundation-authority.md`: approximately 430 words.
- `installed/project-foundation/references/authoring.md`: approximately 248 words.
- `installed/project-foundation/references/friction.md`: approximately 210 words.
- `installed/project-foundation/skills/project-bootstrap/SKILL.md`: approximately 1256 words.
- `installed/project-foundation/skills/git-worktrees/SKILL.md`: approximately 336 words.
- `installed/project-foundation/skills/project-policy/SKILL.md`: approximately 1209 words.
- `installed/project-foundation/skills/project-policy/references/policy-changes.md`: approximately 919 words.
- `installed/project-foundation/skills/project-docs/SKILL.md`: approximately 816 words.
- `installed/project-foundation/skills/project-docs/references/structure.md`: approximately 774 words.
- `installed/project-foundation/skills/source-of-truth/SKILL.md`: approximately 603 words.
- `installed/project-foundation/skills/source-of-truth/references/definitions.md`: approximately 1393 words.
- `installed/project-foundation/skills/clear-writing/SKILL.md`: approximately 549 words.
- `installed/project-foundation/skills/clear-writing/references/instructions.md`: approximately 506 words.
- `installed/project-foundation/templates/docs/foundation.md`: approximately 268 words.
- `installed/project-foundation/templates/README.md`: approximately 8 words.

Harness reading: 86 recorded reads, approximately 26356 words processed. Repeated route target/foundation reads were intentional verification from main, task and relocated roots; the harness does not imply the agent reread every returned skill in full. Detailed per-read paths and counts are in `exercise-results.json`. The first failed harness attempt repeated initial Renderer route checks on retry and is not included in those successful-run counts. Template scope comments were read programmatically again during generation. Agent review additionally read Renderer foundation/AGENTS, Orchard and Pebble foundations (approximately 1,200 words total), the proposal and final diff. No tool output was truncated.

## Verification and Git state

`git diff --cached --check` passed before fixture bootstrap commits; `git diff --check` passed for pending nested Renderer changes. Main fixture bootstrap commits and synthetic policy commits are local only. The nested Renderer routing worktree retains the summary update, local wording edits and proposal for review. No publishing or live-system work occurred.

## Supplemental explicit-unknown case

Added `explicit-unknown-case/parent/docs/foundation.md` and `explicit-unknown-case/member/docs/foundation.md`, with the actual interpretation in `explicit-unknown-case/interpretation.md` and targeted results in `explicit-unknown-case/results.json`. The parent has a known Blender 4.2 default and a known recovery obligation: restore retained originals within 24 hours with no original-source loss, verifying before a readiness claim. The member has an explicit unknown version and unknown recovery implementation readiness. The version stays unresolved instead of silently taking 4.2. Recovery readiness stays unknown while the shared recovery obligation remains effective. No exception, restore evidence or readiness is inferred.

Six supplemental checks passed. SHA-256 comparisons preserved all six baseline foundations (Orchard, relocated Orchard, Renderer main and task worktree, Catalog and Pebble). The full harness was not rerun. The script read two new foundation files; paths and word counts are recorded in its results. Agent review inspected both new foundations, the interpretation and results. This is a synthetic interpretation exercise, not an adopted change to the Orchard recovery targets.

## Initial read classification

“Required” means the selected task or installed workflow explicitly routed the read. “Useful” means it helped this trial but was not needed to bootstrap or interpret the main facts. No initial file was wholly irrelevant to the combined task; that does not make all its content necessary for a smaller task.

Required for entry, distribution and provenance:

- `AGENTS.md`: fixture entry instructions and isolation boundary.
- `installed/project-foundation/COLLECTION.md`: required starting route and conditional workflow selection.
- `installed/UPSTREAM.md`: copied draft provenance accurately without following it into the source repository.

Required for the multi-repository bootstrap and Git edits:

- `references/multi-repository.md`: ownership, named binding, inheritance, relocation and missing-authority rules.
- `references/foundation-authority.md`: constraints, consultation, proposals and evidence.
- `skills/project-bootstrap/SKILL.md`: requested bootstrap workflow.
- `skills/git-worktrees/SKILL.md`: required before edits in Git; orphan and nested worktrees exercised.
- `templates/docs/foundation.md` and `templates/README.md`: bootstrap templates, preserved scaffold and section comments.

Required for establishing and assessing the documents (all following paths under `installed/project-foundation/`):

- `skills/project-policy/SKILL.md`: bootstrap explicitly requires initial policy assessment; also used for hosting and shared change.
- `skills/project-policy/references/policy-changes.md`: required for substantive hosting proposal/shared change assessment.
- `skills/project-docs/SKILL.md`: bootstrap explicitly requires document routes.
- `skills/project-docs/references/structure.md`: explicitly routed for document homes and reader routes.
- `references/authoring.md`: bootstrap explicitly requires it when composing new documents.
- `skills/clear-writing/SKILL.md`: authoring route for choosing wording.
- `skills/clear-writing/references/instructions.md`: required for writing AGENTS instructions.
- `skills/source-of-truth/SKILL.md`: coordinated shared policy and derived summary work.
- `skills/source-of-truth/references/definitions.md`: owner/binding choice and reading shared decisions from their owner. The whole file was read, although the external-reference ownership section was the most directly useful part; vocabulary and multi-language examples exceeded this fixture's needs.

Useful, conditional read:

- `references/friction.md`: recorded actual harness/tool setbacks at the checkpoint. This was unnecessary for successful bootstrap alone, and the setup errors did not establish a collection defect.

Irrelevant files read: none identified. Conditional visual, diagram rendering, worked-example, runtime-boundary and source-authoring references were not read.

## Routing evidence limits

The nearby ordinary wording edit happened in the same context after bootstrap and policy guidance had already been read. It demonstrates that the consumer reused context and performed a focused edit without additional workflow reads; it does not measure startup cost or prove selective routing in a fresh context. A separate cold-start negative trial for a simple wording-only task was not performed.

This trial consumed an installed draft collection. It did not inspect or exercise the source repository's authoring, evaluation or release routes and therefore makes no claim about their correctness. No fresh source-authoring consumer or cold-start negative consumer was spawned for this supplemental check.
