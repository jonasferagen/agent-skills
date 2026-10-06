"""Import the installed service-foundation runtime helpers at a checked interface version.

Copy this file into the repository that runs services, next to its other tools,
and give `load` the installed collection directory. Finding that directory is
the project's decision: a repository holding the installation can derive it from
its own root, and a repository using another one's installation resolves that
owner through its existing declared route. This loader owns what follows -
rejecting an unusable directory and refusing an interface the caller was not
written against - so every consumer gets the same check instead of its own.
"""
from pathlib import Path
import importlib.util
import sys

SCRIPTS = 'skills/runtime-operations/scripts'


def load(collection, *, major, minor=0):
    """Make the helpers importable, or raise before changing `sys.path`.

    Returns the accepted interface label. Verifying first matters: a failed
    version check must not leave a half-wired import path behind for a later
    `import serviceControl` to succeed against.
    """
    scripts = Path(collection).expanduser()
    if scripts.name != SCRIPTS.rsplit('/', 1)[-1]:
        scripts = scripts / SCRIPTS
    if scripts.is_symlink() or not scripts.is_dir():
        raise RuntimeError(f'No service-foundation runtime helpers at {scripts}')
    declaration = scripts / 'runtimeApi.py'
    if declaration.is_symlink() or not declaration.is_file():
        raise RuntimeError(
            f'{scripts}: installed helpers declare no interface version; this '
            'installation predates the loader and must be re-pinned before use')
    specification = importlib.util.spec_from_file_location(
        'serviceFoundationRuntimeApi', declaration)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    accepted = module.require(major, minor)
    entry = str(scripts)
    if entry not in sys.path:
        sys.path.append(entry)
    return accepted
