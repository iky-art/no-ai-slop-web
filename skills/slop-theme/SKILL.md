---
name: slop-theme
description: Tambah tema Otomatis/Terang/Gelap berbasis token dengan pilihan yang tersimpan. Dipicu oleh perintah /slop-theme atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-theme

**Argumen:** `[halaman atau aplikasi]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: seluruh proyek)

1. Inspect token warna dan tema yang sudah ada (`DESIGN.md`, CSS variables, config). Ikuti, jangan ganti identitas visual.
2. Pastikan warna berupa token berperan (latar, permukaan, teks, teks redup, garis, aksen, status). Pindahkan nilai hardcode ke token bila perlu.
3. Definisikan nilai terang sebagai default `:root`, nilai gelap di `@media (prefers-color-scheme: dark)` untuk `:root:not([data-theme="light"])`, dan `:root[data-theme="dark"]`. Atur `color-scheme` untuk tiap mode dan beri `body` latar eksplisit.
4. Tombol tema bergilir Otomatis → Terang → Gelap, label teksnya jelas (bukan ikon saja), target sentuh nyaman, fokus terlihat.
5. Simpan pilihan di penyimpanan lokal dengan try/catch; bila gagal, tetap berfungsi untuk sesi berjalan. Default mengikuti sistem.
6. Periksa kontras kedua mode dengan tool bila ada; jangan menyebut rasio yang tidak diukur. Tandai NOT RUN bila tidak diuji.
7. Laporkan memakai `references/report-template.md`.
