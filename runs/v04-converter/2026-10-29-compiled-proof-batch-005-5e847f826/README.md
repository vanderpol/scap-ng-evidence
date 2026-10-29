# Verified static primary proof expansion — Registry reader completion

All **35** previously reader-limited original Rules now independently prove at
exact implementation `5e847f8268697f7555a442256c06f5bfa48f4676`. Frozen authoring documents and compiled program
hashes are unchanged. The correction completes **3,130 proved / 3,138 assessed**
in the original 32-benchmark candidate cohort. Seven invalid originals and one
deprecated original remain rejected; their exact diagnostics are retained.

[Manifest](manifest.json) · [All 35 proof hashes](proof-hashes.json) ·
[Representative real authoring and independent terms](representatives.json) ·
[Full evidence ZIP](batch-evidence.zip) · [Exact-commit CI](integration-ci.json) ·
[Eight original exclusions](remaining-original-exclusions.json).

Both corrected readers retain all 3,095 preceding new proof hashes and 523
conformance four-hash records. 8 representative source/compiled cardinality
mutations are rejected. Positive, negative, duplicate-array, Filter, cycle and
domain regression tests are part of the hosted maintained integration gate.

For reproduction, use the exact source commit, dependencies in environment.json,
the unchanged frozen DRAFT and source-pins.json at its recorded location, and
the four source ZIPs identified in the manifest. Keep reproduce.py beside
registry-retry-selection.json and run the manifest commands with a fresh output
root. The driver uses `/workspace/scap-ng` and the evidence checkout layout;
it orchestrates the existing public converter and independent readers.
The portable converter CLI is `python tools/v04_direct_converter.py ORIGINAL.zip
--sha256 PIN --verify --rule ORIGINAL_RULE_ID --output NEW_OUTPUT`, repeating
`--rule` for the published selection.

This is a static primary OVAL subset, not scanner-runtime equivalence or a
complete toolchain release. The 35 successful retries supersede earlier
reader-limited outcomes; they are not 35 additional distinct cohort members.
No frozen archive, source, schema, mapping or #255 contract was changed.
Evidence is non-normative; runtime packages have no dependency on this repo.
