---
name: slop-fake
description: Pindai konten dan fungsi palsu (testimoni, statistik, notifikasi live, lorem ipsum, tombol mati) — read-only. Dipicu oleh perintah /slop-fake atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-fake

**Argumen:** `[path atau folder]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: seluruh proyek)

Mode READ-ONLY, jangan edit file. Telusuri file UI saja (bukan node_modules/build):
1. **Konten palsu**: testimoni, rating, jumlah user/pelanggan, statistik, logo klien, notifikasi atau aktivitas "live", nama/foto karangan, lorem ipsum, placeholder tertinggal.
2. **Fungsi palsu**: `href="#"`, `onClick` kosong atau hanya `console.log`/`alert`, form tanpa handler, tombol yang menyimulasikan checkout/scan/deploy/pembayaran tanpa backend nyata, `setTimeout` yang pura-pura loading.
3. Untuk tiap temuan catat: file:baris, kutipan singkat, jenis (konten/fungsi), dan apakah sudah diberi label demo.
4. Beri usulan per temuan: hapus, ganti dengan data nyata dari user, hubungkan ke fungsi sebenarnya, atau beri label "contoh/demo".
5. Jangan menebak: jika tidak yakin sebuah data palsu atau nyata, tandai "perlu konfirmasi".
6. Tutup dengan ringkasan jumlah temuan per jenis.
