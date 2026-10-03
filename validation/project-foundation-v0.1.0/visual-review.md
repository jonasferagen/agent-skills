# Release visual and source-of-truth review — 2026-10-03

**Current disposition:** all findings in this delegated scope are corrected. The final follow-up below supersedes earlier open dispositions and table-rendering limits. No exception is required by this reviewer. Target-specific GitHub/editor/publishing rendering remains unverified.

## Scope and evidence

Fresh delegated review of all 28 files under `collections/project-foundation/skills/diagrams-and-tables` and `skills/source-of-truth` in `/home/ladejarlen/Prosjekter/skills/agent-skills/.worktrees/modelling-conventions`. Initial HEAD: `ca00fc77b9928af4856c57ff46caa79d608282ce`. Repository read-only for this reviewer; temporary artifacts only. Parent edits occurred during review. The correction diff against `fdbbb43` was independently read after the initial review.

Applied self-conformance.md, Clear Writing and instruction guidance, status/evidence, Project Docs verification, the semantic/visual/table rules, and Source of Truth review steps. Every assigned file was read in full (boundaries.md was reread after an initially truncated combined output). No live project systems or publishing were used.

## Actual checks

- `python3 scripts/validate-packages.py`: passed; 25 entries, one collection.
- `python3 -m unittest discover -s collections/project-foundation/tests`: passed; 14 tests.
- Whole committed collection whitespace check: failed at initial HEAD, `skills/project-policy/references/phase-and-scope.md:21`, extra EOF blank. Parent reports correction; final committed check belongs to parent.
- `git diff --check`: passed after parent prose corrections.
- Repository README/scripts search found no documented renderer command or package renderer configuration. Found cached local CLI at `/home/ladejarlen/.npm/_npx/d62b6517736c1e35/node_modules/@mermaid-js/mermaid-cli/src/cli.js`, version 11.17.0, using Mermaid 11.16.1 and `/usr/bin/google-chrome`.
- Sandbox browser launch failed on `setsockopt: Operation not permitted`; approved escalation succeeded. No dependency installed.
- All 26 Mermaid blocks rendered successfully to PNG in default/light theme with page width 830, scale 1. Visually inspected all at that reading width using temporary contact sheets and original images. This establishes only that local renderer/theme, not GitHub or an unspecified publishing preview.
- The first dark-theme batch stalled without producing images and was interrupted. A second attempt was bounded to 45 seconds. See final limit note below.
- All 15 Markdown tables reviewed in source for axes, populated cells, meaning, duplication and unsupported claims. No dedicated Markdown/publishing renderer was documented; table layout/contrast was not visually verified.

Render source manifest: `/tmp/release-visual-render/manifest.json`; extracted `.mmd` files and light-1.png through light-26.png are in that directory. `all.md` contains exact initial diagram source. Light contact sheets cover 1–4, 5–8, 9–12, 13–16, 17–20, 21–24, 25–26. Rendering and parsing are separate from semantic accuracy.

## Findings and disposition

1. **Material, layout guarantee — corrected prose independently checked.** `composition.md` and `mermaid.md` previously guaranteed vertical inner placement even with external edges; worked examples repeated that guarantee. Official Mermaid documentation states internal-to-external edges cause inheritance of parent direction: https://mermaid.js.org/syntax/flowchart.html#direction-in-subgraphs . Local examples 13 and 26 confirm horizontal nodes inside the groups. Parent correction removes the guarantee and directs rendered verification; this preserves the vertical default and changes only the unsupported certainty. Renderer version remains important.
2. **Material, unreadable recommended layered example — unresolved at review snapshot.** `worked-examples.md` block 12 (`light-26.png`) becomes an approximately 830×70 strip with tiny text. The corrected prose is accurate but the recommended visual still fails its own reading-width rule. Minimal correction: remove the duplicate LR block and describe this as an unsuccessful layout at narrow width, or replace with a group-only overview and appropriate separate details. Its TB predecessor (block 11, light-25.png) is readable but cross-group edges are tightly bundled. `mermaid.md` block 3 (light-13.png) is also horizontal but the smaller example remains readable.
3. **Material, ER overview label size — unresolved.** `er/examples.md` block 3 (`light-5.png`) puts four independent clusters side by side; long identifiers shrink to roughly 9px at 830px width. Use short display labels with an explicit mapping, or a layout that preserves readable text. Creature detail block 5 (`light-7.png`) is borderline (~11px) with an edge crossing near attack assignment; lower severity, but worth improving alongside the overview. Character detail block 4 is readable.
4. **Material, unsupported migration claim — corrected and independently checked.** `er/examples.md` said float to numeric(9,3) loses no data. Parent correction requires range/rounding validation, acknowledges precision loss and states that a proposed check is not evidence of passed data. This corrects certainty without silently changing any adopted real migration (the example is proposed/generalized).
5. **Navigation drift — corrected and independently checked.** References to SKILL.md as the location of form selection or composition thresholds now route directly to select.md/composition.md.
6. **Minor self-conformance, ER label quoting.** `er/design.md` requires quoted relationship labels; the positive ER examples use unquoted labels (`contains`, `uses`, etc.). All parse, so this is inconsistent instruction/example practice rather than a syntax failure. Quote the labels or narrow the requirement to problematic labels. Negative excerpts need not be corrected because their defects are deliberate and clearly introduced.
7. **Instruction/example boundary to resolve.** `verification.md` says to label each edge with meaning, while positive flow examples use unlabeled arrows with their meaning supplied by a caption. Source review supports a shared legend/caption as sufficient for repeated next-step semantics (as family reading notes already say); explicitly qualify the blanket requirement to avoid two competing rules. Do not add redundant edge text merely to satisfy the literal wording.
8. **Minor example seam/grounding gaps.** Data-flow detail heading does not repeat exact black-box label `Submission archive`, despite composition's exact-label rule. Worked examples claim artifact registry links to canonical storage detail, but there is no actual link or explicitly fictional placeholder; synthetic status for those examples is less explicit than in the new flowchart/DFD examples. Lifecycle inventory says precedence matters, but input fan-in detail does not state precedence. Clarify illustrative assumptions/omissions instead of implying verified behavior or an available owner.

