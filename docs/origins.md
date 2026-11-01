# Origins

Attribution for material that came from elsewhere, and the moves and
retirements a consumer upgrading from an older pin needs to know. Git history
holds the rest.

### Attribution

- **bash-patterns**, **test-audit**, **diagrams-and-tables** (then named
  `diagrams`) and the durable-check material in **source-of-truth** were
  imported on 29 September 2026 from the owner's Forge Agent Kit at
  `c98147a115a30f36b952df5faf1c869b54480c59`, from its `shell-patterns`,
  `test-audit`, `diagrams` and `selfcheck-guard` skills. Prose was revised,
  sibling-skill links became descriptions of the boundary, and citations of that
  kit's project policy were replaced with statements in place or deferred to the
  reading project's own policy.
- **python-patterns** and **python-design** drew their topic selection from
  Everything Claude Code's Python patterns at
  `c70874fae9eb0e5ad0365beb7e2955899fd1d30f` (MIT, copyright 2026 Affaan
  Mustafa) and the tooling boundary from Trail of Bits' modern-python plugin at
  `82fe8226252622fa807643bdca1710901198553a` (CC-BY-SA-4.0). No prose, examples,
  hooks or code were reused; neither upstream is tracked automatically.
- **bash-patterns** 0.2.0 assessed topics from wshobson/agents
  bash-defensive-patterns at `156b7a5e7a8b93642628a339ee4039c925b34c7f` (MIT,
  copyright 2024 Seth Hobson); its prose and examples are independently
  authored.
- **diagrams-and-tables** consulted Mermaid's official documentation, OWASP's
  system-modeling scope and OMG BPMN 2.0.2 for notation boundaries; its examples
  keep real shapes and counts from the owner's projects with synthetic names.
- **postgres-design**, **source-of-truth**, **node-patterns**,
  **verification-design**, **test-writing** and the
  Docker packages were written from reviews of the owner's own projects. The
  packages carry no project schema names, identifiers, paths or credentials.

- **typescript-patterns** 3.0.0 rebuilds the retired 2.0.3 language package
  from `605cded`, including its tuple-validation and total-registry lessons.
  Schema/handler correlation and readonly ownership cases draw on reviews of
  the owner's TypeScript applications. Primary TypeScript and Node documentation
  inform the language and toolchain guidance; references link to the relevant
  sections. Examples are synthetic. The former class-based design package is
  not restored.

### Moves and retirements

| Former package | Date | Where it is now |
| --- | --- | --- |
| runtime-operations 4.0.0 | 23 October 2026 | Retired by the Owner's decision: it described one framework's credential tiers and controller helpers. `f34f731` is the last commit that ships it; existing pins retain it. |
| project-design 0.2.0, project-contracts 0.2.0 | 22 October 2026 | repository-design owns repository boundaries, external discovery and handoff contracts; application-design owns internal operations. Broad conceptual-model and provider-selection tutorials are outside the replacement scope. Existing pins retain the former packages. |
| service-boundaries 0.5.0 | 22 October 2026 | service-design owns service interfaces, identity, storage custody and evidence matched to the task. Existing pins retain the former package. |
| project-planning 0.1.0, project-bootstrap 0.5.0, pattern-capture 0.3.1, project-policy 0.4.0 | 12 October 2026 | project-bootstrap, since retired; `183148d34dd1434df0402a0c6e69b195da84a525` is the last commit here that ships them |
| work-records 1.0.0 | 12 October 2026 | project-bootstrap; `e2e0ed4` is the last commit here that ships it |
| typescript-patterns 2.0.3, typescript-design 1.0.3 | 13 October 2026 | Retired by the Owner's decision; `605cded` is the last commit that ships both. Language guidance is rebuilt as typescript-patterns 3.0.0; review its changed defaults before replacing an older pin. typescript-design remains retired. |
| containerization 1.1.0 | 9 October 2026 | CLI usage split into docker-cli and docker-compose-cli; PostgreSQL and verification material to database-migrations and verification-design; convention-shaped outcomes, including one service image for API, migration and seed commands, to the consuming project |
| repository-services 0.3.1 | 9 October 2026 | Judgment kept as service-classes 0.1.0; the `services/` home, document shapes, reserved actions, dispatcher and validator to the consuming project |
| project-docs | 4 October 2026 | [project-foundation](https://github.com/jonasferagen/project-foundation) |
| change-workflow | 3 October 2026 | Retired; Git worktree operations, verification, document maintenance and reporting conventions belong to the consuming project |
| shared-code-design | 2 October 2026 | Retired; its distribution-boundary criteria are not carried by another package |
| jonas-email-style | 30 September 2026 | The owner's local `personal-skills` repository, installed for his user account |

Installed copies keep working at their pinned commits. A consumer upgrading from
containerization or repository-services adopts the successor packages and moves
the convention-shaped outcomes into the project itself.

### Current maintenance notes

- The Docker packages duplicate four shared rules under reciprocal copy records
  rather than linking, because each must work alone; the borrowed-definition
  rule is triggered in docker-compose-cli and fixed with a docker-cli bind.
