#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "PROOFPACK" / "MANIFEST.json"

EXCLUDE_DIRS = {".git", ".github", "__pycache__", ".venv"}
EXCLUDE_FILES = {"PROOFPACK/MANIFEST.json"}

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def iter_files() -> list[Path]:
    files: list[Path] = []
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel in EXCLUDE_FILES:
            continue
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        files.append(p)
    return sorted(files, key=lambda x: x.relative_to(ROOT).as_posix())

def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    entries = []
    for p in iter_files():
        rel = p.relative_to(ROOT).as_posix()
        entries.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    manifest = {"spec": "vireon-proofpack-manifest-v1", "root": ".", "entries": entries}
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
