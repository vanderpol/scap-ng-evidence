from pathlib import Path
from hashlib import sha256
import json,zipfile
w=Path('/workspace/native-results-268-20261102');expected=json.loads((w/'archive-receipt.json').read_text());archive=w/'published-download.zip';raw=archive.read_bytes()
assert len(raw)==expected['bytes'] and sha256(raw).hexdigest()==expected['sha256']
extract=w/'published-fresh-extraction';assert not extract.exists();extract.mkdir()
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 manifest=json.loads(z.read('PAYLOAD-MANIFEST.json'));rows=manifest['payloads']
 assert len(z.namelist())==expected['zip_members'] and len(rows)==expected['payloads']
 assert set(z.namelist())=={r['path'] for r in rows}|{'PAYLOAD-MANIFEST.json'}
 for r in rows:
  assert not Path(r['path']).is_absolute() and '..' not in Path(r['path']).parts
  data=z.read(r['path']);assert len(data)==r['bytes'] and sha256(data).hexdigest()==r['sha256']
 z.extractall(extract)
receipt={**expected,'evidence_commit':(w/'evidence-commit.txt').read_text().strip(),'download':'immutable raw.githubusercontent.com commit URL','archive_hash_valid':True,'crc_valid':True,'exact_inventory_valid':True,'all_payload_hashes_valid':True,'fresh_extraction':True}
(w/'download-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
