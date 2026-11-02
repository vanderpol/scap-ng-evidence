"""Bounded 0.4 language/result-contract readiness, separate from runtime qualification.

Read-only: no corpus generation, proof rebaseline, freeze or release. Refs #255.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import urljoin

from jsonschema import Draft202012Validator
from referencing import Registry
from v04_object_contract import resources

ROOT = Path(__file__).resolve().parents[1]


def audit(root=ROOT):
    directory = root/'schema/v0.4.0'
    store = resources(str(directory))
    registry = Registry().with_resources(store.items())
    closure_errors, references, schemas = [], 0, []
    def walk(value, base, path):
        nonlocal references
        if isinstance(value, dict):
            if '$ref' in value:
                references += 1
                ref=value['$ref']
                try:
                    target=urljoin(base,ref)
                    if '/schema/v' in target and '/schema/v0.4.0/' not in target:
                        raise ValueError('cross-version normative reference')
                    registry.resolver(base).lookup(ref)
                except Exception as error:
                    closure_errors.append({'schema':base,'pointer':path,'reference':ref,'error':str(error)})
            for key,child in value.items():walk(child,base,path+'/'+key)
        elif isinstance(value,list):
            for i,child in enumerate(value):walk(child,base,path+'/'+str(i))
    for path in sorted(directory.glob('*.schema.json')):
        schema=json.loads(path.read_text());Draft202012Validator.check_schema(schema)
        if schema.get('x-scap-ng-version')!='0.4.0' or not schema.get('x-last-modified'):
            closure_errors.append({'schema':path.name,'error':'missing version/date metadata'})
        walk(schema,schema.get('$id','https://scap-ng.dev/schema/v0.4.0/'+path.name),'')
        schemas.append({'path':str(path.relative_to(root)),'sha256':sha256(path.read_bytes()).hexdigest()})
    legacy={'id':'registry-value-test','outcome':'error','object_refs':[],
            'state_refs':['registry-value-test.states[0]'],'item_refs':[],'per_item_results':[],
            'item_summary':{'evaluated_items':0,'observed_mismatches':0,'actual_mismatches':'unknown',
                            'returned_items':0,'truncated_evidence':False},
            'check_existence':'all_exist','check':'all','state_operator':'AND'}
    test_schema=json.loads((directory/'test-result.schema.json').read_text())
    errors=list(Draft202012Validator(test_schema,registry=registry).iter_errors(legacy))
    from audit_v04_selector_contracts import audit as selector_audit
    selector_contracts=selector_audit(root)
    missing=selector_contracts['errors']
    # Probe a real source-backed native sample plus independent negative mutations.
    # Outcomes/observations are supplied review evidence, never scanner execution.
    from copy import deepcopy
    from v04_result_contract import validate_assessment_result
    from jsonschema import ValidationError
    example=root/'docs/examples/native-results-20261102'
    source=json.loads((example/'source.assessment.json').read_text())['assessment']
    native=json.loads((example/'native.assessment-result.json').read_text())
    probes=[]
    try:
        validate_assessment_result(source,native)
        probes.append({'case':'source-backed-native-positive','passed':True})
    except (ValueError,ValidationError) as error:
        probes.append({'case':'source-backed-native-positive','passed':False,'error':str(error)})
    mutations={
        'legacy-wire':lambda r:r['tests'][0].update({'state_refs':['test.states[0]']}),
        'foreign-invocation':lambda r:r['tests'][0].update({'invocation_ref':'other'}),
        'missing-error-reason':lambda r:r['tests'][0].update({'outcome':'error'}),
        'pseudo-source-location':lambda r:r['tests'][0]['require_refs'].append('/tests/missing/require'),
        'wrong-native-control':lambda r:r['tests'][0].update({'items_found':'none'}),
        'wrong-source-operand':lambda r:r['tests'][0]['per_item_results'][0]['require_results'][0]['require_results'][1]['field_results'][0]['expected_values'][0].update({'value':2}),
    }
    for case,mutate in mutations.items():
        bad=deepcopy(native);mutate(bad['assessment_result'])
        try:
            validate_assessment_result(source,bad)
            probes.append({'case':case,'passed':False})
        except (ValueError,ValidationError):probes.append({'case':case,'passed':True})
    closed=bool(errors) and all(row['passed'] for row in probes)
    contracts=[{'id':'LC-SELECTOR-CASE','status':'OPEN' if missing else 'CLOSED',
        'owner_decision_needed':False,'decision':22,'evidence':missing,
        'contract_audit':selector_contracts,
        'problem':'All15 per-capability contracts and42 fields are documented against primary references, including target/API-dependent cases; native collector behavior remains future verification.',
        'next_action':'Qualify real providers against these fixed contracts; no universal case switch or undocumented alias.'},
        {'id':'LC-NATIVE-RESULTS','status':'CLOSED' if closed else 'REVIEW_REQUIRED',
         'owner_decision_needed':False,'decisions':[9,17,19,20,24],
         'owner_adoption':'A, 2026-11-02; issue255 comment6566907992',
         'legacy_counterexample':legacy,'legacy_rejected':bool(errors),
         'boundary_probes':probes,
         'problem':'Native Result A adopted and implemented with source-bound require pointers, controls, record correlation and explicit reason/evidence.',
         'next_action':'Maintain bounded semantic tests; actual scanner execution remains future verification.'}]
    decisions=[]
    owner=(root/'docs/audit/v04-owner-final-decisions-20261031.md').read_text()
    for number,rule in re.findall(r'^\| (\d+) \| (.*?) \|',owner,re.M):
        number=int(number)
        linked=[c['id'] for c in contracts if c['status']!='CLOSED' and (number==c.get('decision') or number in c.get('decisions',[]))]
        decisions.append({'decision':number,'approved_rule':rule,'language_contract_blockers':linked,
            'contract_verification': 'Current maintained schema/authoring/compiler boundaries plus separately recorded exact-commit owner-boundary suite; not scanner execution',
            'language_contract_status':'OPEN' if linked else 'CLOSED',
            'presence_surface':'implemented and independently read in program0.2' if number in (15,16) else None,
            'future_verification': ('native collector/invocation/array/error behavior' if number in (9,15,16,17,19,20) else
                                    'VS Code host/save/UI/traversal' if number in (7,27,28) else
                                    'live API lookup/case behavior' if number==22 else
                                    'complete Rule/manual follow-up report with observed target evidence' if number==24 else None)})
    if len(decisions)!=29:raise ValueError('owner decision inventory drift')
    matrix=json.loads((root/'docs/audit/v04-final-decision-verification-20261102.json').read_text())
    if len(matrix['decisions'])!=29 or {r['decision'] for r in matrix['decisions']}!=set(range(1,30)):
        raise ValueError('independent decision verification matrix drift')
    adopted={r['decision']:r['approved_rule'] for r in decisions}
    for row in matrix['decisions']:
        if row['adopted_rule']!=adopted[row['decision']] or row['contract_status']!='CLOSED':
            raise ValueError('stale or incomplete adopted-decision contract matrix')
        if not all((root/path).is_file() for path in row['boundary_suites']):
            raise ValueError('missing decision boundary suite')
    for row in decisions:
        row['boundary_suites']=next(r['boundary_suites'] for r in matrix['decisions'] if r['decision']==row['decision'])
    return {'format':'scap-ng/schema-freeze-readiness/1','scope':'full version-local source and Result schema family; no freeze action',
        'schema_freeze_readiness':'NO_GO' if closure_errors or any(c['status']!='CLOSED' for c in contracts) else 'READY_FOR_OWNER_REVIEW',
        'input_presence_contract':'IMPLEMENTED; supplied binding/result evidence, not scanner execution',
        'field_datatype':'RETAINED_COMPATIBLE; global retirement is outside task and not a blocker under that decision',
        'schemas':schemas,'schema_count':len(schemas),'references_checked':references,'reference_errors':closure_errors,
        'capability_contracts':len(list((directory/'capability-mappings/supported').glob('*.json'))),
        'language_contract_findings':contracts,'decisions':decisions,
        'future_scanner_verification':['real provision/provider and dependency binding adapters','collection completeness/error versus absence',
            'array/Variable/Set execution and cache isolation','selector APIs on supported target platforms','Rule follow-up with actual observed evidence'],
        'future_editor_verification':['TextDocument/WorkspaceEdit/undo and real save serialization','Structured/Guided UI, screenshot evidence and regex/sample playground'],
        'preserved_boundaries':['draft PR268','no merge/freeze/tag/release','no65-stream generation','no proof rebaseline','historical schemas and source archives unchanged']}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():parser.error('refuse to overwrite existing audit')
    result=audit();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('schema_freeze_readiness','schema_count','references_checked','reference_errors')}))
