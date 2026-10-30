# Complete revised 65-STIG DRAFT download

Download the three parts below and `manifest.json` from this directory, then:

```bash
python download_draft.py --parts /path/to/downloaded-parts --output /tmp/all-65-revised-draft.zip
```

Or run `python download_draft.py --output /tmp/all-65-revised-draft.zip` to fetch
the immutable parts automatically. Requires Python 3 standard library only.
Every part and the combined ZIP are checksum-verified. Extract and open index.html.

- [all-65-revised-draft.zip.part01](https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download/all-65-revised-draft.zip.part01)
- [all-65-revised-draft.zip.part02](https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download/all-65-revised-draft.zip.part02)
- [all-65-revised-draft.zip.part03](https://raw.githubusercontent.com/vanderpol/scap-ng-evidence/v04-revised-all65-draft-files-20261030-a08c9beb9/runs/v04-converter/2026-10-30-all-65-revised-draft-download/all-65-revised-draft.zip.part03)

Combined: **108,003,966 bytes**, SHA256
`a09ee9a13cdfeeb1b8599eab61308e935a19b99eb62eadafd32002d13d90f8bd`.

**65 Benchmarks / 8,892 Rules:** 4,258 retained static-proved native +2,559
UNVERIFIED native +422 blocked automated +1,653 manual/OCIL preserved. All
6,817 native candidates compile. All accepted proof hashes remain unchanged.
Original signed source, manual content, full ledgers and native JSON/YAML are
inside the ZIP. [Detailed provenance/counts/cohort recovery](../2026-10-30-all-65-revised-draft-rc/README.md).

Storage exception: preferred GitHub release-asset upload returned HTTP401 for
uploads.github.com; ordinary Git push succeeds. The owner expressly requires a
complete downloadable DRAFT. This bounded fallback retains one 108MB archive
in three parts; no earlier frozen archive is replaced. See manifest.json.
The earlier metadata-only prerelease has no ZIP asset; these immutable Git
links are the actual download. No final 0.4.0 release/tag or runtime claim.
