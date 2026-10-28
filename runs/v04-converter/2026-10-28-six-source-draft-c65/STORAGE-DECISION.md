# Bounded raw-evidence storage decision

Status: **DRAFT — NOT RUNTIME VERIFIED**. Refs vanderpol/scap-ng#251, owner priorities comment 6477986104.

The owner explicitly requested immediate publication of the existing six-benchmark archive in this evidence repository, including inspectable generated JSON/YAML and every-Rule evidence. The existing archive is 12,276,247 bytes and contains 4,301 files. Its SHA-256 is `07f7b24f4d0522630159fbddf9f6d643ffcac3d49d3c482dc7fb263de9793317`.

The preferred release-asset upload failed with HTTP 401 at `uploads.github.com` using configured authentication. Metadata and Git publication succeeded. Recovery confirmed no release asset remained uploaded and the immutable tag was absent. No duplicate upload or conversion regeneration was performed.

For this specifically requested inspectable draft, retain the single unchanged ZIP in evidence Git and pin it with the DRAFT tag. This is an explicit storage decision under LARGE-EVIDENCE-POLICY.md, based on the owner's immediate review requirement and the failed preferred storage route. Compact analysis, hashes, ledger, source pins and reproduction metadata accompany it. No bulk payload enters the schema/source repository. Future routine runs should continue preferring release assets or Actions artifacts; this is not a general raw-evidence retention policy change.

The archive's internal manifest records the originally intended release-asset storage. The external manifest and this addendum supersede only that storage intent. Source/toolchain identities, native bytes, classifications and checksums are unchanged. No release, runtime verification, original-source semantic proof or complete migration is asserted by publication.
