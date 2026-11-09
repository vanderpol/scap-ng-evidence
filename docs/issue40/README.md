# Historical publication boundary

Refs [Tools #40](https://github.com/vanderpol/scap-ng-tools/issues/40), shared gate [Tools PR #41](https://github.com/vanderpol/scap-ng-tools/pull/41). The existing full-65 release workflow is denied through that exact common gate before any download/reflow and again at the actual release step. This is intentional fail-closed behavior: no qualified full-65 reproduction is available. The original historical commands remain in the file and all immutable evidence stays preserved; no release is executed here.

[Preservation receipt](preservation.json) pins the original workflow AST and exact Git trees for all runs/manifests/summaries. Tests reconstruct and check the old workflow after removing only the gates, execute a harmless publication sentinel after the real denial, and verify unchanged historical trees. CI reads tree identities without fetching historical corpus blobs. No current qualification is inferred from old schema/static/compiler proofs.

This is a review proposal, not deployed or repository-wide completion. Server permission policy remains inaccessible (HTTP 403), and historical refs/direct uploads are not proved constrained. Those remain blockers in Tools #40. New current-native publication must use the common approved-producer/schema/final-byte admission; historical artifacts cannot be promoted by reflowing or renaming them.
