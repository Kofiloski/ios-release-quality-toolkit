#!/usr/bin/env python3
"""Validate the public shape of the iOS Release Quality Toolkit."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_ROOT = ROOT / "plugins" / "ios-release-quality-toolkit"
PLUGIN_MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
EXPECTED_SKILLS = {
    "app-store-review-risk",
    "ios-ai-ui-check",
    "ios-ui-testability-contract",
}
MINIMUM_NODE24_MAJORS = {
    "actions/checkout": 5,
    "actions/setup-python": 6,
    "actions/upload-artifact": 6,
    "actions/download-artifact": 7,
}
ACTION_REFERENCE = re.compile(
    r"^[ \t]*(?:-[ \t]*)?(?:uses|['\"]uses['\"]):[ \t]*['\"]?"
    r"(?P<action>actions/[a-z0-9_-]+)@(?P<ref>[^'\"\s#]+)",
    re.IGNORECASE | re.MULTILINE,
)
ACTION_MAJOR_REF = re.compile(r"v(?P<major>\d+)(?:\.\d+){0,2}\Z", re.IGNORECASE)
BLOCK_SCALAR_START = re.compile(
    r"^[ ]*(?:-[ ]*)?(?:[A-Za-z0-9_-]+|['\"][^'\"]+['\"]):"
    r"[ ]*[|>][0-9+-]*[ ]*(?:#.*)?$"
)


def fail(message: str) -> None:
    raise ValueError(message)


def read_json(path: Path) -> dict[str, object]:
    if not path.is_file():
        fail(f"missing required JSON file: {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {error}")
    if not isinstance(value, dict):
        fail(f"expected a JSON object in {path.relative_to(ROOT)}")
    return value


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(?P<body>.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if match is None:
        fail(f"missing YAML frontmatter in {path.relative_to(ROOT)}")

    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line or line.startswith((" ", "\t", "#")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def plugin_file(value: object, field: str) -> Path:
    if not isinstance(value, str) or not value:
        fail(f"plugin interface {field} must be a relative file path")
    relative = Path(value)
    if relative.is_absolute():
        fail(f"plugin interface {field} must stay inside the plugin archive")

    plugin_root = PLUGIN_ROOT.resolve()
    candidate = (PLUGIN_ROOT / relative).resolve()
    try:
        candidate.relative_to(plugin_root)
    except ValueError:
        fail(f"plugin interface {field} escapes the plugin archive")
    if not candidate.is_file():
        fail(f"plugin interface {field} does not resolve to a file")
    return candidate


def action_references(text: str):
    block_parent_indent: int | None = None
    for line in text.splitlines():
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))

        if block_parent_indent is not None:
            if not stripped or indent > block_parent_indent:
                continue
            block_parent_indent = None

        if BLOCK_SCALAR_START.match(line):
            block_parent_indent = indent
            continue

        match = ACTION_REFERENCE.match(line)
        if match:
            yield match


def reviewed_node24_major(action: str, ref: str, relative_path: str) -> int:
    minimum = MINIMUM_NODE24_MAJORS.get(action)
    if minimum is None:
        fail(
            f"{relative_path} uses {action} without a reviewed Node 24 minimum"
        )
    version = ACTION_MAJOR_REF.fullmatch(ref)
    if version is None:
        fail(
            f"{relative_path} uses {action}@{ref}; "
            "the ref requires explicit Node 24 review"
        )
    major = int(version.group("major"))
    if major < minimum:
        fail(
            f"{relative_path} uses {action}@{ref}; "
            f"Node 24 requires at least v{minimum}"
        )
    return major


def validate_node24_action_references(action_surfaces: dict[str, str]) -> None:
    checked_references = 0
    for relative_path, text in action_surfaces.items():
        for match in action_references(text):
            action = match.group("action").lower()
            checked_references += 1
            reviewed_node24_major(action, match.group("ref"), relative_path)

    if checked_references == 0:
        fail("no GitHub Action references were checked for Node 24 compatibility")


def validate() -> None:
    marketplace = read_json(MARKETPLACE_PATH)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail("marketplace must advertise exactly one plugin")

    entry = plugins[0]
    if not isinstance(entry, dict) or entry.get("name") != "ios-release-quality-toolkit":
        fail("marketplace plugin name does not match the toolkit")
    source = entry.get("source")
    if not isinstance(source, dict) or source.get("path") != "./plugins/ios-release-quality-toolkit":
        fail("marketplace source does not point at the bundled plugin")

    manifest = read_json(PLUGIN_MANIFEST_PATH)
    if manifest.get("name") != "ios-release-quality-toolkit":
        fail("plugin manifest name does not match the directory")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail("plugin version must be semantic MAJOR.MINOR.PATCH")
    if manifest.get("skills") != "./skills/":
        fail("plugin manifest must expose ./skills/")

    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        fail("plugin manifest is missing interface metadata")
    for field in (
        "displayName",
        "shortDescription",
        "longDescription",
        "privacyPolicyURL",
        "termsOfServiceURL",
    ):
        if not interface.get(field):
            fail(f"plugin interface is missing {field}")
    for field in ("composerIcon", "logo"):
        plugin_file(interface.get(field), field)

    skills_root = PLUGIN_ROOT / "skills"
    actual_skills = {path.name for path in skills_root.iterdir() if path.is_dir()}
    if actual_skills != EXPECTED_SKILLS:
        fail(
            "bundled skill set differs from the advertised set: "
            f"expected {sorted(EXPECTED_SKILLS)}, found {sorted(actual_skills)}"
        )

    for name in sorted(EXPECTED_SKILLS):
        skill_path = skills_root / name / "SKILL.md"
        if not skill_path.is_file():
            fail(f"missing SKILL.md for {name}")
        values = frontmatter(skill_path)
        if values.get("name") != name:
            fail(f"frontmatter name does not match the {name} directory")
        description = values.get("description", "")
        if len(description) < 80:
            fail(f"{name} needs a concrete trigger description")
        if not (skills_root / name / "agents" / "openai.yaml").is_file():
            fail(f"missing agents/openai.yaml for {name}")

    for required in ("README.md", "LICENSE", "CITATION.cff", "llms.txt"):
        if not (ROOT / required).is_file():
            fail(f"missing public repository file: {required}")

    workflow_root = ROOT / ".github" / "workflows"
    action_surfaces = {
        str(path.relative_to(ROOT)): path.read_text(encoding="utf-8")
        for path in workflow_root.rglob("*")
        if path.is_file() and path.suffix in {".yml", ".yaml"}
    }
    validate_node24_action_references(action_surfaces)

    public_paths = [
        ROOT / ".agents",
        ROOT / ".github",
        ROOT / "plugins",
        ROOT / "scripts",
        ROOT / "tests",
        ROOT / ".gitignore",
        ROOT / "CITATION.cff",
        ROOT / "LICENSE",
        ROOT / "README.md",
        ROOT / "llms.txt",
    ]
    paths_to_validate: list[Path] = []
    for public_path in public_paths:
        paths_to_validate.append(public_path)
        if public_path.is_dir():
            paths_to_validate.extend(public_path.rglob("*"))

    for path in paths_to_validate:
        if path.is_symlink():
            fail(f"public bundle must not depend on a symlink: {path.relative_to(ROOT)}")
        if (
            path.is_file()
            and PLUGIN_ROOT in path.parents
            and (path.suffix in {".pyc", ".pyo"} or "__pycache__" in path.parts)
        ):
            fail(f"generated Python bytecode must not ship: {path.relative_to(ROOT)}")


def main() -> int:
    try:
        validate()
    except (OSError, ValueError) as error:
        print(f"toolkit validation failed: {error}", file=sys.stderr)
        return 1
    print("toolkit validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
