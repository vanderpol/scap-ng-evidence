"""Complete generated navigation metadata; verify accepted content unchanged."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys
import zipfile

import yaml

sys.path.insert(0,'/workspace/scap-ng/tools')
from scap_ng_library.export import original_stream_title,DRAFT_SHA

ROOT=Path(__file__).resolve().parent
SOURCE=Path('/workspace/rc-v040-20261029/all-65-draft')
OUTPUT=ROOT/'normalized-all65'
ARCHIVE=Path('/workspace/rc-v040-20261029/remote-verified-all-65-revised-draft.zip')
assert sha256(ARCHIVE.read_bytes()).hexdigest()==DRAFT_SHA
with zipfile.ZipFile(ARCHIVE) as archive:
    frozen={r['path']:r for r in json.loads(archive.read('all-65-revised-draft/artifact-files.json'))}
    baseline=json.loads(archive.read('all-65-revised-draft/proof-baseline-4258.json'))['records']
def checked(path):
    raw=path.read_bytes();item=frozen[path.relative_to(SOURCE).as_posix()]
    assert sha256(raw).hexdigest()==item['sha256'] and len(raw)==item['bytes'];return raw
catalog_path=OUTPUT/'content/catalog.yaml';catalog=yaml.safe_load(catalog_path.read_text())
retained=set();totals=Counter();non_native=[]
for entry in catalog['benchmarks']:
    record=json.load(open(OUTPUT/'records/streams'/(entry['scope']+'.json')))
    ledger=record['original_ledger'];rows=ledger['rules'];counts=Counter(r['conversion_status'] for r in rows)
    totals.update(counts);entry['conversion_statuses']=dict(counts)
    if entry['native_benchmark_id'] is None:
        entry['title']=original_stream_title(SOURCE/record['source_stream'],ledger,checked)
        non_native.append({'scope':entry['scope'],'title':entry['title'],'original_rules':len(rows),'conversion_statuses':dict(counts)})
    for row in rows:
        key=ledger['original_zip']['file']+'!'+row['source_rule']
        if row['conversion_status']=='CONVERTED_VERIFIED':
            prior=baseline[key]
            assert all(row[k]==prior[k] for k in ['source_rule_sha256','authoring_sha256','program_sha256'])
            retained.add(key)
assert retained==set(baseline)
catalog_path.write_text(yaml.safe_dump(catalog,sort_keys=False,allow_unicode=True))
inventory=json.load(open(OUTPUT/'metadata/native-files.json'));changed_bytes=0
for item in inventory:
    assert sha256((OUTPUT/'content'/item['path']).read_bytes()).hexdigest()==item['yaml_sha256']
    changed_bytes += item['yaml_sha256']!=frozen[item['source_path']]['sha256']
receipt={'status':'PASS','original_rule_statuses':dict(totals),'retained_frozen_proof_pairs':len(retained),
    'native_files':len(inventory),'native_yaml_bytes_changed':changed_bytes,
    'original_only_streams':non_native,'catalog_enrichment':'Generated title/status metadata only; no native payload/ref/program mutation',
    'full_source_conversion_or_oval_proof_replay':False}
(ROOT/'acceptance-preservation.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
