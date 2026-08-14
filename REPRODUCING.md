# Reproducing the public release

This package is intentionally a **sanitized reproducibility bundle**, not a dump of the private evidence workspace.

## What you can verify from this release

The public files are sufficient to verify that the reported arithmetic and claim boundaries are internally consistent, including:

- `297 + 5 = 302` for the repository-creation cycle and the reported 98.34% match fraction;
- `318 + 32 = 350` for the independent oldest-commit replication and its 90.86% match fraction;
- all six released pairwise outbound intersections / unions and their Jaccard values;
- that the four-way intersection cannot exceed the smallest released following set;
- that the released Git-object counts distinguish blob reuse from tree reuse;
- that three morphology pairs out of 15 possible pairs are reported separately from the negative 720-permutation handle-association test;
- that excluded claims remain excluded in the machine-readable summary.

Run:

```bash
python verify_bundle.py
```

Expected result:

```text
PASS: sanitized evidence bundle is internally consistent
```

Optional unit-test form:

```bash
python -m unittest discover -s tests -v
```

## What this release does not reproduce

The package intentionally does not publish:

- raw GitHub API pages captured during collection;
- raw outbound-follow membership lists containing tens of thousands of third-party accounts;
- raw commit-author email addresses;
- private GitHub Actions artifacts;
- authentication metadata or tokens;
- later duplicate collections excluded by the frozen protocols.

Therefore a third party cannot recreate every raw collection byte-for-byte from this release alone. The private source ledger retains run IDs, artifact IDs, SHA-256 digests, and source revisions so the published result remains provenance-bound rather than being presented as an untraceable summary.

## Why the boundary exists

The public question is whether the published inference is supported by a disciplined chain of evidence. Releasing large third-party relationship lists and raw identity strings would add exposure without materially improving that public claim.

The release therefore separates two concepts:

1. **public reproducibility** — verify the released measurements, calculations, exclusions, and claim boundary;
2. **private evidence preservation** — retain the original bounded collection artifacts and cryptographic provenance for audit without publishing unnecessary raw personal data.

## Measurement status

Collection for the published study is closed. Do not reinterpret this package as authorization to rerun failed snapshots until they pass, try alternate identity normalizations, or add accounts to strengthen the narrative.

Any extension should begin with a new question and a protocol fixed before new evidence is scored.
