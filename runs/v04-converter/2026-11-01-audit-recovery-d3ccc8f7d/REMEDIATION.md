# PR #268 conformance remediation — 2026-11-01

**Release disposition: NO-GO; keep PR draft.** The revised29-decision audit is
18 VERIFIED,10 PARTIAL,1 UNPROVED,0 FAILED. Verification is bounded static
source/authoring/compilation/result-plan evidence, never native scanner parity.
[Machine matrix](v04-conformance-remediation-20261101/coverage-matrix.json) and
[CSV](v04-conformance-remediation-20261101/coverage-matrix.csv) classify every
decision and surface. The a8a9db703 read-only audit remains historical evidence.

## Corrections and independent checks

- Decisions4/23: public validation and direct compilation now check inline,
  shared, Variable-owned and Set Object selectors/parameters/record members and
  filters against capability and declared-reference types. Quoted version and
  version Variable positives pass; malformed versions/integer Variables reject.
- Decision11: library ingestion rejects shared SV-only/hash/missing-family names.
  Decision12: global placement needs actual consumers in two Benchmarks and an
  exact body/program-bound original-source receipt. A new nonpromoting qualifier
  validates original closure and independently proves the same technical
  Assessment against Windows Server2025 and Windows11. Repetition of one
  Benchmark, changed values, absent/stale receipts reject. Manual content stays
  unqualified without appropriate proof; no files are moved.
- Decision16: unguarded optional Input use and dangling Object Input now reject.
  Unused optional declarations and correctly typed required Input use pass.
  Safe optional consumption remains unavailable: the approved expression grammar
  has no Input-presence guard. This corrected failure is PARTIAL, not a claim
  that an omission/binding runtime has been implemented.
- The three original red modules pass: owner_identity_context (isolate identity
  failure with structurally valid Variable), direct_file_traversal (semantic
  target/control naming disambiguation), native_capability_names (compare frozen
  validation structure separately from approved help annotations).
- The general review guard now applies the approved 0.4 Test suffix while
  retaining the older version-specific prefix rule; both versions have regression
  coverage and the two fresh review examples pass.
- All610 generated Object property occurrences have resolved help, fixing263
  missing descriptions.264 default-annotation locations/38 controls and all100
  frozen generator fingerprints remain unchanged. The broader schema census
  still finds5359 missing resolved descriptions in7909 property occurrences;
  no universal schema-help completeness claim is made.
- Current documentation now uses the approved grammar; obsolete live examples
  are explicitly historical. No historical schemas or source proofs rewritten.

## Field datatype elimination and human-readable conversion

Fresh converter output emits **no field-comparison datatype declarations**.
Capability domains, YAML primitives, typed operation names and declared
Variables/Inputs carry these domains without a new inference/cast mechanism.
Variable/Input/literal-expression declarations remain distinct, including an
explicit integer regex-result declaration; captured5 can remain integer even
when the searched configuration line is text.

Default conversion compacts unique scalar fields only within one original AND
State, including explicit absence, and hoists complete inherited pairs. It keeps
repeated fields, records, scoped exceptions, cross-State boundaries and one/xor.
Original explicit datatype tokens and entity hashes are retained in provenance.
[Fresh examples and original proofs](../examples/conformance-remediation-20261101/README.md)
are separate from all historical examples/archives.

Independent vectors preserve4226 scalar predicate terms across99 of100 capability
contracts (the remaining contract has no scalar fields).80 float vectors remain
UNPROVED because the independent decoder lacks their semantics;6 structured
record sites are outside that scalar experiment and have separate original-source
record regressions.114 original special-datatype Tests and45 of51 YAML-record
Tests independently prove and compile;6 explicitly unsupported record/function
cases remain blocked. No scanner execution is inferred.

Complete removal from the accepted native grammar is **not lossless yet**:

| Accepted predicate | After stripping datatype | Pinned source legality |
|---|---|---|
| `{datatype: version, matches_regex: '1.*'}` | domain changes version→string | OVAL5.12.3 Schematron forbids regex on version |
| `{datatype: binary, case_insensitive_equals: ff}` | domain changes binary→string | OVAL5.12.3 Schematron allows binary equals/not equal only |

