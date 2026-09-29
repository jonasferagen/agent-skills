#!/usr/bin/env python3
"""Check installable skill packages without a fixed list of skill names."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
VERSION = re.compile(
    r'^  version: "(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)'
    r'(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"$'
)


def check_package(package: Path) -> list[str]:
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

    for page in package.rglob("*.md"):
        for line_number, line in enumerate(page.read_text().splitlines(), 1):
            for match in LINK.finditer(line):
                destination = match.group(1).strip().split()[0].strip("<>")
                parsed = urlsplit(destination)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (page.parent / unquote(parsed.path)).resolve()
                location = f"{page.relative_to(ROOT)}:{line_number}"
                if not target.is_relative_to(package.resolve()):
                    errors.append(f"{location}: link leaves installable package: {destination}")
                elif not target.exists():
                    errors.append(f"{location}: missing link target: {destination}")
    return errors


def main() -> int:
    packages = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    errors = [error for package in packages for error in check_package(package)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(packages)} installable skill packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
