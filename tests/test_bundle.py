import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "evidence_summary.json"


class PublicBundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))

    def test_repository_sequence(self):
        s = self.data["repository_sequencing"]
        self.assertEqual(297 + 5, 302)
        self.assertTrue(math.isclose(s["match_fraction"], 297 / 302, rel_tol=1e-12))

    def test_oldest_commit_replication(self):
        r = self.data["repository_sequencing"]["oldest_commit_replication"]
        self.assertEqual(318 + 32, 350)
        self.assertTrue(math.isclose(r["match_fraction"], 318 / 350, rel_tol=1e-12))
        self.assertEqual(r["creation_to_oldest_commit_lag_seconds"]["within_2_seconds"], 350)

    def test_outbound_fail_closed(self):
        o = self.data["outbound_targeting"]
        self.assertIsNone(o["authoritative_six_way_intersection"])
        self.assertEqual(set(o["excluded_accounts"]), {"KevinWong455", "9Michael-Cooley"})
        self.assertLessEqual(o["four_way_intersection"], min(o["captured_unique_counts"].values()))

    def test_git_provenance_boundary(self):
        g = self.data["git_object_provenance"]
        self.assertEqual(g["cross_owner_blob_sha_count"], 10)
        self.assertEqual(g["blob_shas_spanning_all_six"], 6)
        self.assertEqual(g["cross_owner_tree_sha_count"], 0)
        self.assertFalse(g["exact_cross_owner_author_name_email_bridge"])

    def test_morphology_boundary(self):
        m = self.data["commit_identity_morphology"]
        self.assertEqual(m["exact_normalized_pair_count"], 3)
        self.assertEqual(m["possible_pair_count"], 15)
        self.assertEqual(m["owner_login_association"]["permutations"], 720)
        self.assertEqual(m["owner_login_association"]["observed_rank"], 369)
        self.assertTrue(math.isclose(m["owner_login_association"]["exact_one_sided_p"], 0.5333333333333333))
        self.assertFalse(m["owner_login_association"]["supported"])
        self.assertFalse(m["raw_author_email_values_released"])


if __name__ == "__main__":
    unittest.main()
