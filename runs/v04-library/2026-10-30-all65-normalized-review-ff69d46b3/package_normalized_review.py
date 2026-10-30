"""Archive completed #261 output without conversion, promotion or regeneration."""
from hashlib import sha256
import json
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parent
LIBRARY=ROOT/'normalized-all65'
OUT=ROOT/'publication';OUT.mkdir(exist_ok=True)
(LIBRARY/'README.md').write_text('''# SCAP-NG 0.4 normalized library review candidate (#261)

This is an out-of-place layout preview, not a final 0.4 release or a new
semantic-verification result. Native YAML is under content/. Generated catalog
and SQLite metadata support lazy navigation; records/ preserves the exact
original Rule ledgers and source traces. Native compiler input remains logical
IDs in the existing local/global visibility model. Profiles stay embedded.

65 original streams /8,892 Rules: 4,258 retained static proofs +2,559 unverified
native +422 blocked automated +1,653 manual/OCIL records. All 6,817 compiled
Assessment program hashes and all 4,258 accepted proof triples are unchanged.
All 13,754 native YAML files are byte-identical to the original DRAFT. There
are 60 native Benchmarks, 60 applicability registries, 6,817 Rules and 6,817
Assessments. Five streams lacking native candidates remain original-only
records with publisher titles; no fake native Benchmarks/Assessments are added.

Use the exact source toolchain linked by the parent evidence manifest:

python tools/scap_ng_library_cli.py check /path/to/this/content
python tools/scap_ng_library_cli.py search /path/to/this/content --kind assessment --status CONVERTED_UNVERIFIED
python tools/scap_ng_library_cli.py records /path/to/this/content --status MANUAL_OCIL_ONLY_PRESERVED
python tools/scap_ng_library_cli.py analyze /path/to/this/content

The SQLite cache is disposable; an explicit index rebuild restores proof/
warning associations from durable records and rechecks current hashes. Do not
delete the original records/provenance. Standalone Assessments need no Benchmark
or catalog. Analyze/check never rewrite source. Apply is explicit, diff-first,
presentation-only and guarded; no-op saves remain byte-identical. No automatic
cross-Assessment deduplication or consumer repointing occurs. Reuse proposals
are published separately; titles/fingerprints are never semantic-proof authority.

Original signed ZIP/XML/manual content remains in the immutable complete DRAFT:
https://github.com/vanderpol/scap-ng-evidence/tree/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download
SHA256 a09ee9a13cdfeeb1b8599eab61308e935a19b99eb62eadafd32002d13d90f8bd

Offline native editing/indexing/compilation does not contact that repository.
Original XML inspection needs the separately downloaded source artifact. Exact
per-Rule archive members and source identities remain in records. Runtime
scanner equivalence, full original policy/applicability/manual migration,
publisher authentication and new independent source proofs are not claimed.
Licensing status is unchanged; no new project-wide license grant is made.
''')
inventory=[]
for p in sorted(LIBRARY.rglob('*')):
    if p.is_file() and p.name!='artifact-files.json':
        inventory.append({'path':p.relative_to(LIBRARY).as_posix(),'bytes':p.stat().st_size,
                          'sha256':sha256(p.read_bytes()).hexdigest()})
(LIBRARY/'metadata/artifact-files.json').write_text(json.dumps(inventory,indent=2)+'\n')
archive=OUT/'scap-ng-v04-normalized-library-review.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as out:
    for p in sorted(LIBRARY.rglob('*')):
        if p.is_file():
            info=zipfile.ZipInfo('scap-ng-normalized-review/'+p.relative_to(LIBRARY).as_posix(),date_time=(1980,1,1,0,0,0))
            info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED
            out.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
with zipfile.ZipFile(archive) as check:
    assert check.testzip() is None
    for item in inventory:
        raw=check.read('scap-ng-normalized-review/'+item['path'])
        assert len(raw)==item['bytes'] and sha256(raw).hexdigest()==item['sha256']
receipt={'file':archive.name,'bytes':archive.stat().st_size,'sha256':sha256(archive.read_bytes()).hexdigest(),
         'payload_files':len(inventory)+1,'every_payload_digest':'PASS','zip_crc':'PASS',
         'native_files':13754,'native_yaml_changed':0,'shared_promotions':0}
(OUT/'normalized-archive-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
