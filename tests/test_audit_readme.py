"""local_target skips remote/anchor sources and strips query/fragment suffixes."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_readme import local_target  # noqa: E402


class LocalTargetTests(unittest.TestCase):
    def test_non_local_sources_are_skipped(self) -> None:
        for src in ("https://x/a.png", "http://x/a.png", "data:image/png;base64,AA", "#top"):
            self.assertIsNone(local_target(src, ROOT))

    def test_query_and_fragment_are_stripped(self) -> None:
        expected = (ROOT / "assets" / "a.svg").resolve()
        self.assertEqual(local_target("assets/a.svg?v=2#frag", ROOT), expected)


if __name__ == "__main__":
    unittest.main()
