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


if __name__ == "__main__":
    unittest.main()
