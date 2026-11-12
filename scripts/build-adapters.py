#!/usr/bin/env python3
"""Bangun ulang adaptor lintas-agen dari skills/*/SKILL.md. Hanya stdlib."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!-- no-ai-slop-web:begin -->", "<!-- no-ai-slop-web:end -->"

def meta(p):
    t = p.read_text(encoding="utf-8")
    fm = re.match(r"---\n(.*?)\n---", t, re.S).group(1)
    g = lambda k: re.search(rf"^{k}:\s*(.*)$", fm, re.M).group(1).strip()
    return g("name"), g("description")

def version():
    import json
    return json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]

def block():
    rows = []
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        n, d = meta(p)
        if n == "no-ai-slop-web":
            continue
        d = d.split(". Dipicu oleh")[0]
        rows.append(f"| `/{n}` | {d} |")
    return f"""{BEGIN}
# no-ai-slop-web (v{version()})

Aturan untuk membangun, mengaudit, dan memperbaiki UI website agar punya identitas sendiri, bukan templat AI generik.

## Prinsip
1. Kecocokan produk di atas tren.
2. Fungsi nyata di atas dekorasi palsu: jangan karang testimoni, statistik, notifikasi, atau tombol mati.
3. Ikuti konvensi proyek yang ada; jangan menulis ulang tanpa alasan.
4. Bukti di atas klaim: jalankan lint, typecheck, build, dan test yang memang ada, lalu baca output aslinya.
5. Aksesibilitas adalah baseline: fokus terlihat, kontras, nama aksesibel, dukung reduced motion.
6. Responsif: tidak ada overflow horizontal di lebar 320, 375, 768, 1024, dan 1440 px.
7. Jujur soal tool yang tidak tersedia.

## Alur kerja
inspect, plan, implement, verify, report.

## Status bukti
PASS, FAIL, BLOCKED, NOT RUN, atau PARTIAL. Jangan pernah menandai BLOCKED atau NOT RUN sebagai PASS.

## Batas aman
Minta izin sebelum: menghapus data atau file besar, menulis ulang history Git, mengubah secret/auth/produksi, deploy atau publish, dan memakai layanan berbayar.

## Perintah
Jika agen mendukung skill, pakai skill dengan nama yang sama. Jika tidak, panggil lewat nama, misalnya "jalankan slop-audit pada src/".

| Perintah | Fungsi |
|---|---|
{chr(10).join(rows)}

Skill lengkap dan checklist ada di `skills/no-ai-slop-web/` bila tersedia.
{END}
"""

def write(rel, text):
    p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8")

b = block()
write("AGENTS.md", b)
write("adapters/copilot/copilot-instructions.md", b)
write("adapters/gemini/GEMINI.md", b)
write("adapters/cursor/no-ai-slop-web.mdc", "---\ndescription: Aturan membangun dan mengaudit UI website agar tidak terasa buatan AI (no-ai-slop-web)\nalwaysApply: false\n---\n\n" + b)
write("adapters/windsurf/no-ai-slop-web.md", "---\ntrigger: model_decision\ndescription: Aturan membangun dan mengaudit UI website agar tidak terasa buatan AI (no-ai-slop-web)\n---\n\n" + b)
print("adaptor dibangun dari", len(list((ROOT / 'skills').glob('*/SKILL.md'))), "skill")
