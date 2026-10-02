# SCAP-NG evidence contract

Each independently meaningful evidence run SHALL have a manifest.

## Required metadata

Each run manifest SHALL record:

- a unique evidence ID;
- evidence kind;
- creation timestamp;
- source SCAP-NG repository and commit;
- generating tool path and commit;
- exact command or workflow identity;
- immutable external input revisions, package versions, or digests;
- output root and file count when known;
- validation status and checks performed;
- known limitations;
- original repository/path provenance for migrated evidence.

## Evidence classes

Keep these classes distinguishable:

- **production migration evidence** — real published SCAP/STIG corpus migration and comparison;
- **language-conformance evidence** — OVAL/SCAP semantic and Self-Assertion validation;
- **repository/audit evidence** — dependency, provenance, inventory, and rebaseline proof.

## Hard boundaries

Evidence is non-normative. No Benchmark, Rule, Assessment, schema, specification requirement, or runtime package may depend on this repository being available.

A new run SHALL NOT silently overwrite an older run. Superseded evidence may be archived only if its manifest and provenance remain resolvable.
