---
name: slop-copy
description: Tulis ulang copy generik menjadi bahasa Indonesia yang natural, spesifik, dan jujur. Dipicu oleh perintah /slop-copy atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-copy

**Argumen:** `<file/halaman atau teks yang diperbaiki>`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna

1. Baca konteks produk: apa yang dilakukan, untuk siapa, apa aksi utamanya. Jika tidak jelas, tanyakan SATU hal paling penting.
2. Tandai copy klise dan kosong ("revolusi cara kerja Anda", "solusi terbaik", "tingkatkan produktivitas", "cepat, aman, dan andal") serta klaim yang tidak bisa dibuktikan.
3. Tulis ulang: spesifik (sebut apa yang benar-benar bisa dilakukan), bahasa Indonesia sehari-hari yang natural, judul pendek dengan manfaat jelas, CTA berupa kata kerja konkret.
4. Jangan karang angka, testimoni, harga, atau fitur yang belum ada. Bila perlu data, beri placeholder yang JELAS ditandai agar diisi user.
5. Pertahankan nada brand yang sudah ada; sesuaikan panjang teks dengan ruang UI (tombol, judul, deskripsi).
6. Tampilkan perubahan sebagai tabel sebelum → sesudah, lalu terapkan ke file hanya jika diminta atau target berupa file.
