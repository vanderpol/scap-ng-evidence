"""Owner-adopted native Result A: structural/source evidence, never evaluation.

No scanner, collector, Variable execution, legacy Result conversion or implicit
verdict/default. Historical schemas/results remain separately pinned. Refs #255.
"""
from copy import deepcopy
from functools import lru_cache
from pathlib import Path
import argparse
import json
import re

from jsonschema import Draft202012Validator
from referencing import Registry

from v04_a_authoring_graph_index import canonical_json
from v04_object_contract import resources

ROOT = Path(__file__).resolve().parents[1]
LOGIC = ('and','or','one','xor')
CONTROLS = {'datatype','values_found','values_matching','value_match','redact_result'}


def pointer(parts):
    return '/'+'/'.join(str(p).replace('~','~0').replace('/','~1') for p in parts)


def resolve(document, location):
    """Strict RFC6901: no fragments, URI decoding, bad escapes or array aliases."""
    if not isinstance(location,str) or not location.startswith('/'):
        raise ValueError('absolute RFC6901 pointer required')
    parts=location[1:].split('/')
    if any(re.search(r'~(?![01])',part) for part in parts):
        raise ValueError('invalid pointer escape')
    parts=[p.replace('~1','/').replace('~0','~') for p in parts]
    if pointer(parts)!=location:raise ValueError('noncanonical pointer')
    node=document
    for part in parts:
        if isinstance(node,list):
            if not re.fullmatch(r'0|[1-9][0-9]*',part):raise ValueError('noncanonical array index')
            index=int(part)
            if index>=len(node):raise ValueError('unresolved array location')
            node=node[index]
        elif isinstance(node,dict) and part in node:node=node[part]
        else:raise ValueError('unresolved source/evidence pointer: '+location)
    return node


@lru_cache(maxsize=8)
def validator(name):
    directory=ROOT/'schema/v0.4.0'
    schema=json.loads((directory/name).read_text())
    return Draft202012Validator(schema,registry=Registry().with_resources(resources(str(directory)).items()))


def require_inventory(assessment, test_id):
    """Ordered native nodes and nearest complete explicit requirement provenance."""
    from v04_native_bundle_compiler import compile_assessment_program
    compile_assessment_program(assessment)  # Closes source, including unselected branches.
    if test_id not in assessment['tests']:raise ValueError('unknown source Test')
    entries={}
    def add(node,path,kind,pair,pair_ref,record_scope=None,field=None):
        ref=pointer(path)
        entries[ref]={'node':node,'kind':kind,'pair':deepcopy(pair),'pair_ref':pair_ref,
                      'record_scope':record_scope,'field':field,'path':path}
        return ref
    def condition(node,path,pair=None,pair_ref=None,record_scope=None,kind='condition'):
        if 'field_requirement' in node:
            pair=node['field_requirement'];pair_ref=pointer(path+['field_requirement'])
        add(node,path,kind,pair,pair_ref,record_scope)
        for op in LOGIC:
            for i,child in enumerate(node.get(op,[])):
                condition(child,path+[op,i],pair,pair_ref,record_scope)
        for name,pred in sorted(node.get('fields',{}).items()):
            at=path+['fields',name]
            if 'record' in pred:
                add(pred,at,'record',pair,pair_ref,record_scope,name)
                body=pred['record'];scope=pointer(at+['record'])
                condition(body,at+['record'],pair,pair_ref,scope,'record_instance')
                entries[scope]['field']=name
            else:
                effective,origin=pair,pair_ref
                if set(pred)>={'values_found','values_matching'}:
                    effective={k:pred[k] for k in ('values_found','values_matching')};origin=pointer(at)
                add(pred,at,'field',effective,origin,record_scope,name)
    condition(assessment['tests'][test_id]['require'],['tests',test_id,'require'],kind='test')
    return entries


def _echo(target,key,value):
    if key in target and canonical_json(target[key])!=canonical_json(value):
        raise ValueError('supplied Result conflicts with source '+key)
    target[key]=deepcopy(value)


