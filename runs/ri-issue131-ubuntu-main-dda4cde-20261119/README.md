# Ubuntu 24.04 native benchmark diagnostic — RI main dda4cde

This bundle is a source-traced SCAP-NG 0.4.1 diagnostic execution on Ubuntu 24.04.5. It is **not** a RHEL9 compliance qualification.

- RI: `dda4cde81a56f95d408d66611db075f82883da89`
- Tools: `df2deb1a514cdd0babbccdf2d240fba4e9811d6d`
- Canonical: `5ee55288b369da26f308f40813e545b78dff2753`
- Source ZIP SHA-256: `40229cd7a41e6ff4a8cfb675523f767292d1460edbc68fe9ba5258c530c8b4a7`
- Rules: 33 (`23 pass`, `4 fail`, `6 unknown`, `0 error`)
- Assessments: 34
- Wall: 0.22 s; peak RSS: 61,604 KiB; 1,824 filesystem output blocks
- Authority: non-root, CapEff=0, `sudo -n` unavailable; current process namespaces

The first corrected source-linked transition is `SV-270691`: UNKNOWN (`missing_field_held`) → FAIL (`value_mismatch`) after preserving the complete shellcommand Item and its actual exit status 123. Remaining UNKNOWN results retain explicit collector, completeness, privilege or source-typing reasons.

Human reports include Rule → Assessment → Test → Object/Require → collected Item details and provenance. Results remain canonical machine-readable JSON.