[Exact counterexamples, XPath and source lines](v04-conformance-remediation-20261101/datatype-retirement-counterexamples.json)
justify retaining the existing explicit mechanism for compatibility. These are
native-contract exceptions, not newly alleged DISA/NIWC content bugs. No new typed
operators were invented. Recommended owner decision: reject the two unsupported
operation/domain combinations, then retire the redundant qualifier after float
and structured-domain coverage is independently complete. This proposal is not
adopted by this implementation.

## Exact verification and preservation

- Maintained canonical/schema gate:49/49 scripts PASS; schema integration52 tests
  PASS in that run, then54/54 PASS after adding the retirement counterexample
  and versioned review-guard regressions; affected datatype module3/3 PASS.
- Audit-focused13 modules:103 tests PASS; native capability names5 tests PASS.
- Eight additional original-source modules:43 tests PASS.
- New shared qualification:4 tests PASS, including actual library consumers and
  current/missing/stale receipts; integrated in the maintained schema gate.
- Historical YAML-record suite at exact creation pin379d2cc16:8 tests PASS with
  its full original authoring/program hash assertions. Current suite retains
  source pins, exact frozen evidence-file SHA256, all source/native term hashes,
  admission and diagnostics. New presentation AST/program hashes are not claimed
  to equal the old syntax. The frozen evidence JSON was not edited or rebaselined.
- Existing test_scap_ng_library setup fails before tests on legacy `purpose`
  content at both a8a9db703 and this worktree; that historical fixture was not
  rewritten to manufacture a pass. It is outside the maintained49-script set.

R1/R2 archives, accepted source/program proofs, existing65-stream library,
original sources and unrelated worktrees remain preserved. No merge/freeze/tag/
release/full-corpus regeneration was performed. Publication/hosted-CI receipts
are tracked in PR#268 and #269; local green does not establish hosted CI status.

## Remaining findings and concrete next decisions

All PARTIAL/UNPROVED rows have an explicit disposition; they are **not resolved
by relabeling**. Decisions7/27/28 need actual editor TextDocument/save/UI/traversal
host evidence (scap-ng-vscode#7/#1/#2); the approved offline-adapter fallback is
not host proof. Decision24 needs a complete Rule informational/manual report with
observed evidence. Decisions9/15/17/19/20 need a real qualified native collector/
invocation runtime and positive/negative empty/incomplete/unknown/error traces.
Decision19 remains UNPROVED. Selector-case ledger separates2 documented Windows
capabilities,3 without native selectors and15 unproved cases including independent
EnvironmentVariable; no API behavior was invented (Decision22).

The narrow semantic decision needed for Decisions15/16 is **how an Assessment
explicitly guards an optional Input**. Proposed minimal contract, not implemented:
a static Input-presence condition identifying the declared Input, true only when
provided (including an intentionally empty list), false when omitted; selected
branches alone consume it, references close statically, and indeterminate binding
propagates error/unknown with reason. An alternative is to prohibit optional
Input consumption entirely in0.4. The current fail-closed behavior safely exposes
this gap rather than silently defining either policy. Owner review must choose
and approve exact syntax/binding semantics before guarded consumption is enabled.

DISA and NIWC source namespaces stay separate in the original-proof receipts.
Known NIWC exact ds:uri catalog bindings now produce normal-mode warnings when
unambiguous; missing/ambiguous/conflicting/nonlocal bindings still fail. No missing
content is fabricated and warning admission is not independent source VERIFIED.
No new source-content defect is inferred from a native-contract limitation.

## Interrupted-publication recovery and pack reproducibility

Recovery confirmed implementation `fecb541f9c226706738fd3d113ef1047f37faaaf`
was already pushed. Its13 hosted runs (11 distinct workflows) all passed; the
previous local-only comment is superseded. Fresh recovery ran38 focused tests,
all passing, without repeating the maintained CI or the65-source corpus.

Two fresh external metadata exports at that identical source commit had different
manifest hashes due solely to JSON property ordering originating in selector
sets. The editor's integrity guard correctly rejected the old pin. The pack
exporter now sorts object keys, while preserving every array and schema value.
A separate-process regression compares every exported byte under two Python
hash seeds, checks100 contracts and every resource digest. The six-test metadata
gate passes. Historical packs, generator fingerprints and proof files stay intact;
the corrected export receives a new source/editor pin and separate evidence run.
This closes a reproducibility defect, not any outstanding runtime/UI obligation.
