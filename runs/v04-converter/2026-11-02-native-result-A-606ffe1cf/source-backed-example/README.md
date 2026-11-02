# Source-backed native Result review

The Assessment is a preserved copy of the original-backed SV-278080 example in
[the owner contract packet](../owner-contract-20261031/README.md). See
`provenance.json` for its exact source path/hash. It still compares registry
`type = dword` and integer `value = 1`, with the compatible field datatype retained.

`supplied-observations.json` and `collections.json` are synthetic review inputs.
`native.test-result.json` adds only source metadata through the native projector;
`native.assessment-result.json` demonstrates embedding under a supplied matching
invocation. No Windows collector or scanner was executed; supplied true outcomes
are not independently recomputed. Do not use these files as observed compliance.

Run from the repository root:

```sh
PYTHONPATH=tools python tools/v04_result_contract.py \
  --assessment docs/examples/native-results-20261102/source.assessment.json \
  --result docs/examples/native-results-20261102/native.test-result.json \
  --collections docs/examples/native-results-20261102/collections.json
```

[Adopted Result contract and boundary tests](../../audit/v04-native-result-adoption-20261102.md).
