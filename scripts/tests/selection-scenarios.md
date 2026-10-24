# Selection scenarios

Cross-skill cases: a request, the package that should be selected first, and the
neighbour that should not. They test the catalog's descriptions and the packages'
scope statements together, which no single package can own. Run them as routing
trials by the method in [routing quality](../../docs/verification.md#routing-quality): a fresh agent, the
installed packages' metadata, no expected route. No test checks this table.

| Request | Should select | Should not select |
| --- | --- | --- |
| Which suites must this change run before merging? | verification-design | test-writing, test-audit |
| Do the existing tests protect this behavior? | test-audit | test-writing, verification-design |
| Add a regression test for this parser fix | test-writing | test-audit, verification-design |
| Build sample records for the importer tests | test-writing | single-source-of-truth |
| This vocabulary is defined in the schema and again in the reader | single-source-of-truth | postgres-design, python-design |
| Give these operations and values clear owners in a Python module | python-design | python-patterns |
| Review cancellation and cleanup in this async worker | python-patterns | python-design |
| Check that this harness reports why docker failed | node-patterns | bash-patterns, docker-cli |
| Can this backup script's checks pass when they should fail? | bash-patterns | node-patterns |
| Which agreements involve a given organisation? Model the entities | relational-modeling | postgres-design, diagrams-and-tables |
| Design the tables and keys for an adopted model | postgres-design | relational-modeling |
| Review this migration runner's ledger and locking | database-migrations | postgres-design, docker-compose-cli |
| Assemble a `docker run` for a one-off task with a published port | docker-cli | docker-compose-cli, docker-cleanup |
| This compose command ran against the wrong project | docker-compose-cli | docker-cli |
| A build failed with no space left on device | docker-cleanup | docker-cli, docker-compose-cli |
| Should this nightly export job become a service, and what must its status report? | service-classes | service-design |
| Add MCP access to an operation already exposed over HTTP | service-design | service-classes |
| Define the handoff between design and implementation | repository-design | application-design |
| Shape ownership, publication and dependency boundaries of a new repository | repository-design | application-design, service-design |
| Consolidate a repository's public commands and find every affected caller | repository-design | repository-maintenance, service-design |
| Correct a typo in a CLI help description without changing its interface | none | repository-design, repository-maintenance |
| Design one external generation operation inside an application | application-design | repository-design, service-design |
| Decide whether this section wants a diagram or a table | diagrams-and-tables | clear-writing |
| Tighten this guide without changing what it requires | clear-writing | diagrams-and-tables |
| The feature shipped; bring its guide up to date and deal with the implementation notes appended to it | documentation-records | clear-writing |
| This README's Maintenance section tells the project's history and planned work | documentation-records | clear-writing, repository-maintenance |
| Shorten this paragraph of a current guide without changing what it says | clear-writing | documentation-records |
| Explain the cardinality at one end of an existing ER view | diagrams-and-tables | relational-modeling |
| A headless Godot probe logs a failure and exits zero | godot-gdscript | bash-patterns |
| Correct a spelling error in an operating guide | none | service-classes |
| Rename a screenshot file | none | godot-gdscript |
| Replace a literal spelling in a README | none | clear-writing, relational-modeling |
| Review this repository for structural and semantic drift | repository-maintenance | repository-design, test-audit |
| Correct a spelling error in a maintenance guide | none | repository-maintenance |

| Request | Should select | Should not select |
| --- | --- | --- |
| Our tests need sibling checkouts despite temporary local inputs | repository-design | service-design |
| Introduce aliases for current external references without duplicating package locks | repository-design | application-design |
| A pinned schema differs from its publisher's latest source: is that drift? | single-source-of-truth | service-design |
| Review a saved record whose meaning changes when its dependency updates | application-design or repository-design, according to the affected boundary | service-classes |
