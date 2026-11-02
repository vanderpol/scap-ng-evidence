"""Independent bounded selector/API contract coverage; no target execution.

Checks the maintained catalog against source mappings/generated Object surfaces,
not a completion flag or the old dated disposition ledger. Refs #255 #269.
"""
from pathlib import Path
from hashlib import sha256
from urllib.parse import urlparse
import argparse
import json
import re

ROOT=Path(__file__).resolve().parents[1]
CAPABILITIES=('independent.environmentvariable','windows.appcmd','windows.appcmdlistconfig',
 'windows.cmdlet','windows.fileeffectiverights','windows.group_sid','windows.ntuser',
 'windows.regkeyeffectiverights','windows.service','windows.sid','windows.sid_sid',
 'windows.user_sid','windows.userright','windows.wmi.query','windows.wuaupdatesearcher')
POLICIES={'numeric_identity','sid_identity','filesystem_context','registry_identity',
 'canonical_enum','boolean_control','platform_environment','iis_schema_identity',
 'iis_property_expression','iis_section_path','powershell_command_identity',
 'powershell_module_identity','guid_identity','version_identity','powershell_record_context',
 'scm_identity','windows_account_identity','wmi_namespace_identity','wql_grammar','wua_criteria_grammar'}
CONTEXTUAL={'filesystem_context','registry_identity','platform_environment','iis_schema_identity',
 'iis_property_expression','iis_section_path','powershell_command_identity','powershell_module_identity',
 'powershell_record_context','scm_identity','windows_account_identity','wmi_namespace_identity',
 'wql_grammar','wua_criteria_grammar','sid_identity'}


def audit(root=ROOT,document=None):
    root=Path(root);directory=root/'schema/v0.4.0'
    catalog=document if document is not None else json.loads((directory/'selector-api-contracts.json').read_text())
    errors=[];fields=0;rows=[]
    def require(test,message):
        if not test:errors.append(message)
    def text(value):return isinstance(value,str) and bool(value.strip())
    require(catalog.get('format')=='scap-ng/selector-api-contracts/1','catalog format')
    require(catalog.get('schema_version')=='0.4.0' and catalog.get('owner_decision')==22,'catalog authority/version')
    caps=catalog.get('capabilities',{});sources=catalog.get('sources',{})
    require(set(caps)==set(CAPABILITIES),'exact 15-capability inventory')
    for key,source in sources.items():
        url=urlparse(source.get('url',''))
        require(url.scheme=='https' and url.hostname in {'learn.microsoft.com','pubs.opengroup.org','github.com'},'primary source URL: '+key)
        require(bool(re.fullmatch('[0-9a-f]{64}',source.get('sha256',''))),'source hash: '+key)
        require(text(source.get('claim')),'source claim: '+key)
        if source.get('repository_path'):
            path=root/source['repository_path']
            require(path.is_file() and sha256(path.read_bytes()).hexdigest()==source['sha256'],'pinned repository source: '+key)
        else:require(source.get('status')=='retrieved' and text(source.get('retrieved_at')),'retrieved source receipt: '+key)
    from generate_capability_schema_v04 import generate
    for cap in CAPABILITIES:
        row=caps.get(cap,{})
        mapping=json.loads((directory/'capability-mappings/supported'/(cap+'.json')).read_text())
        native=mapping['native'];selectors=set(native.get('selector_map',{}).values());parameters=set(native.get('collection_parameters',{}))
        surface=generate(mapping,root,authoring_metadata=False)['$defs']['object']['properties']
        # Derive inherited acquisition parameters from the actual generated
        # Object too; mapping-only inventory would miss filesystem scope.
        parameters |= set(surface)-selectors-{'object_title','capability','set','filters','for_each','traversal'}
        declared=row.get('fields',{})
        require(set(declared)==selectors|parameters,'field coverage: '+cap)
        require(row.get('status')=='DOCUMENTED_CONTRACT_NOT_RUNTIME_VERIFIED','contract status: '+cap)
        require(bool(row.get('platform')) and bool(row.get('exceptions')) and bool(row.get('limitations')),'platform/exceptions/limits: '+cap)
        require(text(row.get('value_comparison')) and 'case_insensitive_equals' in row['value_comparison'],'independent collected-value comparison: '+cap)
        require(row.get('traversal_contract')==native.get('traversal_definition'),'traversal scope: '+cap)
        require(text(row.get('common_acquisition_controls')),'shared controls: '+cap)
        for name,field in declared.items():
            fields+=1;prefix=cap+'.'+name
            require(name in surface,'generated Object field: '+prefix)
            require(field.get('role')==('selector' if name in selectors else 'acquisition_parameter'),'field role: '+prefix)
            mode=field.get('case_policy');require(mode in POLICIES,'case policy: '+prefix)
            require(text(field.get('rule')) and text(field.get('uncertainty')),'documented rule/limits: '+prefix)
            refs=field.get('sources',[])
            require(bool(refs) and all(key in sources for key in refs),'source resolution: '+prefix)
            require(mode not in CONTEXTUAL or bool(field.get('required_context')),'explicit conditional context: '+prefix)
            for polarity in ('positive','negative'):
                example=field.get(polarity,{})
                require('operand' in example and text(example.get('expectation')),'concrete '+polarity+' example: '+prefix)
            if name in native.get('selector_value_enums',{}):require(mode=='canonical_enum','enum is not API text: '+prefix)
            if native.get('collection_parameters',{}).get(name,{}).get('type')=='boolean':require(mode=='boolean_control','Boolean not casing: '+prefix)
            if name.endswith('_sid'):require(mode=='sid_identity','SID not account-name folding: '+prefix)
        rows.append({'capability':cap,'selectors':sorted(selectors),'acquisition_parameters':sorted(parameters),
                     'traversal':native.get('traversal_definition'),'field_count':len(declared)})
    return {'format':'scap-ng/selector-api-contract-audit/1','status':'PASS' if not errors else 'FAIL',
            'capabilities':rows,'capability_count':len(rows),'field_count':fields,'source_count':len(sources),
            'errors':errors,'scanner_executed':False,'api_cases_executed':False,
            'scope':'contract coverage, source receipts and generated-surface agreement; conditional API behavior is not a simulated collector'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():p.error('refuse to overwrite audit')
    result=audit();args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','capability_count','field_count','source_count','errors')}))
    raise SystemExit(result['status']!='PASS')
