#!/usr/bin/env python3
"""Check cross-references in the written chapters before a LaTeX build."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
files = []
seen = set()

def visit(path):
    """Follow the actual master document, so orphan labels cannot hide errors."""
    path = path.resolve()
    if path in seen:
        raise SystemExit(f'Repeated TeX input: {path.relative_to(root)}')
    seen.add(path)
    files.append(path)
    source = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text())
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', source):
        child = root / name
        if not child.suffix:
            child = child.with_suffix('.tex')
        if not child.exists():
            raise SystemExit(f'Missing TeX input {name} in {path.name}')
        visit(child)

visit(root / 'monograph.tex')
labels, references, errors = {}, [], []
for path in files:
    source = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text())
    for label in re.findall(r'\\label\{([^}]+)\}', source):
        if label in labels:
            errors.append(f'Duplicate label {label}: {labels[label]} and {path.name}')
        labels[label] = path.name
    references += [(ref, path.name) for ref in re.findall(
        r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}', source)]
for ref, filename in references:
    if ref not in labels:
        errors.append(f'Undefined reference {ref} in {filename}')
print(f'{len(files)} files; {len(labels)} labels; {len(references)} references.')
orphans = sorted(p.name for p in (root / 'chapters').glob('*.tex')
                 if p.resolve() not in seen)
if orphans:
    print('Chapter fragments outside the master: ' + ', '.join(orphans))
if errors:
    raise SystemExit('\n'.join(errors))
print('All explicit cross-references resolve; no duplicate labels.')
