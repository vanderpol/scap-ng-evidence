# SCAP-NG RI Ubuntu current-Tools diagnostic qualification

This directory contains the source-traced, non-root Ubuntu 24.04 diagnostic replay of a compact 20-Rule SCAP-NG 0.4.1 package. It is not RHEL9 compliance qualification.

- RI execution: `c407c8b2b5d89f2edf10b1846df8725e836c7836`
- Tools converter: `273b12cf4590896ce9b55d9c95df5102c6bfd2e6`
- Canonical schema: `5ee55288b369da26f308f40813e545b78dff2753`
- Source ZIP SHA-256: `40229cd7a41e6ff4a8cfb675523f767292d1460edbc68fe9ba5258c530c8b4a7`
- Source XML SHA-256: `eac6f7a6a1e80c52d02c508d939eb09aa09b7fe6eaeb060b8aa21e095719c940`
- Rules: 20 selected from 194 source Rules; 13 PASS / 2 FAIL / 5 UNKNOWN / 0 ERROR
- Assessments: 21; Tests: 28; Items observed/retained: 16/16
- Target: Ubuntu 24.04.5, non-root, CapEff=0, current process namespaces, sudo noninteractive unavailable
- Resource use: 0.73s wall, 59,476 KiB peak RSS

The canonical Result and Assessment JSON files preserve actual collected Items, completeness, reasons and evidence provenance. Source expected outcomes were never supplied to the evaluator. See `qualification-receipt.json` for the complete machine-readable crosswalk and artifact hashes.
