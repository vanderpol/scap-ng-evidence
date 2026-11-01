# 0.4.0 editor-default implementation ledger

Refs [#269](https://github.com/vanderpol/scap-ng/issues/269), [#244](https://github.com/vanderpol/scap-ng/issues/244), [#255](https://github.com/vanderpol/scap-ng/issues/255), [draft PR #268](https://github.com/vanderpol/scap-ng/pull/268), [editor #7](https://github.com/vanderpol/scap-ng-vscode/issues/7).

Recovered source: `05fbd7a4e49aea4f49e223552d18c9951531322d`. Owner decisions 1–29 remain binding. This checkpoint changes presentation metadata only; no merge, freeze, release, scanner-runtime claim or library regeneration.

## Exhaustive dispositions

[Complete 468-row CSV](v04-editor-default-dispositions-20261101.csv) includes all **453 original controls across 100 capability contracts**, plus **15 source declarations with no native control**. Each row records source QName, exact original XSD path/line/hash, schema pointer/capability, effective OVAL default, new-authoring suggestion, explicit serialized representation, applicable context and reason. Repeated pointers are aggregated into **38 distinct activated controls**, with **264 annotated schema locations** across **434 original audit rows**.

| Class | Rows (including source-only) | Treatment |
| --- | ---: | --- |
| A | 249 | Source-corresponding suggestion within the stated context; preserve source effective values on conversion. |
| B | 10 | Existing approved NG preference: mandatory source check has no default; reporting is NG-specific; new-authoring local filesystem differs from omitted source all. |
| C | 16 | Datatype is derived, never a constant default; 15 source-only declarations have no native UI control. |
| D | 186 | Existing explicit group/Set/Filter/traversal only; 11 disabled-traversal rows have no activated path. |
| E | 0 | No new owner semantic vote identified by this bounded default crosswalk. |
| F | 7 | Held canonical Variable function options remain inactive under Decision 29. |

These are default-correspondence classifications, **not proof of arbitrary OVAL conversion equivalence**. Error, unknown, incomplete, missing and expected-population contracts remain unchanged. Source-backed independent semantic verification remains separate.

## Activated versus proposed

**34 controls** permit safe hide-defaults; **four additional controls** (condition logic, Assessment logic, traversal kind and depth) are explicitly aggressive-preview only. Hidden controls always have actual serialized default values; overrides, diagnostics, missing values and exceptions remain visible. Hiding operator dropdowns never hides their operands or predicates.

The five original controls (six scalar values) remain: Item existence, Item satisfaction, complete paired field requirement, reporting and filesystem. New controls cover source-scoped collection parameters, selector `equals`, multivalue matching `every`, and present Set union/Filter exclude. The owner explicitly approved shell exit-status/stderr flags `false`/`false`; these are explicit Boolean **new-authoring** choices, with original XSD acquisition explanations retained.

Operators represented by YAML keys use `x-scap-ng-authoring.default_key`, not an invalid JSON Schema scalar `default` on an object. The consumer derives valid choices from schema alternatives and restrictions. Variable/array matching carries a pointer to the actual schema applicability condition. No separate enum registry is introduced.

Traversal disabled means omit the optional construct: no fabricated traversal, `recurse: none`, null depth or `-1`. Present Unix traversal suggests symlinks-and-directories; Windows suggests directories; hierarchical traversal has depth only. Depth unlimited applies only to present traversal. Explicit group defaults do not wrap direct field maps or single-Test Evaluate. Construct creation requires an explicit author action and supplied operands.

Converter behavior is untouched: explicit source values and omitted-source effective values remain authoritative. In particular source `all` stays `all`, `defined` becomes `same`; the editor's new-authoring `local` suggestion cannot alter conversion. Source Test `check` remains mandatory; `var_check` omission remains documented text, not an invented XSD default. No runtime component consumes these UI annotations as fallback semantics.

## Reproduction and boundaries

```sh
python tools/classify_v04_editor_defaults.py --output /tmp/dispositions.json --table /tmp/dispositions.csv
python tools/test_v04_schema_draft.py
python tools/build_v04_editor_metadata_pack.py --output /tmp/scap-ng-editor-pack
```

The exporter requires committed schema/tools and a new destination. It produces an offline pack with exact source SHA, checksummed schemas/mappings/vocabulary, a manifest and an externally pinned profile. The editor consumes an explicitly selected local pack; upstream assets/code/content are not vendored into the separately licensed editor repository. Updating the pin deliberately enables compatible metadata changes; hash/version mismatch fails closed.

`editor-default-policy.json` is a version-local **generator build recipe** for annotations, not a consumer-side default registry. Static schemas contain corresponding annotations directly; generated schemas receive the recipe at generation. `authoring_metadata=False` exists only to verify original full generator fingerprints. All 100 accepted fingerprint hashes remain untouched. A separate presentation-erased shared-schema hash guard is derived from the recovered source and confirms validation structure did not change (enum/const instance payloads remain opaque).

Editor #7 receives a tested offline adapter and source-range edit foundation. The dedicated editor repository was documentation-only at `2f12e81b38a996e55e115ec72caa02e49099ad53`: no extension host, `CustomTextEditorProvider`, shared `TextDocument`, `WorkspaceEdit`, graphical views or installable VSIX exists. Consequently no genuine editor screenshot or native undo/redo claim can be supplied. Issues #1/#2 must provide that host/UI vertical slice before the screenshot acceptance criteria can be met. This is an implementation dependency, not a new semantic owner vote. Full Assessment evaluation remains unavailable; regex/sample preview remains tracked under #7.

R1/R2 frozen archives, original source bytes, previous proof programs/hashes, historical 0.1–0.3 grammars and the 65-stream review library are unchanged. Raw detailed rerun JSON and logs are retained in the new #269 evidence packet, never written over R1/R2.

## Validation checkpoint

Maintained canonical/schema probe:49 scripts,48 passed initially; the sole failure was a date assertion pinned to2026-10-31. Updated it for this annotation revision; affected five-test gate passes. Final expanded schema entry point:38 tests PASS, including all100 preserved generator fingerprints, every activated default/schema pointer, source provenance and shared normative-structure guards. Unchanged bounded source-import smoke and compilation pass through generator tests. Editor adapter build and eight focused cases pass before pinned-pack integration. Detailed logs and exact publication SHAs are tracked in #269; hosted CI status is reported separately, never inferred from local results.
