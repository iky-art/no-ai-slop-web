# no-ai-slop-web

Skill dan plugin untuk membangun, mengaudit, dan memperbaiki UI website agar punya identitas sendiri, bukan tampilan AI generik. Versi 0.3.0 berjalan di banyak agen AI, tidak hanya Claude.

## Isi paket
- **18 skill**: 1 skill inti `no-ai-slop-web` (prinsip, alur kerja, batas aman) dan 17 skill perintah `/slop-*`.
- **4 referensi** di dalam skill inti: checklist slop (28 butir), arah desain, pola aplikasi satu file, template laporan.
- **Adaptor** untuk agen yang memakai berkas aturan: `AGENTS.md`, Cursor, GitHub Copilot, Windsurf, Gemini CLI.
- **Skrip**: `install.py` (pasang ke agen), `validate.py` (cek paket), `build-adapters.py` (bangun ulang adaptor).

## Dukungan agen
Semua skill mengikuti format Agent Skills (`SKILL.md` dengan `name` dan `description`). Status uji di bawah jujur: paket ini **belum dicoba di agen aslinya**; yang sudah diuji hanya skrip validasi dan installer di folder sementara.

| Agen | Cara pasang | Lokasi | Dasar | Uji di agen |
|---|---|---|---|---|
| Claude Code | plugin atau skill | `.claude/skills/` | dokumentasi Claude | NOT RUN |
| OpenCode | skill | `.opencode/skills/`, `.claude/skills/`, atau `.agents/skills/` | dokumentasi OpenCode | NOT RUN |
| Cursor | skill atau aturan `.mdc` | `.cursor/skills/`, `.cursor/rules/` | sumber komunitas | NOT RUN |
| Hermes | skill (agentskills.io) dan `AGENTS.md` | `~/.hermes/skills/` atau `.agents/skills/` | dokumentasi Hermes dan APM | NOT RUN |
| Codex | `AGENTS.md` atau skill | `AGENTS.md`, `.codex/skills/` | sumber komunitas | NOT RUN |
| GitHub Copilot | instruksi repositori | `.github/copilot-instructions.md` | sumber komunitas | NOT RUN |
| Windsurf | rule | `.windsurf/rules/` | sumber komunitas | NOT RUN |
| Gemini CLI | berkas konteks | `GEMINI.md` | sumber komunitas | NOT RUN |
| Agen lain | `npx skills add` (CLI skills.sh, mendeteksi banyak agen) | sesuai agen | dokumentasi skills CLI | NOT RUN, perlu repositori terbit |

Agen lain yang membaca `AGENTS.md` bisa memakai adaptornya. Aider bisa memuat berkas itu dengan `--read`.

## Pasang
Butuh Python 3 (stdlib saja, cocok untuk Termux).
```
python3 scripts/install.py --list
python3 scripts/install.py opencode hermes          # skill ke proyek di folder aktif
python3 scripts/install.py cursor-rules copilot     # berkas aturan
python3 scripts/install.py claude --global          # skill ke folder pengguna
python3 scripts/install.py opencode --dry-run       # lihat rencana tanpa menulis
```
Berkas `AGENTS.md`, `copilot-instructions.md`, dan `GEMINI.md` yang sudah ada tidak ditimpa: blok bertanda `no-ai-slop-web:begin/end` ditambahkan atau diperbarui, isi lamamu tetap.

Claude Code, satu sesi tanpa memasang: `claude --plugin-dir ./no-ai-slop-web`.
Claude Desktop: unggah zip lewat menu Plugins.
Hermes, satu skill dari URL: `hermes skills install <URL SKILL.md mentah>`.

## Perintah
Di agen dengan slash command, ketik `/slop-audit` dan sejenisnya (di Claude Code plugin, namanya diawali `no-ai-slop-web:`). Di agen tanpa slash command, sebut namanya: "jalankan slop-audit pada src/".

| Perintah | Fungsi | Mengubah file? |
|---|---|---|
| `/slop-plan <tugas>` | Rencana, acceptance criteria, arah desain | Tidak |
| `/slop-design <konteks>` | Tulis `DESIGN.md` khusus produk | Hanya DESIGN.md |
| `/slop-build <tugas>` | Bangun halaman/fitur sampai verifikasi + laporan | Ya |
| `/slop-audit [target]` | Audit + skor + prioritas perbaikan | Tidak |
| `/slop-fix [temuan]` | Perbaiki temuan audit bertahap | Ya |
| `/slop-verify [area]` | Verifikasi jujur PASS/FAIL/BLOCKED | Tidak |
| `/slop-hero <produk>` | Evaluasi dan bangun hero bermotion adaptif | Ya |
| `/slop-mobile [target]` | Tap highlight, dock bawah, safe-area, overflow | Ya |
| `/slop-fake [target]` | Pindai konten & fungsi palsu | Tidak |
| `/slop-copy <target>` | Tulis ulang copy generik jadi natural & jujur | Opsional |
| `/slop-states [target]` | Lengkapi loading/empty/error/success/disabled | Ya |
| `/slop-a11y [target]` | Audit aksesibilitas terfokus | Tidak |
| `/slop-tokens [target]` | Rapikan nilai hardcode jadi token | Ya |
| `/slop-redesign <target>` | Ganti konsep visual saat skor tinggi | Ya |
| `/slop-compare [pembanding]` | Skor sebelum vs sesudah | Tidak |
| `/slop-ship [target]` | Checklist sebelum publish (tanpa deploy) | Tidak |
| `/slop-theme [target]` | Tema Otomatis/Terang/Gelap berbasis token | Ya |

## Alur yang disarankan
- Proyek baru: `/slop-plan` → `/slop-design` → `/slop-build` → `/slop-verify`
- Proyek lama: `/slop-audit` → `/slop-fix` → `/slop-compare`
- Sebelum rilis: `/slop-fake` → `/slop-a11y` → `/slop-ship`
- Skor 13 ke atas: `/slop-redesign`

## Validasi paket
```
python3 scripts/validate.py
```
Memeriksa frontmatter 18 skill (nama sama dengan folder, panjang, kunci yang diizinkan), kesamaan versi, dan adaptor.

## Versi
0.3.0. Lihat `CHANGELOG.md`. Lisensi MIT.