def _field_source(target,meta):
    pred=meta['node'];_echo(target,'field',meta['field'])
    if pred.get('values_found')=='none':
        _echo(target,'values_found','none');return
    operations=set(pred)-CONTROLS
    if len(operations)!=1 or meta['pair'] is None:
        raise ValueError('comparison requires explicit operation and inherited complete pair')
    operation=next(iter(operations));_echo(target,'operation',operation)
    operand=pred[operation]
    if isinstance(operand,dict):
        for kind,key in [('input','input_refs'),('variable','variable_refs')]:
            if kind in operand:_echo(target,key,[operand[kind]])
    for key,value in meta['pair'].items():_echo(target,key,value)
    _echo(target,'requirement_ref',meta['pair_ref'])
    for key in ('datatype','value_match'):
        if key in pred:_echo(target,key,pred[key])


def project_test_result(assessment,test_id,observations,*,collections,evidence=None,bindings=None,variables=None):
    """Attach source metadata to explicit native observations; never choose truth.

    Caller supplies every outcome, Item, count and evidence reference. No legacy
    Result is accepted/rewritten and no absent binding/Item/value is invented.
    """
    inventory=require_inventory(assessment,test_id)
    result=deepcopy(observations);_echo(result,'id',test_id)
    _echo(result,'require_refs',list(inventory))
    source=assessment['tests'][test_id]['require']
    for key in ('items_found','items_satisfying','field_requirement'):
        if key in source:_echo(result,key,source[key])
    def attach(row):
        if row.get('require_ref') not in inventory:raise ValueError('unknown native require_ref')
        meta=inventory[row['require_ref']];node=meta['node']
        for op in LOGIC:
            if op in node:_echo(row,'operator',op)
        for key in ('records_found','records_matching'):
            if key in node:_echo(row,key,node[key])
        for field in row.get('field_results',[]):
            item=inventory.get(field.get('require_ref'))
            if item is None or item['kind']!='field':raise ValueError('field Result must reference scalar native predicate')
            _field_source(field,item)
        for child in row.get('require_results',[]):attach(child)
    for item in result.get('per_item_results',[]):
        for row in item.get('require_results',[]):attach(row)
    validate_test_result(assessment,result,collections=collections,evidence=evidence,bindings=bindings,variables=variables)
    return result


