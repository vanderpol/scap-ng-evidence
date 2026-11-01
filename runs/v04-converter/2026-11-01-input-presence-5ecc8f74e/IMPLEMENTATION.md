# Adopted optional Input presence guard (#255/#269)

**Owner adoption:2026-11-01.** The owner approved implementing the published
design and25 review cases, explicitly retaining compatible field datatypes and
prohibiting merge/freeze/release/corpus generation/proof rebaseline. Authority:
[#255 adoption record](https://github.com/vanderpol/scap-ng/issues/255#issuecomment-6564386515).
The earlier design-only hold is superseded. No further guard semantic vote is
needed. [Immutable original design and cases](https://github.com/vanderpol/scap-ng-evidence/tree/b2c633a1378feaa0a318b34a76843e591e02ddb3/runs/v04-converter/2026-11-01-audit-recovery-final-receipt-37b614858)
remain unchanged.

## Explicit language and supplied-binding behavior

`if: {input_provided: declared-input}` is accepted only as a direct evaluate
if/ordered else_if guard. It is not a standalone expression, a general Boolean
operand, an applicability guard, a predicate operation, or a declaration.
Every branch resolves statically. Optional Input use requires positive dominance
at every reachable consumer, through Test, shared Object, Variable and Set/Filter
dependencies. A guarded use does not authorize another use elsewhere; two
optional dependencies need two enclosing guards. Literal records remain opaque.

Inputs require explicit datatype/cardinality/required. Native domains and the
existing typed `constraints.allowed` vocabulary are closed: unsupported controls,
unknown constraints, invalid declared types and hidden `default` fields reject.
This rejects undefined controls rather than giving them an invented execution.
Direct Input operands in Object selectors remain unsupported by their existing
grammar. Transitive support is demonstrated through the already-supported
Variable → Object Set/Filter → Input path, without widening acquisition syntax.
Dependency Input-binding syntax is not invented; unsupported fields reject.

| Explicit provision observation | Result |
| --- | --- |
| Definitely omitted optional Input | false; select the authored fallback |
| Valid supplied population, including permitted empty | true; select then |
| False, zero or empty string in its correct domain | supplied, never omitted |
| Invalid cardinality/domain/allowed values; omitted required Input | error with source and reason; no fallback |
| Provider cannot establish provision | unknown with source and reason; no fallback |
| Provider/binding failure | error with source and reason; no fallback |
| Pending resolution | no final result; explicit PendingInputBinding |

`bind_inputs` is an explicit local supplied-evidence API, not a new provider or
wire format. It requires a provision entry/source for every declaration; it never
infers omission from a missing mapping entry. Snapshots are immutable canonical
bytes containing contracts, states, sources and invocation identity. Invalid
invocation bindings cannot be hidden in an unselected branch. Definitive binding
errors dominate unresolved provision independently of Input name order; otherwise
pending provision yields no final result. Uncertain required provision propagates
unknown. Values are validated without substituting, parsing or casting them.

The selected-only resolver harness reads only the selected Test/dependency
outcomes, with an invocation-local cache. Supplied cached outcomes must identify
the same immutable binding invocation. This proves dispatch/branch behavior, not
collector, Variable-function, provider or Test execution. Selected false/error
never falls through to manual follow-up. Reasons and explicit follow_up survive
the compiled plan and schema-shaped trace; no implicit child invocation reference
is invented when projecting dependency evidence.

## Versioned compiled contract and compatibility

Only Assessments using the new guard emit
`scap-ng-0.4.0-native-assessment-program/0.2`, with explicit
input_presence_version1, Input contracts, consumer locations and a separate
result_requires.inputs set. `read_input_presence` preserves the local Input ID
and exact source path. The independent package reader reconstructs the guard,
source obligations, requirements and program version without compiler imports.
Container hashes alone do not admit a modified guard, contract or version.

Guard-free source continues to emit program0.1 with its original fields and
bytes. A0.1 program/result-plan cannot carry the new instruction. No old source
or archive is silently migrated. Compatible explicit field datatypes remain
valid; the two previously recorded retirement counterexamples are retained.
No datatype removal or source-invalid operation normalization was performed.

The expression-invocation schema now has an explicit input_presence trace kind,
binding digest/source fields and reason requirements for unknown/error, plus
logical traces and ordered conditional branch index. This is an additive,
owner-approved provision trace contract. It does not resolve the separate legacy
Test/State/Entity Result wire gap found by the full freeze audit.

## Source-backed before/after and rejected alternatives

Before: the immutable original-backed SV-278080 example compares DWORD value1.
After: [complete distinct demonstration](../examples/input-presence-20261101/README.md)
uses an optional integer Input and explicit manual-follow-up fallback. It has a
different policy identity and does not claim source equivalence, change the DISA
Rule, or authorize tailoring a publisher value. The provenance retains the exact
original ZIP/source-example digest; DISA and NIWC namespaces remain distinct.

Rejected: omitted→empty, falsey→omitted, implicit defaults, generic and/not guard
inference, eager guarded acquisition, unknown function/constraint acceptance,
unversioned bytecode and cross-invocation cache reuse. Pinned OVAL external_variable
at oval-definitions-schema.xsd:551 is context, not authority for inventing native
Input-presence semantics; adoption comes from the owner design above.

## Verification and preservation

`tools/test_v04_input_presence.py` executes all25 adopted review cases plus
public/direct/independent package, provenance, snapshot, version-tamper, opaque
record, selected-order and distinct-example boundaries. The maintained schema
entry point imports these tests. Existing proof/semantic fingerprint fixtures
are not rebaselined: the original shared-schema hashes remain fixed, with only
the explicit adopted Input/guard/trace deltas projected away for comparison.
All100 generated capability fingerprints stay pinned. Five preexisting sample
programs compare byte-identically against independent checkout37b614858.

The first maintained pass exposed two integration issues: legacy unsupported
operators lost their specific exception type, and expression-only reconstruction
prematurely resolved mutated data references used by existing negative proof
tests. Both were corrected without changing those tests, source proof floors or
negative coverage. The final maintained and hosted results, exact commits and
evidence are recorded in PR268/#255/#269 and the development checkpoint.

Language acceptance, supplied bindings, static source proof, actual native
runtime and editor host are distinct qualifications. No live-target, full Rule
report, actual provider or VS Code UI claim is made.
