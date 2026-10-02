# Large evidence storage policy

Large generated evidence should not be committed to ordinary Git merely because it can fit under GitHub's single-file limit. The default is to analyze it, retain durable conclusions and provenance, and keep the raw payload only when it has unique long-term value that cannot be reproduced.

## Default rule

Keep compact summaries, manifests, hashes, and reviewer-facing excerpts in Git.

For large generated payloads, prefer a durable non-history storage mechanism such as release assets, artifact/object storage, or a reproducible generation path with immutable source/tool pins.

## Threshold guidance

Any individual generated evidence file above roughly 10 MiB, or any run whose generated payload is large enough to materially inflate repository clone/history size, requires an explicit storage decision before committing the raw payload.

## Required retained material

Even when raw payloads are stored outside Git, retain in this repository:

- evidence/run manifest;
- source SCAP-NG commit;
- external input pins/digests;
- generator/tool identity and exact command/workflow;
- output file list, sizes, and hashes;
- compact result summary;
- validation status and limitations;
- durable locator for retained raw payload, if one exists.

## Analyze-before-retain rule

Before deciding to retain a large raw payload, extract and save all decision-relevant findings, unusual cases, aggregate metrics, limitations, and implications in a compact summary. The summary SHALL include enough provenance to reproduce or recover the raw evidence.

If a large payload is deterministic, reasonably reproducible, and has no unique information beyond its manifest/analysis, it SHOULD be retained as reproducible-only evidence rather than stored permanently. This decision must be explicit in its manifest.

## Current oversized candidate

The migrated-source set `research/iterations/003/evidence/full-current-native-normalize-compile/` is approximately 115 MB across 10 files, dominated by:

- `normalizer-report.json` — ~78 MB;
- `native-schema-census.json` — ~29 MB.

Do not copy those raw files into ordinary Git until a non-history storage/reproducibility decision is made. Compact summaries may be migrated separately.


## Preferred disposition after analysis

For oversized deterministic generated reports, the preferred lifecycle is:

1. Generate the raw report from pinned inputs and a pinned SCAP-NG/tool revision.
2. Analyze the complete report before disposal.
3. Commit a compact durable summary containing:
   - the questions answered;
   - key counts/findings;
   - anomalies and unresolved blockers;
   - conclusions that affected design or implementation;
   - enough representative examples to understand the finding;
   - exact source/tool revisions and reproduction command;
   - raw output file names, byte sizes, and Git/SHA-256 identities when available.
4. Add regressions or conformance tests for every finding that should remain enforceable.
5. Treat the raw generated payload as disposable/reproducible unless it contains unique evidence that cannot be regenerated.
6. Do not retain a raw payload in ordinary Git solely for historical completeness.

A compact summary plus executable regression is generally stronger long-term evidence than a very large unreviewed JSON dump.

### Exceptions

Retain raw payload outside ordinary Git only when at least one of these applies:

- the generating source is expected to disappear or cannot be legally redistributed later;
- the run is non-deterministic or depends on an environment that cannot be reconstructed;
- the raw output contains unique third-party observations not captured by the summary;
- an external review/audit requirement specifically requires the original output.

If none applies, reproducibility metadata plus the analyzed summary is sufficient.
