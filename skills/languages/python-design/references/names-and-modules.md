# Names and modules

Use `CapWords` for classes, `snake_case` for modules, functions, methods and
variables, and `UPPER_CASE` for constants. A leading underscore marks an
implementation detail by convention. Match the project's established public
names rather than renaming an external contract for style.

A module can own related functions, classes and records. Group them by a
responsibility callers can name and a rule that changes for one reason. Keep
closely related behaviour together; split when responsibilities, dependencies or
lifetimes diverge, not merely because a file is long or contains a second class.
Directory names should identify a domain or real pipeline phase; avoid growing
a miscellaneous `utils` or `helpers` bucket.

Trace the dependency direction: core rules should not need a CLI, database
driver or display formatter just to run. Keep transport adapters near their
external boundary and orchestration where inputs, policies and effects meet.
A small program may keep these in one module with clear functions; do not
create layers that only forward calls. Share a helper when callers share its
semantics, not merely similar lines of code.

Name a class for its domain or obligation: a parser validates a representation,
a resolver chooses among sources, and a repository owns persistence operations.
Avoid a generic manager unless it genuinely owns a lifecycle. Name booleans as
predicates, while retaining meaningful domain terms. Prefer names that expose
validation state, units or effects where callers might otherwise guess.
Short mathematical names remain appropriate inside a small calculation.

When a module starts dispatching multiple versions, separate selection from
version-specific rules if the combined responsibility obscures either.
Preserve public names and compatibility adapters until callers can migrate;
renaming alone does not improve ownership.

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
Follow the project's packaging and import conventions; do not mandate a
`src/` migration while reshaping a class.

Sources: [PEP 8](https://peps.python.org/pep-0008/),
[modules](https://docs.python.org/3/tutorial/modules.html).
