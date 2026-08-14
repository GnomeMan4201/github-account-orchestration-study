# Six accounts, four independent signals

## Technical assessment

**Status:** final; collection closed.  
**Scope:** six GitHub accounts observed in the same follower wave and measured under bounded, frozen protocols.  
**Assessment:** shared technical orchestration / generation is strongly supported. Common human ownership is not established.

## Evidence matrix

| Layer | Observation | Derived result | Interpretation | Limitation / disconfirming observation |
|---|---|---|---|---|
| Repository sequencing | 303-event dense creation run | 297/302 expected transitions = 98.34% | coordinated repository production | five deviations retained; timestamps do not identify an operator |
| Oldest-commit replication | 351 repositories in an independently collected provenance set | 318/350 transitions = 90.86%; 350/351 oldest commits within 2 s of repository creation | independent timing corroboration of the already-frozen cycle | 32 deviations retained; not a new cycle-selection procedure |
| Outbound targeting | four count-reconciled following sets | three large sets Jaccard 0.9895–0.9906; four-way intersection 20,067 | coordinated acquisition targeting | two accounts failed validation and remain excluded; no six-way intersection |
| Git-object provenance | exact Git objects across 351 public repositories | 10 cross-owner blob SHAs; six span all six owners | exact shared technical generation inputs | no cross-owner tree SHA reuse; no exact author identity bridge |
| Commit-identity morphology | one predeclared punctuation-insensitive local-part normalization | three disjoint exact normalized pairs; all three are frozen cycle edges | structured identity-generation morphology consistent with shared orchestration | raw identities differ; no raw skeleton group; username-association p = 0.5333 |

## 1. Repository sequencing

A mechanically selected dense run contained 303 repository-creation events. The first complete cycle established the account order:

```text
KevinWong455
-> Seo-yeonLee
-> ElvinHasanov3d
-> badiranssen
-> RashidSaeedAlMazrouei18
-> 9Michael-Cooley
-> repeat
```

Across 302 consecutive transitions, 297 followed the expected next account and five deviated. The match fraction is `297 / 302 = 0.9834437086`.

The five deviations are retained. The result supports coordinated repository production but does not identify the mechanism or operator.

### Independent replication

A later repository-provenance collection did not redefine the cycle. It tested the existing order using oldest-commit timestamps from 351 repositories.

Of 350 consecutive owner transitions, 318 matched the expected cycle: `318 / 350 = 0.9085714286`.

Creation-to-oldest-commit lag was also tightly concentrated:

- median: 1 second;
- 350/351 repositories: within 2 seconds;
- maximum: 72 seconds.

This is independent corroboration of the temporal orchestration signal.

## 2. Outbound target selection

Four captured following sets reconciled to their corresponding captured profile counts:

| Account | Following set |
|---|---:|
| Seo-yeonLee | 20,509 |
| ElvinHasanov3d | 33,938 |
| RashidSaeedAlMazrouei18 | 33,902 |
| badiranssen | 33,822 |

The three approximately 34k sets had pairwise Jaccard values:

- Elvin / Rashid: 0.9905519204
- Elvin / badiranssen: 0.9903069467
- Rashid / badiranssen: 0.9894832702

Their three-way intersection was 33,581 targets, 99.2874% of the smallest of the three sets.

Seo's smaller set was 98.6–99.1% contained in each larger set. The four-way intersection was 20,067 targets, 97.8448% of Seo's captured set.

### Fail-closed exclusions

`KevinWong455` and `9Michael-Cooley` failed the original count-reconciliation check. Each received exactly one stricter, predeclared double-pass retry. Both retries failed closed.

Therefore:

- neither account is included in authoritative overlap metrics;
- no authoritative six-account following snapshot exists;
- no six-way target intersection is claimed.

## 3. Exact Git-object provenance

The provenance phase covered 351 public repositories with zero repository errors and zero recursive-tree truncations.

