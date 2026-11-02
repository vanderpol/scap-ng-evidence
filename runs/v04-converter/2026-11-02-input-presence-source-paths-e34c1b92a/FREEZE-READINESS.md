# Final 0.4 schema-freeze readiness audit (#255/#268)

**Full schema-family readiness: NO-GO. No freeze performed.**
The adopted Input guard is implemented; compatible field datatypes remain.
[Machine audit](v04-schema-freeze-readiness-20261101.json) covers all29 owner
decisions,32 root schemas and230 version-local references; structural/reference
closure passes. Green compilation alone is not complete language acceptance.

## Genuine language-contract gaps

| Finding | Measured scope | Required before full schema freeze | Owner decision? |
| --- | --- | --- | --- |
| LC-SELECTOR-CASE |15 capability/API cases lack documented case contracts; registry/file are documented separately | Complete per-selector/API-backed contracts under approved Decision22, including platform-dependent environment-variable lookup. Do not invent a universal case flag. | No new vote; approved rule, unfinished contract research/documentation |
| LC-NATIVE-RESULTS | Test/State/Entity Result schemas retain OVAL check vocabulary and Test.states lexical addresses absent from native require; error Test may omit reason | Adopt and implement one current native Result wire mapping with source locations, native requirements, reason/evidence and record correlation | **Yes: concrete A/B below** |

The second finding is a source/result schema contract problem, **not** merely
an absent scanner test. The machine audit contains a schema-valid Test Result
with `state_refs: ['registry-value-test.states[0]']`, `check_existence: all_exist`,
`check: all`, `state_operator: AND` and outcome error without reason. Current
authoring for that Test instead has `require.fields` and no states array.
`state-result.schema.json` explicitly describes the old0.3 lexical location.
No collector is needed to demonstrate this drift. Raw collection status may
retain incomplete as an observation; its final technical error/reason mapping
must not be confused with a native all_exist authoring option or source provenance.

The initial independent audit's static18/10/1/0 score remains historical.
It is not promoted to29 language-complete or scanner-proved by the new tests.
Decision16's missing guard grammar is closed; Decisions7/9/15/17/19/20/22/24/27/28
still have explicitly separate runtime/editor obligations. The new machine audit
records language blockers per decision rather than hiding them in one score.

## One genuine owner decision: native Result wire migration

Both options keep0.1–0.3 and existing proof/archive bytes immutable and preserve
technical truth, Item/record correlation, redaction and evidence completeness.
No migration or new scanner is implemented under this audit.

| Option | Concrete change | Tradeoff |
| --- | --- | --- |
| **A — recommended: clean native0.4 Result vocabulary** | Replace state_refs/state_results/state_ref with require_refs/require_results/require_ref; locations are RFC6901 pointers rooted in the owning Assessment (`/tests/<id>/require/...`). Represent native Item/field requirements and canonical operators; keep original OVAL controls solely in migration provenance. Error/incomplete-result paths require meaningful reason/evidence. | Breaking change to the current unqualified0.4 strawman wire schema; best fit before a freeze. Needs bounded schema/semantic/projector tests and human review, no corpus rebaseline. |
| B — retain existing property names for compatibility | Keep state_* keys but explicitly redefine their payloads as source-bound native require pointers; replace OVAL check tokens with native requirement semantics and require error reasons. Document that these are comparison locations, never an authored State registry. | Smaller key migration, but intentionally keeps confusing legacy-shaped vocabulary. Still requires a reviewed mapping and compatibility tests. |

For the actual source-backed lock-screen Test, a candidate A reference is
`/tests/verifies-prevent-enabling-screen-slide-show-is-set-enabled-test/require/fields/value`.
It points at the declared predicate, rather than inventing `states[0]`. When an
Input supplies the operand, the result also identifies the immutable binding
set and source; no publisher value is silently overridden. The new provision
trace schema already supports that binding evidence. A Result migration must
define group/record pointers and inherited complete requirements just as
precisely, and must distinguish field absence from missing/error collection.

## Future verification, not new language votes

- Native provider/dependency binding adapters; real collection, arrays, Variable
  functions, Set/Filter execution and per-invocation cache isolation.
- Actual incomplete/error/unknown versus absence traces and all_exist source
  qualification. The separate OVAL reference-oracle discrepancy remains held;
  it is not solved by grammar acceptance or a proof rebaseline.
- API behavior on supported hosts after case contracts are documented.
- Complete Rule informational/manual follow-up with real observed evidence.
- VS Code TextDocument/save/undo, Structured/Guided UI, real screenshots and the
  required bounded regex/sample playground. The offline adapter is a separate
  tested foundation, not host/UI evidence.

Retaining compatible field datatype declarations closes the retirement question
for this task. Float/record source proof and the old domain-stripping
counterexamples remain qualification limits, not requests to remove datatype or
reopen its owner decision. Freeze/merge/release approval is not requested here.
PR268 remains draft; no65-stream generation or proof rebaseline occurred.
