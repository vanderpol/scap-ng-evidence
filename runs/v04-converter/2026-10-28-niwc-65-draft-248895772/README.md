# DRAFT — NOT RUNTIME VERIFIED

Designated all-65 NIWC checkpoint for [converter #251](https://github.com/vanderpol/scap-ng/issues/251).
Exact toolchain `24889577233c6a75e739676adffe8f676a0f9f3b`; source revision `8c8e5dff860af6b1290ee9273a282db24278f8d5`.
All 65 individual original ZIPs are Git-blob/SHA-256 pinned; the consolidated ZIP is excluded.

[Download complete DRAFT ZIP](https://github.com/vanderpol/scap-ng-evidence/raw/refs/tags/v04-niwc-65-draft-20261028-248895772/runs/v04-converter/2026-10-28-niwc-65-draft-248895772/niwc-65-draft-248895772.zip). See [publication manifest](manifest.json),
[compact machine-readable summary](summary.json), [source pins](source-pins.json),
[observed environment](environment.json), and [storage decision](STORAGE-DECISION.md).

## What is delivered

Actual generated JSON/YAML, diagnostic compiled bundles, every original Rule in JSON/CSV,
primary and overlapping secondary blockers, source graphs/hashes and exact generation scripts.
Four SQL Server packages containing nonstandard `independent.sqlext` remain package-level exceptions.
Their automated Rules are blocked and their manual Rules remain separately accounted.

| Disjoint status | Rules |
| --- | ---: |
| BLOCKED | 2880 |
| OCIL_ONLY_MANUAL_UNCONVERTED | 1653 |
| CONVERTED_COMPILED_UNPROVED_ORIGINAL_VALIDITY_NOT_RUN | 3138 |
| BLOCKED_SOURCE_PACKAGE_SQLEXT | 137 |
| SOURCE_PROVED_COMPILED_PRIMARY_ONLY | 1072 |
| BLOCKED_INVALID_ORIGINAL_SOURCE | 12 |
| Total | 8892 |

Only 1,072 six-anchor primary Rules retain independent original-source proof and valid,
nondeprecated closures, with exact Assessment/program hashes checked. All 1,055 preceding
proof-floor program hashes remain unchanged. Other compiled output is explicitly unproved;
original XSD/Schematron and deprecation checks have NOT run for those sources.
Diagnostic bundles may contain rejected raw candidates and must not replace production packages.
No scanner has executed this output; applicability, complete policy and manual execution are unconverted.

## Largest primary blockers

Counts below are disjoint primary messages, not promised unlock counts. Secondary diagnostics overlap.

| Primary message | Rules |
| --- | ---: |
| unsupported Test existence: all_exist | 1184 |
| OVAL check imports/exports unsupported | 382 |
| unresolved checklist catalog href: U_Apple_macOS_15_V1R4_STIG_SCAP_1-4_Benchmark-enhancedV8-oval2.xml | 157 |
| unresolved checklist catalog href: U_Apple_macOS_26_V1R1_STIG_SCAP_1-4_Benchmark-enhancedV5-oval2.xml | 157 |
| unresolved checklist catalog href: U_Apple_macOS_14_V2R3_STIG_SCAP_1-4_Benchmark-enhancedV7-oval2.xml | 152 |
| nonstandard source capability independent.sqlext; package held fail-closed | 137 |
| unsupported test capability: {http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_test | 125 |
| unresolved checklist catalog href: U_Apple_macOS_13_V1R5_STIG_SCAP_1-4_Benchmark-enhancedV7-oval2.xml | 102 |
| unresolved checklist catalog href: U_MS_Exchange_2019_Edge_Server_V2R2_STIG_SCAP_1-4_Benchmark-enhancedV1-oval2.xml | 55 |
| unresolved checklist catalog href: U_MS_Exchange_2019_Mailbox_Server_V2R3_STIG_SCAP_1-4_Benchmark-enhancedV1-oval2.xml | 51 |
| unresolved checklist catalog href: U_MS_Windows_Server_DNS_V2R3_STIG_SCAP_1-4_Benchmark-enhancedV8-oval2.xml | 41 |
| unresolved checklist catalog href: U_Cisco_IOS-XE_Switch_NDM_V3R5_STIG_SCAP_1-4_Benchmark-enhancedV6-oval2.xml | 37 |
| unresolved checklist catalog href: U_MS_IIS_10-0_Site_V2R14_STIG_SCAP_1-4_Benchmark-enhancedV19-oval2.xml | 33 |
| unsupported test capability: {http://oval.mitre.org/XMLSchema/oval-definitions-5#iosxe}line_test | 31 |
| multiple aggregation components need an approved collection expression | 30 |

Source catalog binding failures are preserved, not repaired. `all_exist`, function/dataflow,
import/export binding and acquisition/existence semantics require their existing approved contracts
or coordination through #255. Unavailable platform capabilities are not silently activated.

## Reproduction

Use a clean checkout of the exact toolchain, Python 3.12 and the pinned dependencies recorded
in the repository workflows (PyYAML, jsonschema, lxml). Place included scripts and
`niwc-65-source-tree.json` in a working directory. Recover ZIPs at `niwc-65-inputs/` using
`recover_65_sources.py`; source Git blob SHA and byte length are checked before use.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/path/to/scap-ng/tools python build_65_draft.py
```

This rebuilds raw compiled/unproved draft output. The finalizer additionally requires the
separately generated six-source acceptance evidence and its exact checked receipt; it only
relabels evidence after matching full program hashes, never changes authored/native operands.
Those local inputs are indexed in the source repository recovery checkpoint. To reproduce
the six-source proof gate, use `tools/verify_v04_direct_scope.py` with the six pinned inputs.

Raw generation, verification and reuse are distinct; do not infer runtime acceptance from any stage.
