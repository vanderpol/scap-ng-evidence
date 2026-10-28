# DRAFT — NOT RUNTIME VERIFIED: Six-benchmark converter preview

[Download generated JSON/YAML and full ledgers](https://github.com/vanderpol/scap-ng-evidence/raw/refs/tags/v04-six-source-draft-20261028-c65a134b5/runs/v04-converter/2026-10-28-six-source-draft-c65/six-source-draft-c65.zip) · [Immutable DRAFT checkpoint](https://github.com/vanderpol/scap-ng-evidence/tree/v04-six-source-draft-20261028-c65a134b5/runs/v04-converter/2026-10-28-six-source-draft-c65)

[Browse every Rule in CSV](ledger.csv). The complete ledger JSON and all native files are in the ZIP.

SHA-256: `07f7b24f4d0522630159fbddf9f6d643ffcac3d49d3c482dc7fb263de9793317`; 12276247 bytes; 4301 files.

[Storage decision and publication addendum](STORAGE-DECISION.md). The archive is unchanged; its internal manifest records the originally intended release-asset route.

The following README describes paths **inside that ZIP**.

# SCAP-NG 0.4 six-benchmark converter — DRAFT

**Inspectable engineering draft. Not a verified release, complete lossless migration, or scanner result.**

Toolchain: `c65a134b539558609ccf3bdc0600f38e411bbb2e` (pristine checkout; local converter WIP excluded).
NIWC pin: `8c8e5dff860af6b1290ee9273a282db24278f8d5`; package hashes in `source-pins.json`.

## Inspect the draft

Open `ledger.csv` or `ledger.json`: all 1,567 source Rules are accounted for, including
1,396 OVAL-bearing and 171 OCIL-only Rules. Primary statuses are disjoint.
There are 1,055 eligible schema-valid/compiled candidates, 341 blocked automated Rules,
and 171 OCIL-only/manual Rules. No independent source proof is newly claimed for this draft.

Each benchmark directory has actual generated `authoring/**/*.yaml` and `.json`,
complete `coverage.json` and `source-trace.json`, a ledger, and compilation evidence.
The raw converter emits 1,057 authoring candidates. Two banner Rules are already known
to fail original Schematron checks: RHEL `SV-270174` and Oracle Linux `SV-271689`.
They are explicitly **BLOCKED_INVALID_ORIGINAL_SOURCE**, not successful conversions.
Their raw native output is retained only for diagnosis. `diagnostic-candidates.scapng`
files include all raw candidates and **must not be treated as accepted assessment packages**.
Read `retained-source-rejections.json` for the exact original validity failures and source pins.

| Benchmark | Total | OVAL | Eligible compiled/unproved | Blocked automated | OCIL-only |
| --- | ---: | ---: | ---: | ---: | ---: |
| apache_server_2-4_unix_server | 45 | 22 | 0 | 22 | 23 |
| ms_windows_11 | 257 | 246 | 228 | 18 | 11 |
| ms_windows_server_2025 | 291 | 261 | 249 | 12 | 30 |
| ms_windows_server_dns | 81 | 41 | 0 | 41 | 40 |
| oracle_linux_9 | 448 | 408 | 286 | 122 | 40 |
| rhel_9 | 445 | 418 | 292 | 126 | 27 |

Server 2025 counts are current: 291 total, 261 OVAL, 30 OCIL-only, 249 eligible
compiled/unproved and 12 blocked automated. Secondary blocker entries overlap; do not sum them.
DNS/Apache automated Rules stop at strict unresolved checklist catalog hrefs. The ledger
retains exact missing references and all discoverable secondary node diagnostics; no aliases are guessed.

## Checks and limits

Fresh draft checks: every producer completed successfully, authoring schema validation,
JSON/YAML value equality, native semantic compilation, all 1,057 diagnostic program operands,
bundle integrity, and all 1,055 previous proof-floor program hashes retained.
Program hash retention does not replace fresh independent OVAL semantic comparison.
Known original-source invalidity is carried forward using unchanged validator/XSD bytes.
Full original XSD/Schematron and source/native proof gates are deferred until after publication.
Exact-toolchain maintained CI already passed: 3,264 tests, zero failures/errors, one existing skip:
https://github.com/vanderpol/scap-ng/actions/runs/40733597054 . No duplicate full suite was launched.
Applicability/CPE, full policy/remediation/scoring, manual execution and scanner runtime remain unconverted/unproved.
A subsequent verified checkpoint requires exact-SHA six-source proof and retention gates.

## Reproduce

Clone `vanderpol/scap-ng` at the exact toolchain SHA; use Python 3.12 and `environment.txt`.
Clone `niwc-atlantic/scap-content-library` at the source pin. ZIPs are under `Current/`.
For each entry in `source-pins.json.sources`, run from the toolchain checkout:

```sh
PYTHONPATH=.:tools python tools/v04_direct_converter.py "$NIWC/Current/$FILE" \
  --sha256 "$SHA256" --all-rules --output "$OUTPUT/$NAME"
```

Actual argv/host paths are in `invocations.json`; logs and per-source metrics are retained.
Packaging uses the included `package-six-draft.py` (native compilation and hash checks).
The included finalizer records two retained source rejections without changing any native operands.
Both helper scripts record original host paths for this evidence run; replace them with your local
toolchain/output/report paths when reproducing packaging. See their source and `manifest.json`.
No schema, compiler, scanner, editor or production `all_exist` behavior was changed.
