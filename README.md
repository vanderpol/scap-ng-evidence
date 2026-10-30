# SCAP-NG Evidence

Reproducible generated evidence for the SCAP-NG project. This repository is intentionally separate from the main design/specification repository.

## Current 0.4.0 review downloads (October 30, 2026)

- **[Download and Assessment sample navigation](https://github.com/vanderpol/scap-ng/blob/main/docs/releases/0.4.0-downloads-and-samples.md)** in the main project explains which archive to use and what has actually been proved.
- **[Normalized editable YAML review library and exact maintenance toolchain](runs/v04-library/2026-10-30-all65-normalized-review-ff69d46b3/README.md)** — 13,754 byte-preserved native YAML files, 60 editable native Benchmarks plus five source-only stream records.
- **[Complete 65-stream original-source DRAFT](runs/v04-converter/2026-10-30-all-65-revised-draft-download/README.md)** — original Rules, manual content, warnings and provenance; the combined archive is downloaded/reassembled from three parts.
- **[Pinned pre-alpha toolchain candidate and decision packet](runs/v04-toolchain/2026-10-30-v040-rc-a5db02e1b/README.md)** — qualified candidate, not a final 0.4.0 release.

These are separate **immutable checkpoints**. The native review library has 6,817 compiled candidates, 4,258 accepted static proofs and 2,559 unverified candidates; 422 automated Rules remain blocked and 1,653 manual/OCIL Rules are source-preserved. No scanner-runtime equivalence, publisher signing or final-release approval is implied.

Main project: https://github.com/vanderpol/scap-ng

## Purpose

The main repository contains material people maintain and review. This repository contains larger proof sets behind those claims: corpus conversions, round trips, validation/comparison reports, normalization/compiler evidence, generated inventories, and exhaustive per-rule/per-package outputs.

Small representative examples may remain in the main repository. Bulk generated evidence belongs here.

## Repository contract

- [Evidence contract](EVIDENCE-CONTRACT.md)
- [Runs](runs/README.md)
- [Manifests](manifests/README.md)
- [Summaries](summaries/README.md)
- [Archive](archive/README.md)

Initial migration is staged and non-destructive. Evidence remains in the source repository until provenance, copy verification, dependency review, updated links, and explicit removal authorization are complete.
