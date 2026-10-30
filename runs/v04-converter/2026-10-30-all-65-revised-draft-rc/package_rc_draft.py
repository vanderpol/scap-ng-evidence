"""Package existing completed corpus; never regenerate converted content."""
from hashlib import sha256
import json
from pathlib import Path
import shutil
import zipfile

ROOT=Path(__file__).resolve().parent
PAYLOAD=ROOT/'all-65-draft'
OUT=ROOT/'publication'
OUT.mkdir(exist_ok=True)
summary=json.loads((PAYLOAD/'summary.json').read_text())
assert summary['conversion_statuses']=={'CONVERTED_UNVERIFIED':2559,
    'MANUAL_OCIL_ONLY_PRESERVED':1653,'CONVERTED_VERIFIED':4258,'BLOCKED':422}
assert sum(s['compiled_programs'] for s in summary['sources'])==6817
for name in ['proof-baseline-4258.json','known-invalid-rc.json','cohort-recovery.json','full-draft-build.log']:
    shutil.copy2(ROOT/name,PAYLOAD/name)
(PAYLOAD/'README.md').write_text('''# Revised all-65 DRAFT — NOT VERIFIED FOR EXECUTION

65 pinned Benchmarks; 8,892 original Rules; 7,239 automated attempts.
4,258 retained independent static primary proofs; 2,559 newly admitted
UNVERIFIED native candidates; 422 blocked automated Rules; 1,653 preserved
manual/OCIL-only Rules. All 6,817 native candidates compile with checked
operands. All 4,258 prior source/authoring/program hash pairs are unchanged.

Open index.html after extraction. ledger.csv and ledger.json separate native
conversion, compilation, static proof and warnings. Per-source ledgers retain
dependency graphs and original Rule identities. Every original signed ZIP and
Rule/manual content is preserved. No blocked/manual placeholder counts as a
native Assessment. The native policy is a partial automated projection.

Authority: vanderpol/scap-ng#260, owner comment 6510844015. Tooling candidate
lineage a08c9beb9dcf781a726adbdf05676f5ae2e57309; see the publication manifest for
the final exact committed candidate and build-materialization record. The
later release-walkthrough invocation fix does not change corpus conversion.

Reproduce intentionally (not a routine regression), from the exact candidate:

python tools/build_v04_full_draft.py --source-pins source-pins.json \\
  --inputs ORIGINAL_ZIPS --baseline proof-baseline-4258.json \\
  --known-invalid known-invalid-rc.json --output NEW_DIRECTORY --workers 3 \\
  --acknowledge-full-corpus-deliverable

Extract ORIGINAL_ZIPS from each source-preservation folder. Original source
validity for newly admitted drafts and semantic proof remain separate work.
Compatibility warnings do not establish unrestricted all_exist equivalence.
No scanner-runtime, publisher-trust, complete policy/manual migration, licensed
software release or final 0.4.0 publication is claimed. Prior frozen archives
remain immutable; do not relabel this DRAFT by subsequent proof findings.
''')
inventory=[{'path':p.relative_to(PAYLOAD).as_posix(),'bytes':p.stat().st_size,
            'sha256':sha256(p.read_bytes()).hexdigest()}
           for p in sorted(PAYLOAD.rglob('*')) if p.is_file() and p.name!='artifact-files.json']
(PAYLOAD/'artifact-files.json').write_text(json.dumps(inventory,indent=2)+'\n')
target=OUT/'all-65-revised-draft.zip'
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for p in sorted(PAYLOAD.rglob('*')):
        if p.is_file():
            info=zipfile.ZipInfo('all-65-revised-draft/'+p.relative_to(PAYLOAD).as_posix(),date_time=(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    for item in inventory:
        raw=archive.read('all-65-revised-draft/'+item['path'])
        assert len(raw)==item['bytes'] and sha256(raw).hexdigest()==item['sha256']
receipt={'file':target.name,'bytes':target.stat().st_size,'sha256':sha256(target.read_bytes()).hexdigest(),
         'payload_files':len(inventory)+1,'crc':'PASS','every_payload_digest':'PASS'}
(OUT/'draft-archive-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
