# Recovered 29-decision audit and reproducible metadata pack

Source **d3ccc8f7d**, recovered remediation **fecb541f9**, editor **ae7f812**.
All12 source hosted runs (11 workflows) and editor CI41349007241 PASS.
Fresh38 recovery tests and6 metadata tests PASS; editor unit, lint, external
integration and package PASS. The original stale pack rejection is retained.

Audit: **18 VERIFIED /10 PARTIAL /1 UNPROVED /0 FAILED**, bounded static scope.
Failures4/11/23 corrected;16 safely rejects unguarded optional Inputs but needs
an approved omission guard before consumption can be supported. The matrix
records every partial disposition. No collector/scanner/editor-host proof.

Fresh conversion omits redundant field datatype; complete grammar removal is
unsafe because version+regex and binary+case-insensitive equality change domain
when stripped. Existing qualifiers remain compatible. No new semantic decision.

The exporter now serializes JSON keys deterministically. Both hash-seed exports
are byte-identical across235 files; all233 parsed resources retain their values.
The pack is a draft checkpoint, not a release. Profile hash:
`5d736b1c82fcb6ea3ee4f7af6704dd1a9b630d25ec8f28e2064645a1500c48dc`.

Original sources, fixtures,0.1–0.3 schema trees and earlier proof/example trees
retain Git tree identity. Existing65-stream corpus and R1/R2 were not regenerated
or overwritten. Keep PR268 draft; no merge/freeze/tag/release.

See manifest.json for exact commands, pins, test evidence and limitations;
PAYLOAD-MANIFEST.json covers every file except itself and the archive.
