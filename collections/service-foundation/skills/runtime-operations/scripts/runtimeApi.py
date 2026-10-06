"""Declare the importable interface these runtime helpers offer their consumers."""

NAME = 'runtime-operations'
MAJOR = 1
MINOR = 0


def label(major: int = MAJOR, minor: int = MINOR) -> str:
    return f'{NAME}/{major}.{minor}'


def require(major: int, minor: int = 0) -> str:
    """Accept a consumer's expected interface, or raise naming both sides.

    A consumer states the interface it was written against. The major number
    changes when a module name, a function signature or a `Service` field
    changes incompatibly; the minor number rises when compatible surface is
    added. A consumer written against 1.0 keeps working on 1.3; one written
    against 1.3 refuses 1.0, because the surface it needs is absent.
    """
    if not isinstance(major, int) or not isinstance(minor, int):
        raise TypeError('An expected interface version is two integers')
    if major != MAJOR or minor > MINOR:
        raise RuntimeError(
            f'This installation offers {label()}; the caller requires '
            f'{label(major, minor)} or a compatible later minor version')
    return label()