def validate_test_result(assessment,result,*,collections,evidence=None,bindings=None,variables=None):
    """Validate supplied evidence identity, native paths, controls and correlation.

    Deliberately does not recompute comparators, aggregate truth or retention caps.
    """
    validator('test-result.schema.json').validate(result)
    inventory=require_inventory(assessment,result['id'])
    source=assessment['tests'][result['id']]
    from v04_comparison_types import contract
    capability_fields=contract(source['capability'])[0]
    if result['require_refs']!=list(inventory):raise ValueError('require_refs must preserve exact native node inventory/order')
    if any(ref not in inventory for ref in result.get('decisive_require_refs',[])):
        raise ValueError('unknown decisive native requirement reference')
    for key in ('items_found','items_satisfying','field_requirement'):
        expected=source['require'].get(key)
        if (key in result)!=(key in source['require']) or result.get(key)!=expected:
            raise ValueError('Result/source requirement mismatch: '+key)
    if not isinstance(collections,list):raise ValueError('explicit collection observations required')
    collection_by_id={}
    for collection in collections:
        validator('collection-result.schema.json').validate(collection)
        if collection['id'] in collection_by_id:raise ValueError('duplicate collection observation')
        collection_by_id[collection['id']]=collection
    if any(ref not in collection_by_id for ref in result['object_refs']):raise ValueError('unknown collection reference')
    selected=[collection_by_id[ref] for ref in result['object_refs']]
    if source.get('object') is not None and not selected:
        raise ValueError('Object-backed Test requires explicit collection evidence')
    if any(c['capability']!=source['capability'] for c in selected):raise ValueError('collection/Test capability conflict')
    if any(c['status'] in ('error','incomplete') for c in selected) and result['outcome']!='error':
        raise ValueError('incomplete/error collection cannot produce a non-error native Test')
    if source['require']['items_found']=='none' and result['outcome']=='true':
        if result['items_observed']!=0 or any(c['status'] not in ('complete','does_not_exist') for c in selected):
            raise ValueError('Item absence needs confirmed complete zero population')
    external=evidence or {}
    if not isinstance(external,dict) or any(not isinstance(v,dict) or not v for v in external.values()):
        raise ValueError('external evidence must be explicit nonempty records')
    known=set(result['object_refs'])|set(external)|set(result['item_refs'])
    if 'binding_set_id' in result:
        from v04_input_presence import InputBindingSnapshot
        if (not isinstance(bindings,InputBindingSnapshot) or bindings.identity!=result['binding_set_id']
                or bindings.document()['invocation_id']!=result['invocation_ref']
                or bindings.document()['contracts']!=assessment.get('inputs',{})):
            raise ValueError('Result must identify the exact supplied binding invocation')
        known.add(bindings.identity)
    def evidence_refs(row):
        if any(ref not in known for ref in row.get('evidence_refs',[])):
            raise ValueError('unresolved evidence reference')
    evidence_refs(result)
    retained=[row['item_ref'] for row in result['per_item_results']]
    if len(retained)!=len(set(retained)) or set(result['item_refs'])!=set(retained):
        raise ValueError('retained Item identities disagree or duplicate')
    summary=result['item_summary']
    observed=result['items_observed']
    if observed!='unknown' and observed<len(set(retained)|{i for c in selected for i in c['item_refs']}):
        raise ValueError('observed Item population is below retained/collection evidence')
    if summary['returned_items']!=len(retained) or summary['evaluated_items']<len(retained):
        raise ValueError('retained/evaluated Item counts disagree')
    if observed!='unknown' and summary['evaluated_items']>observed:
        raise ValueError('evaluated Item count exceeds observed population')
    failures=sum(row['outcome']=='false' for row in result['per_item_results'])
    if not failures<=summary['observed_mismatches']<=summary['evaluated_items']:
        raise ValueError('observed mismatch counts contradict retained evidence')
    actual=summary['actual_mismatches']
    if actual!='unknown' and not summary['observed_mismatches']<=actual<=summary['evaluated_items']:
        raise ValueError('actual mismatch count contradicts observed/evaluated population')
    if summary['observed_mismatches']>failures and not summary['truncated_evidence']:
        raise ValueError('omitted mismatch evidence must be marked truncated')
    for item in result['per_item_results']:
        observed=item['item'];evidence_refs(item)
        if observed['id']!=item['item_ref'] or observed['capability']!=source['capability']:
            raise ValueError('retained Item identity/capability mismatch')
        if selected and item['item_ref'] not in {i for c in selected for i in c['item_refs']}:
            raise ValueError('Item does not belong to selected collection evidence')
        visited=set()
        def walk(row,parent=None,record=None):
            ref=row['require_ref']
            if ref not in inventory:raise ValueError('Result location is not a native requirement node')
            meta=inventory[ref];node=meta['node'];evidence_refs(row)
            if parent and not (ref==parent or ref.startswith(parent+'/')):
                raise ValueError('child requirement escaped its source scope')
            scope=meta['record_scope'];own=row.get('record_ref')
            record_absence=bool(scope and node.get('records_found')=='none')
            if record_absence:
                if own is not None:raise ValueError('absent record cannot identify an existing record instance')
                if row['field_results'] or row.get('require_results'):
                    raise ValueError('absent record cannot carry child comparison evidence')
                if row['outcome']=='true':
                    raw=observed['fields'].get(inventory[scope]['field'])
                    values=raw if isinstance(raw,list) else ([] if raw is None else [raw])
                    if row.get('observation_complete') is not True or observed['status']!='exists':
                        raise ValueError('record absence requires explicit complete observation')
                    if any(v.get('status')!='does_not_exist' for v in values):
                        raise ValueError('present/failed record is not absence')
                    if any(c['status'] not in ('complete','does_not_exist') for c in selected):
                        raise ValueError('collection uncertainty is not record absence')
            elif scope:
                if own is None:raise ValueError('record-scoped Result needs explicit record_ref')
                if record and record!=own:raise ValueError('mixed record instances')
                scope_field=inventory[scope]['field'];prefix=pointer(['fields',scope_field])
                if own!=prefix and not re.fullmatch(re.escape(prefix)+r'/(0|[1-9][0-9]*)',own):
                    raise ValueError('record instance does not belong to source record field')
                value=resolve(observed,own)
                if not isinstance(value,dict) or value.get('datatype')!='record':raise ValueError('record_ref is not a typed record instance')
                record=own
            elif own is not None:raise ValueError('record_ref on non-record source scope')
            identity=(ref,own)
            if identity in visited:raise ValueError('duplicate source/record Result location')
            visited.add(identity)
            expected_op=next((op for op in LOGIC if op in node),None)
            if row.get('operator')!=expected_op:raise ValueError('native logical operator mismatch')
            for key in ('records_found','records_matching'):
                if (key in row)!=(key in node) or row.get(key)!=node.get(key):raise ValueError('record requirement mismatch')
            seen_fields=set()
            for field in row['field_results']:
                fref=field['require_ref'];fmeta=inventory.get(fref)
                if fmeta is None or fmeta['kind']!='field' or not (fref==ref or fref.startswith(ref+'/')):
                    raise ValueError('field Result escaped its source requirement')
                if fref in seen_fields:raise ValueError('duplicate field Result within one record')
                seen_fields.add(fref);evidence_refs(field)
                expected=deepcopy(field);_field_source(expected,fmeta)
                if expected!=field:raise ValueError('Result omitted explicit effective field requirements')
                if fmeta['record_scope']:
                    if record is None or field.get('record_ref')!=record:raise ValueError('field Result mixes or omits record instance')
                    container=resolve(observed,record).get('value',{})
                else:
                    if field.get('record_ref') is not None:raise ValueError('unexpected scalar record_ref')
                    container=observed['fields']
                raw=container.get(field['field'])
                values=raw if isinstance(raw,list) else ([] if raw is None else [raw])
                for typed in values+field.get('expected_values',[]):
                    _typed(typed)
                if not fmeta['record_scope'] and any(v['datatype'] not in capability_fields[field['field']] for v in values):
                    raise ValueError('observed datatype conflicts with capability')
                position=0
                for value in field['observed_values']:
                    while position<len(values) and canonical_json(values[position])!=canonical_json(value):position+=1
                    if position==len(values):raise ValueError('field observation is not retained Item evidence')
                    position+=1
                if fmeta['node'].get('redact_result'):
                    emitted=field['observed_values']+field.get('expected_values',[])+values
                    emitted += [v for pair in field.get('comparison_results',[]) for k,v in pair.items() if k!='outcome']
                    if any(v.get('redacted') is not True for v in emitted):raise ValueError('redacted predicate leaks values')
                for comparison in field.get('comparison_results',[]):
                    for key,allowed in [('observed_value',field['observed_values']),('expected_value',field.get('expected_values',[]))]:
                        if key in comparison and comparison[key] not in allowed:
                            raise ValueError('comparison value escapes its field/record evidence')
                if field.get('values_found')=='none' and field['outcome']=='true':
                    if not field['observation_complete'] or observed['status']!='exists':
                        raise ValueError('incomplete/failed field observation is not confirmed absence')
                    if any(v.get('status')!='does_not_exist' for v in values):raise ValueError('failed/present observation is not confirmed absence')
                    if any(c['status'] not in ('complete','does_not_exist') for c in selected):raise ValueError('collection uncertainty is not field absence')
                _expected_values(assessment,result,field,fmeta,bindings,variables or {})
            for child in row.get('require_results',[]):walk(child,ref,record)
        for row in item['require_results']:walk(row)
    return {'status':'NATIVE_040_RESULT_SOURCE_AND_EVIDENCE_VALID','test':result['id'],
            'requirement_nodes':len(inventory),'retained_items':len(retained),
            'scanner_executed':False,'truth_recomputed':False}


