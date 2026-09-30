# Names and modules

Use `CapWords` for classes, `snake_case` for modules, functions, methods and
variables, and `UPPER_CASE` for constants. A leading underscore marks an
implementation detail by convention. Match the project's established public
names rather than renaming an external contract for style.

A module such as `invoice_total.py` can own `InvoiceTotal` and small related
contracts. Keep one coherent responsibility per module; Python does not need a
one-class-per-file rule. Split when responsibilities diverge, not merely because
a second related dataclass appears. Directory names should identify a domain or
real pipeline phase; avoid growing a miscellaneous `utils` or `helpers` bucket.

Name a class for its domain or obligation: a parser validates a representation,
a resolver chooses among sources, and a repository owns persistence operations.
Avoid a generic manager unless it genuinely owns a lifecycle. Name booleans as
predicates, while retaining meaningful domain terms.

## Keep import boundaries honest

Treat `__init__.py` exports as a deliberate package API. Avoid eager imports of
every submodule, wildcard imports and import-time creation of clients or services.
A small explicit public surface is easier to use without triggering unrelated
side effects. `__all__` describes exports; it is not enforced privacy.

When imports cycle, first inspect ownership: move a neutral contract to its real
owner or inject the dependency. A local import is useful for a genuinely optional
or deferred dependency, but should not hide a structural cycle by default.
`TYPE_CHECKING` imports can remove type-only cycles only when the runtime does
not need those names; frameworks evaluating annotations may still require them.

Keep CLI or application startup behind an entrypoint. Importing a library module
should not parse arguments, launch work or configure the application's logging.
Follow the repository's packaging and import conventions; do not mandate a
`src/` migration while reshaping a class.

Sources: [PEP 8](https://peps.python.org/pep-0008/),
[modules](https://docs.python.org/3/tutorial/modules.html).
