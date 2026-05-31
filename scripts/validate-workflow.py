#!/usr/bin/env python3
"""Validate the workflow pack's documentation contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ENTRYPOINTS = [
    "AGENTS.md",
    "CLAUDE.md",
    "opencode.md",
    ".cursor/rules/ai-dev-workflow.mdc",
    ".claude-plugin/plugin.json",
]

TEXT_SURFACES = [
    "README.md",
    "AGENTS.md",
    ".cursor/rules/ai-dev-workflow.mdc",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def local_link_target(link: str) -> str | None:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
        return None
    if link.startswith("#"):
        return None
    target = link.split("#", 1)[0].strip()
    if not target:
        return None
    return target.strip("<>")


def parse_front_matter(skill_file: Path, failures: list[str]) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        fail(f"{skill_file.relative_to(ROOT)} must start with YAML front matter", failures)
        return {}
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        fail(f"{skill_file.relative_to(ROOT)} must close YAML front matter", failures)
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_entrypoints(failures: list[str]) -> None:
    for path in ENTRYPOINTS:
        if not (ROOT / path).is_file():
            fail(f"missing entrypoint: {path}", failures)

    for path in ["CLAUDE.md", "opencode.md", ".cursor/rules/ai-dev-workflow.mdc"]:
        if (ROOT / path).is_file() and "AGENTS.md" not in read(path):
            fail(f"{path} must point agents back to AGENTS.md", failures)


def validate_skill_contract(failures: list[str]) -> list[str]:
    skill_files = sorted(ROOT.glob("skills/*/*/SKILL.md"))
    if not skill_files:
        fail("no skills found under skills/*/*/SKILL.md", failures)
        return []

    names: set[str] = set()
    skill_dirs: list[str] = []

    for skill_file in skill_files:
        skill_dir = skill_file.parent.relative_to(ROOT).as_posix()
        skill_dirs.append(skill_dir)
        expected_name = skill_file.parent.name
        fields = parse_front_matter(skill_file, failures)

        actual_name = fields.get("name")
        if actual_name != expected_name:
            fail(
                f"{skill_file.relative_to(ROOT)} name must be '{expected_name}', got '{actual_name}'",
                failures,
            )
        if actual_name in names:
            fail(f"duplicate skill name: {actual_name}", failures)
        if actual_name:
            names.add(actual_name)

        description = fields.get("description", "")
        if not description:
            fail(f"{skill_file.relative_to(ROOT)} must include a description", failures)
        if len(description) > 180:
            fail(f"{skill_file.relative_to(ROOT)} description should stay concise", failures)

    return skill_dirs


def validate_plugin_metadata(skill_dirs: list[str], failures: list[str]) -> None:
    plugin_path = ROOT / ".claude-plugin/plugin.json"
    if not plugin_path.is_file():
        return

    try:
        plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f".claude-plugin/plugin.json is invalid JSON: {error}", failures)
        return

    listed = plugin.get("skills")
    if not isinstance(listed, list):
        fail(".claude-plugin/plugin.json must contain a skills list", failures)
        return

    expected = [f"./{skill_dir}" for skill_dir in skill_dirs]
    if sorted(listed) != sorted(expected):
        fail(
            ".claude-plugin/plugin.json skills must match skills/*/*/SKILL.md directories",
            failures,
        )

    for path in listed:
        if not isinstance(path, str):
            fail(".claude-plugin/plugin.json skills entries must be strings", failures)
            continue
        skill_file = ROOT / path / "SKILL.md"
        if not skill_file.is_file():
            fail(f"plugin skill path does not contain SKILL.md: {path}", failures)


def validate_skill_mentions(skill_dirs: list[str], failures: list[str]) -> None:
    for surface in TEXT_SURFACES:
        if not (ROOT / surface).is_file():
            continue
        text = read(surface)
        for skill_dir in skill_dirs:
            mention = f"{skill_dir}/SKILL.md"
            if mention not in text:
                fail(f"{surface} must mention {mention}", failures)


def validate_markdown_links(failures: list[str]) -> None:
    markdown_files = sorted(
        path
        for pattern in ("**/*.md", "**/*.mdc")
        for path in ROOT.glob(pattern)
        if ".git" not in path.parts
    )

    for path in markdown_files:
        file_name = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = local_link_target(match.group(1))
            if target is None:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                fail(f"{file_name} has broken local link: {match.group(1)}", failures)


def main() -> int:
    failures: list[str] = []

    validate_entrypoints(failures)
    skill_dirs = validate_skill_contract(failures)
    validate_plugin_metadata(skill_dirs, failures)
    validate_skill_mentions(skill_dirs, failures)
    validate_markdown_links(failures)

    if failures:
        for message in failures:
            print(f"FAIL: {message}", file=sys.stderr)
        return 1

    print("Workflow validation passed.")
    print(f"Validated {len(skill_dirs)} skills and {len(ENTRYPOINTS)} entrypoints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
