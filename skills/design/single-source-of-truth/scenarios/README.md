# Single source of truth scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Finding the home and deriving copies

| Request and context | Expected behavior |
| --- | --- |
| A vocabulary is enforced by a database constraint and restated in application code | The constraint is authoritative; the application derives the vocabulary or a gate check compares the two. |
| A list in code holds every value the constraint admits | Treated as a copy that will fall behind, not as a policy. |
| A list in code holds some of the values the constraint admits | Treated as a policy over the vocabulary; left in place with its reason stated. |
| An input boundary validates more strictly than the column that stores the value | The stricter check is identified as able only to reject stored values; narrowing needs its own stated reason. |
| A lookup returns a default for an unknown code | Named as the mechanism that makes drift silent; exhaustiveness or explicit failure proposed where the concept must be complete. |
| A consumer states a fixed label and ignores the stored value | Treated as worse than a missing label, because the stated fact becomes false; a derived vague answer preferred. |
| The same rule exists in two languages with different spellings | Copying rejected; the spelling difference is attributed to each language's parsing, and a normalising home-to-home check is proposed. |
| A proposed fix would import a server module into a client bundle | Unification refused; request-time delivery or a dependency-free shared module proposed instead. |
| Only a type is shared across a bundle boundary | Type-only declarations are erased, so the boundary does not block it. |
| Paired processes each hardcode the other's address | The hardcoded value is removed from shared code and supplied at the edge by whichever process owns it. |
| Neither paired process can know the other's value, and a shared settings source is out of scope | Where both settings are in the repository, a check reads both and fails when they disagree (rung 5); otherwise the pair is recorded at rung 6. |
| A vocabulary would need to become rows a check constraint reads | Identified as impossible for a check constraint and as a schema decision; the project's migration rules govern. |
| Two similar lists answer different questions | Not a second home; the questions are compared rather than the contents. |
| One constant is used several times inside one module | Not a duplication. |
| Ranking a stable constant copied many times against one growing cross-medium vocabulary | The growing cross-medium concept ranks higher; copy count alone does not decide. |
| A duplication can be neither derived nor checked | Recorded where the concept lives, naming what must change together and what goes wrong when one is missed. |
| A package name appears in docs, a generated config file and UI prompts | One declaration decides the name; docs reference it, generated files derive the literal, and historical records retain the name they actually used. |
| A config file needs a literal value but its loader does not expand placeholders | A placeholder is rejected; generate the literal or compare it with the declaration in a gate check. |
| Behavior tests parse a Markdown table that states a contract | The structured input belongs to domain code and tests; the document is generated or extracted from it with a check at that boundary. |
| A document cites a shared file through a hosted link to a moving branch | Treated as neither a current nor a historical reference; the citation resolves through the declaration or pins a revision. |

## Maintained prose and records

| Request and context | Expected behavior |
| --- | --- |
| A document and a constraint both list a vocabulary and the document is stale | Remove an unnecessary prose copy or reconcile the needed explanation with the constraint and name its home. |
| Several overviews repeat "no release exists" without a reader needing that status | Remove the snapshots; do not create a release inventory merely to relocate them. |
| Release availability affects a reader's next action and an authoritative release listing exists | Link that listing directly with enough context; do not copy it through intermediate repository summaries. |
| Someone maintains changing prose by hand | Name a bounded maintained set and what changes call for an update; supporting documents point to that home rather than independently tracking status. |
| A requirements document demands input validation that the current loader does not perform | Keep the stated requirement and the observed limitation as separate facts; omission does not hide the gap. |
| An old acceptance report records a passing revision | Retain the assessed revision and conditions as historical evidence, rather than rewriting the report to describe current support. |

## Checks that stay durable

| Request and context | Expected behavior |
| --- | --- |
| A test restates the expected values as the check | Rejected as a third home; the check must compare one home to the other. |
| A unit test states the value an operation should produce | Not a golden; a literal expectation about behaviour is the test doing its job. |
| A relevant test exists but runs only behind an environment variable | Reported as unprotected in the gate rather than as covered. |
| A proposed check has never been observed to fail | Disagreement is introduced deliberately to confirm the check fails, then reverted. |
| A gate check compares a freshly scanned count against a committed expected one | Named as a golden that has to be re-approved on every legitimate change; the check computes its answer live instead. |
| A home cannot be read when the check runs | No committed copy of its answer is added; the dependency is reported as absent, or the duplication is recorded at rung 6. |
| An exemption ledger lists files grandfathered out of a settled convention | Accepted as a bounded exception where it gates hard, may only shrink, and belongs to the tree whose files it lists. |
| A check derives its file inventory with `git ls-files` from the caller's working directory | Flagged; the repository root is resolved first and the verdict names the root and set it measured. |
| A check reports a pass without stating what it measured | Treated as a partial denominator that can read as a whole-tree result; the verdict names its basis. |
| A check's own test builds fixtures at a hard-coded path outside its tree | Rejected; it anchors to its own location and fabricates its world in a temporary directory. |
| A check copies a directory list the build configuration already declares | Rung 1 applied to the check: it reads the declaration rather than restating it. |
| A check's test requires a neighbouring checkout or a running service | Rejected as a dependency on environment shape; external commands are stubbed and the tree fabricated. |
| A check throws, or asserts against empty output, when a required tool is absent | The failure moves to the boundary that owes the tool, naming what is missing. |
| A dependency nobody opted into is unavailable | The check exits successfully with a loud notice; a silent skip is rejected because it reads as a pass. |
| A check is report-only, with nothing consuming its output | Named as cost without teeth; it gains a live invariant and a real gate, or it goes. |
| A check can fire for changes that cannot affect the consequence it protects | The trigger is narrowed, or the proxy's cost is stated against the cost of a missed defect. |
| Mechanical enforcement is proposed as a scanner over a fixed set of directories | Rejected as the anti-pattern enforcing itself; the check lives in the repository it examines and derives its file set from version control. |
| Whether a given check earns its recurring cost | Left to the project's judgment; the durability bar applies to a check already being kept. |

## Project conventions

| Request and context | Expected behavior |
| --- | --- |
| Applying the skill in an existing project | No renaming, code movement or schema change is implied; existing project conventions take precedence. |
| A requirement change raises the consequence of inconsistent copies | Revisit affected copies and checks, record unmet requirements in the issue tracker, and keep stated requirements distinct from observed behavior. |
| The project states no consequence for inconsistent copies | The consequence is assessed from how disagreement would appear, the assumption is stated, and the user is asked when the cost is unclear. |

## Limits

- Document-authoritative extraction into a build artifact is a design option the
  skill describes, not a worked example it provides.
