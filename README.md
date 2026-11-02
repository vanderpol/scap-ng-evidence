# SCAP-NG Evidence

Historical conversions, proof records and reproducible archives for SCAP-NG. This repository is **not the current authoring library**; the [canonical 0.4 schema and examples](https://github.com/vanderpol/scap-ng) are maintained separately.

## Important: October 30 archives are historical

**Do not use the October 30 converted YAML as a template for current 0.4 authoring.** These checkpoints predate the November 2 grouped `require.item_requirement` amendment and retain older Test/field formatting, `assessments/local` directory conventions, and generated hash-suffixed names. They were preserved byte-for-byte; archive integrity does not establish current-schema compatibility or acceptable authoring presentation.

The publication and content-normalization problems are tracked in [Issue #1](https://github.com/vanderpol/scap-ng-evidence/issues/1). Use the [current canonical Assessment examples](https://github.com/vanderpol/scap-ng/tree/main/examples) for the intended concise format.

## Archived October 30 checkpoints

- [Complete 65-benchmark DRAFT](runs/v04-converter/2026-10-30-all-65-revised-draft-download/README.md) — original source, manual content, warnings and full ledger; **108 MB in three ZIP parts**, not browsable YAML.
- [Normalized native review library](runs/v04-library/2026-10-30-all65-normalized-review-ff69d46b3/README.md) — 13,754 unchanged native YAML files, with a compacted but still generated-looking directory hierarchy. **Not normalized to the current 0.4 authoring style.**
- [Pre-alpha toolchain candidate](runs/v04-toolchain/2026-10-30-v040-rc-a5db02e1b/README.md) — historical reproducibility and decision evidence.

The native review checkpoint reports 6,817 compiled candidates, 4,258 accepted **static** proofs, 2,559 unverified candidates, 422 blocked automated Rules and 1,653 preserved manual/OCIL Rules. These numbers describe that archived checkpoint only. No scanner-runtime equivalence, signing, OVAL Board approval or final 0.4 release is implied.

## Purpose and organization

Bulk generated evidence stays here; small readable authoring examples belong in the [canonical repository](https://github.com/vanderpol/scap-ng). Preserve immutable checkpoints and proof hashes rather than silently replacing old archives.

- [Evidence contract](EVIDENCE-CONTRACT.md)
- [Historical runs](runs/README.md)
- [Manifests](manifests/README.md)
- [Summaries](summaries/README.md)
- [Archive](archive/README.md)

Any future current-schema publication requires a fresh, explicitly version-pinned conversion/normalization and validation report. It must distinguish DRAFT content, schema validity, static proof, and live scanner conformance.
