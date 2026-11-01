# Explicit optional Input example (#255/#269)

[Complete current authoring](optional-lock-screen.assessment.yaml) is a distinct
organization-defined demonstration, derived from the pinned DISA SV-278080
Registry example. [Provenance](provenance.json) retains the original pin and the
unchanged source-example digest. This is intentionally **not** the original DISA
policy, a tailoring override, or a new source-equivalence proof.

The Input declaration explicitly states datatype, cardinality and required.
`input_provided` appears only in a direct `if`/`else_if` condition. Providing one
integer permits the selected Test to consume it; definitive omission selects
the authored reason-bearing `not_evaluated` fallback. Provided empty is present,
but violates this example's exactly_one contract and produces binding error.
Use an explicitly zero_or_more declaration when a provided-empty population is
valid. False, zero and empty strings never mean omitted.

The compiler emits program format0.2 only for Assessments using this guard.
The supplied-binding harness exercises immutable explicit provision states and
selected-only result reads; it does not collect the Registry, execute the Test,
bind a real organization provider or establish compliance.

Reproduce the 25 adopted review cases and additional boundaries with:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools python tools/test_v04_input_presence.py -v
```

No source default, implicit empty list, implicit datatype conversion, dependency
binding syntax or collector was added. Compatible explicit field datatypes stay
valid. The former literal-value example, proof archives and corpus are unchanged.
