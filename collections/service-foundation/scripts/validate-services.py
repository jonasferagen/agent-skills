#!/usr/bin/env python3
"""Check an explicitly selected service home without executing controls."""
import argparse
import os
from pathlib import Path
import re
import runpy
from urllib.parse import unquote, urlsplit

ServiceDefinition = runpy.run_path(str(Path(__file__).with_name("service_format.py")))["ServiceDefinition"]

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"(?<!!)\[[^]\n]+\]\(<?([^\s)>]+)>?\)")


def validate(home: Path) -> list[str]:
    errors = []
    if home.is_symlink() or not home.is_dir():
        return [f"{home}: selected service home must be a real directory"]

    def required(path, executable=False):
        if path.is_symlink() or not path.is_file():
            errors.append(f"{path}: expected a regular, non-symlink file")
            return False
        if executable and not os.access(path, os.X_OK):
            errors.append(f"{path}: control must be executable")
        return True

    index = home / "README.md"
    index_ok = required(index)
    required(home / "control", True)
    services = []
    for child in sorted(home.iterdir()):
        if child.is_symlink():
            if child.name not in {"README.md", "control"}:
                errors.append(f"{child}: service entries must not be symlinks")
        elif child.is_dir():
            services.append(child)
            if not NAME.fullmatch(child.name):
                errors.append(f"{child}: expected a lowercase hyphenated service name")
            required(child / "README.md")
            required(child / "control", True)
    identities = set()
    for service in services:
        guide = service / "README.md"
        if guide.is_symlink() or not guide.is_file():
            continue
        try:
            definition = ServiceDefinition.parse(guide.read_text(encoding="utf-8"))
            if definition:
                if definition["id"] in identities:
                    raise ValueError("duplicate service Identity: " + definition["id"])
                identities.add(definition["id"])
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{guide}: {error}")
    if not services:
        errors.append(f"{home}: selected service home has no service definitions")
    if index_ok:
        try:
            text = index.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{index}: cannot read index: {error}")
        else:
            targets = set()
            for raw in LINK.findall(text):
                try:
                    link = urlsplit(raw)
                except ValueError:
                    errors.append(f"{index}: malformed link: {raw}")
                    continue
                if link.scheme or link.netloc or not link.path:
                    continue
                # Compare lexically; never follow links or inspect targets outside
                # this selected home. Only direct service-guide routes are checked.
                relative = Path(os.path.normpath(unquote(link.path)))
                if relative.is_absolute() or ".." in relative.parts:
                    continue
                if len(relative.parts) == 2 and relative.name == "README.md":
                    targets.add(relative.as_posix())
                    if relative.parts[0] not in {p.name for p in services}:
                        errors.append(f"{index}: guide target has no service definition: {raw}")
            for service in services:
                if f"{service.name}/README.md" not in targets:
                    errors.append(f"{index}: missing inline link to {service.name}/README.md")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("home", type=Path, help="adopted service home, e.g. services/")
    args = parser.parse_args()
    try:
        errors = validate(args.home)
    except OSError as error:
        errors = [f"{args.home}: inspection failed: {error}"]
    for error in errors:
        print(error)
    if not errors:
        print(f"Service structure valid: {args.home}")
    print("Scope: files, names, executable permissions and inline index-to-guide links and declared service formats; "
          "controls were not executed. Runtime behavior, route targets and guide meaning are unverified.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
