"""Native Result A: source paths, inheritance, correlation and honest evidence.

Supplied observations only; no collector, comparator or scanner execution.
Refs #255 #269.
"""
from copy import deepcopy
import json
from pathlib import Path
import unittest
from jsonschema import ValidationError

from test_v04_comparison_types import linux
from v04_result_contract import (pointer,resolve,require_inventory,project_test_result,
                                validate_test_result,validate_assessment_result,validator)

ROOT=Path(__file__).resolve().parents[1]
TEST='registry-value-test'
INV='supplied-result-invocation'


def typed(value,datatype='integer'):
    return {'datatype':datatype,'status':'exists','value':value}


def fixture(predicate=None):
    source=linux(predicate or {'equals':0})
    path=pointer(['tests',TEST,'require','fields','owner_uid'])
    item={'id':'file-item','capability':'unix.file','status':'exists',
          'fields':{'owner_uid':typed(0)},'provenance':{'source':'supplied unit observation'}}
    collections=[{'id':'file-collection','capability':'unix.file','status':'complete','item_refs':['file-item']}]
    evidence={'invocation_ref':INV,'outcome':'true','items_observed':1,'object_refs':['file-collection'],
        'item_refs':['file-item'],'per_item_results':[{'item_ref':'file-item','outcome':'true','item':item,
            'require_results':[{'require_ref':pointer(['tests',TEST,'require']),'outcome':'true',
                'field_results':[{'require_ref':path,'outcome':'true','observed_values':[typed(0)],
                                  'expected_values':[typed(0)],'observation_complete':True}]}]}],
        'item_summary':{'evaluated_items':1,'observed_mismatches':0,'actual_mismatches':0,
                        'returned_items':1,'truncated_evidence':False}}
    return source,evidence,collections


def field(result):return result['per_item_results'][0]['require_results'][0]['field_results'][0]


