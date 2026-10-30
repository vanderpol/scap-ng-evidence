from datetime import datetime,timezone
from hashlib import sha256
import gzip
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parent
SOURCE='a08c9beb9dcf781a726adbdf05676f5ae2e57309'
TAG='v04-revised-all65-draft-20261030-a08c9beb9'
DEST=Path('/workspace/scap-ng-evidence/runs/v04-converter/2026-10-30-all-65-revised-draft-rc')
DEST.mkdir(exist_ok=False)
payload=ROOT/'all-65-draft'
receipt=json.loads((ROOT/'publication/draft-archive-receipt.json').read_text())
base='https://github.com/vanderpol/scap-ng-evidence/releases/download/'+TAG+'/'
summary=json.loads((payload/'summary.json').read_text())
frozen=[]
for path,digest in [
 ('2026-10-28-niwc-65-draft-248895772/niwc-65-draft-248895772.zip','5f86d016c1bce82018eec82c6468ab583816ff0b38c8d3ea5e9210a931cc1a08'),
 ('2026-10-29-all-65-complete-draft-stage-one/all-65-complete-draft.zip','5338f760dbc043f6302bc7d65e65a130281c22549f9ea34f2a4e51f4921ff18c')]:
 p=DEST.parent/path
 assert sha256(p.read_bytes()).hexdigest()==digest
 frozen.append({'path':path,'sha256':digest,'unchanged':'PASS'})
manifest={'evidence_id':DEST.name,'evidence_kind':'production migration evidence; UNVERIFIED DRAFT',
 'created_utc':datetime.now(timezone.utc).isoformat(),'source_repository':'vanderpol/scap-ng',
 'source_commit':SOURCE,'generator':{'path':'tools/build_v04_full_draft.py','commit':SOURCE,
 'command':'python tools/build_v04_full_draft.py --source-pins source-pins.json --inputs ORIGINAL_ZIPS --baseline proof-baseline-4258.json --known-invalid known-invalid-rc.json --output NEW_DIRECTORY --workers 3 --acknowledge-full-corpus-deliverable',
 'materialization':'Completed once from candidate working code before commit. Subsequent int32 substring boundary guard audited over all emitted canonical subtrees; no authoring/program change. Release-gate invocation corrections are separate from converter output.'},
 'external_inputs':{'pins':'source-pins.json','proof_baseline':'proof-baseline-4258.json inside archive','known_exclusions':'known-invalid-rc.json inside archive'},
 'output':receipt,'archive_url':base+receipt['file'],'draft_evidence_tag':TAG,
 'conversion_statuses':summary['conversion_statuses'],'overlapping_warning_rules':summary['overlapping_warning_rules'],
 'compiled_native_candidates':6817,'preservation':frozen,'validation_status':'PASS original preservation/accounting/schema/compilation/accepted hash retention; new semantic proof UNPROVED',
 'checks':summary['checks']+['Archive CRC and every expanded payload digest checked','6817 compiled candidates','Canonical function subtrees match committed migration contract'],
 'limitations':summary['limitations']+['No project-wide source/specification license declared; owner decision pending','Not a final 0.4.0 release or scanner-runtime equivalence claim'],
 'storage_decision':'Compressed DRAFT is a prerelease asset, not ordinary Git payload; required external owner review of complete preserved originals/native drafts. Exact payload inventory retained compressed and embedded. Prior archives unchanged.',
 'output_root':'all-65-revised-draft/','output_files':receipt['payload_files']}
(DEST/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
readme=f'''# Revised complete all-65 DRAFT — NOT VERIFIED FOR EXECUTION

[Download the complete original-preserving DRAFT ZIP]({base}{receipt['file']})
({receipt['bytes']:,} bytes). SHA-256:
`{receipt['sha256']}`

Extract and open `index.html`. The archive contains all 65 original signed ZIPs,
8,892 original Rules, all native YAML/JSON, Rule ledgers, dependency/provenance
traces and the 4,258-proof hash baseline. Manual and blocked originals are
preserved; no placeholder counts as native conversion.

| Disjoint outcome | Rules |
| --- | ---: |
| CONVERTED_VERIFIED (retained static source proofs) | 4,258 |
| CONVERTED_UNVERIFIED | 2,559 |
| BLOCKED automated | 422 |
| Manual/OCIL preserved | 1,653 |
| Total | 8,892 |

All 6,817 native candidates compile. All 4,258 accepted hash pairs remain
unchanged. Independent new source proof and scanner-runtime qualification are
separate; warnings do not imply production equivalence. Of the old primary
blocker cohorts, 980/992 catalog, 1,181/1,184 all_exist, 338/381 import/export
and 30/30 aggregation now convert as unverified drafts. These cohort counts
are separate from overlapping warning counts in summary.json.

See cohort-recovery.json for every remaining cohort diagnostic; source-pins.json
for original revision/bytes/digests; artifact-files.json.gz (and the inventory
inside the archive) for every expanded payload path/size/hash. Decompress with
`python -m gzip -d artifact-files.json.gz` on a copy. The archive checksum binds
its embedded inventory as well. Local archive CRC and every payload digest PASS.

Generator lineage: vanderpol/scap-ng `{SOURCE}`. Original source was not repaired,
and no schema/compiler/scanner contract changed. Exact final toolchain candidate,
clean-extract and CI decision packet are tracked separately under
[source #260](https://github.com/vanderpol/scap-ng/issues/260).
No final release/tag is authorized. Source/specification licensing is undecided;
all original and dependency notices remain intact.
'''
(DEST/'README.md').write_text(readme)
(ROOT/'draft-release-body.md').write_text(readme)
for name in ['summary.json','source-pins.json']:
 shutil.copy2(payload/name,DEST/name)
for name in ['cohort-recovery.json','function-contract-audit.json','package_rc_draft.py','prepare_draft_publication.py']:
 shutil.copy2(ROOT/name,DEST/name)
(DEST/'artifact-files.json.gz').write_bytes(gzip.compress((payload/'artifact-files.json').read_bytes(),mtime=0))
(DEST/'STORAGE-DECISION.md').write_text('Owner explicitly requires complete downloadable original-preserving DRAFT review under vanderpol/scap-ng#260. Store the 108 MB archive as a clearly labeled prerelease asset on scap-ng-evidence, not ordinary Git. Retain compact findings, provenance, manifest and compressed complete payload inventory in Git. This is draft content evidence, not final SCAP-NG 0.4.0 publication. Previous immutable archives and accepted proof hashes are untouched.\n')
(DEST/'SHA256SUMS').write_text(''.join(sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in sorted(DEST.iterdir()) if p.is_file() and p.name!='SHA256SUMS'))
print(DEST)
