# Revised complete all-65 DRAFT — NOT VERIFIED FOR EXECUTION

[Download the complete original-preserving DRAFT ZIP](https://github.com/vanderpol/scap-ng-evidence/releases/download/v04-revised-all65-draft-20261030-a08c9beb9/all-65-revised-draft.zip)
(108,003,966 bytes). SHA-256:
`a09ee9a13cdfeeb1b8599eab61308e935a19b99eb62eadafd32002d13d90f8bd`

Extract and open `index.html`. The archive contains all 65 original signed ZIPs,
8,892 original Rules, all native YAML/JSON, Rule ledgers, dependency/provenance
traces and the 4,258-proof hash baseline. Manual and blocked originals are
preserved; no placeholder counts as native conversion.

| Disjoint outcome | Rules |
| --- | ---: |
| CONVERTED_VERIFIED (retained static source proofs) | 4,258 |
| CONVERTED_UNVERIFIED | 2,559 |
| BLOCKED automated | 422 |
| Manual/OCIL preserved | 1,653 |
| Total | 8,892 |

All 6,817 native candidates compile. All 4,258 accepted hash pairs remain
unchanged. Independent new source proof and scanner-runtime qualification are
separate; warnings do not imply production equivalence. Of the old primary
blocker cohorts, 980/992 catalog, 1,181/1,184 all_exist, 338/381 import/export
and 30/30 aggregation now convert as unverified drafts. These cohort counts
are separate from overlapping warning counts in summary.json.

See cohort-recovery.json for every remaining cohort diagnostic; source-pins.json
for original revision/bytes/digests; artifact-files.json.gz (and the inventory
inside the archive) for every expanded payload path/size/hash. Decompress with
`python -m gzip -d artifact-files.json.gz` on a copy. The archive checksum binds
its embedded inventory as well. Local archive CRC and every payload digest PASS.

Generator lineage: vanderpol/scap-ng `a08c9beb9dcf781a726adbdf05676f5ae2e57309`. Original source was not repaired,
and no schema/compiler/scanner contract changed. Exact final toolchain candidate,
clean-extract and CI decision packet are tracked separately under
[source #260](https://github.com/vanderpol/scap-ng/issues/260).
No final release/tag is authorized. Source/specification licensing is undecided;
all original and dependency notices remain intact.
