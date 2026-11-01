# #269 defaults and editor adapter evidence

Source: **a8a9db7039399610cb8af654ab9e880d69cffa04**, draft PR268.
Editor: **44eb6af1ea347d3ff38b5627fd84bd2b527584c0**, main.

All10 triggered exact-source hosted workflows PASS, including Board41302147435,
canonical41302147499, draft schema41302147506 and converter-sync41302147556.
Editor CI41302520698 PASS. Hosted observations are included separately from local logs.

All453 audited rows and15 source-only rows classified,38 unique controls/264 schema
locations. A249/B10/C16/D186/E0/F7.34 safe/4 aggressive-only. No new semantic vote.
See UPSTREAM-LEDGER.md, EDITOR-HANDOFF.md and full CSV/JSON. Recovered baseline
is preserved separately; do not overwrite the old R1/R2 packets.

All100 original generator fingerprints retained;38 expanded schema tests PASS.
The maintained local probe initially had one stale date assertion among49scripts;
that was corrected and its five-test gate rerun successfully. Hosted canonical/schema
CI verifies the committed version. Three bounded source proofs pass; all20 R2 sample
payloads including compiled output remain byte-identical (preservation-receipt.json).
The bounded original Schematron review inventories195 relevant clauses in13 pinned
source schema files and executes20 positive/negative clause checks; it is not a
whole-corpus Schematron validator or scanner runtime oracle.

Editor adapter eight unit cases and three original-backed integration cases PASS,
plus lint/build/library packaging. The exact external pack profile/resource manifest
is included; reconstruct using source tools/build_v04_editor_metadata_pack.py at the
pinned commit. No schema/content/code is vendored into the editor repository.

Remaining implementation dependency: editor host/TextDocument/WorkspaceEdit/graphical
views/VSIX (#1/#2), genuine screenshots and offline regex/sample playground (#7).
This packet demonstrates the tested adapter fallback authorized by #269, not a UI.
Full Assessment evaluation unavailable. No merge, freeze, release, proof rebaseline,
65-stream regeneration or scanner-runtime-equivalence claim.

`defaults-validation-evidence.zip` contains all payloads plus a member manifest.
SHA256SUMS covers payload files, manifest and archive. Read/download receipts are
published separately to avoid self-referential archive hashes.

The recovered baseline CSV retains its original CRLF bytes. Whitespace lint excludes
that byte-preserved input; the new disposition CSV uses LF. No source data was
normalized to satisfy lint.
