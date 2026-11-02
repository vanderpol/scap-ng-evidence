# Native 0.4 Result A adoption (#255/#269)

Owner selected **A on 2026-11-02**, adopting the published clean native wire
migration in the [prior immutable A/B review](v04-schema-freeze-readiness-20261101.md).
[Decision record](https://github.com/vanderpol/scap-ng/issues/255#issuecomment-6566907992).
This is an intentional break to the unqualified 0.4 strawman Result wire contract.
It does not change 0.1–0.3, authored Assessment predicates, scanner truth rules,
proof baselines, or the retained compatible field-level datatype decision.

## Concrete mapping and source provenance

| Previous draft wire | Adopted 0.4 wire |
| --- | --- |
| `state_refs`, `state_results`, `state_ref` | `require_refs`, `require_results`, `require_ref` |
| lexical `test.states[0]` | canonical RFC6901 `/tests/<escaped-id>/require/...` |
| `check_existence`, `check`, `state_operator` | explicit native `items_found`, `items_satisfying`, `field_requirement`; logical `and/or/one/xor` |
| State/Entity comparison schema | Require/Field Result schema; former resource URLs reference the native definitions |
| error without cause | nonblank reason and resolvable evidence references; incomplete/error collection additionally requires stop reason and diagnostic code/message |

The [bounded real-source example](../examples/native-results-20261102/README.md)
retains the exact SV-278080 Assessment with its DWORD1 publisher operand. Its
native reference is `/tests/verifies-prevent-enabling-screen-slide-show-is-set-enabled-test/require/and/1/fields/value`.
The old `states[0]` counterexample is rejected. Observations in this example are
explicitly synthetic, supplied review evidence, not collected target evidence.
Original OVAL State names/check tokens remain historical conversion provenance,
not accepted native Result fields. Original OVAL namespace/specification context
and immutable ZIP/source digests remain in the original-backed example review
manifest; native Result adoption does not reinterpret original OVAL checks.

Pointers are rooted in the owning Assessment body (without the outer
`assessment` wrapper); `~` and `/` escape as `~0` and `~1`. Logical array positions
are preserved, including repeated equal predicates. Only actual requirement,
record and scalar predicate nodes are addressable. Operand objects/literal
records are opaque data. Item-relative `record_ref` identifies a typed record at
`/fields/<escaped-field>` or its canonical array index. Child rows and scalar
observations must stay within the same source and Item record instance.

Complete field requirement pairs inherit from the nearest explicitly declared
Test/group/record scope; a full field pair overrides them. Source operation,
compatible datatype, array `value_match`, record counts and effective pair with
its `requirement_ref` must agree with source. Input operands identify an actual
immutable binding snapshot and invocation. Variable operands need explicit
same-invocation supplied values; no Variable function execution is claimed.

`items_observed` is an explicit population count or `unknown`; evaluated and
retained counts are separate. A true absence assertion needs confirmed complete
zero population or complete field observation. An incomplete/error collection
cannot become a non-error Test. Missing evidence, failed acquisition and a
retention cap cannot silently establish absence. Retained Item identity,
capability, typed values, source operands, comparison scope, redaction and count
consistency are checked without recomputing outcomes.

## Implementation, compatibility and verification

`tools/v04_result_contract.py` projects source metadata onto supplied native
observations and validates native Test/Assessment Results. It never calculates
comparators, truth, counts, defaults, collector completeness, bindings or
retention limits. Parent invocation and binding identity are validated against
children. Actual expression trace evaluation and Variable/provider execution
remain separate future scanner work.

The focused suite has21 test methods; the maintained schema gate has100 tests.
All49 maintained scripts pass. Five prior sample programs are byte-identical.

`tools/test_v04_result_contract.py` covers positive source-backed Results and
negative wire, pointer, record, inheritance, domain, binding, redaction,
completeness, evidence, identity and count mutations. It joins the existing
maintained schema gate. The readiness auditor independently validates the
source-backed parent sample and six negative mutations, plus legacy rejection.

The four original active Result schema payloads are preserved verbatim under
`tests/fixtures/v04-native-results/pre-migration-schemas/`. Their existing
normative hashes remain unchanged; no baseline is rehashed to accept a new
floor. Current native behavior has separate focused tests. All historical
schemas and source/proof archives remain unchanged. Resource URL compatibility
wrappers deliberately do not accept the former wire fields or convert them.

Rejected B: retaining misleading `state_*` names while redefining payloads.
Also rejected: automatic legacy conversion, invented State registries, inferred
counts/empty populations, implicit casts and cross-record/invocation evidence.
No new owner decision is needed for this adopted migration. Draft PR268 remains
unmerged; no freeze, release, 65-STIG generation or proof rebaseline is authorized.
