---
name: slop-build
description: Bangun halaman/fitur UI dari awal sampai verifikasi, dengan alur inspect → plan → implement → verify → report. Dipicu oleh perintah /slop-build atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-build

**Argumen:** `<halaman atau fitur yang dibangun>`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Permintaan: argumen pengguna

Ikuti alur lengkap skill:
1. Inspect proyek dan jaga perubahan user yang sudah ada.
2. Rencana singkat + acceptance criteria (pakai `DESIGN.md` bila ada).
3. Implement dengan perubahan koheren terkecil, reuse token/komponen yang ada.
4. Semua kontrol harus berfungsi atau ditandai demo. Terapkan state loading/empty/error/disabled yang relevan.
5. Untuk aplikasi/dashboard kecil, ikuti `references/app-patterns.md` (penyimpanan try/catch, konfirmasi dua langkah, cadangan lewat dialog, render aman).
6. Terapkan tap highlight transparan, `:focus-visible`, `:active`, reduced-motion, dan uji target lebar 320/375/768/1024/1440 bila tooling tersedia.
7. Jalankan lint/typecheck/build/test yang ada; baca output asli; perbaiki kegagalan akibat perubahanmu; batasi percobaan perbaikan.
8. Review diff akhir lalu tulis laporan sesuai `references/report-template.md`.
Jangan karang testimoni/statistik/aktivitas live. Minta izin sebelum deploy atau tindakan destruktif.
