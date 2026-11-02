import json,os,subprocess,time
from pathlib import Path
root=Path('/workspace/scap-ng-owner-contract-268')
work=Path('/workspace/freeze-closure-268-20261102')
scripts=json.loads((work/'maintained-scripts.json').read_text())
logs=work/'maintained';logs.mkdir(exist_ok=True)
results=[]
for script in scripts:
    start=time.monotonic()
    with (logs/(Path(script).stem+'.log')).open('w') as stream:
        run=subprocess.run(['/workspace/.onboarding/venv/bin/python',script],cwd=root,
            env={**os.environ,'PYTHONPATH':'tools:.','PYTHONDONTWRITEBYTECODE':'1',
                 'SCAP_NG_251_OUTPUT_DIR':str(work/'approved-pipeline')},stdout=stream,stderr=subprocess.STDOUT)
    row={'script':script,'exit_code':run.returncode,'seconds':round(time.monotonic()-start,3)}
    results.append(row)
    (work/'maintained-results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(row),flush=True)
raise SystemExit(any(r['exit_code'] for r in results))
