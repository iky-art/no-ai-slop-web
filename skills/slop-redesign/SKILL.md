---
name: slop-redesign
description: Ganti konsep visual dan hierarki UI yang terasa generik (skor slop tinggi), bukan sekadar mengganti warna. Dipicu oleh perintah /slop-redesign atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-redesign

**Argumen:** `<halaman/produk yang direncanakan ulang>`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna

Dipakai ketika audit menunjukkan skor 13 ke atas atau user meminta perubahan konsep.
1. Jalankan penilaian cepat berdasarkan `references/slop-checklist.md` untuk mencatat kondisi awal (skor + lokasi).
2. Tentukan akar masalahnya: hierarki, layout, metafora visual, atau konten — bukan hanya palet warna.
3. Buat arah desain baru lewat `references/design-direction.md` dan usulkan 2 opsi konsep singkat beserta alasan produknya. Tunggu pilihan user jika perubahan besar atau berisiko.
4. Setelah disetujui: rancang ulang hierarki dan layout, pertahankan fungsi, rute, data, dan antarmuka publik yang ada. Hormati design system proyek bila sudah mapan.
5. Terapkan bertahap per halaman/section agar mudah di-review dan di-rollback; jangan menimpa perubahan user yang belum di-commit.
6. Verifikasi, hitung ulang skor, dan laporkan sebelum vs sesudah memakai `references/report-template.md`.
