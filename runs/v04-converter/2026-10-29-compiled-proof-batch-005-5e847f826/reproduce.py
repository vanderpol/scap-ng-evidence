"""Replay a bounded frozen DRAFT cohort through the existing verified upgrader.

Research/reproduction driver only: no converter, schema, compiler or proof rule
is implemented here. The original archive is read-only and never regenerated.
"""
import argparse,copy,hashlib,json,subprocess,sys,time,zipfile
from pathlib import Path
ROOT=Path('/workspace/scap-ng');sys.path.insert(0,str(ROOT/'tools'))
from verify_v04_direct_scope import accept_source
from v04_direct_converter import load_mappings
from v04_direct_scap_source import SourceModel,digest
from v04_expanded_source_proof import ExpandedSource,expanded_compare
from v04_native_bundle_compiler import compile_assessment_program
from audit_v04_eight_assessment_pilot import verify_program
from oval_source_validation import SourceValidator
from validate_native_json_schemas import build_validators
DRAFT=Path('/workspace/scap-ng-evidence/runs/v04-converter/2026-10-28-niwc-65-draft-248895772/niwc-65-draft-248895772.zip')
PINS=json.loads(DRAFT.with_name('source-pins.json').read_text())
SHA='5f86d016c1bce82018eec82c6468ab583816ff0b38c8d3ea5e9210a931cc1a08'
STATUS='CONVERTED_COMPILED_UNPROVED_ORIGINAL_VALIDITY_NOT_RUN'
ONLY={(r['benchmark'],r['rule']) for r in json.loads(Path(__file__).with_name('registry-retry-selection.json').read_text())}

def require(value,message):
    if not value:raise AssertionError(message)

