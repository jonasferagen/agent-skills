---
name: python-design
description: "Apply the class-based Python house style when shaping operations, domain values, dependency protocols, naming and module boundaries. Use for code organization and ownership decisions."
metadata:
  version: "0.1.1"
---

# Python design

Apply the class-based house style using Python's own naming and call syntax.
Public domain operations belong on static or stateful classes, with the narrow
exceptions in [class shape](references/class-shape.md). This is an adopted
house preference, not a claim that Python requires classes for operations.

<!-- Package-boundary copy: python-patterns/SKILL.md carries the same repository authority rule. Keep both aligned. -->
The repository owns product contracts, framework choices, tooling and test
policy. When its instructions conflict with this package, report both passages
rather than silently changing either owner. Follow the user's explicit decision.

## Workflow

1. Name the operation, invariant or lifecycle that needs an owner.
2. Read the narrowest matching reference below. Trace callers and downstream
   uses before narrowing a dependency or moving behavior.
3. Apply the smallest shape that makes that ownership clear. Preserve public
   contracts and framework-required callables; keep a small edit scoped.
4. Update affected callers and repository examples, then run the relevant
   checks. Explain the deciding trigger and any remaining design tradeoff.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| An operation, service or factory needs a home | [Class shape](references/class-shape.md) |
| A data record gains invariants, or arguments travel together | [Values and call sites](references/values-and-call-sites.md) |
| A consumer depends on a large client or hidden global | [Dependency boundaries](references/dependency-boundaries.md) |
| Names, module placement or package exports are unclear | [Names and modules](references/names-and-modules.md) |

## Shape escalation

| Current shape | Change when |
| --- | --- |
| Positional arguments | Use keyword-only arguments when names remove ambiguity or clarify optional policy. |
| Several keyword arguments | Introduce an input record when they travel together with shared meaning. |
| Passive record | Add value behavior when invariants or repeated derivations need one owner. |
| Stateless operation | Use an instance when dependencies or state have a real lifetime. |

Stop at a passive contract for wire records and one-shot inputs. Classes should
make responsibility visible; inheritance, factories and registries need their
own use case. Language correctness and tool configuration remain separate
concerns; python-patterns is a suitable companion for language correctness when
available. Neither a test framework nor a package manager is prescribed here.
