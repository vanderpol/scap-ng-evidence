# SCAP-NG 0.4 native library normalized-review candidate

Separate, non-normative review delivery for [source issue #261](https://github.com/vanderpol/scap-ng/issues/261), O2/O4/O7/O8, and [editor issue #3](https://github.com/vanderpol/scap-ng-vscode/issues/3). No final release/tag, schema change, source-proof promotion, scanner-runtime claim or project-license assertion.

## Download and open

- [Normalized library ZIP](scap-ng-v04-normalized-library-review.zip): **44,544,308 bytes**, SHA256 `a01ea589501bf8a53e5df68e50ca9478f19543d2bd3844546667fde743c28d8c`.
- [Exact source toolchain ZIP](scap-ng-0.4.0-toolchain-ff69d46b36e0.zip): **24,022,349 bytes**, SHA256 `adbb52973ce608ce918e840658ead7b3265c601b43dc71a466da4e8257fe421d`.
- [Checksums](SHA256SUMS.txt), [manifest](manifest.json), [CLI/editor contract](CLI-CONTRACT.md).

Unzip the review library and open its `content/` folder for authoring. YAML is source; `records/` retains original/proof/warning ledgers and `metadata/` contains disposable generated navigation/index data. The index is rebuildable offline from source plus durable sidecars. Original XML/ZIP sources remain linked to the pinned published DRAFT; no evidence service is required for native authoring/compilation. Extract the toolchain separately and install its pinned dependencies in your Python 3.12 environment. Run its `tools/scap_ng_library_cli.py` against the review `content/` directory. Analyze/check do not write; apply requires reviewed diffs and explicit `--write`.

## Preservation and measured acceptance

One intentional out-of-place acceptance consumed the exact [published DRAFT](https://github.com/vanderpol/scap-ng-evidence/tree/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download), SHA256 `a09ee9a13cdfeeb1b8599eab61308e935a19b99eb62eadafd32002d13d90f8bd`. No source conversion or OVAL proof replay.

| Inventory | Count |
|---|---:|
| Original streams / Rules | 65 / 8,892 |
| Compiled native programs preserved | 6,817 |
| Accepted static proof triples preserved | 4,258 |
| Native candidates still UNVERIFIED | 2,559 |
| Blocked automated / manual originals | 422 / 1,653 |
| Editable native Benchmarks / applicability registries | 60 / 60 |
| Native Rule / Assessment files | 6,817 / 6,817 |
| Native YAML files byte-identical | 13,754 |
| Native YAML bytes changed / sharing promotions | 0 / 0 |

Five streams (four SQL and Tomcat) have no native candidates. All their original records, warnings, source pointers and publisher titles remain in the catalog/ledgers; they have no invented editable Benchmarks or Assessments. Native IDs remain unchanged, including generic `direct-slice` Benchmark IDs in separate existing private namespaces. Profiles remain embedded and shared Objects stay inside Assessments. No scope extension or implicit newest-version selection.

Full export: **705.844 seconds, 279,924 KiB peak RSS**. Maximum/median relative paths: **215/187 -> 138/122 characters** (source-stream-relative before, content-relative after). Example:

```text
Before: authoring/direct-slice/assessments/the-password-for-the-krbtgt-account-on-a-domain-must-be-reset-at-least-30452496-assessment.yaml
After:  assessments/local/microsoft-windows-server-2025-stig-scap-benchmar-3266ecf9/password-krbtgt-account-domain-reset-at-170dd99a.yaml
```

Actual 13,754-document cached scope open/search **0.059s**; notified document check **0.574s**, one parsed document. Separate synthetic 100-stream/10,100-document index audit: cached search **0.012s**, one-document incremental check **0.433s**, **82,256 KiB** peak. Synthetic indexing measures navigation scale, not a new corpus validation or semantic result. Timings are environment observations.

[Separate reuse census](reuse-census.json): **404** ID-neutral exact structural candidate groups; **100** near pairs examined; **zero** unreferenced Assessment documents and **zero** promotions. Candidates remain advisory; no title/fingerprint implies source or runtime equivalence.

## Code and validation

Exact packaged implementation: [ff69d46b36e05e45074a5e7f43bf2ef3cf464ddf](https://github.com/vanderpol/scap-ng/commit/ff69d46b36e05e45074a5e7f43bf2ef3cf464ddf). Full export engine: `03ddc6beda8dcda5ff57439b0c3d7a2d12763d1b`; subsequent CLI/index/provenance hardening did not alter native output. Included post-export helpers enrich only generated catalog original-only titles/status, preserve frozen proof triples and package/verify output. They record their workspace-specific recovery paths; the importable engine itself has no workspace dependency.

- 44 focused library + compatibility normalizer tests PASS; 28 library tests also PASS from a clean extracted toolchain with offline pinned dependency installation and `pip check`.
- Clean-extracted CLI version/export/analyze/manual-source-locator/search/cache-rebuild/compile and independent package consumer PASS. Rebuilding the exact full-ref source snapshot produced identical ZIP bytes.
- Real normalized RHEL 9 and Windows Server 2025 compilation plus independent package consumers PASS: **415 + 257 unchanged program hashes**, including **20 + 18 shared Objects**. This establishes source/package integrity, not new OVAL proof or live scanner equivalence.
- Maintained checkpoint [9e893266f CI](https://github.com/vanderpol/scap-ng/actions/runs/41049843626): **3,359 selected, 3,358 passed, one explicit optional full-corpus skip**, zero failures/errors. Final exact-implementation [ff69d46b3 CI](https://github.com/vanderpol/scap-ng/actions/runs/41052208017) also PASS: **3,359 selected /3,358 passed /one skip**, zero failures/errors, 1,159.586 test seconds. Complete exact test identities/results are retained in `current-regressions.json`; `ci.json` records all three triggered workflows green. Fresh immutable-commit downloads of both ZIPs passed SHA256 and CRC (`remote-download-receipt.json`).
- Earlier representative Board workflow [41039515618](https://github.com/vanderpol/scap-ng/actions/runs/41039515618) PASS.
- Known unrelated historical #214 0.3 preview [41039515609](https://github.com/vanderpol/scap-ng/actions/runs/41039515609) fails at its unchanged renderer/schema gate (1,567 rejected source documents), before invoking the normalizer. Its driver/renderer/schema bytes match the recovered baseline. No protected workflow/schema was altered to hide it.

See individual JSON receipts for counts/hashes/resources, `artifact-files.json.gz` for every expanded file, and `normalized-archive-receipt.json` for CRC/every-payload digest checks. `manifest.json` records exact input/tool/command pins and the bounded storage exception. Only one compressed complete review payload and one exact toolchain snapshot are retained; the expanded corpus and derived runtime packages stay outside Git. All older archives and candidate tags remain untouched.

## Follow-up boundaries

Editor issue #3 may consume this offline CLI/API; no TypeScript/editor change is included. Explicit semantic/provenance review is required before any later sharing/repointing. Independent verification of 2,559 native candidates, 422 genuine blockers, normative decisions, scanner-runtime evidence, license selection and final 0.4 release remain separate workstreams. The scoped #261 deliverable does not silently resolve any of them.
