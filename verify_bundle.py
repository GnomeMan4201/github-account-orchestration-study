#!/usr/bin/env python3
"""Verify arithmetic and claim-boundary invariants in the sanitized release."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "evidence_summary.json"


def close(a: float, b: float, *, tol: float = 1e-12) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def main() -> None:
    d = json.loads(DATA.read_text(encoding="utf-8"))

    # Repository-creation chronology.
    seq = d["repository_sequencing"]
    assert seq["expected_cycle_transitions"] + seq["deviations"] == seq["transition_count"]
    assert close(
        seq["match_fraction"],
        seq["expected_cycle_transitions"] / seq["transition_count"],
    )

    # Independent oldest-commit replication.
    rep = seq["oldest_commit_replication"]
    assert rep["expected_cycle_transitions"] + rep["deviations"] == rep["transition_count"]
    assert close(
        rep["match_fraction"],
        rep["expected_cycle_transitions"] / rep["transition_count"],
    )
    lag = rep["creation_to_oldest_commit_lag_seconds"]
    assert lag["within_2_seconds"] <= lag["analyzable_repositories"]
    assert lag["analyzable_repositories"] == rep["repository_count"]

    # Outbound-target arithmetic.
    outbound = d["outbound_targeting"]
    counts = outbound["captured_unique_counts"]
    for row in outbound["pairwise"]:
        assert row["intersection"] <= min(counts[row["a"]], counts[row["b"]])
        expected_j = row["intersection"] / row["union"]
        assert close(row["jaccard"], expected_j)
        expected_containment = row["intersection"] / min(counts[row["a"]], counts[row["b"]])
        assert close(row["smaller_set_containment"], expected_containment)

    smallest = min(counts.values())
    assert outbound["four_way_intersection"] <= smallest
    assert outbound["authoritative_six_way_intersection"] is None
    assert set(outbound["excluded_accounts"]) == {"KevinWong455", "9Michael-Cooley"}

    # Exact Git-object provenance remains distinct from tree/history reuse.
    git = d["git_object_provenance"]
    assert git["blob_shas_spanning_all_six"] <= git["cross_owner_blob_sha_count"]
    assert len(git["all_six_blob_objects"]) == git["blob_shas_spanning_all_six"]
    assert git["cross_owner_tree_sha_count"] == 0
    assert git["cross_owner_root_tree_sha_count"] == 0
    assert git["exact_cross_owner_author_name_email_bridge"] is False

    # Morphology is a separate structural result, not an exact raw identity bridge.
    morph = d["commit_identity_morphology"]
    assert morph["exact_normalized_pair_count"] == len(morph["exact_pairs"])
    assert morph["possible_pair_count"] == 15
    assert morph["exact_pairs_that_are_frozen_cycle_edges"] <= morph["cycle_edge_count"]
    assert morph["owner_login_association"]["permutations"] == 720
    assert 1 <= morph["owner_login_association"]["observed_rank"] <= 720
    assert 0.0 <= morph["owner_login_association"]["exact_one_sided_p"] <= 1.0
    assert morph["owner_login_association"]["supported"] is False
    assert morph["raw_author_email_values_released"] is False

    # Final claim boundary.
    assessment = d["final_assessment"]
    assert assessment["shared_technical_orchestration_generation_system"] == "strongly_supported"
    for key in (
        "common_human_operator",
        "shared_credentials",
        "shared_network_infrastructure",
        "specific_vendor_or_service",
        "deliberate_targeting",
        "publication_causation",
    ):
        assert assessment[key] == "not_established"

    print("PASS: sanitized evidence bundle is internally consistent")


if __name__ == "__main__":
    main()
