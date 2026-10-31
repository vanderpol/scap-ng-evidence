# SCAP-NG 0.4 owner-contract bounded reconciliation (#255/#268)

New review evidence, not a replacement library, release or scanner qualification.
Generated from source/tool commit
[`0ec285e5c4d5cc92176041355cde3af34fe984a4`](https://github.com/vanderpol/scap-ng/commit/0ec285e5c4d5cc92176041355cde3af34fe984a4).

- [Single editor-default review table](editor-default-review.csv) and
  [full source/type/enum companion](editor-default-review.json): 453 rows,
  100 capability contracts, five annotated controls, source omission/provenance,
  editor-versus-source differences and explicit unapproved/held status.
- [Mechanical drift inventory](mechanical-reconciliation.json): twelve reviewed
  generator migrations resolved without changing old fingerprints; older
  pinned examples/fixtures retain visible historical drift.
- [Three Linux/Windows samples](samples/), with YAML/JSON, generated-schema
  validation, compilation, fresh static source proofs and preservation hashes.
  [Source/sample manifest](samples/manifest.json).
- [49 maintained-script results](validation/maintained-49-results.json),
  [complete local logs](validation/maintained-logs/),
  [clean-extract receipt](validation/clean-extract-report.json), and
  [GitHub CI receipts at a70ec7690](validation/ci-a70ec7690.json).
- [Run manifest](manifest.json), [downloadable bounded review ZIP](owner-contract-reconciliation-bounded.zip),
  [payload checksums](PAYLOAD-SHA256SUMS.txt) and [complete checksums](SHA256SUMS.txt).

All three formerly failing GitHub gates pass at a70ec7690: canonical-fast,
draft-schema and clean-extract. Board and remaining integration checks also
pass. Final draft-branch documentation/tooling CI is reported in
[PR #268](https://github.com/vanderpol/scap-ng/pull/268). Exact local and GitHub
source revisions are separate in the receipts; the audit/tooling snapshot is
not mislabeled as the earlier CI revision.

The 65-stream library and older frozen archives are unchanged. Existing proof
and compiled hash baselines are not rebaselined. Historical anchor bytes retain
original hashes; current generated-contract comparisons allow only the reviewed
native-name/version delta. None of the default table's suggestions constitutes
source-equivalence proof. Fresh sample comparisons are static collection/
comparison-term proofs; no host collection or scanner-runtime results exist.
The Linux sample retains its original source regex and does not fix source intent.

The 15 source-only declaration rows are deprecation/mask metadata or deprecated
acquisition behavior, not fabricated native editor knobs. Variable function
option rows remain held under #264. Additional default annotations remain
unapproved; Decision 28 (editor local versus source all) is closed. Source
namespace/IDs remain exact in the sample provenance.

Reproduce from the pinned source commit, using **new** output locations:

```sh
PYTHONPATH=tools python tools/audit_v04_owner_reconciliation.py --output NEW_RUN/mechanical-reconciliation.json
PYTHONPATH=tools python tools/audit_v04_editor_default_catalog.py --output NEW_RUN/editor-default-review.json --table NEW_RUN/editor-default-review.csv
PYTHONPATH=tools python tools/build_v04_owner_compatibility_samples.py --output NEW_RUN/samples
```

To check a download, extract the ZIP into a new directory and run
`sha256sum -c PAYLOAD-SHA256SUMS.txt` there. The ZIP includes all payloads and
that checksum file; `SHA256SUMS.txt` additionally verifies the outer ZIP.
