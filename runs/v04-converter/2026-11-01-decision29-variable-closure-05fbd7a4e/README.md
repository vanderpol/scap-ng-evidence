# Decision29 qualification and final handoff (#255/#268)

**Final source05fbd7a4e49aea4f49e223552d18c9951531322d: all12 triggered CI runs PASS.**
[Exact final-head IDs/results](ci-exact-head.json) include canonical-fast,
draft-schema, converter synchronization, native/JSON authoring checks, clean-extract,
current-design, Markdown, issue references and Board regression.
[Compatibility-head CI](ci-compatibility-head.json) separately records all12
PASS at dba98d4e8, including restored historical C research; those inputs are
unchanged by the final native scalar-domain guard. No active gate canceled.

Decision29 implementation is b7d39cbb14a360068e72227ecd52539833d5558c;
dba98d4e8e2f6c90af959146a682d3be98ed86ec pins historical research inputs;
05fbd7a4e49aea4f49e223552d18c9951531322d rejects unsupported unique record
transformations while preserving opaque record literals. Current native syntax
and compiler never reactivate retired C syntax or numeric capability aliases.

## Read the contract and examples

[Exact grammar table, support inventory, type boundaries and source findings](https://github.com/vanderpol/scap-ng/blob/05fbd7a4e49aea4f49e223552d18c9951531322d/docs/audit/v04-decision29-variable-closure-20261031.md).
[Two new original-source YAML/JSON examples and provenance](https://github.com/vanderpol/scap-ng/tree/05fbd7a4e49aea4f49e223552d18c9951531322d/docs/examples/owner-variable-contract-20261031).
The copied review.md retains its source checkpoint wording; relative links
resolve to immutable source commit05f. Final CI status is authoritative here.

Active native functions are concat/regex_capture/unique/merge, with literal,
resolved Variable-reference and collected-field operands. Exact required options
and type/arity/shape checks apply to document validation and direct compiler
bypass. Canonical function calls remain inactive; no runtime evaluator added.
Numeric regex-result integer declarations remain valid. Unknown placeholder
[public YAML CLI and direct compiler rejection](counterexample-rejection.json)
uses the unchanged old negative mutation; original DISA proof stays unchanged.

## Measured qualification

- Local99 focused tests PASS; final scalar-domain36, schema24, original-source7
  tests PASS. Independent package smoke includes typed arrays/capture/opaque records.
- Maintained49/49 script results and49 logs retained. Test source is identified
  per phase in manifest; exact final-head CI supplies final integration authority.
- Historical C research:422 total,421PASS/1optional skip; four export checks PASS.
  Native closure/name guards20PASS after the input pin. Original19-Variable
  Apache graph reproduces in all three research views, not scanner proof.
- Pre-Decision29 b21 and initial b7 CI reproduce identical21failures/117errors
  across408 tests. See baseline comparison/logs. Explicit archived schema bytes
  and preserved mappings fix moving-input drift; no C specimens/expected semantics,
  active native schema or workflow selection were relaxed.
- [All three R2 programs remain byte-identical](final-retained-programs.json).
  [Preservation receipt](preservation.json): no existing fixture payload,
  mapping fingerprint, historical0.1–0.3, proof baseline or R1/R2 ZIP changed.
  The65-stream library is neither regenerated nor newly qualified here.

## Namespace-separated source findings

**NIWC:** oval-def_merge.xml declares integer results for colon-delimited merged
text (Variables1/2), and Variable101 declares integer for alphabetic values.
Source IDs, source SHA and exact examples are in the review. Two historical
static comparisons are preserved separately from current compiler acceptance:
24 static anchors retained;22 currently compile/prove in that bounded set.
No scanner-runtime success was established for the contradictory declarations.
**DISA:** no new original-source defect inferred. The negative native mutation
is not a DISA defect. A captured5 may be integer despite text configuration input.

## Freeze and release disposition

**GO recommendation for owner schema-freeze review of the approved native surface:**
Decision29 closes the demonstrated grammar hole and final current gates pass.
The owner must separately approve any actual freeze; no merge/freeze/tag/release
is performed. Toolchain evaluation is bounded, the existing #260 candidate and
license/publication hold remain unchanged, and current65-stream content
qualification is separate. **Scanner/runtime parity remains UNQUALIFIED.**
Runtime populations, lexical conversion failures, collection/error/unknown flags
and optional Input invocation are not proved by these type/schema checks.
No all_exist oracle change or new editor defaults; shell preferences stay unapproved.
Future functions/domains need separate versioned approval and conformance evidence.

[PR268 final report](https://github.com/vanderpol/scap-ng/pull/268#issuecomment-6551030136)
and [#255 report](https://github.com/vanderpol/scap-ng/issues/255#issuecomment-6551249184).
