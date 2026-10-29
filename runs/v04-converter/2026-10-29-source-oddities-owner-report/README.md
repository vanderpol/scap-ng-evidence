# Observed source oddities and improvement opportunities

Owner-requested report of the observed source, packaging, standards and converter
oddities. Start with REPORT.pdf, or download scap-ng-source-oddities-20261029.zip
for standalone HTML/Markdown, filterable affected-rules.csv and detailed JSON.
The CSV covers 3,024 distinct Rules and all 2,981 residual automated blockers.
There are 23 finding classes with affected sources, exact identities, confidence,
likely area of control and suggested improvement checks. Finding counts overlap.

Numeric capture clarification: extracting an integer-representable value such
as 5 is valid for numeric use. SV-215833's HTTP-timeout Variable 21583310 is
explicitly excluded from the text-as-int concern. The separate exec-timeout
intermediate Variables split/capture/merge nonnumeric text; those are the concern.
No original source, validator or scanner was changed. This is an observed static
investigation, not a complete source-semantic audit or runtime-equivalence claim.

Canonical report source:
https://github.com/vanderpol/scap-ng/blob/4d78f700a4a555b474b38c230d7199e6e1a6bf21/docs/audit/v04-source-oddities-owner-report-20261029.md
