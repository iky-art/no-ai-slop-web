# Changelog

## 0.3.0
Dukungan banyak agen AI.
- Perubahan struktur: 17 perintah dipindah dari `commands/` ke `skills/<nama>/SKILL.md` (format Agent Skills). Nama perintah tetap sama. Di Claude Code plugin, namanya kini diawali `no-ai-slop-web:`.
- Isi perintah dibuat netral agen: tanpa `$ARGUMENTS`, argumen adalah teks setelah nama perintah.
- Skill inti: tambah `license`, `compatibility`, `metadata.version`, dan bagian "Kompatibilitas agen".
- Baru: adaptor untuk `AGENTS.md`, Cursor (`.mdc`), GitHub Copilot, Windsurf, dan Gemini CLI, dibangun dari skill oleh `scripts/build-adapters.py`.
- Baru: `scripts/install.py` (pasang ke Claude, OpenCode, Cursor, Hermes, Codex, `.agents`, serta berkas aturan; mendukung `--global`, `--dry-run`, dan penggabungan aman).
- Baru: `scripts/validate.py` dan berkas `LICENSE` (MIT).
- Total: 18 skill, 4 referensi.
- Belum diuji di agen aslinya; hanya validator dan installer yang diuji.

## 0.2.0
Berdasarkan pemakaian nyata (membangun aplikasi Lacak dengan plugin ini).
- Baru: referensi `app-patterns.md` (penyimpanan try/catch, konfirmasi tanpa dialog bawaan, cadangan lewat dialog, render aman, tema tiga mode, dock mobile, verifikasi minimum).
- Baru: perintah `/slop-theme` (tema Otomatis/Terang/Gelap berbasis token).
- Checklist slop: 5 butir baru di kategori Fungsi (penyimpanan tanpa try/catch, `alert/confirm/prompt`, `innerHTML` tanpa escape, hapus massal tanpa konfirmasi, ekspor via tautan unduh).
- `/slop-build`, `/slop-states`, `/slop-ship` diperbarui memakai pola aplikasi dan pemeriksaan penyimpanan.
- Total: 17 perintah.

## 0.1.0
- Rilis awal: skill, 3 referensi, 16 perintah, README, planning.
