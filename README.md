# SCAP-NG Evidence

Reproducible generated evidence for the SCAP-NG project. This repository is intentionally separate from the main design/specification repository.

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
