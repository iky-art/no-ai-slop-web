---
name: slop-hero
description: Evaluasi dan bangun hero/intro bermotion yang cocok dengan produk (adaptif, bukan paksaan). Dipicu oleh perintah /slop-hero atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-hero

**Argumen:** `<produk / halaman yang dikerjakan>`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Konteks: argumen pengguna

Evaluasi dulu, jangan langsung menganimasi:
1. Identifikasi kategori produk, audiens, aksi utama, karakter brand, dan pesan yang harus tersampaikan di bagian pembuka.
2. Putuskan apakah hero bermotion benar-benar membantu pemahaman. Jika tidak, katakan jelas dan pertahankan hero statis yang kuat.
3. Jika ya, pilih SATU metafora visual yang berasal dari produk nyata (bukan partikel/gradien generik).
4. Rancang motion: tujuan, durasi, urutan, dan KEADAAN AKHIR yang stabil. Jangan buat splash screen yang menghalangi konten.
5. Wajib: dukung `prefers-reduced-motion` (tampilkan keadaan akhir tanpa animasi), jangan memblokir aksi utama, hindari efek kontinu yang berat dan animasi yang memicu layout shift.
6. Utamakan CSS/platform API; tambah dependency 3D/animasi hanya jika manfaatnya jelas dan biayanya wajar.
7. Verifikasi dengan tool yang ada; jika performa tidak diukur, tulis NOT RUN. Laporkan memakai `references/report-template.md`.
