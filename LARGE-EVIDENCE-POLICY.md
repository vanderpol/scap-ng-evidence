# Large evidence storage policy

Large generated evidence should not be committed to ordinary Git merely because it can fit under GitHub's single-file limit.

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

## Reproducible-only evidence

If a large payload is deterministic, inexpensive enough to regenerate, and has no unique information beyond its manifest/summary, it MAY be retained as reproducible-only evidence rather than stored permanently. This decision must be explicit in its manifest.

## Current oversized candidate

The migrated-source set `research/iterations/003/evidence/full-current-native-normalize-compile/` is approximately 115 MB across 10 files, dominated by:

- `normalizer-report.json` — ~78 MB;
- `native-schema-census.json` — ~29 MB.

Do not copy those raw files into ordinary Git until a non-history storage/reproducibility decision is made. Compact summaries may be migrated separately.
