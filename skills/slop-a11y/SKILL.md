---
name: slop-a11y
description: Audit aksesibilitas terfokus (kontras, fokus, label, heading, keyboard) dengan pemisahan jelas antara cek kode dan uji nyata. Dipicu oleh perintah /slop-a11y atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-a11y

**Argumen:** `[halaman atau komponen]`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Target: argumen pengguna (jika kosong: seluruh proyek)

Periksa dan beri status per butir (PASS/FAIL/PARTIAL/NOT RUN):
1. Semantik: elemen native bila cocok, landmark, urutan heading, label form.
2. Keyboard: semua kontrol bisa dijangkau dan dioperasikan, urutan fokus logis, tidak ada jebakan fokus.
3. Fokus: `:focus-visible` terlihat jelas dan tidak tertutup elemen fixed/sticky; tidak ada `outline: none` tanpa pengganti.
4. Nama aksesibel: tombol/tautan ikon-saja, gambar bermakna (alt), dialog dan menu (`aria-expanded`, Escape, dismiss).
5. Kontras teks/latar: gunakan tool bila ada; JANGAN mengarang angka rasio kontras yang tidak diukur.
6. Info tidak hanya lewat warna; hover bukan satu-satunya cara akses; dukung `prefers-reduced-motion`.
7. Pisahkan jelas: "dicek dari kode" vs "diuji di browser/screen reader". Jangan menyatakan kepatuhan WCAG penuh dari checklist saja.
8. Keluarkan daftar perbaikan terurut prioritas dengan lokasi file. Edit kode hanya jika diminta.
