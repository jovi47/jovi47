#!/usr/bin/env python3
"""Build self-contained README SVGs from the existing static technology list."""

import argparse
import copy
import hashlib
import html
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
OUTPUTS = {"images/technologies.svg": "#1f2328", "images/technologies-dark.svg": "#f0f6fc"}


def technology_list():
    readme = (ROOT / "README.md").read_text()
    static = readme.split("<summary>All technologies (static list)</summary>", 1)[1].split("</details>", 1)[0]
    items = re.findall(r'<img src="images/([a-z0-9-]+\.svg)"[^>]*></picture>&nbsp;(.*?)&nbsp;&nbsp;', static)
    items = [(file, html.unescape(label).replace("\xa0", " ")) for file, label in items]
    assert len(items) == 27 and len({label for _, label in items}) == 27
    return items


def icon_symbol(file):
    source = ET.parse(ROOT / "images" / file).getroot()
    icon = copy.deepcopy(source)
    prefix = "icon-" + Path(file).stem
    ids = {node.get("id"): prefix + "-" + node.get("id") for node in icon.iter() if node.get("id")}
    for node in icon.iter():
        for key, value in list(node.attrib.items()):
            if key == "id":
                node.set(key, ids[value])
            else:
                for old, new in ids.items():
                    value = value.replace("url(#" + old + ")", "url(#" + new + ")")
                    if key.endswith("href") and value == "#" + old:
                        value = "#" + new
                node.set(key, value)
    icon.tag = "{" + SVG + "}symbol"
    for key in ["width", "height", "role", "aria-label"]:
        icon.attrib.pop(key, None)
    icon.set("id", prefix)
    # Paths and paint values stay as supplied; only local reference IDs change.
    assert [n.get("d") for n in source.iter() if n.tag.endswith("}path")] == [n.get("d") for n in icon.iter() if n.tag.endswith("}path")]
    return ET.tostring(icon, encoding="unicode").replace(' xmlns="' + SVG + '"', "")


def build(items, color):
    labels = ", ".join(label for _, label in items)
    symbols = "\n".join(icon_symbol(file) for file in dict.fromkeys(file for file, _ in items))
    rows, lengths = [], []
    for index, row in enumerate((items[:14], items[14:]), start=1):
        x, content = 0, []
        for file, label in row:
            content.append(f'<g transform="translate({x} 0)"><use href="#icon-{Path(file).stem}" width="29" height="29"/><text x="39" y="20">{html.escape(label)}</text></g>')
            x += 39 + max(24, len(label) * 8) + 28
        lengths.append(x)
        rows.append(f'<g id="row-{index}">' + "".join(content) + "</g>")
    belts = "\n".join(f'<g transform="translate(12 {y})"><g class="belt-{index}"><use href="#row-{index}"/><use href="#row-{index}" x="{length}"/></g></g>' for index, (length, y) in enumerate(zip(lengths, (16, 64)), start=1))
    result = f'''<svg xmlns="{SVG}" width="840" height="108" role="img" aria-labelledby="title description">
<title id="title">{html.escape(labels)}</title>
<desc id="description">Two gently scrolling rows of technology icons and names. Motion stops when reduced motion is preferred. The README also provides every technology in a static list. Artwork and licenses: images/LICENSE.txt and images/TECHNOLOGY-LICENSES.txt.</desc>
<style>
text{{fill:{color};font:550 15px Arial,Helvetica,sans-serif}}
.belt-1{{animation:travel-1 56s linear infinite}}.belt-2{{animation:travel-2 62s linear infinite reverse}}
@keyframes travel-1{{to{{transform:translateX(-{lengths[0]}px)}}}}@keyframes travel-2{{to{{transform:translateX(-{lengths[1]}px)}}}}
@media(prefers-reduced-motion:reduce){{.belt-1,.belt-2{{animation:none}}}}
</style>
<defs>
{symbols}
{chr(10).join(rows)}
<linearGradient id="fade"><stop stop-color="white" stop-opacity="0"/><stop offset=".025" stop-color="white"/><stop offset=".975" stop-color="white"/><stop offset="1" stop-color="white" stop-opacity="0"/></linearGradient>
<mask id="edges" maskUnits="userSpaceOnUse" x="0" y="0" width="100%" height="100%"><rect width="100%" height="100%" fill="url(#fade)"/></mask>
</defs>
<g mask="url(#edges)">{belts}</g>
</svg>
'''
    root = ET.fromstring(result)
    ids = [node.get("id") for node in root.iter() if node.get("id")]
    assert len(ids) == len(set(ids)), "Duplicate SVG IDs"
    assert [node.text for node in root.iter() if node.tag == "{" + SVG + "}text"] == [label for _, label in items]
    for node in root.iter():
        assert node.tag.rsplit("}", 1)[-1] not in {"script", "foreignObject", "image"}
        for key, value in node.attrib.items():
            assert not key.lower().startswith("on"), "SVG event handler"
            if key.endswith("href"):
                assert value.startswith("#") and value[1:] in ids, "External or unresolved SVG reference"
            for reference in re.findall(r"url\(#([^)]*)\)", value):
                assert reference in ids, "Unresolved SVG paint reference"
    return result.encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated SVGs and manifest without writing")
    args = parser.parse_args()
    items = technology_list()
    manifest_path = ROOT / "docs/readme-assets.json"
    manifest = json.loads(manifest_path.read_text())
    previous = copy.deepcopy(manifest)
    manifest["technology_marquee"] = {
        "source": "README.md static technology list and existing images/*.svg; portfolio src/skills.mjs and public/technology-marquee.css are the layout reference.",
        "outputs": list(OUTPUTS),
        "viewport": "840x108 CSS pixels, no root viewBox; constrained image width clips the moving rows instead of shrinking labels.",
        "motion": "Two seamless repeated rows, 56s left / 62s right; CSS prefers-reduced-motion disables both animations.",
        "accessibility": "All 27 names in image alt and SVG title; the native static icon/name list remains available in README details.",
        "generation": "python3 scripts/build-technology-marquee.py; --check verifies deterministic outputs, embedded paths, names, IDs and local-only references.",
        "source_artwork": "Original path geometry and paint retained, with collision-safe local IDs; source files and license notices unchanged.",
    }
    manifest["assets"] = [asset for asset in manifest["assets"] if asset["file"] not in OUTPUTS]
    for file, color in OUTPUTS.items():
        data = build(items, color)
        if args.check:
            assert (ROOT / file).read_bytes() == data, f"Regenerate {file}"
        else:
            (ROOT / file).write_bytes(data)
        manifest["assets"].append({
            "file": file,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "source": "Self-contained composition of the 26 existing technology SVGs, reused for 27 labels; no external image/font requests.",
            "license": "Original notices retained in images/LICENSE.txt and images/TECHNOLOGY-LICENSES.txt; brand rights retained.",
        })
        print(f"{file}: {len(data):,} bytes; 27 labels, 26 embedded icons, local references only")
    if args.check:
        assert manifest == previous, "Regenerate docs/readme-assets.json"
    else:
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
