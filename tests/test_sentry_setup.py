"""Sentry stays disabled without SENTRY_DSN and reports no PII when enabled."""

from __future__ import annotations

import importlib
import io
import json
import os
import subprocess
import sys
import tomllib
import unittest
import warnings
from contextlib import redirect_stderr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
STUBS = Path(__file__).resolve().parent / "stubs"
sys.path.insert(0, str(SCRIPTS))

import sentry_setup  # noqa: E402


class SentrySetupTests(unittest.TestCase):
    def setUp(self) -> None:
        self._saved_modules = dict(sys.modules)
        self._env = {
            key: os.environ.get(key)
            for key in (
                "SENTRY_DSN",
                "SENTRY_RELEASE",
                "SENTRY_ENVIRONMENT",
                "SENTRY_TRACES_SAMPLE_RATE",
                "SENTRY_SERVER_NAME",
            )
        }
        for key in self._env:
            os.environ.pop(key, None)

    def tearDown(self) -> None:
        for key, value in self._env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        sys.modules.clear()
        sys.modules.update(self._saved_modules)
        importlib.reload(sentry_setup)

    def test_version_matches_project_manifest(self) -> None:
        project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertEqual(sentry_setup.VERSION, project["project"]["version"])
        self.assertEqual(
            sentry_setup.RELEASE, f"readme-orchestrator@{sentry_setup.VERSION}"
        )
        self.assertIn("sentry-sdk", project["project"]["dependencies"][0])

    def test_unset_dsn_does_not_initialize(self) -> None:
        sys.modules["sentry_sdk"] = _ExplodingSdk()
        self.assertFalse(sentry_setup.init_sentry())

    def test_blank_dsn_does_not_initialize(self) -> None:
        os.environ["SENTRY_DSN"] = "   "
        sys.modules["sentry_sdk"] = _ExplodingSdk()
        self.assertFalse(sentry_setup.init_sentry())

    def test_missing_sdk_warns_and_continues(self) -> None:
        os.environ["SENTRY_DSN"] = "https://public@o0.ingest.sentry.io/1"
        # A None entry makes `import sentry_sdk` raise ModuleNotFoundError.
        sys.modules["sentry_sdk"] = None
        buffer = io.StringIO()
        with redirect_stderr(buffer):
            enabled = sentry_setup.init_sentry()
        self.assertFalse(enabled)
        self.assertIn("sentry-sdk is not installed", buffer.getvalue())

    def test_init_disables_pii_and_uses_conservative_tracing(self) -> None:
        os.environ["SENTRY_DSN"] = "https://public@o0.ingest.sentry.io/1"
        stub = _RecordingSdk()
        sys.modules["sentry_sdk"] = stub
        self.assertTrue(sentry_setup.init_sentry())
        kwargs = stub.kwargs
        self.assertEqual(kwargs["dsn"], os.environ["SENTRY_DSN"])
        self.assertFalse(kwargs["send_default_pii"])
        self.assertFalse(kwargs["include_local_variables"])
        self.assertEqual(kwargs["traces_sample_rate"], 0.0)
        self.assertEqual(kwargs["release"], "readme-orchestrator@2.0.0")
        self.assertEqual(kwargs["server_name"], "readme-orchestrator")
        self.assertNotIn("environment", kwargs)

    def test_release_and_trace_rate_are_configurable(self) -> None:
        os.environ["SENTRY_DSN"] = "https://public@o0.ingest.sentry.io/1"
        os.environ["SENTRY_RELEASE"] = "readme-orchestrator@9.9.9"
        os.environ["SENTRY_TRACES_SAMPLE_RATE"] = "0.05"
        os.environ["SENTRY_SERVER_NAME"] = "ci-runner"
        stub = _RecordingSdk()
        sys.modules["sentry_sdk"] = stub
        self.assertTrue(sentry_setup.init_sentry())
        self.assertEqual(stub.kwargs["release"], "readme-orchestrator@9.9.9")
        self.assertEqual(stub.kwargs["traces_sample_rate"], 0.05)
        self.assertEqual(stub.kwargs["server_name"], "ci-runner")

    def test_invalid_trace_rate_falls_back_without_raising(self) -> None:
        os.environ["SENTRY_DSN"] = "https://public@o0.ingest.sentry.io/1"
        os.environ["SENTRY_TRACES_SAMPLE_RATE"] = "nope"
        stub = _RecordingSdk()
        sys.modules["sentry_sdk"] = stub
        buffer = io.StringIO()
        with redirect_stderr(buffer):
            self.assertTrue(sentry_setup.init_sentry())
        self.assertEqual(stub.kwargs["traces_sample_rate"], 0.0)
        self.assertIn("SENTRY_TRACES_SAMPLE_RATE", buffer.getvalue())


