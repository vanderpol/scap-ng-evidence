import argparse,json
from pathlib import Path
from verify_v04_direct_scope import accept_source
p=argparse.ArgumentParser();p.add_argument('--inputs',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
records=json.loads(Path(__file__).with_name('summary.json').read_text())['records']
sources={r['source']['file']:r['source'] for r in records}
for file,pin in sources.items():
    ids=[r['rule'] for r in records if r['source']['file']==file]
    report=accept_source(a.inputs/file,pin['sha256'],a.output/Path(file).stem,rule_ids=ids)
    assert sum(r['outcome']=='PROVED' for r in report['cases'])==len(ids)
