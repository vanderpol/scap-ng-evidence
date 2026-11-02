# Final 0.4 schema-freeze acceptance assessment (#255/#269)

**Recommendation: GO for owner acceptance of the complete0.4 schema family.**
No freeze, merge, tag or release is performed. Exact-commit CI, evidence archive
and fresh-download receipts are recorded in PR268 after the containing commit.
The [machine audit](v04-schema-freeze-readiness-final-20261102.json),
[29-decision verification matrix](v04-final-decision-verification-20261102.json)
and [selector/API packet](v04-selector-api-contracts-20261102.md) distinguish
contract completion from product/runtime qualification.

| Acceptance question | Assessment |
| --- | --- |
| All29 adopted language contracts complete? | Yes at the source/schema/compiler/metadata contract boundary; no owner decision reopened. Matrix lists the specific boundary suites. |
| All15 final selector/API contracts complete? | Yes:42 fields, including inherited filesystem scope, and32 primary/pinned source receipts. Platform/API/schema-dependent behavior is explicit; no universal case switch or undocumented alias is promised. |
| Schemas and references internally consistent? | All34 version-local schemas and242 references resolve; generated native surfaces and negative authoring/Result cases are checked. |
| Tests and CI? | Final exact-commit results are published with the completion receipt; maintained49 scripts, additional8 owner/converter boundary suites and new8 selector methods form the bounded qualification. No runtime test is invented. |
| Prior proofs and compatibility preserved? | Historical schemas,100 mapping bytes/fingerprints, prior proof floors, Native Result A and explicit Input guards unchanged. Compatible field datatypes remain. Five existing compiled samples are compared byte-for-byte. |
| Complete schema family ready to freeze? | GO for owner approval after the linked exact-head receipts pass. All language-contract findings CLOSED; the actual freeze remains explicitly unauthorized. |

## Remaining implementation and release work

These are separate from the completed language contracts:

- Native scanner providers still need target/API execution qualification:
  collection completeness/error/absence, process and dependency binding adapters,
  arrays/Variables/Set evaluation, caching, real IIS schema discovery, WMI/WUA
  behavior and complete Rule follow-up with observed target evidence. The API
  contracts do not turn unsupported or failed collection into an empty Item.
- VS Code remains an offline metadata/source-preservation foundation. Real
  TextDocument/save/undo, Guided/Structured UI, screenshots and required regex
  playground remain product implementation/verification under editor#7.
- Publishing0.4 requires owner acceptance and separate authorization to
  merge/freeze/tag/release, the final exact-SHA release/candidate packaging and
  clean-extract/dependency/notice/checksum gates in #260, and an honest supported
  subset. Production runtime parity or full65-STIG execution is not asserted.
- The current [license inventory](../releases/0.4.0-LICENSE-INVENTORY.md) records
  no project-wide source/specification distribution grant. An owner licensing
  decision remains necessary before representing a published software release
  as licensed. Public repository access is not that grant. This does not require
  another selector semantic vote or authorize changing notices now.
- Any required full-corpus release checkpoint needs separate owner approval;
  the existing65-stream library/proofs remain immutable. No regeneration or
  proof rebaseline is performed by this closure.

## Integration correction discovered by the broader audit

The additional direct-converter suite exposed two existing pinned-source Set/
Filter regressions: presentation compaction grouped a single State’s scalar AND
into a multi-field leaf, while the Filter adapter still accepted only one field.
The adapter now restores an explicit AND of field leaves. Original operators,
quantifiers, action/order and record boundaries are preserved. The existing
independent original-source readers verify the result; no expected proof floor
is changed. The correction has no effect on the five existing sample programs.

The old18 VERIFIED/10 PARTIAL/1 UNPROVED independent snapshot remains historical;
contract closure here is not a claim of29 runtime-proved decisions. Native Result
A’s intentional pre-freeze wire break remains the previously approved change;
this closure adds documentation/annotations and repairs the converter boundary,
without silently migrating historical Results or canonical authoring defaults.