class AuditCliTests(unittest.TestCase):
    def test_audit_without_dsn_matches_previous_success_output(self) -> None:
        env = os.environ.copy()
        env.pop("SENTRY_DSN", None)
        for script in (
            ROOT / "scripts" / "audit_readme.py",
            ROOT / "bundled-skills" / "beautify-github-readme" / "scripts" / "audit_readme.py",
        ):
            with self.subTest(script=script.name, parent=script.parent.parent.name):
                completed = subprocess.run(
                    [sys.executable, str(script), str(ROOT / "README.md")],
                    cwd=ROOT,
                    env=env,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertEqual(completed.stderr, "")
                self.assertIn("Local images checked: 8", completed.stdout)
                self.assertIn(
                    "OK: image references and SVG basics passed", completed.stdout
                )

    def test_audit_usage_error_is_unchanged(self) -> None:
        env = os.environ.copy()
        env.pop("SENTRY_DSN", None)
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "audit_readme.py")],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("usage: audit_readme.py", completed.stderr)

    def test_audit_with_dsn_initializes_sdk_and_still_passes(self) -> None:
        log_path = ROOT / "tests" / ".sentry-stub-log.json"
        env = os.environ.copy()
        env["SENTRY_DSN"] = "https://public@o0.ingest.sentry.io/1"
        env["SENTRY_TRACES_SAMPLE_RATE"] = "0.1"
        env["SENTRY_STUB_LOG"] = str(log_path)
        env["PYTHONPATH"] = str(STUBS) + os.pathsep + str(SCRIPTS) + os.pathsep + env.get(
            "PYTHONPATH", ""
        )
        scripts = (
            ROOT / "scripts" / "audit_readme.py",
            ROOT / "bundled-skills" / "beautify-github-readme" / "scripts" / "audit_readme.py",
        )
        try:
            for script in scripts:
                log_path.unlink(missing_ok=True)
                with self.subTest(script=str(script.relative_to(ROOT))):
                    completed = subprocess.run(
                        [sys.executable, str(script), str(ROOT / "README.md")],
                        cwd=ROOT,
                        env=env,
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    self.assertEqual(completed.returncode, 0, completed.stderr)
                    self.assertIn(
                        "OK: image references and SVG basics passed", completed.stdout
                    )
                    recorded = json.loads(log_path.read_text(encoding="utf-8"))
                    self.assertEqual(recorded["dsn"], env["SENTRY_DSN"])
                    self.assertFalse(recorded["send_default_pii"])
                    self.assertFalse(recorded["include_local_variables"])
                    self.assertEqual(recorded["traces_sample_rate"], 0.1)
                    self.assertEqual(recorded["release"], "readme-orchestrator@2.0.0")
        finally:
            log_path.unlink(missing_ok=True)

    def test_render_entrypoint_calls_monitoring_hook(self) -> None:
        for script in (
            ROOT / "scripts" / "render_motion_gif.py",
            ROOT
            / "bundled-skills"
            / "beautify-github-readme"
            / "scripts"
            / "render_motion_gif.py",
        ):
            source = script.read_text(encoding="utf-8")
            self.assertIn("def _init_error_monitoring()", source)
            self.assertIn("_init_error_monitoring()", source.split("def run(", 1)[1])


class RealSdkTests(unittest.TestCase):
    def test_installed_sdk_accepts_privacy_options(self) -> None:
        sys.modules.pop("sentry_sdk", None)
        os.environ["SENTRY_DSN"] = "https://public@o0.ingest.sentry.io/1"
        os.environ.pop("SENTRY_ENVIRONMENT", None)
        os.environ.pop("SENTRY_RELEASE", None)
        os.environ.pop("SENTRY_TRACES_SAMPLE_RATE", None)
        import sentry_sdk

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="The send_default_pii option is deprecated",
                category=DeprecationWarning,
            )
            self.assertTrue(sentry_setup.init_sentry())
        options = sentry_sdk.get_client().options
        self.assertFalse(options["send_default_pii"])
        self.assertFalse(options["include_local_variables"])
        self.assertFalse(options["data_collection"]["user_info"])
        self.assertFalse(options["data_collection"]["stack_frame_variables"])
        self.assertEqual(options["traces_sample_rate"], 0.0)
        self.assertEqual(options["release"], "readme-orchestrator@2.0.0")
        self.assertEqual(options["environment"], "production")
        self.assertEqual(options["server_name"], "readme-orchestrator")
        sentry_sdk.get_client().close()


class _RecordingSdk:
    def __init__(self) -> None:
        self.kwargs = None

    def init(self, **kwargs):
        self.kwargs = kwargs


class _ExplodingSdk:
    def init(self, **kwargs):
        raise AssertionError(f"Sentry was initialized without a DSN: {kwargs}")


if __name__ == "__main__":
    unittest.main()
