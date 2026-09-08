#!/usr/bin/env python3
"""Read-only SHA-256 rows and verification for a Review Package's local members.

hash --root PROJECT FILE... prints a marked Markdown table.
verify --root PROJECT MANIFEST checks that table, not analytical correctness.
Paths are relative to --root (default: cwd), or absolute; labels may be localized.
Legacy manifests without markers must use an equivalent identity check.
"""

import argparse
import hashlib
import re
import sys
from pathlib import Path

START = "<!-- evidencecraft:local-members -->"
END = "<!-- /evidencecraft:local-members -->"


def digest(path):
    before = path.stat()
    if not path.is_file():
        raise ValueError(f"Not a regular file: {path}")
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(chunk)
    after = path.stat()
    if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns,
            before.st_ctime_ns) != (after.st_dev, after.st_ino, after.st_size,
                                   after.st_mtime_ns, after.st_ctime_ns):
        raise ValueError(f"File changed during hashing: {path}")
    return checksum.hexdigest()


def resolve(root, value):
    if not value or any(c in value for c in "|`\r\n"):
        raise ValueError(f"Unsupported Markdown path: {value!r}")
    return (root / value).resolve()


def members(manifest):
    content = manifest.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError("Expected exactly one local-members marker pair")
    start, end = content.index(START), content.index(END)
    if end <= start:
        raise ValueError("Reversed local-members markers")
    lines = [line.strip() for line in content[start + len(START):end].splitlines()
             if line.strip()]
    if len(lines) < 3:
        raise ValueError("Local-members table is empty or incomplete")
    rows = []
    for line in lines:
        if not line.startswith("|") or not line.endswith("|"):
            raise ValueError(f"Expected a table row: {line}")
        cells = [cell.strip() for cell in line[1:-1].split("|")]
        if len(cells) != 3:
            raise ValueError("Local-members table needs role, path, SHA-256 columns")
        rows.append(cells)
    if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1]):
        raise ValueError("Invalid table separator")
    for role, path, identity in rows[2:]:
        path, identity = path.strip("`"), identity.strip("`")
        if not role or not re.fullmatch(r"[0-9a-fA-F]{64}", identity):
            raise ValueError(f"Missing role or invalid SHA-256 for {path}")
        yield path, identity.lower()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("hash", "verify"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument("--root", type=Path, default=Path.cwd())
        command_parser.add_argument("paths", nargs="+" if command == "hash" else 1)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        if not root.is_dir():
            raise ValueError(f"Root is not a directory: {root}")
        seen = set()
        if args.command == "hash":
            rows = []
            for value in args.paths:
                path = resolve(root, value)
                if path in seen:
                    raise ValueError(f"Duplicate member: {value}")
                seen.add(path)
                rows.append(f"| file | `{value}` | `{digest(path)}` |")
            print("\n".join([START, "| Role | Exact path | SHA-256 |",
                             "|---|---|---|", *rows, END]))
        else:
            manifest = resolve(root, args.paths[0])
            failures = []
            for value, expected in members(manifest):
                path = resolve(root, value)
                if path == manifest or path in seen:
                    raise ValueError(f"Self-reference or duplicate member: {value}")
                seen.add(path)
                try:
                    if digest(path) != expected:
                        failures.append(f"Identity mismatch: {value}")
                except (OSError, ValueError) as exc:
                    failures.append(f"{value}: {exc}")
            if failures:
                raise ValueError("\n".join(failures))
            print(f"Verified {len(seen)} local member identities. "
                  "Coverage, source freshness, and analytical correctness require review.")
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
