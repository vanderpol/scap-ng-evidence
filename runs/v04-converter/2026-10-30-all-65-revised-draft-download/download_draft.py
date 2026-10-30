#!/usr/bin/env python3
"""Download or locally reassemble the immutable revised DRAFT; verify each hash."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import urllib.request

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--parts',type=Path,help='local directory containing manifest.json and archive parts')
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
base='https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download/'
manifest=json.loads((args.parts/'manifest.json').read_text()) if args.parts else json.loads(urllib.request.urlopen(base+'manifest.json').read())
if args.output.exists():raise SystemExit('refusing to overwrite output')
digest=sha256()
with args.output.open('xb') as output:
    for item in manifest['parts']:
        raw=(args.parts/item['file']).read_bytes() if args.parts else urllib.request.urlopen(base+item['file']).read()
        if len(raw)!=item['bytes'] or sha256(raw).hexdigest()!=item['sha256']:raise SystemExit('part checksum mismatch: '+item['file'])
        output.write(raw);digest.update(raw)
if digest.hexdigest()!=manifest['archive']['sha256']:raise SystemExit('reassembled archive checksum mismatch')
print(str(args.output)+'  SHA256 '+digest.hexdigest())
