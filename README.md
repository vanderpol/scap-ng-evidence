# SCAP-NG Evidence

Reproducibility and evidence artifacts for the SCAP-NG project. The current pre-alpha 0.4 specification, schemas, and readable Assessment examples live in [SCAP-NG](https://github.com/vanderpol/scap-ng).

**No full 65-benchmark package in this repository is presently qualified as the current November 2, 2026, 0.4 authoring library.** Earlier experimental conversion packages have been retired from public navigation; do not use historical generated YAML as an authoring baseline.

Current-native publication requires the shared [Tools publication gate](https://github.com/vanderpol/scap-ng-tools/pull/41). The legacy full-65 release workflow is fail-closed before downloading or reflowing content. Historical payloads/proofs remain unchanged; server/ref permission controls are still unverified, so this is not a claim of deployed, repository-wide enforcement.

## Repository purpose

This repository is for reviewable evidence and receipts associated with published claims, not for distributing obsolete draft authoring libraries. Historical conversion source and research records are retained separately in the private research repository.

- [Evidence contract](EVIDENCE-CONTRACT.md)
- [Evidence runs](runs/README.md)
- [Manifests](manifests/README.md)
- [Summaries](summaries/README.md)

A new publicly downloadable corpus should only be advertised after normalization against the current pinned schema, full-content accounting, validation and a readable path/authoring review. Schema acceptance and historical static proofs do not establish scanner-runtime equivalence.
