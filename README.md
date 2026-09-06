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

## Longitudinal follow-on

The original six-account investigation remains **closed**. New observations are not retroactively folded into its frozen protocols or measurements.

A separate follow-on record documents later follower waves observed through September 5, 2026, including repeated Git-history artifacts, social-graph expansion, same-account pruning, coordinated entry into the observer's follower set, and cross-generation graph relationships.

Start with [`LONGITUDINAL_UPDATE_2026-09-05.md`](LONGITUDINAL_UPDATE_2026-09-05.md).

Five representative August 28 Git commits cited in that update were independently rechecked on September 6 and remain publicly resolvable with the exact published merge grammar and `nancodero` co-author trailer.

Published narrative: https://dev.to/gnomeman4201/kept-getting-strange-github-followers-so-i-measured-them-3fac

## What is public here

This package contains the publication article, a technical assessment, sanitized machine-readable results, a provenance ledger, a separated longitudinal follow-on record, and consistency checks that can be run locally.

The release intentionally omits raw GitHub API page captures, full outbound-follow membership lists, raw commit-author email addresses from the original closed study, private workflow artifacts, and other material that adds exposure without being necessary to understand the published claim.

Because those raw inputs are not released, this package supports **audit of the reported arithmetic, protocol boundaries, evidence lineage, public immutable anchors, and claim discipline**. It does not pretend to offer a byte-for-byte public rerun of every private collection step. See [`REPRODUCING.md`](REPRODUCING.md).

## Start here

- [`REPORT.md`](REPORT.md) — concise technical assessment of the closed six-account study
- [`ARTICLE.md`](ARTICLE.md) — reader-facing narrative for the closed study
- [`LONGITUDINAL_UPDATE_2026-09-05.md`](LONGITUDINAL_UPDATE_2026-09-05.md) — later follower-wave evidence and claim ledger
- [`data/evidence_summary.json`](data/evidence_summary.json) — sanitized machine-readable findings for the closed study
- [`data/source_ledger.json`](data/source_ledger.json) — frozen run / artifact / commit provenance
- [`REPRODUCING.md`](REPRODUCING.md) — public verification scope and commands
- [`NOTICE.md`](NOTICE.md) — sanitization and attribution boundaries

## Collection status

The investigation phase covered by `REPORT.md` is **closed**. Failed validations remain failed, excluded accounts remain excluded from measurements they did not pass, and no alternate normalization or additional account was added after results were observed.

The longitudinal update is explicitly a separate follow-on observation record. Future promotion of a pruning-mechanism claim requires a complete pre-event graph baseline and a post-event collection under a newly frozen protocol.
