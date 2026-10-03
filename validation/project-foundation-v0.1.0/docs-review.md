# Release documentation review — 2026-10-03

## Scope and revision

Read-only independent review of the working-tree candidate at `/home/ladejarlen/Prosjekter/skills/agent-skills/.worktrees/modelling-conventions`, based on HEAD `ca00fc7`. The index was still unmerged during review. This is a review of the candidate file contents, not a claim that HEAD contains the merge resolution. Compared each changed assigned passage independently against both `ca00fc7` and `14086af` using working-tree diffs. No repository files edited. No live systems inspected.

Applied `validation/self-conformance.md`: clear-writing result comparison and instruction rules, source-of-truth ownership review, project-docs link/ownership/current-history checks, and semantic table/diagram review. Read the referenced owner checklists. The parent handles full release integration, routing acceptance and final committed-state checks.

## Full file coverage

All of the following files were read fully (paths relative to the worktree above):

- `AGENTS.md`
- `README.md`
- `docs/project-foundation-authoring.md`
- `collections/project-foundation/COLLECTION.md`
- `collections/project-foundation/templates/README.md`
- `collections/project-foundation/templates/project-docs/foundation.md`
- `collections/project-foundation/references/authoring.md`
- `collections/project-foundation/references/document-homes.md`
- `collections/project-foundation/references/friction.md`
- `collections/project-foundation/references/installation.md`
- `collections/project-foundation/skills/project-bootstrap/SKILL.md`
- `collections/project-foundation/skills/project-bootstrap/agents/openai.yaml`
- `collections/project-foundation/skills/project-docs/SKILL.md`
- `collections/project-foundation/skills/project-docs/agents/openai.yaml`
- `collections/project-foundation/skills/project-docs/references/diagrams.md`
- `collections/project-foundation/skills/project-docs/references/structure.md`
- `collections/project-foundation/skills/project-docs/references/worked-example.md`
- `collections/project-foundation/skills/clear-writing/SKILL.md`
- `collections/project-foundation/skills/clear-writing/agents/openai.yaml`
- `collections/project-foundation/skills/clear-writing/references/instructions.md`
- `collections/project-foundation/skills/clear-writing/references/short-text.md`

The four explicitly excluded shared references belong to the other reviewer.

## Findings and dispositions

No material prose, ownership, routing-link or semantic-table findings in the assigned files. No exception proposed.

The following release check issue was observed outside this review's file ownership and sent to the parent:

- **Open mechanical prerequisite:** `collections/project-foundation/skills/project-policy/references/phase-and-scope.md:21` has a new blank line at EOF in committed HEAD. `git diff --check <empty-tree> HEAD -- collections/project-foundation` exits 2. This must pass against the eventual release commit. Ordinary working-tree `git diff --check` passes, so that narrower command cannot establish the release prerequisite. The file is outside assigned content ownership; parent owns disposition.

## Comparison conclusions

- The collection entrypoint's installation material was moved to `references/installation.md`, preserving complete-directory installation, provenance, full source commit, draft identification, explicit project hooks and the absence of automatic nested-skill discovery. The source-maintenance boundary remains explicit.
- Retirement of `git-worktrees` remains explicit at `references/installation.md:30`. Adopted project working agreements survive retirement. No active assigned route still selects the retired skill. Removal of the old inventory wording avoids claiming that it remains installed.
- Canonical document homes remain authoritative in `references/document-homes.md`; bootstrap, templates and documentation structure agree on `project-docs/foundation.md`. Existing installations retain declared routes until deliberate migration. Technical documentation remains repository-owned. The table describes permitted types, not mandatory files; its headers and rows match that distinction.
- The authority-loading condition changed relative to ca00fc7 but is the deliberate task-routing behavior already present in 14086af. Known-term reading still requires relevant owners and evidence; changed meaning still selects the governing workflow. Unknowns, missing owners and proposals do not waive obligations.
- The new source-authoring convention preserves task scope, consequential-gap discovery, unaffected work, conditional capture, and independent comparison after moves. It does not require installed consumers to load authoring maintenance guidance.
- Foundation scaffold tables retain five sections, header-only declarations and explicit Unknown values. Added Phase and scope aligns the template with the merged policy model; template values do not claim verified implementation.
- Catalog tables, document-home tables, documentation ownership tables, short-text examples and synthetic glossary tables received semantic review. The two synthetic worked-example diagrams preserve conceptual scope and do not invent cardinalities or permissions. No conflicting table claim found.

## Release version and current claims

`README.md:220-223` defines annotated collection tags as `project-foundation/v<version>` and the collection version owner is `COLLECTION.md:3` (`0.1.0`). No existing project-foundation or project-bootstrap release tag was present in local Git. Collection and member versions correctly remain separate.

A potential concern was investigated: 14086af uses bootstrap 5.0.0 and the old default, while the candidate has 5.0.1 and canonical homes. The deployed ca00fc7 already has bootstrap 5.0.1 and the canonical default, and neither draft bootstrap version was published. The merged candidate preserves that deployed behavior; no additional version bump is required solely because the other branch carried an earlier draft. Project-docs is likewise a retained 4.0.1 here. This disposition follows the publication/deployment history confirmed by the parent, plus local tag inspection.

The catalog labels bootstrap, design, planning and contracts as draft (`README.md:21-24`). A 0.1.0 collection release can still contain intentionally draft workflows; the labels do not themselves falsely claim an unpublished collection once tagged. No correction is required unless the owner intends this release to declare those workflows non-draft. The release description should preserve their maturity limits.

## Checks and limits

Passed on reviewed candidate:

- `python3 scripts/validate-packages.py`: 25 entries, one collection.
- `python3 -m unittest discover -s collections/project-foundation/tests`: 14 tests.
- `git diff --check` on current working tree.
- Local Markdown link targets and heading-anchor checks across all 18 assigned Markdown files (additional targeted Python check): no missing targets or anchors.

Failed separately: committed whole-collection whitespace check above.

No rendered visual checks were performed. Diagram and table coverage is semantic/source review only, not a claim about clipping, themes or readability in a particular renderer. No new behavioral routing trial was performed by this reviewer; the parent must combine this review with routing evidence and the other reviewers. Final commit, complete mechanical checks and a dated release record remain integration responsibilities.
