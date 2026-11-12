---
name: slop-tokens
description: Kumpulkan nilai hardcode (warna, spasi, radius, bayangan) menjadi token desain yang konsisten. Dipicu oleh perintah /slop-tokens atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-tokens

**Argumen:** `[folder style/komponen]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: seluruh proyek)

1. Baca `DESIGN.md` dan token/tema yang sudah ada (CSS variables, tailwind config, theme file). Ikuti, jangan ganti.
2. Inventarisasi nilai hardcode: warna hex/rgb, ukuran spasi, radius, bayangan, font-size yang berulang atau hampir sama.
3. Kelompokkan menjadi peran (latar, permukaan, teks, aksen, status; skala spasi; skala radius; skala bayangan). Gabungkan nilai yang hampir identik secara sadar dan catat perubahannya.
4. Buat/rapikan token di satu tempat, lalu ganti pemakaian hardcode secara bertahap dengan perubahan minimal. Jaga tampilan tetap sama kecuali penggabungan nilai yang dicatat.
5. Pastikan kontras peran warna tetap memadai; jangan menyebut rasio yang tidak diukur.
6. Jalankan build/lint yang ada setelah perubahan; laporkan memakai `references/report-template.md`.
