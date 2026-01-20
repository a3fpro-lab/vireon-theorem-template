#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PROOFPACK" / "MANIFEST.json"

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    if not MANIFEST.exists():
        raise SystemExit(f"Missing {MANIFEST}. Run: python tools/make_manifest.py")

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ok = True

    for e in data["entries"]:
        p = ROOT / e["path"]
        if not p.exists():
            print(f"FAIL missing: {e['path']}")
            ok = False
            continue
        got = sha256_file(p)
        if got != e["sha256"]:
            print(f"FAIL hash: {e['path']}\n  want {e['sha256']}\n  got  {got}")
            ok = False

    if ok:
        print("OK manifest verified")
        return 0
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
