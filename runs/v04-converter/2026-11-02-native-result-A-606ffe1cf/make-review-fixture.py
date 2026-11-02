from pathlib import Path
from hashlib import sha256
import json
from v04_result_contract import project_test_result,pointer,validate_assessment_result
root=Path.cwd(); out=root/'docs/examples/native-results-20261102';out.mkdir(exist_ok=True)
p=root/'docs/examples/owner-contract-20261031/windows-server-2025-shows-on-lock-screen-sv-278080-assessment.json'
doc=json.loads(p.read_text());a=doc['assessment'];test=next(iter(a['tests']));base=['tests',test,'require']
def typed(value,domain):return {'datatype':domain,'status':'exists','value':value}
fields={'type':typed('dword','string'),'value':typed(1,'integer')}
item={'id':'supplied-registry-item','capability':'windows.registry','status':'exists','fields':fields,'provenance':{'source':'synthetic supplied observation for Result contract review; no scanner execution'}}
collections=[{'id':'supplied-registry-collection','capability':'windows.registry','status':'complete','item_refs':[item['id']]}]
rows=[]
for i,name in enumerate(('type','value')):
 ref=pointer(base+['and',i]);rows.append({'require_ref':ref,'outcome':'true','field_results':[{'require_ref':pointer(base+['and',i,'fields',name]),'outcome':'true','observed_values':[fields[name]],'expected_values':[fields[name]],'observation_complete':True}]})
observation={'invocation_ref':'supplied-native-result-review','outcome':'true','items_observed':1,'object_refs':[collections[0]['id']],'item_refs':[item['id']],'per_item_results':[{'item_ref':item['id'],'outcome':'true','item':item,'require_results':[{'require_ref':pointer(base),'outcome':'true','field_results':[],'require_results':rows}]}],'item_summary':{'evaluated_items':1,'observed_mismatches':0,'actual_mismatches':0,'returned_items':1,'truncated_evidence':False}}
result=project_test_result(a,test,observation,collections=collections)
parent={'assessment_result':{'result_schema_version':'0.4.0','execution_id':observation['invocation_ref'],'assessment':{'id':a['id'],'version':a['version']},'purpose':'assessment','class':a['class'],'mode':'automated','outcome':'true','summary':'Supplied synthetic complete registry observation matches source DWORD 1; no scanner executed.','logical_complete':True,'population_complete':True,'evidence_complete':True,'tests':[result],'objects':collections,'variables':[],'diagnostics':[],'target_ref':'synthetic-review-target','expression_execution':{'assessment':a['id'],'invocation_ref':observation['invocation_ref'],'outcome':'true','executed_tests':[test],'trace':[],'diagnostics':[]},'field_uses':[],'dependent_assessments':[],'evidence_retention':{'scope':'per_test','maximum_items':None,'source':'run_request'}}}
validate_assessment_result(a,parent)
for name,value in [('source.assessment.json',doc),('supplied-observations.json',observation),('collections.json',collections),('native.test-result.json',result),('native.assessment-result.json',parent)]:
 (out/name).write_text(json.dumps(value,indent=2)+'\n')
(out/'provenance.json').write_text(json.dumps({'source_path':str(p.relative_to(root)),'source_sha256':sha256(p.read_bytes()).hexdigest(),'source_copy_sha256':sha256((out/'source.assessment.json').read_bytes()).hexdigest(),'rule':'SV-278080','observations':'synthetic supplied unit-review evidence only','scanner_executed':False,'truth_recomputed':False},indent=2)+'\n')
