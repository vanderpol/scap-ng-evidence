# Complete all-65 stage-one DRAFT — NOT VERIFIED FOR EXECUTION

Download `all-65-complete-draft.zip`, extract it, and open `index.html`.
All 65 original ZIPs, all 8,892 original Rules and manual/OCIL components are
preserved. All 7,239 automated Rules received conversion attempts. The ledger
distinguishes 4,206 unchanged published static proofs, 52 structurally valid
UNVERIFIED candidates, 2,981 explicit blockers and 1,653 manual/OCIL-only Rules.
All 4,258 native candidates compile with checked operands. No blocked/manual
Rule receives a fictional executable Assessment. Native Rule/policy wrappers
cover a partial primary automated subset; the original policy remains separate.

Toolchain: vanderpol/scap-ng at `0b2fdb2d392c5d80a4128d73ae4ac5ada573cf26`.
This is a reconstruction of the interrupted completed deliverable: its previous
local payload was lost when the session workspace was replaced. The existing
builder was run once from identical pinned originals and the recovered published
4,206-proof baseline; no frozen archive or accepted hash was replaced.

Reproduce from that source checkout with the dependencies recorded there:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools python tools/build_v04_full_draft.py \
  --source-pins source-pins.json --inputs ORIGINAL_ZIPS \
  --baseline proof-baseline.json --known-invalid known-invalid-final.json \
  --output NEW_UNIQUE_DIRECTORY --workers 3 --acknowledge-full-corpus-deliverable
```

The originals are embedded under each benchmark's `source-preservation/` folder.
Recovery scripts retain their original workspace paths as forensic records;
the maintained builder command above is the portable generation entry point.
Stage-two proofs are published separately and never relabel this frozen DRAFT.
No scanner-runtime parity, publisher trust, complete policy migration or final
verified release is claimed. Unsupported #255 contracts remain explicit.
