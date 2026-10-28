# Verified static primary OVAL — not runtime verified

[Download accepted primary subsets and complete rejection ledgers](https://github.com/vanderpol/scap-ng-evidence/raw/refs/tags/v04-six-primary-static-verified-20261028-248895772/runs/v04-converter/2026-10-28-six-primary-static-verified-248895772/six-primary-static-verified-248895772.zip).
[Manifest](manifest.json), [new Rule/program hash receipt](receipt.json),
[source pins](source-pins.json), [checksum](SHA256SUMS).

Exact toolchain `24889577233c6a75e739676adffe8f676a0f9f3b`.
NIWC revision `8c8e5dff860af6b1290ee9273a282db24278f8d5`.

1,072 primary OVAL Rules prove (+17: RHEL +12, Oracle +5); 324 automated
Rules remain blocked and 171 are manual/OCIL-only. All 1,055 preceding program
hashes match. Accepted bundles exclude invalid/deprecated original closures.

Exact-commit [maintained suite](https://github.com/vanderpol/scap-ng/actions/runs/40788102371):
3,268 run, 3,267 passed, zero failures/errors, one existing skip (1,167.519 seconds).
Exact-commit [six-source validity/proof/hash gate](https://github.com/vanderpol/scap-ng/actions/runs/40788102434)
passed with the same 1,072 proofs. All nine triggered workflows passed.

This is static primary source/semantic/compilation evidence, not scanner-runtime
verification, complete policy/applicability/manual conversion or a toolchain release.
It is published separately from the immutable six-source and all-65 DRAFT previews.

Reproduce with the exact toolchain and pinned original ZIPs:

```sh
PYTHONPATH=tools python tools/verify_v04_direct_scope.py \
  --inputs ORIGINAL_SIX_ZIP_DIRECTORY --output NEW_EVIDENCE_DIRECTORY
```

Archive: 4327 files, 8654136 bytes, SHA-256 `809e6da4c4139bf8a671ed0d81ae464feb41f82c28ebadbdfb4edc05a253f4bd`.
