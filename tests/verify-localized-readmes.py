#!/usr/bin/env python3
"""Check the English Transformaiton.com customer page.

The installed skill still points at the original author's public catalogs.
This script checks the homepage, install guide, and usage guide in this copy.
"""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
readme_names = {
    "README.md",
    "README.en.md",
    "README.zh-CN.md",
    "README.ja.md",
    "README.ko.md",
    "README.fr.md",
    "README.pt-BR.md",
    "README.tr.md",
    "README.id.md",
}
assert {p.name for p in root.glob("README*.md")} == readme_names
source = (root / "README.md").read_text()
assert source == (root / "README.en.md").read_text(), "Default homepage must match English"

required = (
    "# Stickman Video Director by Transformaiton.com",
    "https://transformaiton.com/",
    "info@transformaiton.com",
    "https://github.com/Transformaiton",
    "https://github.com/kaomei/stickman-video-director",
    "Transformaiton.com is not affiliated with or endorsed by the original author.",
    "**Modifications by Transformaiton.com.**",
    "Copyright (c) 2026 Stickman Video Director contributors",
    "docs/INSTALL.md",
    "docs/USAGE.md",
    "GEMINI_API_KEY",
    "npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos",
    '<a id="requirements"></a>',
    '<a id="install"></a>',
    '<a id="quick-start"></a>',
    '<a id="faq"></a>',
    '<a id="troubleshooting"></a>',
    '<a id="contact"></a>',
    '<a id="credits"></a>',
    '<a id="a-styles"></a>',
    '<a id="b-styles"></a>',
)
for phrase in required:
    assert phrase in source, phrase

forbidden = (
    "telegram.me",
    "CrazyKaomei",
    "sjolt.ai",
    "apimart.ai",
    "api.star-history.com",
    "utm_source=crazykaomei",
    "100% Free & Open-Source",
)
for phrase in forbidden:
    assert phrase not in source, phrase
assert not re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", source), "Homepage must be English"

license_text = (root / "LICENSE").read_text()
assert license_text.startswith("MIT License\n")
assert "Copyright (c) 2026 Stickman Video Director contributors" in license_text

for name in sorted(readme_names - {"README.md", "README.en.md"}):
    text = (root / name).read_text()
    assert "# Stickman Video Director by Transformaiton.com" in text, name
    assert "](README.md)" in text, name
    assert "not affiliated with or endorsed" in text, name
    assert "**Modifications by Transformaiton.com.**" in text, name
    assert not re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", text), name

customer_docs = [root / "docs/INSTALL.md", root / "docs/USAGE.md", root / "CHANGELOG.md"]
for path in customer_docs:
    text = path.read_text()
    assert "Transformaiton.com is not affiliated with or endorsed by the original author." in text, path
    assert not re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", text), path
install = (root / "docs/INSTALL.md").read_text()
for phrase in (
    "Node.js 20",
    "FFmpeg",
    "GEMINI_API_KEY",
    "npx skills add Transformaiton/stickman-video-director --skill directing-stickman-videos",
    "Do not commit the key",
):
    assert phrase in install, phrase
usage = (root / "docs/USAGE.md").read_text()
for phrase in ("Code Engine", "Model Engine", 'B1 "Minimal Line Art"', "After I approve"):
    assert phrase in usage, phrase

links = re.findall(r"\]\(([^)]+)\)", source) + re.findall(r'(?:src|href)="([^"]+)"', source)
anchors = set(re.findall(r'<a id="([^"]+)"></a>', source))
for link in links:
    if link.startswith("mailto:") or "://" in link or link.startswith("#"):
        if link.startswith("#"):
            assert link[1:] in anchors, link
        continue
    target, _, fragment = link.partition("#")
    file = root / target
    assert file.is_file(), link
    if fragment and target.endswith(".md"):
        assert fragment in re.findall(r'<a id="([^"]+)"></a>', file.read_text()) or fragment in file.read_text(), link

images = re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', source)
assert images, "Homepage should show real sample images"
for src in images:
    file = root / src
    assert file.is_file(), src
    header = file.read_bytes()[:6]
    assert header in (b"GIF87a", b"GIF89a") or header.startswith(b"\xff\xd8"), src

selected = sys.argv[1:]
if selected:
    assert all(name in readme_names for name in selected), selected
print("English customer homepage, install guide, usage guide, credits, and sample media links passed.")
