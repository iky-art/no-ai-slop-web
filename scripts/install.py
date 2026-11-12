#!/usr/bin/env python3
"""Pasang no-ai-slop-web ke agen AI. Hanya stdlib, aman dipakai di Termux.

Contoh:
  python3 scripts/install.py --list
  python3 scripts/install.py opencode hermes            # ke proyek di folder aktif
  python3 scripts/install.py cursor-rules copilot       # berkas aturan
  python3 scripts/install.py claude --global --dry-run
"""
import argparse, shutil, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!-- no-ai-slop-web:begin -->", "<!-- no-ai-slop-web:end -->"
SKILLS = {  # agen: (folder proyek, folder global)
    "claude": (".claude/skills", "~/.claude/skills"),
    "opencode": (".opencode/skills", "~/.config/opencode/skills"),
    "cursor": (".cursor/skills", "~/.cursor/skills"),
    "hermes": (".agents/skills", "~/.hermes/skills"),
    "codex": (".codex/skills", "~/.codex/skills"),
    "agents": (".agents/skills", "~/.agents/skills"),
}
RULES = {  # agen: (sumber, tujuan di proyek, mode)
    "cursor-rules": ("adapters/cursor/no-ai-slop-web.mdc", ".cursor/rules/no-ai-slop-web.mdc", "file"),
    "windsurf": ("adapters/windsurf/no-ai-slop-web.md", ".windsurf/rules/no-ai-slop-web.md", "file"),
    "copilot": ("adapters/copilot/copilot-instructions.md", ".github/copilot-instructions.md", "block"),
    "gemini": ("adapters/gemini/GEMINI.md", "GEMINI.md", "block"),
    "agentsmd": ("AGENTS.md", "AGENTS.md", "block"),
}

def say(dry, msg): print(("[dry-run] " if dry else "") + msg)

def install_skills(agent, target, glob, dry):
    proj, glob_dir = SKILLS[agent]
    dest = Path(glob_dir).expanduser() if glob else target / proj
    names = sorted(p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists())
    for n in names:
        say(dry, f"{agent}: salin skill {n} -> {dest / n}")
        if not dry:
            shutil.copytree(ROOT / "skills" / n, dest / n, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("__pycache__"))
    return len(names)

def install_rule(agent, target, dry):
    src, dst, mode = RULES[agent]
    text = (ROOT / src).read_text(encoding="utf-8")
    out = target / dst
    if mode == "file" or not out.exists():
        say(dry, f"{agent}: tulis {out}")
        if not dry:
            out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text, encoding="utf-8")
        return
    cur = out.read_text(encoding="utf-8")
    blk = text[text.index(BEGIN): text.index(END) + len(END)]
    if BEGIN in cur and END in cur:
        new = cur[: cur.index(BEGIN)] + blk + cur[cur.index(END) + len(END):]
        say(dry, f"{agent}: perbarui blok di {out}")
    else:
        new = cur.rstrip("\n") + "\n\n" + blk + "\n"
        say(dry, f"{agent}: tambahkan blok ke {out} (isi lama dipertahankan)")
    if not dry: out.write_text(new, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("agents", nargs="*", help="nama agen, lihat --list")
    ap.add_argument("--global", dest="glob", action="store_true", help="pasang ke folder pengguna (hanya jenis skill)")
    ap.add_argument("--target", default=".", help="folder proyek tujuan (default: folder aktif)")
    ap.add_argument("--dry-run", action="store_true", help="tampilkan rencana tanpa menulis")
    ap.add_argument("--list", action="store_true", help="daftar agen yang didukung")
    a = ap.parse_args()
    if a.list or not a.agents:
        print("Jenis skill (SKILL.md):", ", ".join(SKILLS))
        print("Jenis aturan (berkas):", ", ".join(RULES))
        return 0 if a.list else 2
    bad = [x for x in a.agents if x not in SKILLS and x not in RULES]
    if bad:
        print("Agen tidak dikenal:", ", ".join(bad), "(lihat --list)", file=sys.stderr); return 2
    target = Path(a.target).resolve()
    for ag in a.agents:
        if ag in SKILLS:
            n = install_skills(ag, target, a.glob, a.dry_run); say(a.dry_run, f"{ag}: {n} skill diproses")
        else:
            if a.glob:
                print(f"{ag}: --global tidak berlaku untuk berkas aturan, dilewati", file=sys.stderr); continue
            install_rule(ag, target, a.dry_run)
    return 0

if __name__ == "__main__":
    sys.exit(main())
    
