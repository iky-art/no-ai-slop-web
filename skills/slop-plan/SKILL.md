---
name: slop-plan
description: Buat rencana + acceptance criteria + arah desain sebelum membangun UI (tanpa mengubah kode). Dipicu oleh perintah /slop-plan atau permintaan yang setara.
license: MIT
metadata:
  version: "0.3.0"
---

# /slop-plan

**Argumen:** `<deskripsi halaman/fitur>`

Muat skill `no-ai-slop-web` lebih dulu (referensi ada di `no-ai-slop-web/references/`). Tugas: argumen pengguna

Lakukan HANYA perencanaan, jangan edit file:
1. Inspect proyek (instruksi proyek, stack, token desain, komponen, git status).
2. Isi tabel arah desain dari `references/design-direction.md`.
3. Tulis acceptance criteria yang bisa diuji.
4. Daftar file yang kemungkinan berubah, state yang diperlukan, asumsi, dan risiko.
5. Sebutkan perintah verifikasi yang benar-benar tersedia di proyek.
6. Jika ada kebutuhan yang memblokir, ajukan SATU pertanyaan fokus.
