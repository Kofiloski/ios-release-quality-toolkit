from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check-toolkit.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("check_toolkit", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load toolkit validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ToolkitTests(unittest.TestCase):
    def test_public_toolkit_contract(self) -> None:
        load_validator().validate()

    def test_plugin_assets_cannot_escape_the_archive(self) -> None:
        validator = load_validator()

        for path in ("../../README.md", "/tmp/icon.svg"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    validator.plugin_file(path, "logo")

    def test_tag_push_can_create_a_release_without_personal_auth(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn('tags:\n      - "v*.*.*"', workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("GH_TOKEN: ${{ github.token }}", workflow)
        self.assertIn('gh release create "${RELEASE_TAG}"', workflow)
        self.assertNotIn("secrets.", workflow)

    def test_node20_action_major_is_rejected(self) -> None:
        validator = load_validator()

        for uses_key in ("uses", '"uses"'):
            with self.subTest(uses_key=uses_key):
                with self.assertRaisesRegex(ValueError, "Node 24 requires at least v6"):
                    validator.validate_node24_action_references(
                        {
                            ".github/workflows/ci.yml": (
                                f"- {uses_key}: actions/setup-python@v5\n"
                            )
                        }
                    )

    def test_unknown_official_action_requires_review(self) -> None:
        validator = load_validator()

        with self.assertRaisesRegex(ValueError, "without a reviewed Node 24 minimum"):
            validator.validate_node24_action_references(
                {".github/workflows/ci.yml": "- uses: actions/setup-node@v4\n"}
            )

    def test_sha_pinned_official_action_requires_review(self) -> None:
        validator = load_validator()

        with self.assertRaisesRegex(ValueError, "explicit Node 24 review"):
            validator.validate_node24_action_references(
                {
                    ".github/workflows/ci.yml": (
                        f"- uses: actions/setup-python@{'a' * 40}\n"
                    )
                }
            )

    def test_commented_action_reference_is_ignored(self) -> None:
        validator = load_validator()

        validator.validate_node24_action_references(
            {
                ".github/workflows/ci.yml": (
                    "- uses: actions/setup-python@v6\n"
                    "  # migrated from uses: actions/setup-python@v5\n"
                    "  run: |\n"
                    "    uses: actions/setup-python@v5\n"
                )
            }
        )


if __name__ == "__main__":
    unittest.main()
