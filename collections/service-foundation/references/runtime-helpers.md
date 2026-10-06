# Import the runtime helpers

[Runtime operations](../skills/runtime-operations/SKILL.md) ships Python helpers
that service controllers import: `serviceControl`, `serviceHealth`,
`credentialStore` and `databaseBackup`. They are files in an installed
collection, not an installed package, so a consumer must put their directory on
`sys.path` before importing them. This reference owns how, and what the
collection guarantees across an update.

## Who owns what

The project owns **discovery**: which installed collection a repository uses and
how it finds that directory. A repository that holds the installation can derive
it from its own root. A repository using another repository's installation
resolves that owner through its existing declared route, and keeps that route in
the owner it already uses for cross-repository paths. The collection selects no
workspace layout and reads no project document.

Resolve a declared relative route against the document that declares it, not the
working directory a controller happens to run from. A route that works from the
repository root and fails from a service directory is the same defect either way,
and an absolute declared target hides it until someone makes the target relative.

The collection owns **admission**: rejecting an unusable directory and refusing
an interface the caller was not written against. Copy
[the loader](../templates/repository-docs/tools/service_runtime.py) into the
repository that runs services and give it the resolved directory:

```python
from service_runtime import load

load(collection_root, major=1)
import serviceControl
```

Deploy it verbatim, as with the services dispatcher; keep the project's
discovery in its own function or module so a later refresh replaces only the
loader. Each consumer then performs the same check instead of its own.

## What the two numbers mean

[The declaration](../skills/runtime-operations/scripts/runtimeApi.py) states the
interface the installed helpers offer. Its **major** number changes when a module
name, a function signature or a `Service` field changes incompatibly. Its
**minor** number rises when compatible surface is added. A consumer names the
version it was written against: one written against 1.0 keeps working on 1.3,
and one written against 1.3 refuses 1.0, because the surface it needs is absent.

This interface is versioned separately from the skill's `metadata.version` and
from the collection version. Prose guidance and importable surface change for
different reasons; a clarified paragraph is not an interface event, and a new
helper argument is not a guidance event.

A refusal raises before `sys.path` changes, naming both the installation's
interface and the caller's requirement. That ordering is the point: a failed
check must not leave an import path behind for a later `import serviceControl`
to succeed against. An installation predating this declaration is reported as
such and must be re-pinned before use rather than imported hopefully.

## Limits

The loader performs no discovery, installs nothing, and starts no service. It
does not verify the collection's source pin; [installation](installation.md)
owns that, and a passing version check is not evidence that the intended
revision is installed. It admits a Python import path only: helpers remain files
in a vendored directory, and a non-Python controller calls its own commands.

Because [an update replaces the whole directory](installation.md#update-as-one-unit),
every consumer importing these helpers is re-pointed at once. The version check
makes an incompatible replacement fail at the importing controller, with a
message naming both sides, instead of failing later inside a helper call. It
cannot make such a replacement safe: review the consumers a major change affects
and exercise each affected controller.
