# Routing and obligation preservation review

Reviewed the working-tree diff against `fd7326a`, including the four untracked references. Started with repository `AGENTS.md`. No repository files were edited and no external actions were taken.

## Findings

### Medium: direct contract application can miss a changed-circumstance trigger

`collections/project-foundation/skills/project-contracts/SKILL.md:13–15` now loads foundation authority only when establishing or reconciling obligations or resolving conflicting authority. It says reading or applying known terms needs only relevant owners. Unlike the changed policy/docs entrypoints and collection entrypoint, it omits assessing changed circumstances.

Concrete case: enter project-contracts directly to assess an existing handoff under newly introduced real user data or public exposure, with unchanged contract terms. The Apply branch compares the action with the agreement but does not route the newly observed circumstance to policy assessment. The policy route in `references/design.md` is reachable for design/change and some deeper reviews, but applying known terms expressly avoids that route. The collection now explicitly permits bypassing its entrypoint when the workflow is known, so its changed-circumstances trigger is insufficient for this direct entry.

Previously the contracts entrypoint routed adopted constraints to foundation authority, whose operating instructions explicitly revisit affected owners for real private data, another user, network access or hosting. Preserve that conditional trigger in contracts while keeping ordinary application narrow. This is a source-level missing route, not an observed consumer failure; a focused direct-entry trial should establish its practical effect.

### Low: the moved installation text has an ambiguous copy source

`collections/project-foundation/references/installation.md:17` retains “copy this whole directory” from `COLLECTION.md`. In its new location, the containing directory is `references/`, which is not the installation unit. Earlier lines correctly require the complete collection, so the intended instruction is recoverable, but the concrete copying instruction should name the collection root or link `../COLLECTION.md`. Copying only `references/` would omit skills and templates and break installation routes.

## Preserved obligations and scope boundaries

The policy split retains the former establishment/change reference's six axes, requirement discovery, consequential unknowns, table-only policy owner, relocation-before-removal rule, source tracing, explicit commitment preservation, authorized execution limits, and distinction between adoption and compliance.

Every policy edit still requires an impact assessment outside the policy table. Literal edits explicitly allow a no-obligation-change result without rebuilding the profile. Substantive relaxation and tightening retain the consequence review, existing queue, owners, dependencies, acceptance evidence, gates, observed-transition handling and authorized follow-through. The removed paragraph about stricter requirements is covered by the existing policy-changes execution and queue instructions.

Establishment reaches requirements and writing guidance. Adequacy review reaches requirements without requiring document restructuring. Changed circumstances reach policy-changes even if no policy text changed. Writing guidance remains reachable when facts are updated. Full-profile adequacy review can reach the six axes through the explicit requirements link. Narrow reading/compliance routes preserve unknowns and evidence gaps without automatically starting a broad audit.

The installation reference retains whole-collection packaging, declared shared/local ownership, provenance including uncommitted drafts, explicit AGENTS routing, user-wide scope, and worktree activation through bootstrap. Foundation inheritance remains reachable through collection foundation-format routing, substantive foundation-authority routing and the policy member route.

## Checks and limitations

- `python3 scripts/validate-packages.py`: passed; 25 skill entries and one collection.
- `git diff --check`: passed.
- Searched for the removed `establish-and-change` name: remaining occurrences are dated validation read logs/source-review history, not active instruction links. Historical references should remain historical.
- No practical consumer routing trial was performed by this reviewer. Static preservation and link checks do not satisfy the repository's routing acceptance requirement by themselves.
- No installation copy or external client discovery test was performed. No operational compliance was assessed.
- Read the full tracked diff and all four untracked references; full policy, contracts, docs and design entrypoints; contracts design/review references; foundation-authority, authoring, multi-repository and friction references; repository authoring convention and Clear Writing; relevant routing acceptance/method excerpts. The baseline contracts opening was also read directly. Tool outputs were not truncated.
- Historical trial search matches were used only to classify obsolete-name occurrences. No prior task or trial conclusions were used as evidence for this review.

## Final focused disposition

Re-read the final contracts opening, installation reference and foundation-authority reference, and checked foundation-format and multi-repository lookup/access instructions. Both original findings are resolved in source:

- Contracts now explicitly routes changed scope or operating circumstances to foundation authority and limits its narrow read/apply exemption to unchanged constraints. Foundation authority retains affected-owner consultation, transition examples and the project-policy route.
- Installation now explicitly names the complete `project-foundation/` directory as the copy source.

The new foundation-authority opening preserves the relevant distinction: declared/inherited foundation values require foundation-format; established separate owners can be interpreted directly without a format/template read. It still starts from owners named by project instructions, and its multi-repository paragraph still requires declared shared owners and prohibits automatic local override.

Shared lookup and unavailable-authority obligations remain intact in the reachable references: foundation-format resolves bindings in the declaring owner's context, requires reading inherited sections, detects cycles, prohibits stale substitutions and defers only dependent decisions for missing bindings/unreadable owners. Multi-repository still preserves selected revision/snapshot authority and defers dependent work when authority is unavailable. Both keep missing-owner behavior locally readable in AGENTS, which matters if the shared installation itself is absent. Conditional format loading does not exempt a task that actually needs those declarations or inherited values.

No further source-level preservation finding in these final changes. `git diff --check` passed again. This disposition is a source review only: no consumer trial, copy/install test or runtime discovery test was run, and no repository file was edited.
