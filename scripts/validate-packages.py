#!/usr/bin/env python3
"""Check installable skill packages without a fixed list of skill names."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
COLLECTIONS = ROOT / "collections"
LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
VERSION = re.compile(
    r'^  version: "(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)'
    r'(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"$'
)


def check_package(package: Path, check_links: bool = True) -> list[str]:
    errors = []
    manifest = package / "SKILL.md"
    if not manifest.is_file():
        return [f"{package.name}: missing SKILL.md"]

    content = manifest.read_text()
    parts = content.split("---", 2)
    if len(parts) != 3 or parts[0] != "" or "\n" not in parts[1]:
        errors.append(f"{manifest.relative_to(ROOT)}: invalid frontmatter")
    else:
        frontmatter = parts[1].splitlines()
        for field in (f"name: {package.name}", "metadata:"):
            if field not in frontmatter:
                errors.append(f"{manifest.relative_to(ROOT)}: missing {field}")
        if not any(VERSION.fullmatch(line) for line in frontmatter):
            errors.append(f"{manifest.relative_to(ROOT)}: missing string metadata.version")
        if not any(line.startswith("description: ") for line in frontmatter):
            errors.append(f"{manifest.relative_to(ROOT)}: missing description")

    if check_links:
        errors.extend(check_local_links(package))
    return errors


def check_local_links(unit: Path) -> list[str]:
    errors = []
    for page in unit.rglob("*.md"):
        for line_number, line in enumerate(page.read_text().splitlines(), 1):
            for match in LINK.finditer(line):
                destination = match.group(1).strip().split()[0].strip("<>")
                parsed = urlsplit(destination)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (page.parent / unquote(parsed.path)).resolve()
                location = f"{page.relative_to(ROOT)}:{line_number}"
                if not target.is_relative_to(unit.resolve()):
                    errors.append(f"{location}: link leaves installation unit: {destination}")
                elif not target.exists():
                    errors.append(f"{location}: missing link target: {destination}")
    return errors


def find_packages(directory: Path) -> list[Path]:
    """Descend through categories, stopping at a package or an invalid leaf."""
    if (directory / "SKILL.md").is_file():
        return [directory]
    children = sorted(path for path in directory.iterdir() if path.is_dir())
    if not children:
        return [directory]
    return [package for child in children for package in find_packages(child)]


def main() -> int:
    packages = find_packages(SKILLS)
    errors = [error for package in packages for error in check_package(package)]
    collections = sorted(path for path in COLLECTIONS.iterdir() if path.is_dir()) if COLLECTIONS.exists() else []
    for collection in collections:
        if not (collection / "COLLECTION.md").is_file():
            errors.append(f"{collection.relative_to(ROOT)}: missing COLLECTION.md")
        if not (collection / "skills").is_dir():
            errors.append(f"{collection.relative_to(ROOT)}: missing skills directory")
            continue
        members = find_packages(collection / "skills")
        packages.extend(members)
        errors.extend(error for package in members for error in check_package(package, check_links=False))
        errors.extend(check_local_links(collection))
    names: dict[str, Path] = {}
    for package in packages:
        if package.name in names:
            errors.append(
                f"Duplicate package name {package.name}: "
                f"{names[package.name].relative_to(ROOT)} and {package.relative_to(ROOT)}"
            )
        names[package.name] = package
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(packages)} skill entries, including {len(collections)} collections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
