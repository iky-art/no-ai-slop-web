---
name: slop-ship
description: Checklist sebelum publish (tautan, meta, favicon, 404, placeholder, build). Tidak pernah deploy tanpa izin. Dipicu oleh perintah /slop-ship atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-ship

**Argumen:** `[target: folder atau URL staging]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: proyek ini)

Mode pemeriksaan, JANGAN deploy atau publish:
1. Placeholder dan konten palsu masih tertinggal? (jalankan logika `/slop-fake` secara ringkas)
2. Tautan dan rute: tombol/anchor mati, rute 404, tautan eksternal yang jelas rusak.
3. Meta dasar: `<title>`, deskripsi, viewport, favicon, bahasa halaman (`lang`), gambar share bila relevan.
4. Halaman 404 dan state error yang ramah.
5. Penyimpanan dan konfirmasi: `localStorage` dibungkus try/catch dengan peringatan saat gagal; aksi destruktif tidak bergantung pada `alert/confirm/prompt`; ekspor/cadangan tidak bergantung pada tautan unduh.
6. Rahasia: tidak ada API key, token, atau kredensial yang tertanam di kode klien; `.env` tidak ikut ter-commit.
7. Build produksi dan lint/typecheck yang tersedia; catat exit status asli.
8. Responsif dan aksesibilitas inti (ringkas): overflow, fokus terlihat, reduced-motion — tandai NOT RUN jika tidak diuji.
9. Keluarkan status PASS/FAIL/BLOCKED/NOT RUN/PARTIAL per butir dan daftar yang wajib dibereskan sebelum rilis. Deploy hanya dilakukan setelah user menyetujui secara eksplisit.
