"""Test double for sentry_sdk. Records init kwargs and never sends events."""

from __future__ import annotations

import json
import os

INIT_CALLS: list[dict] = []


def init(**kwargs):
    INIT_CALLS.append(kwargs)
    path = os.environ.get("SENTRY_STUB_LOG", "").strip()
    if path:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(kwargs, handle)
