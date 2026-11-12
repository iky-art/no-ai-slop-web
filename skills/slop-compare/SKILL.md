---
name: slop-compare
description: Bandingkan skor AI-slop sebelum dan sesudah perubahan beserta daftar yang berubah (read-only). Dipicu oleh perintah /slop-compare atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-compare

**Argumen:** `[commit/branch pembanding atau 'terakhir']`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Pembanding: argumen pengguna (jika kosong: perubahan terakhir)

Mode READ-ONLY:
1. Tentukan kondisi "sebelum" dari hasil `/slop-audit` sebelumnya, atau dari Git (diff/commit/branch pembanding) bila tersedia. Jika tidak ada sumber yang bisa dipercaya, katakan jelas dan nilai hanya kondisi sekarang.
2. Nilai kondisi "sesudah" dengan `references/slop-checklist.md`.
3. Tampilkan tabel per kategori: skor sebelum, sesudah, selisih, dan temuan yang selesai/tersisa/baru.
4. Tandai temuan yang bergantung pada uji browser dan belum diuji sebagai PARTIAL atau NOT RUN.
5. Jangan menyimpulkan perbaikan visual dari diff kode saja; nyatakan batas buktinya.
6. Tutup dengan 3 langkah berikutnya yang paling berdampak.
