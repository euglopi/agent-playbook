#!/usr/bin/env python3
"""Check the declared public collection without loading or running its skills."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(root):
    errors = []
    manifest = json.loads((root / "collection.json").read_text())
    declared = set(manifest["files"]) | {"collection.json"}
    actual = {
        str(p.relative_to(root))
        for p in root.rglob("*")
        if (p.is_file() or p.is_symlink()) and ".git" not in p.relative_to(root).parts
    }
    for path in sorted(actual - declared):
        errors.append(f"Undeclared file: {path}")
    for path in sorted(declared - actual):
        errors.append(f"Missing file: {path}")

    skills = {entry["path"] for entry in manifest["skills"]}
    discovered = {path for path in actual if path.endswith("/SKILL.md")}
    if skills != discovered:
        errors.append("Skill entries do not match the published skill folders")
    guides = {entry["path"] for entry in manifest["guides"]}
    if guides != {path for path in actual if path.startswith("guides/") and path.endswith(".md")}:
        errors.append("Guide entries do not match the published guide files")
    catalog = (root / "CATALOG.md").read_text()
    for target in skills | guides | {entry["url"] for entry in manifest["external_skills"]}:
        if f"]({target})" not in catalog:
            errors.append(f"Missing catalog link: {target}")

    for entry in manifest["skills"]:
        path = root / entry["path"]
        if not path.exists():
            continue
        text = path.read_text()
        frontmatter = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", text, re.S)
        if not frontmatter:
            errors.append(f"Missing skill metadata: {entry['path']}")
            continue
        for field in ("name", "description"):
            if not re.search(rf"^{field}:\s*\S", frontmatter[1], re.M):
                errors.append(f"Missing {field}: {entry['path']}")
        name = re.search(r"^name:\s*([^\n]+)", frontmatter[1], re.M)
        if name and name[1].strip("\"' ") != entry["name"]:
            errors.append(f"Skill name differs from catalog: {entry['path']}")
        if not (root / entry["license_file"]).is_file():
            errors.append(f"Missing license: {entry['path']}")

    for entry in manifest["external_skills"]:
        if urlsplit(entry["url"]).scheme != "https" or not entry.get("publisher"):
            errors.append(f"Missing public source or publisher: {entry['name']}")

    # These checks catch common mistakes; manual privacy and rights review is still needed.
    sensitive_patterns = {
        "literal home directory": r"/(?:Users|home)/[A-Za-z0-9_.-]+/",
        "private temporary directory": r"/private/tmp/[A-Za-z0-9_.-]+",
        "GitHub credential": r"\bgh[pousr]_[A-Za-z0-9]{20,}",
        "GitHub fine-grained credential": r"\bgithub_pat_[A-Za-z0-9_]{20,}",
        "service credential": r"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}",
        "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    }
    for relative in sorted(actual):
        path = root / relative
        if path.is_symlink():
            errors.append(f"Symlinks are not publication inputs: {relative}")
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            errors.append(f"Unreviewed binary file: {relative}")
            continue
        for label, pattern in sensitive_patterns.items():
            if re.search(pattern, text):
                errors.append(f"Possible {label}: {relative}")
        if path.suffix != ".md":
            continue
        # Examples inside fences and inline code are not actual Markdown links.
        prose = re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text, flags=re.M | re.S)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", prose):
            target = target.strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            dest = (path.parent / unquote(parts.path)).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():
                errors.append(f"Broken local link in {relative}: {target}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    problems = check(args.root)
    if problems:
        print("\n".join(problems))
        raise SystemExit(1)
    print("Collection inventory, licenses, local links and basic privacy checks passed.")
