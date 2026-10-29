# Verified static enum-selector conformance — not runtime verified

Exact toolchain `66a166bf282a377c233bc4a1ffd1ac43d0bd734c`.
[Manifest](manifest.json), [all 523 proof hashes](proof-hashes.json),
[retention receipt](receipt.json).

Two pinned original Tests are added: AppCmd Test 101 and AppCmdListConfig
Test 301. Their actual generated authoring JSON/YAML, compiled programs,
independent original/native typed terms and source pins are in the two
subdirectories. All artifacts match the hashes in the source review packet.

523/713 configured conformance Tests compile and independently compare out of
803 originals. All preceding 521 authoring/source-term/native-term/program
hashes are unchanged. Both added original closures are valid/nondeprecated.
No new primary production Rule is claimed: all 1,072 six-source program hashes
and their outcomes are unchanged (324 blocked automated, 171 manual/OCIL-only).

Exact-commit [maintained suite](https://github.com/vanderpol/scap-ng/actions/runs/40793748077):
3,273 run, 3,272 passed, zero failures/errors and one existing skip, 1,132.409 seconds.
The [six-source original validity/proof/hash gate](https://github.com/vanderpol/scap-ng/actions/runs/40793748148)
also passed. All nine triggered workflows passed.

Reproduce with the exact toolchain and Self-Assertion revision
`e3538595c5083b9c34d937a81d319234df9bbfaa`:

```sh
PYTHONPATH=tools python tools/audit_v04_oval_test_corpus.py \
  --source-root PINNED_OVAL_TEST_CONTENT --output NEW_CORPUS_REPORT.json
```

This is language-conformance evidence using synthetic single-Test Assessments,
not scanner runtime, full Benchmark/policy/applicability or release verification.
Full deterministic coverage reports are reproducible-only; retain the compact
proof ledger and actual two-case excerpts here. Earlier DRAFT/static-primary
checkpoints remain immutable and are not duplicated.
