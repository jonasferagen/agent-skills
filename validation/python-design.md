# Validation scenarios — Python design

Version 0.1.0 mirrors the structure and class-based preference of the local
TypeScript design package, while adapting its choices to Python.

| Request and context | Expected outcome |
| --- | --- |
| A public pure domain operation has no state | Use a static method on its operation class; purity does not exempt it. |
| A service owns a client or state across calls | Use an instance with explicit dependencies and lifetime. |
| A method needs the receiving subclass | Use classmethod; staticmethod receives neither self nor cls. |
| A fixture, decorator, contextmanager factory or framework entrypoint needs a function | Preserve the natural integration point under the documented exception. |
| A private helper or small value parser is clearer as a function | Allow the narrow exception; prefer an existing value owner when it fits. |
| Optional positional arguments are ambiguous | Start with keyword-only arguments; do not automatically add an input class. |
| Several callers pass a meaningful group of fields | Consider a shared input record when the fields travel together. |
| A value has ordering invariants | Enforce ordinary construction, not just a bypassable factory. |
| A wire DTO only describes an external payload | Keep it passive; runtime parsing remains a separate boundary concern. |
| A property would perform network I/O | Use an explicit operation rather than hiding costly work behind attribute access. |
| A test patches a module-level margin to exercise a failure | Give the margin to its owning operation as a keyword or constructor parameter; the test passes the value. |
| A consumer calls one method but forwards the client elsewhere | Trace downstream and lifecycle needs before narrowing to a protocol. |
| Two clients have matching methods but different session ownership | Preserve semantic and lifetime requirements; structural matching is insufficient. |
| An injected client is borrowed | Do not close it as though the consumer acquired it. |
| A small module holds a class and related records | Keep it cohesive; do not copy a one-class-per-file rule. |
| An import cycle is hidden with TYPE_CHECKING | Confirm runtime annotation consumers and inspect ownership before hiding the import. |
| A small correction is requested | Keep the edit scoped; no general class or module migration. |
| Local instructions conflict with the house style | Report the conflict and follow the user's explicit decision. |
| Asked to select a formatter or packaging layout | Defer to project policy; this skill owns no toolchain. |

## Sources and adaptations — 2026-09-30

The local TypeScript split at
`7edfed2603406269b78be95a2dcf6a6d8a628219` supplies the entrypoint structure,
class-based preference and separation of language correctness from design.
Python naming, keyword-only calls, dataclasses and protocols replace mechanical
translations of TypeScript syntax. Cohesive modules may hold related classes and
records. Python has no private constructor equivalent; ordinary construction
must enforce value invariants.

The [language validation](python-patterns.md#sources-and-adoption--2026-09-30)
records the pinned third-party skills inspected for this pair. No upstream
files, prose, examples, hooks or executable helpers were imported. Official
Python and typing documentation is linked within each installable reference.
This package is independently usable and does not require its TypeScript or
Python sibling to be installed.

## Verification — 2026-09-30

The author reviewed every scenario above against the four design references.
Clear writing made the house preference explicit and kept its exceptions
concrete. Diagrams and tables produced separate symptom and shape-escalation
tables: one chooses a reference, the other states when a design should change.

The three design examples are included in the seven-example strict type check
and thirteen runtime probes recorded in the
[shared verification results](python-patterns.md#verification--2026-09-30).
The probes check static invocation, direct-construction invariants, frozen value
behavior, protocol use and preservation of borrowed resource ownership and
failures. A negative type-checking probe rejects an incompatible sink contract.
Package, isolated-copy, manifest, Markdown link and whitespace checks passed.

No independent agent trial, live discovery check or consumer rollout is claimed.
The examples demonstrate selected rules; they do not establish that every design
choice suits a real application. The package remains an unreleased starting set.

The entrypoint tables were rendered in a temporary 830-pixel content column
and inspected in external Chrome; text remained readable without horizontal
clipping. This was a local preview, not a check of every hosting renderer.

## Policy values that tests vary — 2026-10-10

Version 0.2.0 adds a section to [Class shape](../skills/languages/python-design/references/class-shape.md)
and a symptom row routing to it: a policy value that tests or callers vary,
such as a margin or limit, belongs to the operation that applies it, preferably
as a keyword-only or constructor parameter whose default is the policy, with a
class attribute as the smaller step. Tests pass the value instead of patching a
module global. [Values and call sites](../skills/languages/python-design/references/values-and-call-sites.md)
also names the NamedTuple alternative and python-patterns as its owner, after
the routing trial recorded on the
[python-patterns page](python-patterns.md#namedtuple-versus-frozen-dataclass--2026-10-10)
showed that reference alone pointing toward a frozen dataclass. The trigger was
a consumer layout compiler whose test patched a clearance margin.

The example parsed with Python 3.11's syntax feature version and ran on CPython
3.13 and 3.14.4. A probe confirmed that passing `margin=` changes the result and
that reassigning the class attribute after definition leaves the bound default
unchanged, as the reference states.

One routing trial ran in a fresh general-purpose agent with the same fixture
setup. The neutral task asked it to remove a `unittest.mock.patch` of a module
margin while keeping default behavior. It read the hook, the code and test,
python-design's entrypoint, followed the new row to class-shape and moved the
margin to a class attribute used as a keyword-only default; the test now passes
`margin=0.80` and both tests passed. It read no python-patterns material. One run
demonstrates the route, not its reliability; the nearby-scope case was not
exercised.
