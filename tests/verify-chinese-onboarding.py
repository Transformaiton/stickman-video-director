#!/usr/bin/env python3
"""Keep the published sample files byte-for-byte.

The Chinese marketing homepage this file used to lock has been replaced by the
English customer guide. These hashes still stop an accidental media rewrite.
"""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[1]
expected = {
    "skills/directing-stickman-videos/assets/b1/approved-2026-10-23.mp4":
        "111c241a836a0c26b27df2cbff3ba5697b97460dbb873b68dd2f6eda2383b3fc",
    "assets/readme/b1-minimal-handdrawn.mp4":
        "9d2a1789eec25ad3b825631ee3d1ea3cb7417aafb0a5c223ccce08434cedcc3a",
}
for relative, digest in expected.items():
    file = root / relative
    assert hashlib.sha256(file.read_bytes()).hexdigest() == digest, relative
print("Published B1 sample files are unchanged.")
