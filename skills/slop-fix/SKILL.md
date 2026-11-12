---
name: slop-fix
description: Perbaiki temuan audit AI-slop secara bertahap dengan perubahan minimal dan verifikasi. Dipicu oleh perintah /slop-fix atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-fix

**Argumen:** `[nomor temuan atau 'top3']`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Fokus: argumen pengguna (jika kosong: top3)

1. Ambil temuan dari hasil `/slop-audit` sebelumnya (jika tidak ada, jalankan audit singkat dulu).
2. Kerjakan HANYA temuan yang dipilih, dengan perubahan koheren terkecil. Jangan refactor tak terkait.
3. Jaga fungsi dan antarmuka publik yang sudah ada.
4. Jalankan check relevan setelah tiap perbaikan; perbaiki regresi; laporkan hasil dengan status PASS/FAIL/BLOCKED/NOT RUN/PARTIAL.
5. Perbarui skor checklist dan tampilkan sebelum vs sesudah.
