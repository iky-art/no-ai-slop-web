---
name: no-ai-slop-web
description: Bangun, audit, atau perbaiki UI website supaya punya identitas visual sendiri, bukan template AI generik. Gunakan saat user minta membuat/mendesain/merapikan website, landing page, dashboard, atau menyebut "no ai slop", "terlihat generik", "kayak buatan AI", audit tampilan, atau polish UI. Mencakup arah desain per-produk, responsif, aksesibilitas, tap highlight, motion adaptif, dan laporan berbasis bukti.
license: MIT
compatibility: Agen apa pun yang mendukung Agent Skills (SKILL.md) atau AGENTS.md. Verifikasi browser memerlukan tool browser atau Playwright, bila ada.
metadata:
  version: "0.3.0"
---

# No AI Slop Web

## Misi
Hasilkan antarmuka yang terasa dirancang khusus untuk produk dan audiensnya, bukan template. Fungsional, responsif, aksesibel, dan dilaporkan jujur.

## Prinsip
1. Kecocokan produk di atas tren.
2. Fungsi nyata di atas dekorasi palsu.
3. Ikuti konvensi proyek yang sudah ada; jangan rewrite tanpa alasan.
4. Bukti terukur di atas klaim percaya diri.
5. Motion adaptif, bukan paksaan. Selalu hormati `prefers-reduced-motion`.
6. Aksesibilitas adalah baseline, bukan bonus.
7. Minim dependency dan minim scope.
8. Jujur soal ketidakpastian dan tool yang tidak tersedia.

## Alur kerja
1. **Inspect** — baca CLAUDE.md/AGENTS.md/README, kenali stack, token desain, komponen, `git status`. Jangan timpa perubahan user.
2. **Plan** — rencana singkat + acceptance criteria yang bisa diuji (bukan "buat premium").
3. **Arah desain** — tentukan hierarki, tipografi, warna (peran + kontras), spasi, permukaan, ikon, feedback interaksi. Lihat `references/design-direction.md`.
4. **Implement** — perubahan koheren terkecil. Setiap kontrol harus berfungsi atau jelas ditandai demo.
5. **Verify** — jalankan lint/typecheck/build/test yang memang ada. Baca output asli.
6. **Report** — pakai format laporan di `references/report-template.md`.

## Pola AI-slop yang dihindari (kecuali ada alasan khusus produk)
Gradien ungu-biru default, kartu kaca blur di mana-mana, glow neon, kartu super bulat seragam, emoji sebagai ikon, layout sidebar + grid kartu tanpa alasan, section filler ("Fitur Unggulan" 3 kartu identik), testimoni/statistik/rating palsu, copy generik ("Revolusi cara kerja Anda"). Daftar lengkap: `references/slop-checklist.md`.

## Aturan data & kejujuran
Jangan karang testimoni, jumlah user, notifikasi, lokasi, atau aktivitas live. Data ilustrasi wajib diberi label. Jangan simulasi checkout/scan/deploy yang tidak terhubung.

## Aplikasi satu file dan halaman terpublikasi
Untuk dashboard/aplikasi kecil, ikuti `references/app-patterns.md`: penyimpanan aman (try/catch), konfirmasi tanpa dialog bawaan, cadangan lewat dialog, render aman, tema tiga mode, dan verifikasi minimum yang jujur.

## Tap highlight mobile
Hilangkan flash biru/abu bawaan lewat stylesheet global (`-webkit-tap-highlight-color: transparent`), TETAP pertahankan `:focus-visible` yang jelas dan beri `:active` yang disengaja. Jangan `outline: none` global.

## Responsif
Target uji: 320, 375, 768, 1024, 1440 px. Tidak ada overflow horizontal, teks terpotong, atau aksi saling menimpa. Pertimbangkan safe-area inset untuk dock/bottom bar.

## Status bukti
PASS / FAIL / BLOCKED / NOT RUN / PARTIAL. Jangan pernah menandai BLOCKED atau NOT RUN sebagai PASS.

## Kompatibilitas agen
- Skill ini mengikuti format Agent Skills (SKILL.md) dan tidak bergantung pada fitur satu agen.
- Perintah /slop-* adalah skill terpisah. Di agen tanpa slash command, panggil dengan nama: "jalankan slop-audit pada src/". Argumen adalah teks setelah nama perintah.
- Pakai tool yang dimiliki agen (baca/tulis file, terminal, browser bila ada). Jika tool tidak tersedia, tandai BLOCKED atau NOT RUN dan jangan berpura-pura lulus.

## Batas aman
Minta izin sebelum: hapus data/file besar, rewrite history Git, ubah secret/auth/produksi, deploy/publish, layanan berbayar.
