# Checklist AI-Slop (skor 0 = bersih)

Beri 1 poin per temuan. Setiap temuan wajib disertai lokasi file/komponen.

## Visual
- [ ] Palet default ungu/biru-gradien tanpa alasan produk
- [ ] Glassmorphism/blur berlebihan di semua permukaan
- [ ] Glow/neon dekoratif
- [ ] Radius besar seragam di semua elemen
- [ ] Emoji dipakai sebagai ikon UI
- [ ] Bayangan berlapis tanpa sistem

## Layout & hierarki
- [ ] Sidebar + grid kartu tanpa alasan
- [ ] Tiga kartu fitur identik sebagai pengisi
- [ ] Aksi utama tidak jelas / semua elemen bersaing
- [ ] Mobile hanya "desktop yang dikecilkan"

## Konten
- [ ] Copy generik / klise
- [ ] Testimoni, rating, jumlah user, atau statistik palsu
- [ ] Notifikasi / aktivitas live palsu
- [ ] Lorem ipsum atau placeholder tertinggal

## Fungsi
- [ ] Tombol/tautan mati (href="#", onClick kosong)
- [ ] Tidak ada state loading/empty/error/disabled
- [ ] Simulasi operasi backend yang tidak nyata tanpa label demo
- [ ] `localStorage`/penyimpanan dipakai tanpa try/catch atau tanpa peringatan saat gagal
- [ ] `alert/confirm/prompt` sebagai satu-satunya konfirmasi aksi destruktif
- [ ] Data pengguna dimasukkan lewat `innerHTML` tanpa escape
- [ ] Hapus massal tanpa konfirmasi atau tanpa menampilkan jumlahnya
- [ ] Fitur unduh/ekspor yang bergantung pada tautan unduh di halaman terpublikasi

## Aksesibilitas & interaksi
- [ ] `outline: none` global tanpa pengganti
- [ ] Ikon-saja tanpa nama aksesibel
- [ ] Hover sebagai satu-satunya cara akses
- [ ] Info hanya lewat warna
- [ ] Tidak ada dukungan `prefers-reduced-motion`
- [ ] Tap highlight bawaan bertabrakan dengan desain

## Interpretasi skor
0–2 bersih · 3–6 perlu polish · 7–12 terasa generik · 13+ ubah konsep visual, bukan hanya warna.