class NativeResultContract(unittest.TestCase):
    def test_source_backed_assessment_parent_identity_and_native_children(self):
        folder=ROOT/'docs/examples/native-results-20261102'
        source=json.loads((folder/'source.assessment.json').read_text())['assessment']
        result=json.loads((folder/'native.assessment-result.json').read_text())
        validate_assessment_result(source,result)
        for mutate in (
            lambda r:r['assessment'].update({'id':'foreign'}),
            lambda r:r['tests'][0].update({'invocation_ref':'foreign'}),
            lambda r:r['tests'].append(deepcopy(r['tests'][0])),
        ):
            bad=deepcopy(result);mutate(bad['assessment_result'])
            with self.assertRaises(ValueError):validate_assessment_result(source,bad)

    def test_native_projection_attaches_only_source_metadata_and_preserves_inputs(self):
        source,evidence,collections=fixture();before=deepcopy((source,evidence,collections))
        result=project_test_result(source,TEST,evidence,collections=collections)
        self.assertEqual((source,evidence,collections),before)
        self.assertEqual(result['items_found'],'one_or_more');self.assertEqual(result['items_satisfying'],'every')
        self.assertEqual(field(result)['values_matching'],'every')
        self.assertEqual(field(result)['requirement_ref'],pointer(['tests',TEST,'require','field_requirement']))
        self.assertEqual(resolve(source,field(result)['require_ref']),{'equals':0})
        report=validate_test_result(source,result,collections=collections)
        self.assertFalse(report['truth_recomputed']);self.assertFalse(report['scanner_executed'])

    def test_missing_outcome_counts_or_items_never_acquire_defaults(self):
        for key in ('outcome','invocation_ref','item_summary','per_item_results'):
            source,evidence,collections=fixture();del evidence[key]
            with self.subTest(key=key),self.assertRaises((ValueError,ValidationError)):
                project_test_result(source,TEST,evidence,collections=collections)

    def test_old_test_state_entity_wire_rejects_without_conversion(self):
        old={'id':TEST,'outcome':'error','object_refs':[],'state_refs':[TEST+'.states[0]'],
             'item_refs':[],'per_item_results':[],'item_summary':{'evaluated_items':0,'observed_mismatches':0,
                 'actual_mismatches':'unknown','returned_items':0,'truncated_evidence':False},'check_existence':'all_exist','check':'all','state_operator':'AND'}
        self.assertTrue(list(validator('test-result.schema.json').iter_errors(old)))
        for name,payload in [('state-result.schema.json',{'state_ref':TEST+'.states[0]','outcome':'true','entity_results':[]}),
                             ('entity-result.schema.json',{'entity':'owner_uid','outcome':'true','entity_check':'all','var_check':'all'})]:
            self.assertTrue(list(validator(name).iter_errors(payload)))

    def test_legacy_resource_uris_accept_only_current_native_shapes(self):
        source,evidence,collections=fixture();result=project_test_result(source,TEST,evidence,collections=collections)
        row=result['per_item_results'][0]['require_results'][0]
        self.assertEqual(list(validator('state-result.schema.json').iter_errors(row)),[])
        self.assertEqual(list(validator('entity-result.schema.json').iter_errors(field(result))),[])

    def test_pointer_spelling_missing_nodes_and_foreign_test_reject(self):
        source,evidence,collections=fixture();result=project_test_result(source,TEST,evidence,collections=collections)
        for bad in ['#/tests/x/require','/tests/foreign-test/require','/tests/'+TEST+'/require/fields/nope',
                    '/tests/'+TEST+'/require/fields/owner_uid/equals']:
            changed=deepcopy(result);field(changed)['require_ref']=bad
            with self.subTest(pointer=bad),self.assertRaises((ValueError,ValidationError)):validate_test_result(source,changed,collections=collections)
        for bad in ['/a~2b','/rows/01','/rows/-','/rows/99']:
            with self.assertRaises(ValueError):resolve({'rows':[1]},bad)

    def test_nearest_complete_group_and_field_pairs_win(self):
        source,evidence,collections=fixture();req=source['tests'][TEST]['require'];req.pop('fields')
        req['and']=[{'field_requirement':{'values_found':'zero_or_more','values_matching':'every'},
                     'fields':{'owner_uid':{'equals':0}}},
                    {'fields':{'owner_uid':{'equals':0,'values_found':'exactly_one','values_matching':'one_or_more'}}}]
        evidence['per_item_results'][0]['require_results']=[{'require_ref':pointer(['tests',TEST,'require','and',i]),
            'outcome':'true','field_results':[{'require_ref':pointer(['tests',TEST,'require','and',i,'fields','owner_uid']),
                'outcome':'true','observed_values':[typed(0)],'expected_values':[typed(0)],'observation_complete':True}]} for i in range(2)]
        result=project_test_result(source,TEST,evidence,collections=collections)
        first,second=result['per_item_results'][0]['require_results']
        self.assertEqual(first['field_results'][0]['values_found'],'zero_or_more')
        self.assertTrue(first['field_results'][0]['requirement_ref'].endswith('/field_requirement'))
        self.assertEqual(second['field_results'][0]['values_matching'],'one_or_more')
        self.assertTrue(second['field_results'][0]['requirement_ref'].endswith('/fields/owner_uid'))
        second['field_results'][0]['values_matching']='every'
        with self.assertRaises(ValueError):validate_test_result(source,result,collections=collections)

    def test_all_native_logical_operators_and_duplicate_positions_are_distinct(self):
        for operator in ('and','or','one','xor'):
            source,evidence,collections=fixture();req=source['tests'][TEST]['require'];child={'fields':req.pop('fields')}
            req[operator]=[deepcopy(child),deepcopy(child)]
            inventory=require_inventory(source,TEST)
            self.assertIn(pointer(['tests',TEST,'require',operator,0,'fields','owner_uid']),inventory)
            self.assertIn(pointer(['tests',TEST,'require',operator,1,'fields','owner_uid']),inventory)
            evidence['per_item_results'][0]['require_results'][0]['field_results']=[]
            result=project_test_result(source,TEST,evidence,collections=collections)
            self.assertEqual(result['per_item_results'][0]['require_results'][0]['operator'],operator)
            result['per_item_results'][0]['require_results'][0]['operator']='AND'
            with self.assertRaises((ValueError,ValidationError)):validate_test_result(source,result,collections=collections)

    def test_incomplete_and_error_need_reason_diagnostics_and_test_evidence(self):
        for status in ('incomplete','error'):
            source,evidence,collections=fixture();collections[0].update(status=status)
            with self.assertRaises((ValueError,ValidationError)):project_test_result(source,TEST,evidence,collections=collections)
            collections[0].update(stop_reason='Collection interrupted',diagnostics=[{'code':'provider-failure','message':'Explicit supplied failure'}])
            if status=='incomplete':collections[0]['population_complete']=False
            with self.assertRaises(ValueError):project_test_result(source,TEST,evidence,collections=collections)
            evidence.update(outcome='error',reason='Collection interrupted',evidence_refs=['file-collection'])
            result=project_test_result(source,TEST,evidence,collections=collections)
            self.assertEqual(result['outcome'],'error')
            result.pop('reason')
            with self.assertRaises((ValueError,ValidationError)):validate_test_result(source,result,collections=collections)

    def test_field_absence_is_not_failed_incomplete_or_capped_observation(self):
        source,evidence,collections=fixture({'values_found':'none'})
        evidence['per_item_results'][0]['item']['fields']={}
        f=field(evidence);f.pop('expected_values');f['observed_values']=[]
        result=project_test_result(source,TEST,evidence,collections=collections)
        self.assertNotIn('operation',field(result));self.assertNotIn('values_matching',field(result))
        for mutation in ('incomplete','item-error','value-error','present'):
            changed=deepcopy(result)
            if mutation=='incomplete':field(changed)['observation_complete']=False
            elif mutation=='item-error':changed['per_item_results'][0]['item']['status']='error'
            else:changed['per_item_results'][0]['item']['fields']['owner_uid']=(typed(0) if mutation=='present' else {'datatype':'integer','status':'error'})
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):validate_test_result(source,changed,collections=collections)

    def record_fixture(self):
        source,evidence,collections=fixture();test=source['tests'][TEST]
        test.update(capability='windows.wmi.query',object={'namespace':'ROOT\\CIMV2','query':'SELECT Value FROM Example'})
        test['require']['fields']={'result':{'record':{'records_found':'one_or_more','records_matching':'every',
            'fields':{'a/b~c':{'equals':'first'}}}}}
        item=evidence['per_item_results'][0]['item'];item['capability']='windows.wmi.query'
        collections[0]['capability']='windows.wmi.query'
        item['fields']={'result':[{'datatype':'record','status':'exists','value':{'a/b~c':typed(value,'string')}} for value in ['first','second']]}
        root=['tests',TEST,'require'];body=root+['fields','result','record'];member=body+['fields','a/b~c']
        evidence['per_item_results'][0]['require_results']=[{'require_ref':pointer(body),'record_ref':'/fields/result/'+str(i),
            'outcome':'true','field_results':[{'require_ref':pointer(member),'record_ref':'/fields/result/'+str(i),
                'outcome':'true','observed_values':[typed(value,'string')],'expected_values':[typed('first','string')],
                'observation_complete':True}]} for i,value in enumerate(['first','second'])]
        return source,evidence,collections

    def test_record_absence_requires_explicit_complete_observation(self):
        source,evidence,collections=self.record_fixture()
        source['tests'][TEST]['require']['fields']['result']['record']={'records_found':'none'}
        row={'require_ref':pointer(['tests',TEST,'require','fields','result','record']),
             'outcome':'true','field_results':[],'observation_complete':True}
        evidence['per_item_results'][0]['require_results']=[row]
        evidence['per_item_results'][0]['item']['fields']={}
        project_test_result(source,TEST,evidence,collections=collections)
        for raw in (typed('failed'),{'datatype':'record','status':'error'},
                    {'datatype':'record','status':'exists','value':{}}):
            bad=deepcopy(evidence);bad['per_item_results'][0]['item']['fields']['result']=raw
            with self.assertRaises((ValueError,ValidationError)):
                project_test_result(source,TEST,bad,collections=collections)
        for complete in (False,None):
            bad=deepcopy(evidence);bad['per_item_results'][0]['require_results'][0]['observation_complete']=complete
            with self.assertRaises((ValueError,ValidationError)):
                project_test_result(source,TEST,bad,collections=collections)

    def test_escaped_dynamic_members_and_multiple_record_instances_remain_correlated(self):
        source,evidence,collections=self.record_fixture();result=project_test_result(source,TEST,evidence,collections=collections)
        rows=result['per_item_results'][0]['require_results']
        self.assertTrue(rows[0]['field_results'][0]['require_ref'].endswith('a~1b~0c'))
        self.assertEqual(resolve(source,rows[0]['field_results'][0]['require_ref']),{'equals':'first'})
        rows[0]['field_results'][0]['observed_values']=rows[1]['field_results'][0]['observed_values']
        with self.assertRaisesRegex(ValueError,'not retained'):validate_test_result(source,result,collections=collections)

    def test_record_ref_cannot_cross_instances_or_point_to_a_scalar(self):
        source,evidence,collections=self.record_fixture();result=project_test_result(source,TEST,evidence,collections=collections)
        for bad in ['/fields/result/1','/fields/result/01','/fields/result/0/value/a~1b~0c','/fields/other/0']:
            changed=deepcopy(result);changed['per_item_results'][0]['require_results'][0]['field_results'][0]['record_ref']=bad
            with self.subTest(ref=bad),self.assertRaises((ValueError,ValidationError)):validate_test_result(source,changed,collections=collections)

    def test_expected_values_datatypes_and_native_quantifiers_are_source_bound(self):
        source,evidence,collections=fixture({'equals':0,'datatype':'integer'})
        result=project_test_result(source,TEST,evidence,collections=collections)
        self.assertEqual(field(result)['datatype'],'integer')
        for key,value in [('operation','all'),('values_matching','all'),('datatype','string'),('expected_values',[typed('0','string')])]:
            changed=deepcopy(result);field(changed)[key]=value
            with self.subTest(key=key),self.assertRaises((ValueError,ValidationError)):validate_test_result(source,changed,collections=collections)

    def test_explicit_input_binding_identity_and_population(self):
        from test_v04_input_presence import guarded,provided,snapshot,INPUT
        source=guarded();_,evidence,collections=fixture()
        bound=snapshot(source,provided([0]),INV);evidence['binding_set_id']=bound.identity
        result=project_test_result(source,TEST,evidence,collections=collections,bindings=bound)
        self.assertEqual(field(result)['input_refs'],[INPUT]);self.assertEqual(field(result)['value_match'],'every')
        with self.assertRaises(ValueError):validate_test_result(source,result,collections=collections)
        other=snapshot(source,provided([0]),'another-invocation')
        with self.assertRaises(ValueError):validate_test_result(source,result,collections=collections,bindings=other)

    def test_variable_observations_need_explicit_same_invocation(self):
        source,evidence,collections=fixture({'equals':{'variable':'owner-variable'},'value_match':'every'})
        source['variables']={'owner-variable':{'kind':'constant','datatype':'integer','expression':{'literal':0}}}
        with self.assertRaises(ValueError):project_test_result(source,TEST,evidence,collections=collections)
        result=project_test_result(source,TEST,evidence,collections=collections,variables={'owner-variable':{'invocation_ref':INV,'values':[0]}})
        self.assertEqual(field(result)['variable_refs'],['owner-variable'])
        for values in (0,'0',None):
            with self.assertRaises(ValueError):
                project_test_result(source,TEST,evidence,collections=collections,
                    variables={'owner-variable':{'invocation_ref':INV,'values':values}})

    def test_missing_collection_item_count_and_evidence_references_reject(self):
        source,evidence,collections=fixture();result=project_test_result(source,TEST,evidence,collections=collections)
        for mutation in ('objects','item','count','refs','duplicate'):
            changed=deepcopy(result)
            if mutation=='objects':changed['object_refs']=[]
            elif mutation=='item':changed['per_item_results'][0]['item']['id']='another-item'
            elif mutation=='count':changed['item_summary']['returned_items']=0
            elif mutation=='refs':changed['evidence_refs']=['not-retained']
            else:changed['per_item_results']*=2
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):validate_test_result(source,changed,collections=collections)

    def test_redaction_and_comparison_values_do_not_leak_or_cross_scope(self):
        source,evidence,collections=fixture({'equals':0,'redact_result':True})
        with self.assertRaises(ValueError):project_test_result(source,TEST,evidence,collections=collections)
        redacted={'datatype':'integer','status':'exists','redacted':True}
        evidence['per_item_results'][0]['item']['fields']['owner_uid']=deepcopy(redacted)
        field(evidence).update(observed_values=[deepcopy(redacted)],expected_values=[deepcopy(redacted)])
        result=project_test_result(source,TEST,evidence,collections=collections)
        field(result)['comparison_results']=[{'outcome':'true','observed_value':typed(0)}]
        with self.assertRaises(ValueError):validate_test_result(source,result,collections=collections)

    def test_projection_does_not_evaluate_or_replace_supplied_truth(self):
        source,evidence,collections=fixture();evidence['outcome']='unknown'
        result=project_test_result(source,TEST,evidence,collections=collections)
        self.assertEqual(result['outcome'],'unknown')

    def test_item_absence_requires_explicit_complete_zero_population(self):
        source,evidence,collections=fixture();source['tests'][TEST]['require']={'items_found':'none'}
        evidence.update(items_observed=0,item_refs=[],per_item_results=[],item_summary={'evaluated_items':0,
            'observed_mismatches':0,'actual_mismatches':0,'returned_items':0,'truncated_evidence':False})
        collections[0]['item_refs']=[]
        result=project_test_result(source,TEST,evidence,collections=collections)
        self.assertNotIn('items_satisfying',result);self.assertNotIn('field_requirement',result)
        for status in ('not_collected','incomplete','error'):
            changed=deepcopy(collections);changed[0]['status']=status
            if status in ('error','incomplete'):
                changed[0].update(stop_reason='No reliable population',diagnostics=[{'code':'incomplete','message':'Supplied diagnostic'}],population_complete=False)
            with self.assertRaises((ValueError,ValidationError)):validate_test_result(source,result,collections=changed)

    def test_history_payloads_are_preserved_and_current_source_program_is_unchanged(self):
        from v04_native_bundle_compiler import compile_assessment_program
        source,evidence,collections=fixture();before=compile_assessment_program(source)
        project_test_result(source,TEST,evidence,collections=collections)
        self.assertEqual(before,compile_assessment_program(source))
        for name in ['test-result.schema.json','state-result.schema.json','entity-result.schema.json','collection-result.schema.json']:
            old=json.loads((ROOT/'tests/fixtures/v04-native-results/pre-migration-schemas'/name).read_text())
            self.assertEqual(old['x-scap-ng-version'],'0.4.0')
        for version in ('v0.1.0','v0.2.0','v0.3.0'):
            path=ROOT/'schema'/version/'test-result.schema.json'
            if path.exists():self.assertIn('state_refs',json.loads(path.read_text())['properties'])


if __name__=='__main__':unittest.main()
