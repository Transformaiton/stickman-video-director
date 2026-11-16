#!/usr/bin/env python3
"""Check homepage cover examples and the shared finishing-kit skill wiring."""
from pathlib import Path
import re
import struct

root = Path(__file__).resolve().parents[1]
source = (root / "README.md").read_text()
assert source == (root / "README.en.md").read_text()
image_paths = [
    "assets/readme/thumbnails/no-camera.jpg",
    "assets/readme/thumbnails/first-job.jpg",
    "assets/readme/thumbnails/a2-busy-vs-better.jpg",
]
for image_path in image_paths:
    assert image_path in source, image_path
    data = (root / image_path).read_bytes()
    assert data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9"), image_path
    assert len(data) < 2_000_000, image_path
    offset = 2
    dimensions = None
    while offset < len(data):
        assert data[offset] == 0xFF, image_path
        while data[offset] == 0xFF:
            offset += 1
        marker = data[offset]
        offset += 1
        length = struct.unpack(">H", data[offset:offset + 2])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[offset + 3:offset + 7])
            dimensions = (width, height)
            break
        offset += length
    assert dimensions == (1280, 720), (image_path, dimensions)

skill = root / "skills/directing-stickman-videos"
entry = (skill / "SKILL.md").read_text()
guide = (skill / "references/getting-started.md").read_text()
autopilot = (skill / "references/autopilot.md").read_text()
finishing = skill / "references/thumbnail-publishing-kit.md"
assert "(references/thumbnail-publishing-kit.md)" in entry
assert "(thumbnail-publishing-kit.md)" in guide and "(thumbnail-publishing-kit.md)" in autopilot
assert finishing.is_file()
for document in (skill / "SKILL.md", skill / "references/getting-started.md",
                 skill / "references/autopilot.md", finishing):
    for target in re.findall(r"\]\(([^)]+\.md)(?:#[^)]*)?\)", document.read_text()):
        if not target.startswith(("https://", "http://")):
            assert (document.parent / target).is_file(), (document, target)
assert len(re.findall(r"^\d\. \*\*", finishing.read_text(), re.M)) == 5
print("Homepage cover examples and shared optional finishing reference passed.")
