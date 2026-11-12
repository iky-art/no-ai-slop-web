---
name: slop-design
description: Tentukan arah desain khusus produk (tipografi, warna, permukaan, motion) dan tulis ke DESIGN.md. Dipicu oleh perintah /slop-design atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-design

**Argumen:** `<nama produk / audiens / kesan yang diinginkan>`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Konteks: argumen pengguna

1. Baca aset, brand, dan design system yang sudah ada. Jangan menggantinya tanpa alasan.
2. Isi seluruh tabel di `references/design-direction.md` dengan keputusan konkret (bukan "modern & clean").
3. Tulis hasilnya ke `DESIGN.md` di root proyek: peran warna + kontras, skala tipografi, spasi, radius/bayangan, ikon, state interaksi, aturan motion + reduced-motion.
4. Tutup dengan "uji akhir": apakah desain ini masih khas produk jika logo diganti? Jelaskan jawabannya jujur.
Jangan ubah kode UI pada perintah ini.
