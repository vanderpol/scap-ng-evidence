# SCAP-NG RI Ubuntu 24.04 native benchmark receipt

This is a real same-host Ubuntu 24.04.5 diagnostic run of 20 source-linked native SCAP-NG 0.4.1 Rules. It is not a RHEL9 compliance claim and is not independent OVAL/OpenSCAP equivalence.

The package was converted with Tools main and the canonical schema pins recorded in `receipt.json`. The package archive is included for exact replay. Raw target namespace identifiers are intentionally excluded; the receipt retains authority and scope classification.

## Replay

```bash
# Build RI from RI commit in receipt.json with Go 1.27.x.
go build -trimpath -buildvcs=false -o ri-benchmark ./cmd/ri-benchmark

./ri-benchmark \
  --package ubuntu2404-current-tools-package \
  --output-dir results \
  --evidence-dir evidence \
  --workers 4 --queue 8 --timeout 60s \
  --report both --progress off \
  --target ubuntu-24.04-b317 --snapshot ubuntu-b317
```

The original source ZIP is the pinned Ubuntu 24.04 STIG archive identified by its SHA-256 in `receipt.json`; it is not redistributed here.
