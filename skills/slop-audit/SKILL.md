---
name: slop-audit
description: Audit UI yang sudah ada terhadap pola AI-slop dan beri skor + daftar perbaikan berurutan prioritas (read-only). Dipicu oleh perintah /slop-audit atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-audit

**Argumen:** `[path atau URL halaman]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: seluruh proyek)

Mode READ-ONLY, jangan edit file:
1. Telusuri file UI yang relevan saja (bukan node_modules/build).
2. Nilai terhadap `references/slop-checklist.md`; catat setiap temuan dengan lokasi file/komponen.
3. Hitung skor dan beri interpretasinya.
4. Susun daftar perbaikan dari dampak terbesar, tiap item: masalah, lokasi, usulan perbaikan, perkiraan usaha (kecil/sedang/besar).
5. Bedakan temuan dari analisis kode statis vs yang benar-benar diuji di browser. Jangan menyimpulkan perilaku browser dari kode saja.
6. Akhiri dengan 3 perbaikan teratas yang disarankan dikerjakan lebih dulu.
