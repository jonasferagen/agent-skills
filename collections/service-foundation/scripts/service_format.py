"""Read service-definition/v1 and enumerate one explicitly adopted service home."""
from __future__ import annotations

import re
from pathlib import Path


class ServiceHome:
    """Discover only the index and immediate guides; never execute controllers."""

    @staticmethod
    def documents(home: Path) -> list[Path]:
        if home.resolve() != home or not home.is_dir():
            raise ValueError(f'{home}: service home must be a real directory without symlinks')
        guides = [home / 'README.md']
        for child in sorted(home.iterdir()):
            if child.is_symlink():
                raise ValueError(f'{child}: service entries must not be symlinks')
            if child.is_dir():
                if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', child.name):
                    raise ValueError(f'{child}: expected a lowercase hyphenated service name')
                guides.append(child / 'README.md')
        if len(guides) == 1:
            raise ValueError(f'{home}: selected service home has no service definitions')
        for guide in guides:
            if guide.resolve() != guide or not guide.is_file():
                raise ValueError(f'{guide}: expected a regular, non-symlink guide')
        return guides


class ServiceDefinition:
    VERSION = 'service-definition/v1'
    FIELDS = ('Identity', 'Owner', 'Purpose', 'Status', 'Lifetime', 'Exposure',
              'Dependencies', 'State', 'Operations', 'Readiness', 'Recovery', 'Evidence')
    ROUTES = frozenset(('Dependencies', 'State', 'Operations', 'Readiness', 'Recovery', 'Evidence'))
    LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\(([^\s)]+)\)')

    @staticmethod
    def _visible(text: str) -> list[tuple[int, str]]:
        visible = []
        fence = None
        comment = False
        for number, line in enumerate(text.splitlines(), 1):
            if fence:
                if re.fullmatch(r' {0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}\s*', line):
                    fence = None
                continue
            match = re.match(r' {0,3}(`{3,}|~{3,})', line)
            if match and not comment:
                fence = match[1]
                continue
            # Comments carry no declarations, including an inline example.
            cleaned = ''
            rest = line
            while rest:
                if comment:
                    if '-->' not in rest:
                        break
                    rest = rest.split('-->', 1)[1]
                    comment = False
                elif '<!--' in rest:
                    before, rest = rest.split('<!--', 1)
                    cleaned += before
                    comment = True
                else:
                    cleaned += rest
                    break
            visible.append((number, cleaned))
        return visible

    @classmethod
    def parse(cls, text: str) -> dict | None:
        lines = cls._visible(text)
        markers = [(number, line.strip()) for number, line in lines if line.strip().startswith('Service format:')]
        if not markers:
            return None
        if len(markers) != 1 or markers[0][1] != 'Service format: ' + cls.VERSION:
            raise ValueError('expected one supported Service format: ' + cls.VERSION)
        headings = [(i, number) for i, (number, line) in enumerate(lines) if line.strip() == '## Service definition']
        if len(headings) != 1:
            raise ValueError('expected one ## Service definition section')
        start, heading_line = headings[0]
        if markers[0][0] >= heading_line:
            raise ValueError('Service format declaration must precede Service definition')
        body = []
        for number, line in lines[start + 1:]:
            if re.match(r' {0,3}#{1,2}\s', line):
                break
            if line.strip():
                body.append((number, line.strip()))
        def cells(line):
            if not line.startswith('|') or not line.endswith('|'):
                raise ValueError('Service definition must contain only its Field / Value table')
            return [cell.strip() for cell in re.split(r'(?<!\\)\|', line[1:-1])]
        if len(body) < 2 or cells(body[0][1]) != ['Field', 'Value'] or len(cells(body[1][1])) != 2 or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in cells(body[1][1])):
            raise ValueError('Service definition requires a Field / Value table')
        facts = []
        seen = set()
        links = []
        for number, line in body[2:]:
            row = cells(line)
            if len(row) != 2:
                raise ValueError(f'line {number}: expected two fact cells')
            name, value = row
            if name not in cls.FIELDS or name in seen:
                raise ValueError(f'line {number}: unknown or duplicate service field {name}')
            if not value:
                raise ValueError(f'line {number}: empty service field {name}; use Unknown or None explicitly')
            seen.add(name)
            if name == 'Identity' and not re.fullmatch(r'[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*', value):
                raise ValueError(f'line {number}: invalid service Identity')
            targets = cls.LINK.findall(value)
            if name in cls.ROUTES and not targets and value not in ('Unknown', 'None'):
                raise ValueError(f'line {number}: {name} needs a Markdown route, Unknown or None')
            for label, target in targets:
                if ':' in target or target.startswith(('/', '//')) or '\\' in target:
                    raise ValueError(f'line {number}: service routes must be local or symbolic Markdown targets')
                links.append({'field': name, 'label': label, 'target': target, 'line': number})
            facts.append({'name': name, 'value': value, 'line': number})
        if set(cls.FIELDS) != seen:
            raise ValueError('missing service fields: ' + ', '.join(name for name in cls.FIELDS if name not in seen))
        identity = next(fact['value'] for fact in facts if fact['name'] == 'Identity')
        return {'version': cls.VERSION, 'id': identity, 'line': heading_line, 'facts': facts, 'links': links}
