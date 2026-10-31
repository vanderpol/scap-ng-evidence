# Schema-freeze decision packet (#255/#268)

**NO-GO for an immutable 0.4 schema freeze at this checkpoint.** The maintained
fast gates and published download integrity pass, but the Variable expression
contract is not closed. This is separate from release, content-library and
scanner-runtime qualification. No freeze, merge or tag is performed.

## Concrete remaining grammar gap

The [minimal current-authoring counterexample](v04-freeze-variable-expression-counterexample-20261031.json)
is a negative mutation of the pinned, freshly proved Windows Server 2025
SV-278080 sample. It replaces expected integer 1 with a declared integer
Variable whose expression is `{unapproved_placeholder: {value: 1}}`.

[Measured observations and original-source provenance](v04-schema-freeze-observations-20261031.json):
current authoring validation reports **zero errors** and the program compiler
accepts the declaration. Independent original-source comparison returns
**UNVERIFIABLE/UNSUPPORTED**. No new proof is promoted. Assessment variables
currently accept generic objects; the isolated
`variable-function-expression.schema.json` explicitly says it is not bound to
the Assessment schema. A program/source preservation pass cannot establish a
closed authoring grammar or an executable meaning for an invented function.

Reproduce against the current branch:

```sh
PYTHONPATH=tools python - <<'PY'
import json
from pathlib import Path
from validate_native_json_schemas import build_validators, document_errors
from v04_native_bundle_compiler import compile_assessment_program
p = Path('docs/audit/v04-freeze-variable-expression-counterexample-20261031.json')
d = json.loads(p.read_text())
v = build_validators(Path('schema/v0.4.0'))['assessment.schema.json']
print('schema errors:', len(list(document_errors(v, d))))
print('compiled tests:', len(compile_assessment_program(d['assessment'])['test_instructions']))
PY
```

This is a native contract gap measured with a source-backed negative mutation.
The DISA original and its accepted proof remain unchanged. It does not establish
a DISA or NIWC source defect, nor does it change the separate all_exist oracle.

## True owner choice

| Option | Scope | Compatibility tradeoff |
| --- | --- | --- |
| **A — recommended:** close and validate the existing legacy Variable expression grammar | Bind a finite schema/validator to the currently supported expression vocabulary; reject unknown functions and invalid arities. Keep the isolated canonical-call candidate separate. | Preserves valid existing shapes and proof evidence; requires focused declaration/function positive and negative qualification before freeze. |
| B — activate the isolated canonical function-call grammar now | Author functions using the reviewed `function: {name, arguments, options}` form, with coordinated compiler/source-reader migration. | Requires explicit grammar authority, reversible migration and fresh proof for changed authoring/program hashes. Frozen proofs cannot be inherited by assertion. |

A numeric regex capture remains valid when its declared result is integer: the
text argument `exec-timeout 5 0` and extracted result `5` are separate types.
Neither option may ban that valid case or introduce generic silent coercion.
No unapproved function syntax or runtime evaluator was implemented here.

The editor-default review also proposes A/B preferences for new shellcommand
exit/stderr controls. Source-aligned **false** is recommended when those
preferences are reviewed; both choices must serialize explicitly, and original
OVAL values remain source-effective. Those optional metadata activations do not
justify asking again about Decisions 1–28 or changing the five existing controls.

## Closed corrections and separate qualifications

- #266 already approves explicit dependency invocation purpose. The schema now
  preserves optional `purpose: assessment|applicability` at that reference,
  rejects unknown explicit values, and never compares it to intrinsic target
  purpose or supplies an implicit default. Tests reuse one target from a Rule,
  applicability catalog and explicit dependency across all five classes.
- #264 concerns bounded field inheritance/compaction, **not** Variable function
  syntax. R1's six audit rows used the wrong issue label. R1 remains immutable
  and hash-valid; a uniquely named r2 packet corrects those metadata references.
- #265 remains the content-level Benchmark/applicability identity and metadata
  workstream. The 65-stream library is preserved, not regenerated or declared
  compatible with the new authoring contract by assertion.
- GO for bounded schema/compiler/source review of the published packet and
  the three identified samples. Existing toolchain candidate work under #260
  remains pinned to its own exact source/version and licensing decision.
- NO-GO for final release or a newly qualified complete content library here;
  those are outside this handoff. Scanner-runtime parity remains **UNQUALIFIED**.
