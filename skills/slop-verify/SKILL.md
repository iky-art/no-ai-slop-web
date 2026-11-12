---
name: slop-verify
description: Verifikasi perubahan UI dengan tool yang tersedia dan laporkan PASS/FAIL/BLOCKED/NOT RUN secara jujur. Dipicu oleh perintah /slop-verify atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-verify

**Argumen:** `[area yang diverifikasi]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Area: argumen pengguna (jika kosong: perubahan terakhir)

1. Temukan script dan tooling yang benar-benar ada (package.json, config test, tool browser). Jangan install dependency hanya demi hasil hijau.
2. Pilih check relevan: test terarah, lint, typecheck, build, cek tautan/rute, aksesibilitas, uji browser, uji viewport.
3. Untuk tiap check catat: perintah persis, apakah benar dijalankan, exit status, output kegagalan penting, dan relevansinya dengan perubahan.
4. Bedakan kegagalan baru dari kegagalan yang sudah ada sebelumnya.
5. Periksa manual (dari kode): fokus terlihat, nama aksesibel ikon, reduced-motion, tap highlight, overflow — tandai PARTIAL bila tidak diuji di browser.
6. Keluarkan laporan memakai `references/report-template.md`. Build sukses tidak membuktikan kualitas visual, aksesibilitas, atau kesiapan produksi.
