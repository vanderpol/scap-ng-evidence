from pathlib import Path
import os,subprocess,json,time
w=Path('/workspace/freeze-closure-268-20261102');root=Path('/workspace/scap-ng-owner-contract-268');out=w/'owner-boundaries';out.mkdir(exist_ok=True)
scripts=['test_v04_owner_decision_schema_lock.py','test_v04_owner_conditional_plan.py','test_v04_owner_identity_context.py','test_v04_owner_producer_contract.py','test_v04_comparison_types.py','test_v04_native_capability_names.py','test_v04_direct_converter.py','test_v04_variable_result_incomplete.py'];rows=[]
for name in scripts:
 start=time.monotonic()
 with (out/(name+'.log')).open('w') as f:
  r=subprocess.run(['/workspace/.onboarding/venv/bin/python','tools/'+name,'-v'],cwd=root,env={**os.environ,'PYTHONPATH':'tools','PYTHONDONTWRITEBYTECODE':'1'},stdout=f,stderr=subprocess.STDOUT)
 rows.append({'script':'tools/'+name,'exit_code':r.returncode,'seconds':round(time.monotonic()-start,3)});print(rows[-1],flush=True);(w/'owner-boundary-results.json').write_text(json.dumps(rows,indent=2)+'\n')
raise SystemExit(any(r['exit_code'] for r in rows))
