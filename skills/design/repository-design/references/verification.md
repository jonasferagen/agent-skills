# Verification across repositories

Start with the repository's promised operations and declared prerequisites. Define
what “standalone” means for them: a clean checkout plus its selected packages and
toolchain can build and run local tests; an operation using a database still needs
that declared database. Do not hide missing required verification behind a skip.

## Keep local evidence local

Local behavior tests use owned inputs and fixtures. Inject the external boundary
when a test checks local decisions; a temporary store directory should not need
another source checkout merely to enter the operation under test. Keep independent
expected results instead of computing them with the implementation being tested.

Pinned public contract fixtures can establish which adopted inputs a reader
accepts or refuses. Record their publication identity and provenance. Validate
generated fixtures against their selected source, not the publisher's current
working tree. A fake adapter does not prove the real provider still implements
that interface; keep an explicit integration check for that claim.

Separate local tests from cross-repository integration by their prerequisites and
claims. Both can be required gates when the project needs them. Integration is not
synonymous with optional or manual. Run it against explicitly selected versions,
with clear failure reports when a prerequisite is missing. Publisher compatibility
tests may exercise supported consumers without forcing their normal tests to read
private publisher paths.

## Exercise the proposed independence

Use a temporary standalone checkout or archive, with ordinary declared prerequisites
available and incidental siblings absent. Where relevant, change its directory name
or configure the same dependency at a different location. An archive may omit Git
metadata, so distinguish a declared Git requirement from a sibling dependency.
Do not rename or remove live repositories to create the experiment.

Select a failure that could disprove the proposed boundary: change an upstream
private filename without changing its interface, supply unsupported contract bytes,
remove an optional capability or make a required provider unavailable. Verify
that useful local operations remain usable and affected operations refuse with
the correct cause. A help command working alone does not establish that builds,
record reading or publication work independently.

When narrowing a dependency, preserve supported behavior with a representative
successful handoff and a rejection or recovery case. Do not make a suite green by
deleting interoperability coverage or replacing every boundary with an unverified
mock. Report local behavior, selected-version interoperability and latest-upstream
compatibility as separate claims, including checks that could not run.
