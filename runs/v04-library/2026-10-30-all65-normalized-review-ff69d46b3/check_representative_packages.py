from hashlib import sha256
import json
from pathlib import Path
import sys
import time

sys.path.insert(0,'/workspace/scap-ng/tools')
from scap_ng_library.index import Library
from scap_ng_library.documents import parse,read
from verify_v04_package_consumer import verify

ROOT=Path(__file__).resolve().parent
library=Library(ROOT/'normalized-all65/content')
output=ROOT/'representative-packages';output.mkdir(exist_ok=True)
reports=[]
try:
    for name,query in [('linux','Red Hat Enterprise Linux 9'),('windows','Windows Server 2025')]:
        matches=library.search(kind='benchmark',query=query,limit=2)
        assert len(matches)==1,(query,matches)
        scope=matches[0]['scope'];started=time.perf_counter()
        raw,manifest=library.compile_scope(scope)
        package=output/(name+'.scapng');package.write_bytes(raw)
        external={}
        for row in library.rows("WHERE scope IN (?, 'shared')",(scope,)):
            doc=parse(read(library.root,row['path']))
            folder='shared' if row['scope']=='shared' else 'library'
            external[(row['kind'],row['id'])]=('authoring/'+folder+'/'+row['path'],doc)
        checked=verify(package,source=external)
        assert checked['status']=='INDEPENDENT_PACKAGE_CONSUMER_PASS'
        for a in library.rows("WHERE kind='assessment' AND scope=?",(scope,)):
            if a['mode']=='automated':assert manifest['build_provenance']['compiled_programs'][a['id']]['sha256']==a['program_sha']
        reports.append({'scope':scope,'name':name,'seconds':time.perf_counter()-started,
            'package_sha256':sha256(raw).hexdigest(),'independent_consumer':checked,
            'unchanged_program_hashes':len(manifest['build_provenance']['compiled_programs'])})
finally:library.close()
(output/'report.json').write_text(json.dumps({'status':'PASS','cases':reports,'new_source_proofs':0,'scanner_evaluated':False},indent=2)+'\n')
print(json.dumps(reports,indent=2))
