"""Decision22 coverage, failure mutations and source-preserving integration.

No OS/API calls or invented case comparison implementation. Refs #255 #269.
"""
from copy import deepcopy
from pathlib import Path
import json
import unittest

from audit_v04_selector_contracts import audit,CAPABILITIES
from generate_capability_schema_v04 import generate
from test_generate_capability_schema_v04 import validate
from v04_editor_annotations import semantic_schema
from v04_native_bundle_compiler import compile_assessment_program

ROOT=Path(__file__).resolve().parents[1]


def catalog():return json.loads((ROOT/'schema/v0.4.0/selector-api-contracts.json').read_text())
def fixture():return json.loads((ROOT/'tests/fixtures/v04-selector-contracts/authoring.assessment.json').read_text())


class SelectorContracts(unittest.TestCase):
    def test_exact_all_fifteen_and_forty_two_fields_are_source_bound(self):
        result=audit();self.assertEqual(result['errors'],[])
        self.assertEqual((result['capability_count'],result['field_count']),(15,42))
        self.assertFalse(result['scanner_executed']);self.assertFalse(result['api_cases_executed'])

    def test_missing_selector_parameter_source_or_context_fails_closed(self):
        changes=[
            lambda c:c['capabilities']['windows.service']['fields'].pop('service_name'),
            lambda c:c['capabilities']['windows.cmdlet']['fields'].pop('select'),
            lambda c:c['capabilities']['windows.sid']['fields']['trustee_name'].update(role='acquisition_parameter'),
            lambda c:c['capabilities']['windows.fileeffectiverights']['fields']['name'].update(required_context=[]),
            lambda c:c['capabilities']['windows.wmi.query']['fields']['query'].update(sources=['invented']),
            lambda c:c['sources']['service'].update(sha256='not-a-digest'),
            lambda c:c['capabilities']['windows.wuaupdatesearcher']['fields']['include_superseded_updates'].update(case_policy='scm_identity'),
            lambda c:c['capabilities']['windows.group_sid']['fields']['group_sid'].update(case_policy='windows_account_identity'),
            lambda c:c['capabilities']['windows.appcmdlistconfig']['fields']['section'].update(negative={}),
        ]
        for mutate in changes:
            c=catalog();mutate(c)
            with self.subTest(change=mutate):self.assertEqual(audit(document=c)['status'],'FAIL')

    def test_final_freeze_audit_closes_all_contracts_and_propagates_failures(self):
        from audit_v04_schema_freeze_readiness import audit as freeze_audit
        from unittest.mock import patch
        result=freeze_audit()
        self.assertEqual(result['schema_freeze_readiness'],'READY_FOR_OWNER_REVIEW')
        self.assertEqual((result['schema_count'],result['references_checked']),(34,242))
        self.assertEqual(result['reference_errors'],[])
        self.assertEqual({r['decision'] for r in result['decisions']},set(range(1,30)))
        self.assertTrue(all(r['language_contract_status']=='CLOSED' for r in result['decisions']))
        failed=audit();failed['errors']=['missing selector contract source'];failed['status']='FAIL'
        with patch('audit_v04_selector_contracts.audit',return_value=failed):
            self.assertEqual(freeze_audit()['schema_freeze_readiness'],'NO_GO')

    def test_case_context_is_specific_and_values_remain_independent(self):
        caps=catalog()['capabilities']
        expected={('independent.environmentvariable','name'):'platform_environment',
                  ('windows.service','service_name'):'scm_identity',
                  ('windows.ntuser','key'):'registry_identity',
                  ('windows.fileeffectiverights','name'):'filesystem_context',
                  ('windows.appcmd','identifier'):'iis_schema_identity',
                  ('windows.appcmdlistconfig','section'):'iis_section_path',
                  ('windows.cmdlet','parameters'):'powershell_record_context',
                  ('windows.wmi.query','query'):'wql_grammar',
                  ('windows.wuaupdatesearcher','search_criteria'):'wua_criteria_grammar'}
        for (cap,name),mode in expected.items():self.assertEqual(caps[cap]['fields'][name]['case_policy'],mode)
        for row in caps.values():
            self.assertIn('case-sensitive equals',row['value_comparison'])
            self.assertIn('case_insensitive_equals',row['value_comparison'])
        # This is context/documentation inspection, not fake API execution.

    def test_editor_descriptions_are_complete_and_normative_shapes_identical(self):
        for cap in CAPABILITIES:
            m=json.loads((ROOT/'schema/v0.4.0/capability-mappings/supported'/(cap+'.json')).read_text())
            before=generate(m,ROOT,authoring_metadata=False);after=generate(m,ROOT)
            self.assertEqual(semantic_schema(before),semantic_schema(after),cap)
            for name in catalog()['capabilities'][cap]['fields']:
                text=after['$defs']['object']['properties'][name]['description']
                self.assertIn('Decision22',text);self.assertIn('Sources: https://',text)
                self.assertIn('Collected-value comparisons remain independent.',text)

    def test_all_fifteen_authoring_objects_validate_and_compile_without_rewriting(self):
        doc=fixture();before=deepcopy(doc)
        for test in doc['assessment']['tests'].values():
            m=json.loads((ROOT/'schema/v0.4.0/capability-mappings/supported'/(test['capability']+'.json')).read_text())
            self.assertEqual(validate(generate(m,ROOT),'object',test['object']),[],test['capability'])
        compile_assessment_program(doc['assessment']);self.assertEqual(doc,before)

    def test_no_universal_case_switch_is_accepted_or_implicitly_materialized(self):
        for test in fixture()['assessment']['tests'].values():
            m=json.loads((ROOT/'schema/v0.4.0/capability-mappings/supported'/(test['capability']+'.json')).read_text());schema=generate(m,ROOT)
            bad={**deepcopy(test['object']),'case_sensitive':False}
            self.assertTrue(validate(schema,'object',bad),test['capability'])
            self.assertNotIn('case_sensitive',test['object'])

    def test_enum_case_boolean_and_version_lookalikes_are_not_hidden_conversions(self):
        doc=fixture()
        changes=[('windows-service-test','case_sensitive',False),
                 ('windows-cmdlet-test','verb','get'),
                 ('windows-cmdlet-test','module_version','latest'),
                 ('windows-sid-test','include_group','true'),
                 ('windows-userright-test','userright',{'equals':'se_backup_name'})]
        for identity,key,value in changes:
            test=deepcopy(doc['assessment']['tests'][identity]);test['object'][key]=value
            m=json.loads((ROOT/'schema/v0.4.0/capability-mappings/supported'/(test['capability']+'.json')).read_text())
            self.assertTrue(validate(generate(m,ROOT),'object',test['object']),(identity,key))


if __name__=='__main__':unittest.main()