No accepted exception was supplied to this reviewer. Material unresolved findings require correction or an explicitly owner-accepted exception before release.

## Semantic results

- Flowchart review loop: accepted, revision and pause paths consistent with caption; retry requires a changed draft. No execution/publication authorization inferred.
- Both data-flow examples: boundary payloads balance; processes perform selection/delivery, stores retain content; byte/reference distinction is preserved. Normal-path omission is explicit.
- ER: endpoint meanings and cardinality reference table agree. Counts in family map are consistent: 11 nodes, 12 solid plus 7 dotted edges; solid counts total 33; fan-in tables account for 15 blob references (13 external) and 15 game-core references. Therefore 33 + 13 = 46 cross-family references, with 28 attributed to the named hubs. The two enormous unreadable ER excerpts are explicitly bad/replaced examples; no readability finding is raised merely for their intentionally illustrated failure.
- Source-of-truth: six derivation/check rungs, boundary examples, check-design requirements and durability references remain aligned. Package-boundary copy comments identify consumers; no unacknowledged conflicting copied value found in assigned files. Cross-package parity is covered structurally by package validation, not proven semantically outside this assignment. The promise that derivation makes disagreement impossible is an idealized design claim; consumers still need correct generation/runtime implementation, as the surrounding verification rules imply.
- Tables: axes and explicit none/unknown values are generally clear. The migration cell was the concrete unsupported guarantee. Longer schema cells remain a rendering limit, not a claimed visual pass.

## Complete file coverage

All paths below are relative to `collections/project-foundation/skills/`. Each received prose, meaning, routing/ownership and duplication review; D/T show Mermaid-block/Markdown-table counts. D>0 additionally received full light rendering and visual inspection.

- `diagrams-and-tables/SKILL.md` — read; D=0, T=1.
- `diagrams-and-tables/agents/openai.yaml` — read; D=0, T=0.
- `diagrams-and-tables/references/composition.md` — read; D=0, T=1.
- `diagrams-and-tables/references/data-flow/design.md` — read; D=0, T=0.
- `diagrams-and-tables/references/data-flow/examples.md` — read; D=2, T=0.
- `diagrams-and-tables/references/data-flow/guide.md` — read; D=0, T=0.
- `diagrams-and-tables/references/data-flow/read.md` — read; D=0, T=0.
- `diagrams-and-tables/references/er/design.md` — read; D=0, T=0.
- `diagrams-and-tables/references/er/examples.md` — read; D=7, T=5.
- `diagrams-and-tables/references/er/guide.md` — read; D=0, T=0.
- `diagrams-and-tables/references/er/large-models.md` — read; D=0, T=0.
- `diagrams-and-tables/references/er/read.md` — read; D=0, T=1.
- `diagrams-and-tables/references/flowchart/design.md` — read; D=0, T=0.
- `diagrams-and-tables/references/flowchart/examples.md` — read; D=1, T=0.
- `diagrams-and-tables/references/flowchart/guide.md` — read; D=0, T=0.
- `diagrams-and-tables/references/flowchart/read.md` — read; D=0, T=0.
- `diagrams-and-tables/references/mermaid.md` — read; D=4, T=0.
- `diagrams-and-tables/references/review.md` — read; D=0, T=0.
- `diagrams-and-tables/references/select.md` — read; D=0, T=1.
- `diagrams-and-tables/references/tables.md` — read; D=0, T=1.
- `diagrams-and-tables/references/verification.md` — read; D=0, T=0.
- `diagrams-and-tables/references/worked-examples.md` — read; D=12, T=4.
- `source-of-truth/SKILL.md` — read; D=0, T=0.
- `source-of-truth/agents/openai.yaml` — read; D=0, T=0.
- `source-of-truth/references/boundaries.md` — read; D=0, T=0.
- `source-of-truth/references/check-design.md` — read; D=0, T=1.
- `source-of-truth/references/definitions.md` — read; D=0, T=0.
- `source-of-truth/references/durable-checks.md` — read; D=0, T=0.

