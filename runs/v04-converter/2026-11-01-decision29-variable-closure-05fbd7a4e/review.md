# Decision 29 — existing native Variable-expression closure

**Owner-approved A, 2026-10-31:** [exact authority](https://github.com/vanderpol/scap-ng/pull/268#issuecomment-6550047257).
This closes the existing native contract; it does not activate the isolated
canonical `function: {name, arguments, options}` candidate or add a scanner.
Prior [freeze counterexample](https://github.com/vanderpol/scap-ng/blob/05fbd7a4e49aea4f49e223552d18c9951531322d/docs/audit/v04-freeze-variable-expression-counterexample-20261031.json)
and R1/R2 bytes remain unchanged. That exact mutation now fails both structural
schema validation and direct program compilation. Historical 0.1–0.3 untouched.

## Exact supported grammar and evidence

Every declaration requires `kind: local|constant`, native `datatype`, and
`expression`; optional `title` is metadata. Constant declarations contain only
a literal expression. Every expression has exactly one discriminating key.

| Node / function | Arguments and allowed options | Derived datatype / restrictions | Actual support / original examples |
| --- | --- | --- | --- |
| `literal` | Scalar, homogeneous scalar array (including explicitly typed empty array), or exact `{datatype, value}` wrapper | Literal/declared type must agree; typed records are opaque data | Converter and static source reader; original constant/local-variable Self-Assertion sources |
| `variable` | One resolved local Variable ID | Inherits target declaration; cycles/unresolved references reject | Converter, dependency DAG and independent source reader; Apache and variable_component source |
| `values` | Exact `{object, field}`; Object inline with explicit capability or shared reference | Field must exist in capability mapping; constrain to its declared domain | Converter and static reader; original Windows registry/shell and Apache discovery |
| `concat` | Ordered array, **at least two** expression operands; no options | String components → string; no generic numeric/string coercion | Converter and independent static terms; pinned oval-def_concat_function.xml tst291; original XSD/Schematron ConcatFunctionType |
| `regex_capture` | Exact `{pattern: string, value: expression}`; one text operand | Text capture; explicit local declared result may be integer. Input text and extracted result remain distinct | Converter and independent static reader; Windows SV-278139 / Apache SV-214251; numeric capture boundary fixture |
| `unique` | Exactly one expression, not an argument list; no options | Preserves scalar element datatype/collection meaning; record transformations unsupported | Converter and independent static terms; Apache SV-214251 |
| `merge` | Exact `{delimiter: string, sort, order, values: expression}`; one collection expression | Scalar values → string; reject record operands. Sort document/lexical/numeric/natural; order ascending/descending | Converter and independent static terms; Apache SV-214251; NIWC merge fixture carries separate datatype defects |

No function above executes in the compiler. It preserves source operands,
counts, ordering, dependency/context and hashes. Actual live execution, Cartesian
populations, error/unknown/incomplete flags, regex dialect execution, lexical
conversion failures and scanner equivalence remain separate qualification.
No collection status or absent result becomes a synthetic zero or Item.

Inventory inspected schema, direct compiler, converter, source readers and all
pinned JSON fixture declarations: **72 locals**, four emitted native function
forms. Literal/Variable/collected-field leaves are not additional functions.
The source reader also has a bounded canonical count proof and the isolated
candidate names thirteen OVAL functions; neither establishes active native
executable support. Count/split/substring and multi-component merge/unique
canonical draft paths now stop with precise unsupported conversion diagnostics.
Existing frozen DRAFT content is not rewritten or newly qualified. The opt-in
research migration remains readable, but its envelope fails public validation
and direct native compilation.

## Explicit result-type boundaries

Pinned `oval-def_local_variable.xml` tst827 declares local integer with a string
literal `9`. Its existing explicit declaration cast is retained and its numeric
lexical form validated without changing the AST. Non-numeric text such as
`exec-timeout 5 0` cannot be an integer literal. A regex extracting `5` from that
line can have a declared integer result. No generic text-to-number inference
is added to comparison operands or constant arrays. Other unsupported cast
contexts fail closed rather than inventing conversion rules.

Typed arrays retain duplicates and order, with their explicit declaration for
empty arrays. Unknown/mixed literal types, invalid wrapper payloads, reference
conflicts and invalid field projections reject. Semantic validation supplements
JSON Schema where declarations/references/capability fields require context.
The direct compiler invokes the same version-local closure even when its caller
bypasses the document-schema front end. Literal record contents are opaque to
all dependency readers, including the independent package consumer.

## Source findings kept separate

**NIWC:** pinned `tests/fixtures/v04-direct-variables/oval-def_merge.xml`, SHA256
`e9cf10371c2d41a3c92087a93f62f597043828d0914a21c5ab4314f03fd8a6ef`.
Namespace `oval:navy.navwar.niwcatlantic.scc`. Local Variables1/2 declare integer
while merging integer collection1,4,5,2,3 with colon delimiter; output text is
colon-separated, not an integer. Variables3/4 also declare integer, and source
constant Variable101 declares integer for `abc`, `mno`, etc. Source bytes remain
untouched. Decision29 now rejects the two previously structurally comparable
merge cases for derived/declaration type conflict. The earlier **24 static-term
comparisons** and pinned counts remain intact; **22** remain currently compiled/
proved in this bounded fixture set, with **2** historical static comparisons
retained separately from current acceptance. Never describe that old structural
evidence as scanner-runtime success. No proof/hash baseline was rewritten.

**DISA:** no new original-source defect identified by this closure. The old
SV-278080 negative native mutation is not a DISA defect. Source intent issues
previously reported for Linux remain separate and unchanged. Numeric regex
result declarations are not categorically content bugs.

## Qualification and recovery

[New bounded original-source examples and provenance](https://github.com/vanderpol/scap-ng/blob/05fbd7a4e49aea4f49e223552d18c9951531322d/docs/examples/owner-variable-contract-20261031/README.md).
Existing three R1/R2 programs recompiled **byte-identically**; full before/after
digests are recorded with implementation evidence. No 100-mapping fingerprint,
frozen proof/hash, original source, R1/R2 archive or 65-stream library changed.

Focused tests cover unknown function/canonical envelope, malformed expressions,
wrong arity/options/type, typed arrays, references/cycles, field projection,
source examples, numeric capture, exact old counterexample, opaque records and
independent package smoke. The new test class is included in the maintained
schema test entry point without changing workflow behavior. Local focused99 tests and final affected22 PASS; maintained49/49 scripts PASS.
Exact source SHA, maintained/Board CI and final freeze recommendation are recorded
in PR268/#255 after the checkpoint CI completes.

**Freeze assessment while CI is pending:** Decision29 closes the demonstrated
grammar hole; qualification is pending exact-head CI. If those gates pass,
recommend GO for owner schema-freeze review, distinct from owner approval to
freeze/release. No final freeze/tag/merge here. Shell editor preferences remain
unapproved and no new annotations are activated. Scanner parity unqualified;
all_exist oracle and #260 candidate/licensing hold unchanged.

## Historical research gate input preservation (2026-11-01)

Decision29 source b7d39cbb14a360068e72227ecd52539833d5558c passed current
fast/schema/converter/compiler gates. A newly triggered C-research lane failed
with21 failures/117 errors across408 tests (one skip). Detached pre-Decision29
b21b10ed3 reproduces the same failure identities/counts: it read moving active
requirement enums and renamed mappings for unchanged historical C specimens.
This was existing drift, not a new native grammar or evaluation failure.

The compatibility checkpoint pins that research to exact archived requirement
schema bytes (dd26d0d1e40c60576f3d5de05799df11bf10d6b8, original SHA256 in
fixture provenance) and existing preserved original mappings. It does not
migrate C or restore any retired form to current native authoring. The current
Decision29/native schema/compiler checks stay strict. No workflow selection,
test expectation, original C specimen or accepted proof was relaxed/rebaselined.
All research cases run after restored class setup; the full source/export
steps reproduce the original19-Variable Apache graph in all three forms.
Exact final counts/CI appear in the final issue/evidence receipt.
