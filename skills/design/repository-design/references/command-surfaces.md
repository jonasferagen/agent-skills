# Command surfaces

A command is a supported interface when a person or another system may rely on
its invocation and result. An executable file is not necessarily public; a
package script or configured entrypoint can be public without a dedicated file.
Use the consuming project's conventions for names, layout and CLI grammar.

## Find the surface and its callers

Establish the review boundary from the request and repository instructions.
Discover candidate entrypoints from tracked source and declarations, not only
one directory or the executable bit. Examine conventional root commands,
component tools, package scripts, installed console entrypoints, service controls,
workflow configuration and executable adapters as relevant. Exclude dependency
copies, generated output and other worktrees from the source inventory.

Trace each candidate through wrappers to its parser and operation. Classify its
owner, audience, supported invocation and effects. Distinguish an interactive
command, a machine protocol, an internal adapter and a verification helper. A
machine-facing interface can be public even when nobody runs it by hand.

Find callers in code, tests, package and service configuration, documentation,
skills and declared dependent repositories. Follow dynamically assembled paths
and subprocess arguments when a literal search cannot account for them. Separate
known callers from unexamined external consumers; no search result does not prove
disuse. Search project-owned invocation guidance; imported skill scenarios and
vendor examples are not evidence of this project's callers. Do not execute a
command merely to discover its options: inspect first,
and use help only when it is known to avoid operational effects.

Report the scope and exclusions of an inventory. Count public entrypoints,
operations and retained internal executables separately when comparing designs.
Moving a file out of a tool directory does not remove its maintenance burden.

## Choose the public boundary

Group operations when callers recognize a shared responsibility and owner. A
subcommand family can improve discovery while retaining separate implementation
modules. Preserve distinctions in target selection, effects, output, failure,
state lifetime and evidence; a shared word such as "check" does not make two
operations interchangeable. Do not create a universal dispatcher just to meet a
file-count target.

Keep verification helpers and adapters with the component whose behavior they
implement. Where another component relies on an adapter, preserve or replace its
supported interface before making it private. A generic runner belongs with its
execution owner; domain-specific preparation belongs with the domain. Expose the
operation the consumer needs rather than making provider fixtures or private
configuration public by renaming them.

The owner should publish a discoverable command entrypoint and its contract.
Help or a parser-derived reference can own syntax and defaults; component guides
explain effects and guarantees. Avoid maintaining independent copies of complete
argument lists. Language module names need not match executable names.

## Change and verify the interface

Identify affected callers before choosing a rename, move, merge or split. Update
invocations, configuration, skills, documentation and checks together within the
authorized scope. Independently deployed consumers may need a compatibility
adapter and an explicit removal condition; neither permanent aliases nor an
immediate breaking change is a universal default. Keep the old and new behavior
distinguishable until migration evidence supports retiring the old interface.

Choose checks for the actual risks: argument boundaries and forwarding, selected
defaults, output and exit status, failure without unintended effects, and
interoperability at affected consumer boundaries. Public help should be reachable
without starting the operation. A syntax check alone does not establish preserved
behavior, and fewer entrypoints do not establish less coupling.

When adding discovery checks, derive candidates from the repository's current
sources or declarations. Check resolution and classification rather than a frozen
list of today's filenames or exact prose. Give exceptions a reason and owner.
Keep consumer checks tied to the adopted contract; an explicit upgrade check may
compare a selected publisher revision. Do not make ordinary local checks depend
on a moving upstream checkout.
