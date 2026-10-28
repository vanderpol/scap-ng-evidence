# Evidence runs

Generated evidence sets live here.

Use a stable run identifier and include a manifest satisfying [EVIDENCE-CONTRACT.md](../EVIDENCE-CONTRACT.md).

Suggested shape:

```text
runs/
  niwc-current/
    YYYY-MM-DD-description/
  oval-self-assertion/
    YYYY-MM-DD-description/
  repository-audit/
    YYYY-MM-DD-description/
```

- [2026-10-28 SCAP-NG 0.4 six-source converter DRAFT](v04-converter/2026-10-28-six-source-draft-c65/README.md): actual generated JSON/YAML, complete 1,567-Rule ledger, exact c65a134b5 toolchain and NIWC source pins.

- [2026-10-28 SCAP-NG 0.4 all-65 NIWC DRAFT](v04-converter/2026-10-28-niwc-65-draft-248895772/README.md): 8,892 original Rules, generated JSON/YAML, complete ledgers and four explicit SQL-extension package exceptions.

- [2026-10-28 verified static six-source primary OVAL](v04-converter/2026-10-28-six-primary-static-verified-248895772/README.md): 1,072 independent primary proofs, all 1,055 previous program hashes retained, exact-commit maintained suite green; no runtime claim.
