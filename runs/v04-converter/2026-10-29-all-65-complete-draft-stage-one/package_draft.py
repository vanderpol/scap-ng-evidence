import hashlib,json,platform,shutil,subprocess,sys,zipfile
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).parent
PAYLOAD=ROOT/'all-65-draft'
DEST=Path('/workspace/scap-ng-evidence/runs/v04-converter/2026-10-29-all-65-complete-draft-stage-one')
SHA='0b2fdb2d392c5d80a4128d73ae4ac5ada573cf26'
summary=json.loads((PAYLOAD/'summary.json').read_text())
assert summary['statuses']=={'BLOCKED_EXPLICIT':2981,'MANUAL_OCIL_ONLY_PRESERVED':1653,
    'RETAINED_PUBLISHED_STATIC_PRIMARY_PROOF':4206,'CONVERTED_SCHEMA_VALID_UNVERIFIED':52},summary['statuses']
assert sum(s['compiled_programs'] for s in summary['sources'])==4258
DEST.mkdir(parents=True,exist_ok=False)
for name in ['proof-baseline.json','known-invalid-final.json','recover_inputs.py','recover_baseline.py','generation.log']:
    shutil.copy2(ROOT/name,PAYLOAD/name)
readme='''# Complete all-65 stage-one DRAFT — NOT VERIFIED FOR EXECUTION

Download `all-65-complete-draft.zip`, extract it, and open `index.html`.
All 65 original ZIPs, all 8,892 original Rules and manual/OCIL components are
preserved. All 7,239 automated Rules received conversion attempts. The ledger
distinguishes 4,206 unchanged published static proofs, 52 structurally valid
UNVERIFIED candidates, 2,981 explicit blockers and 1,653 manual/OCIL-only Rules.
All 4,258 native candidates compile with checked operands. No blocked/manual
Rule receives a fictional executable Assessment. Native Rule/policy wrappers
cover a partial primary automated subset; the original policy remains separate.

Toolchain: vanderpol/scap-ng at `'''+SHA+'''`.
This is a reconstruction of the interrupted completed deliverable: its previous
local payload was lost when the session workspace was replaced. The existing
builder was run once from identical pinned originals and the recovered published
4,206-proof baseline; no frozen archive or accepted hash was replaced.

Reproduce from that source checkout with the dependencies recorded there:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools python tools/build_v04_full_draft.py \\
  --source-pins source-pins.json --inputs ORIGINAL_ZIPS \\
  --baseline proof-baseline.json --known-invalid known-invalid-final.json \\
  --output NEW_UNIQUE_DIRECTORY --workers 3 --acknowledge-full-corpus-deliverable
```

The originals are embedded under each benchmark's `source-preservation/` folder.
Recovery scripts retain their original workspace paths as forensic records;
the maintained builder command above is the portable generation entry point.
Stage-two proofs are published separately and never relabel this frozen DRAFT.
No scanner-runtime parity, publisher trust, complete policy migration or final
verified release is claimed. Unsupported #255 contracts remain explicit.
'''
(PAYLOAD/'README.md').write_text(readme)
environment={'python':sys.version,'platform':platform.platform(),'toolchain_sha':SHA}
for name in ['lxml','yaml','jsonschema']:
    module=__import__(name);environment[name]=getattr(module,'__version__','see installed package metadata')
(PAYLOAD/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
inventory=[]
for p in sorted(PAYLOAD.rglob('*')):
    if p.is_file():inventory.append({'path':p.relative_to(PAYLOAD).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(PAYLOAD/'artifact-files.json').write_text(json.dumps(inventory,indent=2)+'\n')
archive=DEST/'all-65-complete-draft.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(PAYLOAD.rglob('*')):
        if not p.is_file():continue
        info=zipfile.ZipInfo(p.relative_to(PAYLOAD).as_posix(),date_time=(2026,10,29,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
        z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for row in inventory:assert hashlib.sha256(z.read(row['path'])).hexdigest()==row['sha256']
    count=len(z.namelist())
digest=hashlib.sha256(archive.read_bytes()).hexdigest()
manifest={'evidence_id':'v04-all-65-complete-draft-stage-one-20261029','evidence_kind':'production-migration-draft',
 'created_at':datetime.now(timezone.utc).isoformat(),'source_repository':'vanderpol/scap-ng','source_commit':SHA,
 'generating_tool':'tools/build_v04_full_draft.py + tools/finalize_v04_full_draft.py','generating_tool_commit':SHA,
 'reproduction':'README.md and pinned builder command; packaging script included separately',
 'inputs':'source-pins.json; 65 original ZIPs at NIWC 8c8e5dff860af6b1290ee9273a282db24278f8d5',
 'output_root':'all-65-complete-draft.zip','output_file_count':count,
 'archive':{'file':archive.name,'bytes':archive.stat().st_size,'sha256':digest},
 'validation_status':'DRAFT; original preservation, accounting, schema, compilation and retained-proof hashes PASS; 52 native candidates independently UNVERIFIED',
 'checks':summary['checks']+['4258 candidates compiled with checked operands','archive CRC and every expanded payload digest checked'],
 'counts':{k:summary[k] for k in ['benchmarks','rules','automated_conversion_attempts','retained_published_proofs','statuses','blocked_primary_dispositions']},
 'maintained_ci':{'source_commit':SHA,'run':40927089208,'job':123635368063,'tests_run':3308,'passed':3307,'skips':1,'failures':0,'errors':0,'seconds':603.717,'artifact':12920644342},
 'limitations':summary['limitations'],'storage_decision':'See STORAGE-DECISION.md; explicit inspectable DRAFT deliverable authorized under #251',
 'interrupted_payload_recovery':'Original local build directory absent; regenerated once because necessary, preserving pinned code/input/proof floor and all prior archive bytes.'}
(DEST/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(DEST/'README.md').write_text(readme)
(DEST/'STORAGE-DECISION.md').write_text('''# Bounded review-storage decision (Refs vanderpol/scap-ng#251)

The owner explicitly requested a complete downloadable all-65 DRAFT, preserved
originals/manual content and permanent evidence publication. After analysis,
retain this single compressed review archive under a unique immutable DRAFT tag,
following the existing all-65 review-storage exception. Compact counts, source
pins, manifest, checksum and complete per-file inventory accompany it. Expanded
generated payload is not committed. The earlier frozen archive remains unchanged.
This is draft content publication, not a specification or toolchain release.
''')
for name in ['summary.json','source-pins.json','environment.json','artifact-files.json']:
    shutil.copy2(PAYLOAD/name,DEST/name)
shutil.copy2(Path(__file__),DEST/'package_draft.py')
(DEST/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in sorted(DEST.iterdir()) if p.is_file() and p.name!='SHA256SUMS'))
print(json.dumps(manifest['archive']),flush=True)
