#!/usr/bin/env python3
"""Validasi paket: frontmatter skill, versi, adaptor, installer. Hanya stdlib."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errs, ok = [], 0
ver = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]
for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
    t = p.read_text(encoding="utf-8"); d = p.parent.name
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m: errs.append(f"{d}: frontmatter tidak ada"); continue
    keys = {}
    for line in m.group(1).split("\n"):
        if re.match(r"^[A-Za-z-]+:", line): k, v = line.split(":", 1); keys[k] = v.strip()
    n, desc = keys.get("name", ""), keys.get("description", "")
    for c, msg in [(n == d, "name harus sama dengan nama folder"), (bool(NAME.match(n)) and len(n) <= 64, "name tidak valid"),
                   (1 <= len(desc) <= 1024, f"description {len(desc)} karakter (harus 1-1024)"),
                   (set(keys) <= ALLOWED, f"kunci tak dikenal: {set(keys) - ALLOWED}"),
                   (f'version: "{ver}"' in m.group(1), f"metadata.version tidak sama dengan {ver}")]:
        if not c: errs.append(f"{d}: {msg}")
    # referensi lokal di skill inti harus ada
    if d == "no-ai-slop-web":
        for r in re.findall(r"`references/([a-z-]+\.md)`", t):
            if not (p.parent / "references" / r).exists(): errs.append(f"{d}: references/{r} tidak ada")
    ok += 1
for rel in ["AGENTS.md", "adapters/cursor/no-ai-slop-web.mdc", "adapters/copilot/copilot-instructions.md",
            "adapters/windsurf/no-ai-slop-web.md", "adapters/gemini/GEMINI.md"]:
    f = ROOT / rel
    if not f.exists(): errs.append(f"{rel}: tidak ada"); continue
    t = f.read_text(encoding="utf-8")
    if "<!-- no-ai-slop-web:begin -->" not in t or f"(v{ver})" not in t: errs.append(f"{rel}: marker/versi tidak sesuai")
print(f"skill diperiksa: {ok}, versi paket: {ver}, kesalahan: {len(errs)}")
for e in errs: print(" -", e)
sys.exit(1 if errs else 0)
