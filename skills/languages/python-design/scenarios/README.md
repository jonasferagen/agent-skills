# Python design scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A public pure domain operation has no state | Keep a module function when its inputs and responsibility are clear; do not require a wrapper class. |
| A service owns a client or state across calls | Use an instance with explicit dependencies and lifetime. |
| A method needs the receiving subclass | Use classmethod; staticmethod receives neither self nor cls. |
| A fixture, decorator, contextmanager factory or framework entrypoint needs a function | Preserve the natural integration point without treating functions as exceptions. |
| A one-shot builder has substantial coordinated working state | A class can own that state; expose a completed result rather than requiring callers to manipulate its internals. |
| A project deliberately exposes a class-based public API | Preserve the contract; do not remove static wrappers solely for style. |
| A private helper or small value parser is clearer as a function | Keep the function; consider an existing value owner when it clarifies the contract. |
| Optional positional arguments are ambiguous | Start with keyword-only arguments; do not automatically add an input class. |
| Several callers pass a meaningful group of fields | Consider a shared input record when the fields travel together. |
| A value has ordering invariants | Enforce ordinary construction, not just a bypassable factory. |
| A value needs tuple behavior: unpacking, ordering, set membership | A NamedTuple is named as the alternative; the values reference must not steer toward a frozen dataclass by default. |
| A wire DTO (a record mirroring an external payload) only describes that payload | Keep it passive; runtime parsing remains a separate boundary concern. |
| A property would perform network I/O | Use an explicit operation rather than hiding costly work behind attribute access. |
| A test patches a module-level margin to exercise a failure | Give the margin to its owning operation as a keyword-only or constructor parameter; the default may live with the module or class, and tests pass the value. |
| A consumer calls one method but forwards the client elsewhere | Trace downstream and lifecycle needs before narrowing to a protocol. |
| Two clients have matching methods but different session ownership | Preserve semantic and lifetime requirements; structural matching is insufficient. |
| An injected client is borrowed | Do not close it as though the consumer acquired it. |
| A small module holds a class and related records | Keep it cohesive; do not copy a one-class-per-file rule. |
| Several modules call an underscored query helper and interpret its prose messages | Identify the shared capability and define an internal result/failure contract; do not merely rename it or make it an external API. |
| Parsing establishes a validated object that is discarded and rebuilt downstream | Carry the validated result forward unless a new trust boundary or invalidating mutation justifies revalidation. |
| Stages communicate by filling unrelated optional fields on one object | Make each handoff's invariants and mutation ownership explicit; use distinct records or variants where guarantees differ, without requiring an immutable object for every pass. |
| Two input versions have similarly shaped records with different meanings | Keep version selection visible and share only semantically compatible downstream representations. |
| A replacement plan is requested | Plan around public compatibility, success and refusal cases, known defects, a useful first path, switching criteria and retirement; do not implement the plan without authorization. |
| A long but coherent module is flagged solely for its length | Trace responsibility, dependencies and callers before proposing a split; a line count is not an architectural boundary. |
| An import cycle is hidden with TYPE_CHECKING | Confirm runtime annotation consumers and inspect ownership before hiding the import. |
| A small correction is requested | Keep the edit scoped; no general class, phase or module migration. |
| A numeric key collision or tolerance bug needs a local correction | Treated as a language-level correctness fix outside this skill's scope; no program-wide redesign is inferred from the defect. |
| The project's instructions prescribe a different architecture | The conflict is reported to the user with both passages and the user's decision followed; a preference is distinguished from a correctness issue. |
| Asked to select a formatter or packaging layout | Deferred to the project's conventions or the user; this skill covers no toolchain. |

## Limits

- These scenarios exercise design decisions, not the correctness of a particular
  application. Domain semantics, performance requirements and migration risks
  still need project-specific evidence.
- The cases cannot establish that the skill consistently selects the right
  boundaries across all Python architectures.