## Follow-up evidence and current dispositions

Parent requested additional coverage of `project-docs/references/worked-example.md`: read its full prose, one vocabulary table and both Mermaid blocks. Synthetic status, conceptual relationship labels, withheld cardinalities and permission distinctions are consistent. Both diagrams rendered and inspected successfully in light and dark at width 830 (`final/light-6.png`, `final/light-7.png`, corresponding dark files). No finding.

The second eight-job dark attempt timed out after 45 seconds (exit 124). Retrying with `-j 1` succeeded for all 26 original diagrams; all 26 dark PNGs were visually inspected. Contrast remains readable; existing width findings are unchanged. Thus dark coverage is completed, not an outstanding tooling gap. Output: `/tmp/release-visual-render/dark-1.png` through `dark-26.png` and dark contact sheets.

Independently compared parent changes against `fdbbb43`:

- ER aliases preserve entity IDs, endpoints, optionality and labels. Companion tables use the same aliases. Changed overview, character and creature details were rerendered in both themes (`final/light-1.png` through `light-3.png`, corresponding dark files). Overview is now readable. Creature detail is compact but traceable; crossing is minor, with no collision or clipped labels. Finding 3 is corrected.
- The layered group-only overview preserves the two group-level dependency relations and now states existential rather than all-to-all meaning. It is readable in both themes (`final/light-4.png`, `final/dark-4.png`). Original fine-grained nine-edge source is retained in a TB detail. However, the local renderer attaches those edges to group borders rather than individual boxes (`final/light-5.png`, `final/dark-5.png`), so the particular dependencies cannot be traced. Finding 2 remains open pending removal of detail subgraph wrappers or equivalent representation preserving endpoints. The parent has been informed.
- All seven changed/new diagrams parsed/rendered in both themes with CLI `-j 1`; manifest `/tmp/release-visual-render/final/manifest.json` captures their actual source and block mapping.

No claim is made about a project publishing preview or another Mermaid version. Tables received source semantic review only, not browser layout verification. Full final release mechanical checks and findings acceptance remain with the coordinating reviewer.


## Final correction review — current disposition

Independently read the final changes against `fdbbb43` and the preceding review snapshot.

- **Finding 2 corrected:** removing the three subgraph wrappers preserves all eight nodes and all nine dependency edges. The caption retains membership in the three named groups. Final diagram rendered and visually inspected at 830px in both themes; each specific endpoint is now visible and the limited crossings are traceable. Evidence: `/tmp/release-visual-render/last/light.png`, `dark.png`, and exact `layer.mmd`.
- **Finding 6 corrected:** quoting is now conditional on spaces/reserved words. This is an explicit rule correction, not an assertion that every previous label had been quoted; meaning labels remain required. Existing positive examples satisfy the corrected requirement and parse.
- **Finding 7 corrected:** shared captions/legends can carry repeated arrow semantics. Every edge must still have explicit meaning, and role distinctions are retained.
- **Finding 8 corrected:** DFD heading repeats `Submission archive`; fictional storage/delivery owners are explicitly identified as illustrative, with actual links required in a real project. Candidate-input precedence is newly stipulated for the synthetic example: authored values override imported values on conflicting fields and other imported fields remain. This is a deliberate new illustrative assumption, not a recovered fact or an adopted consumer-project rule. It resolves the previously unexplained precedence without changing the fan-in topology.
- Earlier corrections 1, 3, 4 and 5 remain satisfactory. No material or minor finding from this review remains unresolved after these changes.

### Completed table rendering

An installed Python `markdown_it` renderer was available. Rendered all 15 assigned Markdown tables plus the project-docs vocabulary table to a temporary HTML harness with ordinary 16px Arial text, 13px monospace code, collapsed borders and normal wrapping. Width was 830px. Existing local Puppeteer/Chrome produced 16 light and 16 dark screenshots; all were visually inspected. Column headers, cardinality symbols, explicit none/unknown values and schema fields remain readable, with no clipped text or horizontal overflow observed.

The first temporary harness had incorrect dark text inheritance; that harness-only CSS error was corrected and all screenshots regenerated before final inspection. No repository file was changed by this reviewer. These are generic local Markdown/browser checks, not a claim of matching GitHub/editor/publishing CSS. Those target-specific renderers remain untested because none was documented/configured in the project.

Artifacts: `/tmp/release-visual-render/last/tables.html`, `tables.json` (source/file inventory), `table-light-1.png` through `table-light-16.png`, corresponding `table-dark-*`, and eight light/dark contact sheets. Local rendering required no dependency installation. The final full-collection mechanical gate and release record remain the coordinating reviewer's responsibility.

Markdown renderer version: markdown-it-py 3.0.0.
