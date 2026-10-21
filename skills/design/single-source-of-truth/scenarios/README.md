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
| A plugin namespace appears in docs, a generated manifest and UI prompts | One project-owned lookup value decides the namespace; docs use its key, generated files derive the literal, and historical pins retain their original names. |
| A manifest needs a literal namespace but its loader does not expand variables | A placeholder is rejected; generate the literal or compare it with the owner in a required check. |
| Behavior tests parse a Markdown table that states a contract | The structured input belongs to domain code and tests; the document is generated or extracted from it with a check at that boundary. A consistency check may live in a required suite that the affected inputs select. |
| A document cites a shared file through a hosted link to a moving branch | Treated as neither a current nor a historical reference; the citation resolves through the project's declared binding or pins a revision. |

## Maintained prose and records

| Request and context | Expected behavior |
| --- | --- |
| A document and a constraint both list a vocabulary and the document is stale | Remove an unnecessary prose copy or reconcile the needed explanation with the constraint and name its home. |
| Several overviews repeat "no release exists" without a reader needing that status | Remove the snapshots; do not create a release inventory merely to relocate them. |
| Release availability affects a reader's next action and an authoritative release listing exists | Link that listing directly with enough context; do not copy it through intermediate repository summaries. |
| A keeper maintains changing prose by hand | Name a bounded maintained set and update triggers; supporting documents point to its homes rather than independently tracking status. |
| Policy requires hash verification but the current loader does not perform it | Preserve the requirement and the observed limitation with their respective owners; omission does not hide the gap. |
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
| Mechanical enforcement is proposed as a scanner over a fixed set of directories | Rejected as the anti-pattern enforcing itself; enforcement is scoped to the tree it checks and derives its file set from version control. |
| Whether a given check earns its recurring cost | Deferred to the reading project's own policy; the durability bar applies to a check already being kept. |

## Adoption and authority

| Request and context | Expected behavior |
| --- | --- |
| Adopting the skill into an existing project | No renaming, code movement or schema change is implied; existing project conventions take precedence. |
| A changed policy raises the consequence of inconsistent copies | Revisit affected copies and checks, link unmet requirements to active work, and keep desired requirements distinct from observed behavior. |
| A project states no consequence for inconsistent copies | Use available project decisions and expose consequential unknowns; do not require installing another skill. |

## Candidate, not adopted: record meaning versus storage origin

When code decides what a record means from where it came from — its table, file
or assertion kind — moving that kind of record to another home changes behavior
without an error, and a catch-all branch makes the fallback silent. Giving each
fact one home is exactly such a move, so consumers should be checked for branches
on provenance before it. Provenance can itself be the meaning: a review status
or trust level that decides what a value may do is a correct branch and stays.
The simplest rule would be to store the kind of record as data and branch on
that, keeping provenance for reporting and trust decisions.

One reproduced case supports this; before adoption it needs a second, unrelated
reproduction (such as configuration behaving differently by whether a value came
from a file or the environment), a case outside the rule confirming the guidance
does not discourage branching on review status, and a decision between a short
addition to the definitions reference beside the silent-fallback passage and one
line in the review list.

## Limits

- The rung ladder has not been exercised on a build-time generation case
  (rung 2), and the language-boundary guidance rests on one observed instance.
- No check has been observed failing on environment shape and then surviving the
  same move after the durability bar was applied; that claim rests on experience
  outside this repository.
- The rule that a verdict names the root and set it measured has not been tested
  against a case where the inventory basis was actually wrong.
- Document-authoritative extraction into a build artifact is an informed design
  option, not a demonstrated implementation.
