#!/usr/bin/env python3
"""Print a bounded source excerpt around an exact LaTeX label.

Usage: python3 Output/tools/source_excerpt.py LABEL [--context 35]
The generated source index avoids rescanning the full manuscripts.
"""
import argparse
import json
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('label')
p.add_argument('--context', type=int, default=35)
args = p.parse_args()
root = Path(__file__).resolve().parents[2]
index = json.loads((root / 'Output/blueprint/source-index.json').read_text())
found = False
for entry in index:
    for item in entry['labels']:
        if item['label'] != args.label:
            continue
        found = True
        lines = (root / entry['file']).read_text().splitlines()
        start = max(1, item['line'] - 3)
        stop = min(len(lines), item['line'] + args.context)
        print(f"\n{entry['file']}:{item['line']} [{start}-{stop}]")
        for n in range(start, stop + 1):
            print(f'{n:5d} {lines[n - 1]}')
if not found:
    p.error('label not found in the supplied source snapshot')
