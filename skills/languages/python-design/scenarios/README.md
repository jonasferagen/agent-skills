# Python design scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A public pure domain operation has no state | Use a static method on its operation class; purity does not exempt it. |
| A service owns a client or state across calls | Use an instance with explicit dependencies and lifetime. |
| A method needs the receiving subclass | Use classmethod; staticmethod receives neither self nor cls. |
| A fixture, decorator, contextmanager factory or framework entrypoint needs a function | Preserve the natural integration point under the documented exception. |
| A private helper or small value parser is clearer as a function | Allow the narrow exception; prefer an existing value owner when it fits. |
| Optional positional arguments are ambiguous | Start with keyword-only arguments; do not automatically add an input class. |
| Several callers pass a meaningful group of fields | Consider a shared input record when the fields travel together. |
| A value has ordering invariants | Enforce ordinary construction, not just a bypassable factory. |
| A value needs tuple behavior: unpacking, ordering, set membership | Name the NamedTuple alternative and hand the choice to python-patterns; the values reference alone must not steer toward a frozen dataclass. |
| A wire DTO only describes an external payload | Keep it passive; runtime parsing remains a separate boundary concern. |
| A property would perform network I/O | Use an explicit operation rather than hiding costly work behind attribute access. |
| A test patches a module-level margin to exercise a failure | Give the margin to its owning operation as a keyword-only or constructor parameter whose default is the policy, with a class attribute as the smaller step; the test passes the value. |
| A consumer calls one method but forwards the client elsewhere | Trace downstream and lifecycle needs before narrowing to a protocol. |
| Two clients have matching methods but different session ownership | Preserve semantic and lifetime requirements; structural matching is insufficient. |
| An injected client is borrowed | Do not close it as though the consumer acquired it. |
| A small module holds a class and related records | Keep it cohesive; do not copy a one-class-per-file rule. |
| An import cycle is hidden with TYPE_CHECKING | Confirm runtime annotation consumers and inspect ownership before hiding the import. |
| A small correction is requested | Keep the edit scoped; no general class or module migration. |
| Local instructions conflict with the house style | Report the conflict and follow the user's explicit decision. |
| Asked to select a formatter or packaging layout | Defer to project policy; this skill owns no toolchain. |

## Limits

- The design examples passed a strict type check and runtime probes on CPython
  3.11 through 3.14; they demonstrate selected rules, not that every choice suits
  a real application.
- One supplied-metadata routing trial reached the policy-value section from a
  patched-margin task; the nearby-scope case was not exercised.
