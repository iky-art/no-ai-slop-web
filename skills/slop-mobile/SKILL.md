---
name: slop-mobile
description: Rapikan pengalaman mobile — tap highlight, dock bawah, safe-area, target sentuh, overflow. Dipicu oleh perintah /slop-mobile atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-mobile

**Argumen:** `[halaman atau komponen]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: seluruh proyek)

1. Inspect stylesheet global dan komponen navigasi/dock yang ada; ikuti konvensi proyek.
2. Tap highlight: setel `-webkit-tap-highlight-color: transparent` di stylesheet global. Catat bahwa ini khusus WebKit; jangan klaim berlaku di semua browser.
3. Pertahankan `:focus-visible` yang jelas (jangan `outline: none` global) dan beri `:active` yang disengaja tanpa layout shift.
4. Dock/bottom bar: tambahkan `padding-bottom: max(0.75rem, env(safe-area-inset-bottom))`, pastikan tidak menutupi konten penting (beri ruang di bawah halaman).
5. Target sentuh nyaman dipakai; ikon-saja wajib punya nama aksesibel.
6. Periksa overflow horizontal, teks terpotong, dan aksi saling menimpa pada 320/375/768 px bila tooling tersedia. Jika tidak, tandai NOT RUN/PARTIAL, jangan menyimpulkan dari kode saja.
7. Menu toggle: `aria-expanded`, tombol Escape, klik di luar, dan tutup setelah navigasi.
8. Laporkan memakai `references/report-template.md`.
