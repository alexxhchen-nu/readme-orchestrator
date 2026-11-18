"""Opt-in Sentry error monitoring for readme-orchestrator CLIs.

The tool stays quiet unless ``SENTRY_DSN`` is set. No DSN is stored in the
repository. ``send_default_pii`` stays off, and performance traces are sampled
only when ``SENTRY_TRACES_SAMPLE_RATE`` says so.
"""

from __future__ import annotations

import os
import sys

VERSION = "2.0.0"
RELEASE = f"readme-orchestrator@{VERSION}"
TRACES_SAMPLE_RATE_ENV = "SENTRY_TRACES_SAMPLE_RATE"
DEFAULT_TRACES_SAMPLE_RATE = 0.0


def init_sentry() -> bool:
    """Initialize Sentry when ``SENTRY_DSN`` is set.

    Returns True when the SDK was initialized. Returns False when monitoring
    is disabled or the SDK is not installed. Never raises for a missing SDK
    or a bad sample-rate value.
    """
    dsn = os.environ.get("SENTRY_DSN", "").strip()
    if not dsn:
        return False

    try:
        import sentry_sdk
    except ImportError:
        print(
            "SENTRY_DSN is set but sentry-sdk is not installed. "
            "Error monitoring is disabled. "
            "Install it with: python3 -m pip install 'sentry-sdk>=2.70,<3'",
            file=sys.stderr,
        )
        return False

    release = os.environ.get("SENTRY_RELEASE", "").strip() or RELEASE
    # Omit environment so the SDK keeps its own default ("production") and
    # still honors SENTRY_ENVIRONMENT. Passing environment= here would win
    # over that variable.
    # Pass send_default_pii=False explicitly. On sentry-sdk 2.x a partial
    # data_collection dict opts into permissive defaults, which is looser than
    # send_default_pii=False. Late 2.x warns that the flag is deprecated; that
    # DeprecationWarning stays inside the SDK and does not change CLI output
    # under Python's default warning filters.
    sentry_sdk.init(
        dsn=dsn,
        release=release,
        send_default_pii=False,
        include_local_variables=False,
        traces_sample_rate=_traces_sample_rate(),
        server_name=os.environ.get("SENTRY_SERVER_NAME", "").strip()
        or "readme-orchestrator",
    )
    return True


def _traces_sample_rate() -> float:
    raw = os.environ.get(TRACES_SAMPLE_RATE_ENV, "").strip()
    if not raw:
        return DEFAULT_TRACES_SAMPLE_RATE
    try:
        value = float(raw)
    except ValueError:
        value = None
    if value is None or not 0.0 <= value <= 1.0:
        print(
            f"{TRACES_SAMPLE_RATE_ENV} must be a number between 0 and 1; "
            f"using {DEFAULT_TRACES_SAMPLE_RATE}.",
            file=sys.stderr,
        )
        return DEFAULT_TRACES_SAMPLE_RATE
    return value
