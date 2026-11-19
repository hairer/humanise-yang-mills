#!/usr/bin/env python3
"""Collect only cited entries from the supplied and editorial bibliographies."""
from pathlib import Path
import re

out = Path(__file__).resolve().parents[1]
root = out.parent
sources = [root / 'Scott/references.bib', root / 'Martin/references.bib']
sources += sorted((out / 'audit').glob('*.bib'))
sources += sorted((out / 'blueprint').glob('*bibliography.bib'))
sources += [out / 'bibliography-additions.bib']
entries = {}
for path in sources:
    if not path.exists():
        continue
    for chunk in re.split(r'(?m)(?=^@)', path.read_text()):
        match = re.match(r'@\w+\s*\{\s*([^,]+),', chunk)
        if match:
            entries.setdefault(match.group(1), chunk.strip())
keys = set()
for path in [out / 'monograph.tex', *sorted((out / 'chapters').glob('*.tex'))]:
    for group in re.findall(r'\\(?:cite|nocite)\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', path.read_text()):
        keys.update(k.strip() for k in group.split(','))
missing = keys - entries.keys()
if missing:
    raise SystemExit('Missing bibliography entries: ' + ', '.join(sorted(missing)))
(out / 'references.bib').write_text('\n\n'.join(entries[k] for k in sorted(keys)) + '\n')
print(f'Collected {len(keys)} cited references.')
