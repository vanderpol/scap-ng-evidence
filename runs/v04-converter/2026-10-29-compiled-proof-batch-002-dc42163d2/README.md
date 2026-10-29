# Verified static primary OVAL proof expansion — batch-002

602 new original primary Rule proofs from 602 frozen compiled/unproved candidates.
All 602 frozen authoring/program pairs retain exact identity; 70 representative negative comparisons reject mutations.

[Proof hashes and all selected outcomes](proof-hashes.json) · [Actual representative authoring/independent terms](representatives.json) · [Manifest](manifest.json) · [Full bounded evidence ZIP](batch-evidence.zip).

The ZIP contains accepted primary packages, authoring JSON/YAML, source traces, original validity/outcome accounting, full independent terms, selection lists and the exact reproduction driver. The driver calls the existing verified upgrader and independent readers; no converter/schema/compiler/proof-rule implementation changed. Full maintained exact-code CI at `10f4e35b3` already passed; it was not repeated for new evidence inputs.

Reproduction uses the recorded `/workspace/scap-ng` and evidence checkout layout. Set up exact source implementation `10f4e35b331c622c14f6e3aa2bd4aa8981c810c1`, the unchanged frozen DRAFT at its recorded checksum and source-pins.json, and only the selected SHA/Git-blob-verified original ZIPs. Run the manifest commands with a fresh output root. `reproduce.py` snapshots orchestration only; the portable public CLI is `python tools/v04_direct_converter.py ORIGINAL.zip --sha256 PIN --verify --rule ORIGINAL_RULE_ID --output NEW_OUTPUT`, repeating `--rule` for the published selection.

**Scope:** static primary OVAL subset. Full policy, applicability/CPE, manual execution, scanner-runtime equivalence and a verified toolchain release remain outside this claim. The original all-65 DRAFT is not regenerated or relabeled. Evidence is non-normative and runtime packages have no dependency on this repository.
