# 0.4 schema-freeze readiness after Result A (#255/#269)

**NO-GO for the whole schema family; no freeze performed.** The
[machine audit](v04-schema-freeze-readiness-20261102.json) rechecks all29 owner
decisions, version-local schema/reference closure, native source-backed Result
acceptance and negative mutations. The earlier dated audit remains historical.

| Language-contract finding | Current disposition | Owner input |
| --- | --- | --- |
| LC-NATIVE-RESULTS | CLOSED: owner adopted A; native wire, source/record locations, controls and reason/evidence implemented and tested. [Review packet](v04-native-result-adoption-20261102.md). | None |
| LC-SELECTOR-CASE | OPEN:15 capability/API cases still lack documented per-selector case contracts under approved Decision22. This is unfinished contract research/documentation, distinct from executing collectors. | No new vote; finish source/API-backed documentation without inventing a universal switch |

Optional Input presence is implemented using the adopted explicit guard and25
review cases. Compatible field-level datatype declarations remain supported;
no global removal or proof rebaseline occurred. The independent initial audit
and its later18 VERIFIED/10 PARTIAL/1 UNPROVED score remain historical snapshots;
they are not relabeled as29 scanner-proved decisions.

Future scanner verification includes actual provider/dependency adapters,
collection/error versus absence behavior, arrays/Variable/Set execution and cache
isolation, platform/API lookup behavior and Rule follow-up with observed target
evidence. Future VS Code verification includes real host/save/undo, Guided and
Structured UI, screenshots and the bounded regex playground. These do not require
new language votes and do not substitute for the remaining selector contracts.

No genuine owner decision remains in this migration/audit. Keep PR268 draft;
no merge/freeze/release/corpus regeneration or baseline replacement.
