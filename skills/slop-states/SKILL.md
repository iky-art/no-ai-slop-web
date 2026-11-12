---
name: slop-states
description: Lengkapi state UI yang sering terlewat (loading, empty, error, success, disabled) pada komponen yang membutuhkannya. Dipicu oleh perintah /slop-states atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-states

**Argumen:** `[komponen atau halaman]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: komponen yang paling sering dipakai)

1. Inspect komponen dan pola state yang sudah ada; reuse, jangan buat sistem baru.
2. Tentukan state yang RELEVAN per komponen saja (daftar data → loading/empty/error; form → disabled/error/success; tombol aksi → loading/disabled). Jangan menambah state yang tidak berguna.
3. Tambahkan juga state "penyimpanan tidak tersedia" bila aplikasi memakai `localStorage` (peringatan jelas + opsi cadangan).
4. Implement: loading dengan indikator yang tidak menggeser layout, empty state yang menjelaskan dan menawarkan langkah berikutnya, error dengan pesan jelas + cara mencoba lagi, success yang tidak hanya mengandalkan warna.
5. Pastikan state bisa diakses: `aria-busy`/`aria-live` seperlunya, tombol disabled tetap jelas, pesan error terkait ke field-nya.
6. Jangan mengarang data atau mensimulasikan error/loading palsu di produksi; untuk demo, beri label.
7. Verifikasi dengan check yang tersedia dan laporkan memakai `references/report-template.md`.
