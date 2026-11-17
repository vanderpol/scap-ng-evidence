# Tools P0 0.4.1 qualification

Clean Tools `02b283c3dbe81c84532f434fbbf6d180d5eb84a8` against canonical `5ee55288b369da26f308f40813e545b78dff2753` and merged RI main `dc77e33cb9cc74479622681e00ff776e2161b6ba`.

**46/46 actual Definition outcomes match: 44 TRUE, one FALSE, one UNKNOWN.** The independent checker did not supply outcomes to RI. Original source and expected outcomes remain unchanged.

Go 1.27.4 full/race/vet and exact schema checks pass. Converter suite: 287 tests, five fixture-dependent skips. Two pack/pin rebuilds match committed bytes; 304 original source truth vectors remain covered.

Five Windows relation schema holds and 13 historical signed-benchmark assertion failures remain. The latter reproduce on pre-change Tools with its approved snapshot. No release, whole-corpus or original malformed OVAL equivalence claim.

See manifest.json for exact commands, input pins, raw-output hashes and the explicit reproducible-only storage decision. Actual ledger, independent gate, canonical delta, all eight source normalization records and diagnostic holds are retained here.