def _typed(value):
    from v04_input_presence import DOMAINS,_value_valid
    if value['datatype'] not in DOMAINS:raise ValueError('unsupported native Result datatype')
    if value['status']=='exists' and value.get('redacted') is not True:
        if 'value' not in value or not _value_valid(value['value'],value['datatype']):
            raise ValueError('invalid native typed observation; no implicit value/cast')


def _expected_values(assessment,test_result,field,meta,bindings,variables):
    if field.get('values_found')=='none':return
    operand=meta['node'][field['operation']]
    refs={'input':[],'variable':[]}
    if isinstance(operand,dict):
        kind,identity=next(iter(operand.items()))
        if kind not in refs:raise ValueError('unknown expected operand reference')
        refs[kind].append(identity)
        if kind=='input':
            if bindings is None or test_result.get('binding_set_id')!=bindings.identity:
                raise ValueError('Input observation requires explicit binding_set_id/snapshot')
            entry=bindings.document()['bindings'][identity]
            if entry['state']!='provided':raise ValueError('unprovided Input cannot be consumed as expected values')
            values=entry['values'];domain=assessment['inputs'][identity]['datatype']
        else:
            record=variables.get(identity)
            if not isinstance(record,dict) or record.get('invocation_ref')!=test_result['invocation_ref'] or 'values' not in record:
                raise ValueError('Variable Result requires explicit same-invocation observations')
            values=record['values'];domain=assessment['variables'][identity]['datatype']
    else:
        values=operand if isinstance(operand,list) else [operand];domain=None
    if not isinstance(values,list):raise ValueError('expected observations must be an explicit value population array')
    for kind,key in [('input','input_refs'),('variable','variable_refs')]:
        if field.get(key,[])!=refs[kind]:raise ValueError('expected operand reference mismatch')
    from v04_comparison_types import contract,predicate_type,TEXT_TYPES
    allowed = (TEXT_TYPES|{'boolean','integer','float'} if meta['record_scope'] else
               set(contract(assessment['tests'][test_result['id']]['capability'])[0][field['field']]))
    inferred=predicate_type(meta['node'],allowed,assessment,field['require_ref'])
    if domain is not None and domain!=inferred:raise ValueError('expected domain conflicts with source predicate')
    domain=inferred
    if 'datatype' in field and field['datatype']!=domain:raise ValueError('compatible Result datatype conflicts with source')
    supplied=field['expected_values']
    if len(supplied)!=len(values):raise ValueError('expected population does not match source/binding observations')
    for emitted,original in zip(supplied,values):
        if domain and emitted['datatype']!=domain:raise ValueError('expected declared datatype conflict')
        if emitted['status']!='exists':raise ValueError('known expected operand cannot invent missing/error value')
        if emitted.get('redacted') is not True and canonical_json(emitted.get('value'))!=canonical_json(original):
            raise ValueError('expected value differs from source/binding evidence')


