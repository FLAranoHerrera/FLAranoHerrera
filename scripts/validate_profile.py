"""Dependency-free checks for this repository's inline Markdown/HTML format."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []


class ProfileHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.links.extend(attrs[key] for key in ('href', 'src') if attrs.get(key))
        if tag == 'img' and not attrs.get('alt', '').strip():
            errors.append('HTML image is missing alt text')
        if tag in ('div', 'details', 'summary', 'p', 'picture', 'a'):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ('div', 'details', 'summary', 'p', 'picture', 'a'):
            if not self.stack or self.stack.pop() != tag:
                errors.append(f'Unbalanced HTML closing tag: {tag}')


for doc in [ROOT / 'README.md', *sorted((ROOT / 'docs').glob('*.md'))]:
    content = doc.read_text(encoding='utf-8')
    fences = re.findall(r'^```.*$', content, re.M)
    if len(fences) % 2:
        errors.append(f'{doc.name}: unclosed fenced code block')
    if not content.endswith('\n'):
        errors.append(f'{doc.name}: missing final newline')
    for number, line in enumerate(content.splitlines(), 1):
        if line.rstrip() != line:
            errors.append(f'{doc.name}:{number}: trailing whitespace')
    parser = ProfileHTML()
    parser.feed(re.sub(r'^```.*?^```\s*$', '', content, flags=re.M | re.S))
    if parser.stack:
        errors.append(f'{doc.name}: unclosed HTML tags: {parser.stack}')
    links = parser.links + re.findall(r'\]\(([^\s)]+)\)', content)
    for link in links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (doc.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            errors.append(f'{doc.name}: missing or out-of-repository local file: {link}')

for asset in (ROOT / 'assets').rglob('*.svg'):
    try:
        root = ET.parse(asset).getroot()
        if root.tag != '{http://www.w3.org/2000/svg}svg':
            errors.append(f'{asset.name}: invalid SVG root')
    except ET.ParseError as error:
        errors.append(f'{asset.name}: {error}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print('PASS: Markdown hygiene, HTML structure, local file links and SVG XML')
