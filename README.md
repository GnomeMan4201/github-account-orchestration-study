# GitHub Account Orchestration Study

A sanitized reproducibility package for a bounded OSINT investigation into six GitHub accounts that exhibited coordinated repository creation, outbound targeting, exact Git-object reuse, and commit-identity morphology.

## Final assessment

The released measurements strongly support a **shared technical orchestration / generation system** across the six-account cohort.

They do **not** establish:

- one human operator;
- shared credentials;
- shared IP or network infrastructure;
- a specific service, vendor, or account farm;
- deliberate targeting of the observer;
- publication-triggered discovery;
- malicious intent beyond the behavior directly measured.

## Four evidence layers

| Layer | Released result | Primary limitation |
|---|---|---|
| Repository sequencing | 297/302 consecutive repository-creation transitions matched one six-account cycle (98.34%) | five deviations retained; timestamps do not identify an operator |
| Outbound targeting | three large reconciled following sets had Jaccard 0.9895–0.9906; four-way intersection 20,067 | two accounts failed completeness/stability validation and remain excluded |
| Git-object provenance | 10 exact blob SHAs crossed owner namespaces; six occurred under all six owners | no cross-owner tree SHA reuse; no exact cross-owner author identity bridge |
| Commit-identity morphology | three disjoint pairs became exact under a normalization frozen before scoring; all three align to frozen cycle edges | raw identities differ; handle-to-email permutation test was negative (p = 0.5333) |

A later provenance dataset independently reproduced the account cycle from oldest commits: 318/350 transitions (90.86%). In the same dataset, 350/351 repositories received their oldest observed commit within two seconds of repository creation.

## What is public here

This package contains the publication article, a technical assessment, sanitized machine-readable results, a provenance ledger, and consistency checks that can be run locally.

The release intentionally omits raw GitHub API page captures, full outbound-follow membership lists, raw commit-author email addresses, private workflow artifacts, and other material that adds exposure without being necessary to understand the published claim.

Because those raw inputs are not released, this package supports **audit of the reported arithmetic, protocol boundaries, evidence lineage, and claim discipline**. It does not pretend to offer a byte-for-byte public rerun of every private collection step. See [`REPRODUCING.md`](REPRODUCING.md).

## Start here

- [`REPORT.md`](REPORT.md) — concise technical assessment
- [`ARTICLE.md`](ARTICLE.md) — reader-facing narrative
- [`data/evidence_summary.json`](data/evidence_summary.json) — sanitized machine-readable findings
- [`data/source_ledger.json`](data/source_ledger.json) — frozen run / artifact / commit provenance
- [`REPRODUCING.md`](REPRODUCING.md) — public verification scope and commands
- [`NOTICE.md`](NOTICE.md) — sanitization and attribution boundaries

## Collection status

The investigation phase covered by this package is **closed**. Failed validations remain failed, excluded accounts remain excluded from measurements they did not pass, and no alternate normalization or additional account was added after results were observed.

Any future extension requires a genuinely new research question and a protocol frozen before inspecting new evidence.