Ten Git blob SHA values appeared under repositories owned by more than one cohort account. Six exact blob objects occurred under all six owner namespaces:

| Blob SHA | Representative path | Repositories |
|---|---|---:|
| `7c155d430d2335afd110471ef99c6d3f6037870c` | `.gitignore` | 48 |
| `833251b73be2d2d6640f0c4d54ae0a00bd1cacc8` | `.gitignore` | 48 |
| `86e9532eaaf9caf0ea9df8e68dff85cab2b2d2d7` | `tsconfig.json` | 50 |
| `9a459cec46abd170feaaf4afa81085aff55da08c` | `.env.example` | 48 |
| `ce9b28e4333b3b0345f1b9647937cc54d724dc0e` | `.gitignore` | 102 |
| `d9cf46be4a2c3a44a748a13abc1060fe58bf1aac` | `src/App.css` | 48 |

Exact blob equality is byte-level object reuse. It can arise from shared templates or tooling and does not by itself prove common control.

No cross-owner tree SHA reuse or root-tree SHA reuse was observed. The result therefore demonstrates shared file objects, not shared repository trees or history.

No exact cross-owner author `(name, email)` identity bridge was observed. A generic `GitHub` / `web-flow` committer identity was present across owners but is platform metadata and is treated as non-discriminating.

The highest defensible linkage class is **exact shared Git-object provenance with independent sequencing corroboration**.

## 4. Commit-identity morphology

The provenance dataset exposed visually related but non-identical commit-author email strings. Because similarity was not predeclared in that phase, the strings were not scored there.

A separate protocol fixed one normalization before scoring:

1. take the email local part;
2. Unicode-casefold it;
3. remove characters outside ASCII `[a-z0-9]`.

No alternate normalization was selected after the result was known.

Across all 15 account pairs, three disjoint pairs became exact under that rule:

- `KevinWong455` / `9Michael-Cooley`
- `Seo-yeonLee` / `ElvinHasanov3d`
- `badiranssen` / `RashidSaeedAlMazrouei18`

All three are edges in the six-account cycle frozen before the morphology phase. The three alternating cycle edges had Levenshtein distances 9, 11, and 9.

This release does not publish the raw author-email strings.

### Negative test

A separately predeclared test asked whether visible GitHub handles predicted the corresponding normalized local parts. All `6! = 720` assignments were enumerated.

The observed assignment ranked 369/720 with exact one-sided `p = 0.5333333333`.

That test does not support a simple handle-derived identity generator.

The morphology result is therefore **not an identity bridge**. It is structured morphology consistent with the same orchestration structure measured independently elsewhere.

## 5. Triangulation

The four primary evidence types use different observables:

- repository timestamps;
- following-set membership;
- exact content-addressed Git objects;
- predeclared commit-identity morphology.

No formal joint-probability model is claimed, and the measurements are not described as statistically independent in the probabilistic sense.

The narrower conclusion is sufficient: differently constructed measurements, including failed validations and negative tests, converge on the same operational explanation.

## 6. Claim boundary

### Strongly supported

A shared technical orchestration / generation system across the measured cohort.

### Not established

- one human operator;
- shared credentials;
- shared IP or network infrastructure;
- a specific service, vendor, or account farm;
- deliberate targeting of the observer;
- publication-triggered discovery;
- malicious intent beyond the measured behavior.

## 7. Reproducibility and closure

Machine-readable values are in [`data/evidence_summary.json`](data/evidence_summary.json). Provenance anchors are in [`data/source_ledger.json`](data/source_ledger.json). Run [`python verify_bundle.py`](verify_bundle.py) to verify the released arithmetic and invariants.

The public package intentionally omits large raw relationship lists, raw commit-author emails, and private workflow artifacts. See [`REPRODUCING.md`](REPRODUCING.md) for the exact verification boundary.

Collection for this study is closed. Any future extension requires a new research question and a protocol fixed before new evidence is inspected.