def validate_assessment_result(assessment,document,*,evidence=None,bindings=None,variables=None):
    """Validate native child Results against the supplied parent invocation.

    Parent truth, expression trace and Variable execution are not recomputed.
    """
    validator('assessment-result.schema.json').validate(document)
    result=document['assessment_result']
    if result['assessment']['id']!=assessment['id'] or result['assessment']['version']!=assessment['version']:
        raise ValueError('Assessment Result/source identity mismatch')
    if len({row['id'] for row in result['tests']})!=len(result['tests']):
        raise ValueError('duplicate Test Result')
    if bindings is not None and (result.get('binding_set_id')!=bindings.identity or
                                bindings.document()['invocation_id']!=result['execution_id']):
        raise ValueError('parent Result binding identity mismatch')
    for row in result['tests']:
        if row['invocation_ref']!=result['execution_id']:
            raise ValueError('Test Result belongs to another invocation')
        if row.get('binding_set_id') is not None and row['binding_set_id']!=result.get('binding_set_id'):
            raise ValueError('Test/parent binding identity mismatch')
        validate_test_result(assessment,row,collections=result['objects'],evidence=evidence,
                             bindings=bindings,variables=variables)
    return {'status':'NATIVE_040_ASSESSMENT_RESULT_SOURCE_AND_EVIDENCE_VALID',
            'scanner_executed':False,'truth_recomputed':False}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--assessment',type=Path,required=True)
    p.add_argument('--result',type=Path,required=True);p.add_argument('--collections',type=Path,required=True)
    args=p.parse_args();source=json.loads(args.assessment.read_text())
    print(json.dumps(validate_test_result(source.get('assessment',source),json.loads(args.result.read_text()),
        collections=json.loads(args.collections.read_text())),indent=2))
