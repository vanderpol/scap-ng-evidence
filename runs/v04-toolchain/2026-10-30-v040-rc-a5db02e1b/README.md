# SCAP-NG 0.4.0 pre-alpha candidate — owner decision packet

Exact candidate source: **a5db02e1b29a2d7c312ddcf593be1ee055afb750**.
Authority: [owner tasking #260](https://github.com/vanderpol/scap-ng/issues/260#issuecomment-6510844015).
This packet completes candidate preparation; it is not final release approval.

**Technical GO for scoped pre-alpha toolchain/draft evaluation. NO-GO for final
0.4.0 publication/tag until the owner chooses source/specification licensing
and explicitly approves publication.** No scanner-runtime or production claim.
The owner replied that the license choice is currently uncertain. No grant was
invented. The archive's license inventory preserves that gap and dependency notices.
Apache-2.0 for tooling and CC-BY-4.0 for specification prose are options for owner
review; they are recommendations, not applied licenses. The owner should also
settle treatment of schemas/examples while retaining third-party notices.

## Downloads and SHA-256

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| [scap-ng-0.4.0-toolchain-a5db02e1b29a.zip](https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-toolchain-rc-20261030-a5db02e1b/runs/v04-toolchain/2026-10-30-v040-rc-a5db02e1b/scap-ng-0.4.0-toolchain-a5db02e1b29a.zip) | 23918086 | `88a15598faca3219eb97153867eb36f52ba95b774d958d8b4af243ccaf220a4d` |
| [scap-ng-0.4.0-linux-py312-offline-dependencies.zip](https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-toolchain-rc-20261030-a5db02e1b/runs/v04-toolchain/2026-10-30-v040-rc-a5db02e1b/scap-ng-0.4.0-linux-py312-offline-dependencies.zip) | 11602246 | `f86fe53b6b7ee0c5e5b52c764e48a7c1146148b7bf55b58718eeefe2bb7c4647` |
| [clean-extract-seven-case-evidence.zip](https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-toolchain-rc-20261030-a5db02e1b/runs/v04-toolchain/2026-10-30-v040-rc-a5db02e1b/clean-extract-seven-case-evidence.zip) | 607617 | `bf07867b64780052c4625c4f2fa2e769ea565233635fb5a019a84d378609a2e8` |

The source ZIP is a deterministic exact-ref snapshot of all 6,783 committed
files, with canonical schemas, 100 capability contracts, converter/compiler,
independent verifiers, docs/examples/tests, dependency lock and license inventory.
Two exact-ref builds are byte-identical. Every manifest member was integrity
checked. Offline wheels retain all original embedded dependency license notices.
The evidence ZIP retains the seven-case clean-extract commands/reports/outputs.
See manifest.json and SHA256SUMS for machine-readable provenance and integrity.

[Complete 65-STIG revised DRAFT, download/reconstruction script and parts](https://github.com/vanderpol/scap-ng-evidence/tree/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download).
Combined ZIP: 108,003,966 bytes; SHA256
`a09ee9a13cdfeeb1b8599eab61308e935a19b99eb62eadafd32002d13d90f8bd`.
A fresh public GitHub download was reassembled and passed the combined hash,
ZIP CRC, 8,892-Rule total and 4,258-proof retention checks. All 37,283 original
payload files were individually digest-checked during packaging.

## Qualification evidence

- [Exact-SHA maintained CI](https://github.com/vanderpol/scap-ng/actions/runs/41029222399):
  **3,331 selected / 3,330 passed / 0 failures / 0 errors / 1 skip**.
  Job 123974642484; artifact 12966345704; test execution 629.728 seconds; job elapsed 655 seconds.
  The skip is the separately routed optional full original-source census.
  All four workflows triggered by the final commit are green (ci-runs.json).
- Prior implementation commit a08c9beb9 completed all 15 triggered workflows,
  including [six-source requirement/hash retention](https://github.com/vanderpol/scap-ng/actions/runs/40985824393).
  Final changes correct the release walkthrough and prose; converter/compiler/
  schema bytes are unchanged. Those unchanged expensive lanes were not duplicated.
- Fresh clean extraction, without .git or source checkout imports: offline
  hash-pinned installation of all **11** dependencies and pip check PASS.
- **Seven** bounded CLI cases PASS: original Amazon Linux static proof; original
  Windows Server 2025 static proof with a shared Object; catalog warning;
  Test all_exist warning; typed Input/Parameter binding warning; incompatible
  original source rejected; explicitly synthetic ambiguous catalog rejected.
- Independent package reader checks references, operands, programs, JSON/YAML
  parity and source document graphs. This is separate from original-source
  static proof, and does not establish scanner-runtime equivalence.
- **61 affected integration tests** PASS, plus seven targeted function/binding
  tests after the int32 option boundary addition. Existing 4,258 source/authoring/
  program proof hash pairs are unchanged; prior frozen archive hashes retained.
- [Five sample sets](https://github.com/vanderpol/scap-ng-editor-sample-data/tree/b595b490226934a26cd7265b86974904d5db1cce/focused-fixtures/v04-release-candidate-a5db02e1b)
  published at sample-data commit b595b490226934a26cd7265b86974904d5db1cce.
  All 54 file digests and 22 JSON/YAML document pairs checked. No editor changes.

## Exact corpus ledger

| Disjoint outcome | Rules |
| --- | ---: |
| CONVERTED_VERIFIED — retained independent static primary proofs | 4,258 |
| CONVERTED_UNVERIFIED — additional native drafts | 2,559 |
| BLOCKED — automated, originals preserved | 422 |
| MANUAL_OCIL_ONLY_PRESERVED | 1,653 |
| Total original Rules in 65 Benchmarks | 8,892 |

7,239 automated conversion attempts. **All 6,817 native candidates compile.**
No manual/blocked placeholder is counted as native content. There is no new
promotion to VERIFIED; independent proof of the additions is separate stage two.

| Old primary blocker cohort | Native drafts recovered | Still blocked |
| --- | ---: | ---: |
| Catalog/reference — 992 | 980 | 12 |
| Test all_exist — 1,184 | 1,181 | 3 |
| Imports/exports — 381 | 338 | 43 |
| Multiple aggregation — 30 | 30 | 0 |

These are cohort recovery counts, not additive coverage attribution. All remaining
cohort Rule IDs and diagnostics are in cohort-recovery.json. Catalog leftovers
have secondary capability/State/path/cast issues; the three all_exist leftovers
require arithmetic. No unresolved dependency was fabricated.

Overlapping warning counts: NIWC catalog **989**, Test all_exist **1,767**,
function expression **55**, multiple aggregation **30**, typed check export
**326**. One Rule may have several warnings. Their sum is not a Rule total.

The 422 primary dispositions are 137 nonstandard SQL-extension package cases,
151 effectively deprecated originals, 48 recorded original-invalid/deprecated
exclusions, six other contract blockers and 80 remaining converter/source cases.
Examples include Value operator/constraint adapters, old WMI Objects, numeric
ordering/casts, comparator-bearing absence and malformed path recursion.
Original-invalid, deprecated, unsupported and extension cases remain distinct in
per-Rule diagnostics; originals remain available for producer review.

## Supported scope and boundaries

Normal direct CLI uses **52** explicitly enabled capability mappings (the
versioned registry is inside tools/v04_direct_capabilities.json). The intentional
full-65 DRAFT builder tries all **100** existing reviewed supported mappings
diagnostically. A mapping's presence does not imply every source shape works.
No schema, compiler, scanner or editor semantics were changed for this task.

Draft NIWC ds:uri resolution follows exact named component-ref/component/
Definition identity, prefers standard catalogs and rejects ambiguous/missing/
conflicting targets. Signed originals, QName, IDs and hashes are preserved.
Test all_exist lowers to items_found one_or_more only with explicit warnings;
field/record existence is unchanged. No absent Item is synthesized. Missing
expected targets, incomplete, error and unknown collection are not proved to
pass from a positive Item. Original Test/Object/Variable/Set context is retained.
Warning-bearing content cannot inherit verified status through the strict path.

Typed expected-state check exports retain Input/Parameter/Rule links, defaults
and allowed values. Unsupported acquisition/import/constraint contexts remain
blocked. Draft count/split/substring and multi-component aggregation use existing
migration-expression contracts with warnings, without promoting new normative
grammar or changing previous function proof hashes. All emitted canonical
subtrees pass their committed contract, including int32 substring bounds.

Remaining qualification: independent semantic proof of new drafts; runtime
scanner behavior/populations/error/unknown states; publisher signatures/trust;
complete policy/applicability/CPE/manual migration; non-Linux installation;
remaining unsupported source shapes; and the project license/publication decision.
0.5.0, editor implementation and cross-Assessment dedup were not started.

## Reproduce the candidate locally

Extract source and offline-dependency ZIPs to separate new directories:

```bash
python -m zipfile -e scap-ng-0.4.0-toolchain-a5db02e1b29a.zip /tmp/scap-ng-source
python -m zipfile -e scap-ng-0.4.0-linux-py312-offline-dependencies.zip /tmp/scap-ng-wheels
python -m venv /tmp/scap-ng-env
/tmp/scap-ng-env/bin/python -m pip install --no-index --find-links /tmp/scap-ng-wheels --require-hashes -r /tmp/scap-ng-wheels/requirements-linux-py312.lock
cd /tmp/scap-ng-source/scap-ng-0.4.0-toolchain
/tmp/scap-ng-env/bin/python tools/build_versioned_toolchain.py --verify /path/to/source-toolchain.zip
/tmp/scap-ng-env/bin/python tools/audit_v04_release_candidate.py --require-extracted --output /tmp/scap-ng-new-gate
```

Linux x86_64 / CPython3.12 is the pinned qualified environment. The walkthrough
uses original Linux and Windows content, not a Windows execution environment.
Use a fresh output path. Full corpus regeneration is an intentional deliverable,
not a routine regression. Its exact pins, exclusions and baseline are embedded
in the DRAFT archive; preserve frozen originals and prior proof hashes.

## Storage and final owner action

GitHub release-asset upload failed HTTP401 at uploads.github.com, while Git
pushes work. The attempted release did not produce a downloadable release asset.
The explicitly documented fallback retains one corpus ZIP in three <50MiB parts
and this bounded source/dependency/evidence set in ordinary Git under immutable
DRAFT/candidate evidence tags. No previous archive was replaced. See manifests.

Choose source/specification/schema/example licensing, review this exact candidate
and approve or reject final scoped 0.4.0 pre-alpha publication. No final source
v0.4.0 tag/release has been created. Additional independent semantic verification
continues separately and does not retract the transparently labeled DRAFT.
