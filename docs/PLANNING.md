# Planning — Plugin no-ai-slop-web

## 1. Tujuan
Plugin yang memaksa hasil UI punya alasan desain per-produk, berfungsi nyata, responsif, aksesibel, dan dilaporkan jujur.

## 2. Masalah yang diselesaikan
- UI hasil AI terlihat seragam (gradien ungu, kartu kaca, 3 kartu fitur).
- Konten palsu (testimoni, statistik, aktivitas live).
- Tombol mati dan state tidak lengkap.
- Klaim "sudah dites" tanpa bukti.

## 3. Pengguna & konteks
Pengembang web berbahasa Indonesia, sering bekerja di mobile (Termux/Acode) → perintah ringan, tidak bergantung tool berat; verifikasi mengakui tool yang tidak ada (BLOCKED, bukan pura-pura PASS).

## 4. Ruang lingkup
**Termasuk (v0.1):** 1 skill, 4 referensi, 17 perintah (inti, hero, mobile, plus fake, copy, states, a11y, tokens, redesign, compare, ship, theme), README, planning.
**Tidak termasuk:** generator template, screenshot otomatis, integrasi deploy, hook otomatis.

## 5. Arsitektur
```
no-ai-slop-web/
├─ .claude-plugin/plugin.json
├─ skills/no-ai-slop-web/
│  ├─ SKILL.md
│  └─ references/ (slop-checklist, design-direction, report-template)
├─ skills/ (1 skill inti + 17 skill perintah /slop-*)
├─ adapters/ (AGENTS.md, Cursor, Copilot, Windsurf, Gemini)
├─ scripts/ (install.py, validate.py, build-adapters.py)
├─ docs/PLANNING.md
└─ README.md
```

## 6. Roadmap
| Fase | Isi | Kriteria selesai |
|---|---|---|
| 0 — Fondasi (selesai) | Manifest, skill, referensi, 17 perintah | Struktur valid, perintah terbaca |
| 1 — Uji coba | Pakai di 2–3 proyek nyata (audit lalu fix) | Skor audit turun, tidak ada regresi, catat perintah yang membingungkan |
| 2 — Penajaman | Revisi checklist dari temuan nyata; perdalam referensi motion/hero adaptif & viewport | Checklist menangkap pola yang benar-benar muncul |
| 3 — Otomasi ringan | Skrip `scripts/` (cek overflow, grep tombol mati, kontras) yang jalan di Node/Python standar | Berjalan di Termux tanpa dependency berat |
| 4 — Rilis | Versi 1.0, changelog, contoh before/after | Dokumentasi + contoh lengkap |

## 7. Risiko
| Risiko | Mitigasi |
|---|---|
| Checklist terlalu subjektif | Skor wajib disertai lokasi file; revisi dari uji nyata |
| Agen menimpa kerja user | Aturan "inspect dulu, jaga perubahan user" di skill |
| Klaim verifikasi palsu | Kosakata status baku + wajib exit status |
| Loop perbaikan tak berujung | Batas percobaan; lapor blocker |
| Terlalu panjang untuk tugas kecil | Rencana proporsional; `/slop-plan` opsional |
| Terlalu banyak perintah, membingungkan | Alur terpandu di README; evaluasi pemakaian di Fase 1 |

## 8. Metrik keberhasilan
- Skor slop turun ≥ 50% setelah `/slop-fix`.
- 0 klaim PASS tanpa eksekusi nyata.
- 0 konten palsu tanpa label demo.
- Tidak ada overflow horizontal di lebar yang diuji.

## 9. Langkah berikutnya
1. Instal plugin dan jalankan `/slop-audit` di satu proyek yang sudah ada.
2. Catat temuan yang terlewat checklist → tambah ke referensi.
3. Coba perintah baru di proyek nyata; hapus atau gabungkan perintah yang jarang dipakai agar daftar tetap ringkas.
4. Pertimbangkan menggabungkan `/slop-fake` ke dalam `/slop-audit` sebagai sub-langkah jika terasa tumpang tindih.

## 10. Status v0.2.0
- Fase 0 selesai. Fase 1 (uji coba) berjalan: 1 proyek nyata (aplikasi Lacak) dibangun dengan plugin ini.
- Hasil: pola baru dirangkum di `references/app-patterns.md`, checklist bertambah 5 butir, perintah `/slop-theme` ditambahkan.
- Belum terbukti: uji klik/viewport/kontras di browser untuk hasil bangunan tersebut (NOT RUN). Perlu diuji di perangkat nyata sebelum dianggap valid.
- Berikutnya: jalankan `/slop-audit` dan `/slop-fake` pada 1–2 proyek lama, catat butir yang terlewat, lalu putuskan apa yang digabung atau dihapus.

## 11. Status v0.3.0
- Selesai: struktur skill lintas agen (18 skill), adaptor, installer, validator, LICENSE.
- Teruji: validator (18 skill, 0 kesalahan) dan installer di folder sementara (semua agen, dry-run, global, penggabungan aman, idempoten).
- Belum terbukti: pemasangan dan pemakaian di Claude Code, OpenCode, Cursor, Hermes, dan agen lain; `npx skills add` (butuh repositori terbit dan jaringan).
- Berikutnya: terbitkan repositori GitHub, uji `npx skills add` dan pemasangan di tiap agen, lalu perbarui kolom "Uji di agen" pada README.