def batch(benchmark,output,inputs,archive,mappings,validator,schemas):
    started=time.perf_counter();output.mkdir(parents=True,exist_ok=False)
    ledger=json.loads(archive.read(benchmark+'/ledger.json'))
    cohort=[r for r in ledger['rules'] if r['draft_status']==STATUS and (benchmark,r['source_rule']) in ONLY]
    require(cohort,'No frozen unproved cohort')
    require(len({r['source_rule'] for r in cohort})==len(cohort),'Duplicate cohort Rule')
    pin=next(p for p in PINS['sources'] if p['file']==benchmark+'.zip')
    source_path=inputs/pin['file'];raw=source_path.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==pin['sha256'],'Original ZIP SHA-256 drift')
    require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin['git_blob_sha'],'Original Git blob drift')
    selection=[r['source_rule'] for r in cohort]
    (output/'selection.json').write_text(json.dumps(selection,indent=2)+'\n')
    own=accept_source(source_path,pin['sha256'],output/'accepted',rule_ids=selection,mappings=mappings,source_validator=validator,validators=schemas)
    cases={c['rule']:c for c in own['cases'] if c['rule'] in selection}
    require(set(cases)==set(selection),'Cohort membership lost')
    previous={p['assessment']:p['program_sha256'] for p in json.loads(archive.read(benchmark+'/compilation.json'))}
    programs={p['assessment']:p['program_sha256'] for p in own['programs']}
    source=SourceModel(source_path,pin['sha256'],inventory_broken_references=True)
    trace=json.loads((output/'accepted/source-trace.json').read_text())
    bindings={b['source_rule']:b for b in trace['rules']}
    proofs=[];rows=[];mutants=[];seen_caps=set()
    def deps(ds):return {(d['component'],d['id'],d['kind']):d['sha256'] for d in ds}
    for old in cohort:
        case=cases[old['source_rule']]
        require(case['source_rule_sha256']==old['source_rule_sha256'],'Original Rule identity drift: '+case['rule'])
        require(deps(case['dependencies'])==deps(old['dependencies']),'Original closure drift: '+case['rule'])
        record={'rule':case['rule'],'outcome':case['outcome'],'diagnostic':case.get('diagnostic'),'source_validity':case.get('source_validity'),'proof':case.get('proof')}
        if case['outcome']!='PROVED':rows.append(record);continue
        path=next(p for p in old['artifacts'] if '/assessments/' in p and p.endswith('.json'))
        old_raw=archive.read(benchmark+'/'+path);old_doc=json.loads(old_raw)
        new_doc=json.loads((output/'accepted'/path).read_text())
        require(old_doc==new_doc,'Frozen authoring semantic drift: '+case['rule'])
        a=new_doc['assessment'];identifier=a['id']
        require(previous[identifier]==programs[identifier],'Frozen program hash drift: '+case['rule'])
        binding=bindings[case['rule']]
        proof=expanded_compare(ExpandedSource(source.components[binding['component']]),binding['definition'],a)
        require(proof['outcome']=='PROVED','Independent proof not repeatable: '+case['rule'])
        for c in proof['comparisons']:
            require(digest(c['source_term'])==digest(c['native_term']),'Source/native term hash mismatch')
        record.update(assessment=identifier,source_rule_sha256=case['source_rule_sha256'],source_zip_sha256=pin['sha256'],source_closure_sha256=digest(old['dependencies']),frozen_authoring_file_sha256=hashlib.sha256(old_raw).hexdigest(),authoring_sha256=digest(a),program_sha256=programs[identifier],frozen_program_sha256=previous[identifier],independent_proof_sha256=digest(proof),source_terms_sha256=digest([c['source_term'] for c in proof['comparisons']]),native_terms_sha256=digest([c['native_term'] for c in proof['comparisons']]))
        proofs.append({'rule':case['rule'],**proof})
        # One original counterexample per first-seen capability: both the source
        # reader and compiled operand reader must reject a changed cardinality.
        caps={t['capability'] for t in a['tests'].values()}
        if caps-seen_caps:
            mutated=copy.deepcopy(a);test=next(iter(mutated['tests'].values()));req=test['require']
            field='items_satisfying' if 'items_satisfying' in req else 'items_found'
            req[field]=('none' if req[field]!='none' else 'one_or_more')
            rejected=False
            try:rejected=expanded_compare(ExpandedSource(source.components[binding['component']]),binding['definition'],mutated)['outcome']!='PROVED'
            except ValueError:rejected=True
            require(rejected,'Source comparator accepted cardinality mutant')
            rejected=False
            try:verify_program(mutated,compile_assessment_program(a))
            except (ValueError,AssertionError):rejected=True
            require(rejected,'Compiled operand reader accepted cardinality mutant')
            mutants.append({'rule':case['rule'],'capabilities':sorted(caps),'field':field,'source_comparison':'REJECTED','compiled_operand_comparison':'REJECTED'});seen_caps|=caps
        rows.append(record)
    from collections import Counter
    summary={'format':'scap-ng/frozen-draft-proof-batch/1','benchmark':benchmark,'source_pin':pin,'source_revision':PINS['revision'],'frozen_archive_sha256':SHA,'checkout_sha':subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip(),'verified_implementation':'5e847f8268697f7555a442256c06f5bfa48f4676','reader_sha256':hashlib.sha256((ROOT/'tools/v04_source_package_semantics.py').read_bytes()).hexdigest(),'expanded_reader_sha256':hashlib.sha256((ROOT/'tools/v04_expanded_source_proof.py').read_bytes()).hexdigest(),'selected':len(cohort),'outcomes':dict(Counter(r['outcome'] for r in rows)),'unchanged_frozen_authoring_program_pairs':len(proofs),'negative_mutants':mutants,'elapsed_seconds':time.perf_counter()-started,'scope':'Primary OVAL only; no complete policy/applicability/manual/runtime or release acceptance','cases':rows}
    (output/'independent-terms.json').write_text(json.dumps(proofs,indent=2)+'\n')
    (output/'proof-receipt.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ['benchmark','selected','outcomes','unchanged_frozen_authoring_program_pairs','elapsed_seconds']}),flush=True)
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--benchmark',action='append',required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--inputs',type=Path,default=Path('/workspace/recovery-20261029/inputs'));args=p.parse_args()
    require(hashlib.sha256(DRAFT.read_bytes()).hexdigest()==SHA,'Frozen DRAFT archive hash drift')
    subprocess.run(['git','-C',str(ROOT),'diff','--exit-code','10f4e35b331c622c14f6e3aa2bd4aa8981c810c1','--','schema','third_party','tools/v04_direct_converter.py','tools/v04_native_bundle_compiler.py'],check=True)
    require(subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip()=='5e847f8268697f7555a442256c06f5bfa48f4676','Use the exact published implementation')
    require(not subprocess.check_output(['git','-C',str(ROOT),'diff','HEAD','--','tools','schema','third_party'],text=True),'Dirty toolchain')
    mappings=load_mappings();validator=SourceValidator(ROOT/'third_party/scap-1.4-schemas/oval_5.12.3');schemas=build_validators(ROOT/'schema/v0.4.0')
    with zipfile.ZipFile(DRAFT) as archive:
        for i,b in enumerate(args.benchmark):batch(b,args.output/b,args.inputs,archive,mappings,validator,schemas)
