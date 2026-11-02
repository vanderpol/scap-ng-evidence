import json,sys,unittest
from pathlib import Path
from test_v04_input_presence import InputPresenceTests

class Recorded(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.methods={};self.subcases={}
    def addSuccess(self,test):
        self.methods[test._testMethodName]='PASS';super().addSuccess(test)
    def addSubTest(self,test,subtest,error):
        self.subcases[subtest.params['case']]='PASS' if error is None else 'FAIL'
        super().addSubTest(test,subtest,error)

run=unittest.TextTestRunner(verbosity=2,resultclass=Recorded).run(unittest.defaultTestLoader.loadTestsFromTestCase(InputPresenceTests))
root=Path('/workspace/scap-ng-owner-contract-268');work=Path('/workspace/input-presence-268-20261101')
design=json.loads((root/'tests/fixtures/v04-input-presence/design-review-vectors.json').read_text())
rows=[]
for i,row in enumerate(design['binding_vectors'],1):
    rows.append({'case':i,'name':row['name'],'status':run.subcases.get(row['name'],'NOT_RUN')})
for i,row in enumerate(design['static_and_scheduling_vectors'],12):
    names=[n for n in run.methods if n.startswith('test_'+str(i)+'_')]
    rows.append({'case':i,'name':row['case'],'status':run.methods[names[0]] if len(names)==1 else 'NOT_RUN'})
assert len(rows)==25
report={'review_cases':rows,'adopted_cases_passed':sum(r['status']=='PASS' for r in rows),'test_methods':run.testsRun,
        'test_method_results':run.methods,'errors':len(run.errors),'failures':len(run.failures),
        'scope':'static public/direct/independent package and supplied-binding harness; not scanner/provider/UI execution'}
(work/'25-case-execution.json').write_text(json.dumps(report,indent=2)+'\n')
raise SystemExit(not run.wasSuccessful() or any(r['status']!='PASS' for r in rows))
