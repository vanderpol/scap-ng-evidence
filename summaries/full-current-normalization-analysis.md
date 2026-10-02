# Full-current normalization experiment — retained analysis

This document is the durable analysis retained from the large generated normalization/compiler evidence formerly stored in `vanderpol/scap-ng`.

The raw reports are intentionally **not** treated as long-term Git assets. The durable record is the compact metrics, conclusions, hashes/tree identities, source pins, and reproduction workflow summarized here.

## Source and reproduction

- SCAP-NG historical recovery tag: `pre-rebaseline-2026-10-02`
- Pinned NIWC source revision: `8c8e5dff860af6b1290ee9273a282db24278f8d5`
- Source packages: 65
- Generated native Benchmarks: 65
- Blocked source packages: 0
- Generator/normalizer/compiler workflow: `.github/workflows/scap-ng-full-current-native-normalize-compile.yml`
- Current workflow now retains generated output as an Actions artifact rather than committing bulk output to `main`.

The historical generated evidence tree was:

`research/iterations/003/evidence/full-current-native-normalize-compile/`

and the companion review tree was:

`research/iterations/003/review/full-current-native-normalized/`

The pre-rebaseline tag preserves both exact historical trees.

## Exact-normalization findings

Across the 65-package corpus:

- 16,125 referenced Assessment instances existed before exact normalization.
- 10,633 Assessment definitions remained after exact normalization.
- 5,492 duplicate Assessment definitions were avoided.
- This is a **34.06% reduction in repository Assessment definitions**.
- 2,987 exact duplicate groups were identified.
- 8,479 local Assessment files were removed by the normalization experiment.
- 6,140 Rule files and 42 applicability files were rewritten to use normalized references.
- 99 near-duplicate review groups were identified.
- 45,794 Rule-level near-duplicate candidates were reported for further analysis.

The principal demonstrated benefit is therefore **maintenance-definition reuse**, not necessarily smaller independently distributed packages.

## Standalone bundle-size finding

The normalization experiment compiled all 65 Benchmarks before and after normalization.

- Before: 21,982,501 bytes
- After: 22,079,306 bytes
- Net change: **+96,805 bytes**
- Aggregate change: approximately **+0.44%**

Thus, exact repository normalization reduced duplicate definitions substantially while making the aggregate set of self-contained standalone bundles slightly larger.

This is not contradictory. Each distributed Benchmark remains self-contained, so cross-Benchmark repository reuse does not automatically translate to smaller independent bundle payloads. The normalization value is primarily reduced maintenance duplication and shared-definition identity.

Per-Benchmark comparison:

- 13 Benchmarks became smaller.
- 52 became larger.
- None were byte-identical.
- 197 compiled object instances were removed in aggregate.

The largest reductions were observed in:
- Solaris 11 SPARC: -38,248 bytes and 59 fewer objects.
- Solaris 11 x86: -38,221 bytes and 59 fewer objects.
- Microsoft Windows Server DNS: -38,001 bytes and 28 fewer objects.

Examples of modest growth included:
- RHEL 9: +19,158 bytes while removing 1 object.
- Oracle Linux 9: +17,646 bytes while removing 1 object.
- Windows 11: +12,384 bytes with unchanged object count.

This supports treating **repository reuse** and **distribution/package size** as separate optimization goals.

## Signing experiment

The compiler produced 65 self-signed CMS test bundles.

This demonstrated signing mechanics only. The recorded trust state was:

`self-signed-experimental-no-publisher-trust`

It does not demonstrate a publisher trust model, certificate profile, key-management policy, or production signature-validation ecosystem.

## Large raw reports

The historical evidence included several generated reports whose size makes them poor long-term Git assets:

- `normalizer-report.json` — 78,393,021 bytes — Git blob `961589420a1680f00c16e4373218864682897696`
- `native-schema-census.json` — 29,400,845 bytes — Git blob `e0fc3423fea78baee1e143938b83fc3a6f11fd97`
- `schema-validation-before-normalization.json` — 4,327,368 bytes — Git blob `ffb9fd2d8f3969abc61fb02d7bc40403c52229f6`
- `schema-validation-after-normalization.json` — 3,181,038 bytes — Git blob `5d363adbf4862ade3bf3cff71bb33aa519d7c354`

The compact compiler and experiment summaries are sufficient to retain the principal measured conclusions above. The raw reports remain recoverable from the pre-rebaseline history and can be regenerated from the pinned inputs/workflow.

## Retention decision

For this class of evidence, the preferred long-term model is:

1. analyze the complete raw output;
2. retain compact decision-relevant metrics and conclusions;
3. retain immutable source/tool pins and raw-output identities/hashes;
4. retain representative excerpts only when needed to explain a finding;
5. make generation reproducible in CI;
6. avoid committing large raw generated reports to Git unless they contain unique information that cannot be summarized or regenerated.

If later Board or implementation work requires a raw detail not represented here, regenerate the evidence from the pinned inputs or recover the historical blob, then update this analysis with the durable conclusion that was missing.
