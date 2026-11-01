"""Bounded #269 source-clause review; not a whole corpus Schematron validator."""
from hashlib import sha256
from pathlib import Path
import json
import sys
from lxml import etree as E
root=Path(sys.argv[1]);out=Path(sys.argv[2])
source=root/'third_party/scap-1.4-schemas/oval_5.12.3'
ns={'sch':'http://purl.oclc.org/dsdl/schematron'}
files={source/'oval-definitions-schema.xsd'}
for p in (root/'schema/v0.4.0/capability-mappings/supported').glob('*.json'):
 files.add(root/json.loads(p.read_text())['source']['definitions_schema'])
rows=[];cases=[]
for path in sorted(files):
 tree=E.parse(str(path),E.XMLParser(resolve_entities=False,no_network=True))
 checksum=sha256(path.read_bytes()).hexdigest()
 for rule in tree.xpath('//sch:rule',namespaces=ns):
  for clause in rule:
   if not isinstance(clause.tag,str):continue
   if E.QName(clause).localname not in ('assert','report'):continue
   text=' '.join(' '.join(clause.itertext()).split());expr=clause.get('test','');context=rule.get('context','')
   if not any(k in expr+' '+context for k in ('operation','var_check','recurse','max_depth','check_existence','set_operator','@action','error_if_','item_creation','include_group','skip_','multiline','singleline','ignore_case')):continue
   rows.append(dict(source_path=str(path.relative_to(root)),source_sha256=checksum,source_line=clause.sourceline,source_xpath=tree.getpath(clause),context=context,test=expr,kind=E.QName(clause).localname,documentation=text))
   # Datatype restrictions allow default equality; no dtype is invented.
   if path.name=='oval-definitions-schema.xsd' and clause.tag.endswith('}assert') and '@operation' in expr and 'datatype' in context:
    element=E.Element('value',operation='equals');actual=bool(element.xpath(expr,namespaces={k:v for k,v in rule.nsmap.items() if k}))
    assert actual,expr
    cases.append(dict(source_xpath=tree.getpath(clause),case='equals permitted within source datatype restriction',actual=actual))
core=E.parse(str(source/'oval-definitions-schema.xsd'))
clause=core.xpath('//sch:rule[contains(@context,"objects") and contains(@context,"@var_check")]/sch:assert[@test="@var_ref"]',namespaces=ns)[0]
for attrs,expected in [({'var_check':'all'},False),({'var_check':'all','var_ref':'oval:example:var:1'},True)]:
 actual=bool(E.Element('value',**attrs).xpath(clause.get('test')));assert actual==expected
 cases.append(dict(source_xpath=core.getpath(clause),case='var_check requires variable dependency',attributes=attrs,actual=actual,expected=expected))
# Execute actual pinned file-context assertions, keeping the sibling relationship.
independent=E.parse(str(source/'independent-definitions-schema.xsd'))
for fragment,attribute in [('filepath','max_depth'),('path','recurse')]:
 clauses=independent.xpath('//sch:rule/sch:assert[contains(@test,$needle)]',namespaces=ns,needle='preceding-sibling::ind-def:behaviors[@'+attribute)
 if fragment=='filepath':clauses=[c for c in clauses if '/ind-def:filepath' in c.getparent().get('context','')]
 else:clauses=[c for c in clauses if '/ind-def:path[' in c.getparent().get('context','') and c.get('test')=='not(preceding-sibling::ind-def:behaviors[@recurse])']
 clause=clauses[0];bindings={k:v for k,v in clause.nsmap.items() if k}
 for present,expected in [(False,True),(True,False)]:
  obj=E.Element('{'+bindings['ind-def']+'}object')
  if present:E.SubElement(obj,'{'+bindings['ind-def']+'}behaviors',**{attribute:'directories' if attribute=='recurse' else '1'})
  field=E.SubElement(obj,'{'+bindings['ind-def']+'}'+fragment,operation='pattern match')
  actual=bool(field.xpath(clause.get('test'),namespaces=bindings));assert actual==expected
  cases.append(dict(source_xpath=independent.getpath(clause),context=clause.getparent().get('context'),case='source path/behavior context',behavior_present=present,actual=actual,expected=expected))
result={'scope':'Relevant original embedded Schematron clauses across supported source schema files; bounded evaluation, not full Schematron/corpus or runtime parity',
 'source_commit':'a8a9db7039399610cb8af654ab9e880d69cffa04','source_files':len(files),'clauses':rows,'bounded_cases':cases,
 'conclusions':['Equality stays within source datatype-operation constraints; no constant datatype default.',
 'Variable/array matching requires dependency context; Schematron rejects var_check without var_ref and reports omitted var_check with var_ref.',
 'Source filepath/pattern-path contexts restrict recursion behaviors. Existing NG file selection rejects full_path plus traversal. Defaults only fill an explicitly requested present construct; host must validate full context and preserve diagnostics.',
 'Clause review does not establish scanner/collection equivalence. Converted explicit and effective values remain untouched.']}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'source_files':len(files),'relevant_clauses':len(rows),'bounded_cases_passed':len(cases)}))
