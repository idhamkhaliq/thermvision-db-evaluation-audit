#!/usr/bin/env python3
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "REPOSITORY_SHA256SUMS.txt"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit(f"Missing manifest: {MANIFEST}")
    failures = []
    checked = 0
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        digest, rel = raw.split(None, 1)
        rel = rel.strip()
        path = ROOT / rel
        checked += 1
        if not path.is_file():
            failures.append(f"MISSING {rel}")
            continue
        got = sha256(path)
        if got != digest:
            failures.append(f"HASH_MISMATCH {rel}: expected={digest} got={got}")
    if failures:
        print("Repository integrity check: FAIL")
        for item in failures:
            print(" -", item)
        raise SystemExit(1)
    print(f"Repository integrity check: PASS ({checked} files)")


if __name__ == "__main__":
    main()
