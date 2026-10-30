"""Assemble exact-SHA candidate evidence without rerunning corpus or CI."""
from datetime import datetime,timezone
from hashlib import sha256
import json
from pathlib import Path
import shutil
import zipfile

ROOT=Path(__file__).resolve().parent
DEST=Path('/workspace/scap-ng-evidence/runs/v04-toolchain/2026-10-30-v040-rc-a5db02e1b')
SHA='a5db02e1b29a2d7c312ddcf593be1ee055afb750'
SAMPLE='b595b490226934a26cd7265b86974904d5db1cce'
DEST.mkdir(parents=True,exist_ok=False)
def copy(source,name=None):
    target=DEST/(name or Path(source).name);shutil.copy2(source,target);return target
source=next((ROOT/'final-toolchain').glob('*.zip'))
replay=next((ROOT/'final-toolchain-replay').glob('*.zip'))
assert source.read_bytes()==replay.read_bytes()
toolchain=copy(source)
gate=json.loads((ROOT/'final-clean-gate/release-gate.json').read_text())
assert gate['status']=='PASS' and gate['extracted'] and len(gate['cases'])==7
lock=Path('/workspace/scap-ng/docs/audit/v04-package-acceptance/requirements-linux-py312.lock')
inventory=json.loads((ROOT/'dependency-inventory.json').read_text());assert inventory['status']=='PASS' and len(inventory['packages'])==11

def archive(path,entries):
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as output:
        for name,raw in sorted(entries.items()):
            item=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));item.compress_type=zipfile.ZIP_DEFLATED
            output.writestr(item,raw,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    with zipfile.ZipFile(path) as result:assert result.testzip() is None

wheels={p.name:p.read_bytes() for p in sorted((ROOT/'wheelhouse').glob('*.whl'))}
wheels['requirements-linux-py312.lock']=lock.read_bytes()
wheels['dependency-inventory.json']=(ROOT/'dependency-inventory.json').read_bytes()
wheels['README.md']=b'''# Offline Linux x86_64 CPython3.12 dependencies

Original unmodified hash-pinned wheels with embedded licenses/notices.
python -m venv /tmp/scap-ng-env
/tmp/scap-ng-env/bin/python -m pip install --no-index --find-links . --require-hashes -r requirements-linux-py312.lock
/tmp/scap-ng-env/bin/python -m pip check

Use with the exact source archive in the candidate decision packet. This is
not a Windows/macOS installation qualification or a project license grant.
'''
deps=DEST/'scap-ng-0.4.0-linux-py312-offline-dependencies.zip';archive(deps,wheels)
evidence={p.relative_to(ROOT/'final-clean-gate').as_posix():p.read_bytes()
          for p in sorted((ROOT/'final-clean-gate').rglob('*')) if p.is_file()}
gatezip=DEST/'clean-extract-seven-case-evidence.zip';archive(gatezip,evidence)
for name in ['dependency-inventory.json','function-contract-audit.json','cohort-recovery.json','branch-audit.json',
             'final-offline-install.log','final-offline-pip-check.log','affected-tests.log','function-boundaries.log',
             'remote-draft-download.log']:
    copy(ROOT/name)
copy(ROOT/'final-clean-gate/release-gate.json')
copy(ROOT/'prepare_candidate_packet.py')
copy(ROOT/'final-toolchain/SHA256SUMS.txt','source-toolchain-SHA256SUMS.txt')
records=[{'file':p.name,'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
         for p in [toolchain,deps,gatezip]]
manifest={'evidence_id':DEST.name,'evidence_kind':'repository/audit evidence; pre-alpha toolchain release candidate',
 'created_utc':datetime.now(timezone.utc).isoformat(),'source_repository':'vanderpol/scap-ng','source_commit':SHA,
 'generator':{'path':'tools/build_versioned_toolchain.py','commit':SHA,
 'command':'python tools/build_versioned_toolchain.py --version 0.4.0 --ref '+SHA+' --output-dir NEW_DIRECTORY'},
 'gate_command':'python tools/audit_v04_release_candidate.py --require-extracted --output NEW_DIRECTORY',
 'external_inputs':{'originals':'Source ZIPs/provenance embedded in exact source snapshot; corpus pins in adjacent v04-converter run',
                    'dependency_lock_sha256':sha256(lock.read_bytes()).hexdigest(),'dependency_inventory':'dependency-inventory.json'},
 'artifacts':records,'validation_status':'Local clean-extract/offline/independent CLI PASS; exact-SHA maintained CI pending receipt',
 'checks':['Exact-ref deterministic source archive replay','6783 committed source files inventoried by manifest',
 'Fresh offline hash-pinned installation of 11 dependencies','pip check PASS','7 original-source/warning/negative CLI cases PASS',
 'Independent package reader compares JSON/YAML and compiled references/program operands','All 4258 accepted corpus proof hashes retained',
 'Remote DRAFT download reassembly SHA256 PASS'],
 'draft_counts':{'CONVERTED_VERIFIED':4258,'CONVERTED_UNVERIFIED':2559,'BLOCKED':422,'MANUAL_OCIL_ONLY_PRESERVED':1653},
 'samples':{'repository':'vanderpol/scap-ng-editor-sample-data','commit':SAMPLE,'path':'focused-fixtures/v04-release-candidate-a5db02e1b','cases':5,'file_hashes_checked':54,'json_yaml_pairs':22},
 'publication_scope':'Candidate evidence only; final 0.4.0 release/tag requires owner approval',
 'storage_decision':'Owner requires reviewable downloadable exact-SHA candidate. uploads.github.com denied release assets with HTTP401; Git push works. Bounded fallback retains source/wheelhouse/evidence ZIPs here, with full file/license/hash inventories; no final release or corpus duplication.',
 'limitations':['No scanner runtime evidence','New draft compatibility/function/Input parity independently unproved',
 'Partial native policy/applicability/manual migration','Publisher trust NOT_VERIFIED','Linux x86_64 Python3.12 environment only',
 'Project source/specification license UNDECLARED; owner replied unsure; no license grant fabricated']}
(DEST/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(records,indent=2))
