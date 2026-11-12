# Pola Aplikasi Satu File (dari uji nyata)

Berlaku untuk dashboard/aplikasi kecil yang berjalan di browser, termasuk halaman yang dipublikasikan.

## 1. Penyimpanan
- Bungkus SETIAP baca/tulis `localStorage` dengan try/catch dan render benar saat hasilnya kosong.
- Beri kunci berversi (`app.v1`) dan validasi data saat dimuat atau diimpor; abaikan entri yang rusak.
- Jika penyimpanan gagal, tampilkan peringatan yang jelas (data hilang saat halaman ditutup) dan tawarkan cadangan.
- Preferensi (tema, urutan) disimpan terpisah dari data utama.

## 2. Konfirmasi tanpa dialog bawaan
- `alert/confirm/prompt` bisa diblokir di iframe/sandbox. Jangan jadikan satu-satunya konfirmasi.
- Aksi destruktif: konfirmasi dua langkah (tombol berubah jadi "Yakin hapus?" dan kembali otomatis setelah beberapa detik) atau `<dialog>`.
- Hapus massal wajib menampilkan jumlah yang akan dihapus.

## 3. Cadangan dan ekspor
- Tautan unduh dan simpan-file lewat skrip bisa tidak berfungsi di halaman terpublikasi.
- Pakai `<dialog>` dengan `<textarea>` berisi JSON: tombol Salin (fallback: pilih teks agar disalin manual) dan Pulihkan (validasi dulu, beri tahu bahwa data akan ditimpa).

## 4. Keamanan render
- Data pengguna masuk lewat `textContent`/`createElement`, bukan `innerHTML`.
- Batasi panjang input; abaikan field tak dikenal saat impor.

## 5. Tema
- Warna sebagai token di `:root`; tiga mode Otomatis/Terang/Gelap lewat `data-theme` + `prefers-color-scheme`, dan `color-scheme` ikut diatur.
- Pilihan pengguna tersimpan; default mengikuti sistem.

## 6. Navigasi mobile
- Filter utama di dock bawah dengan `env(safe-area-inset-bottom)`; di layar lebar pindah ke atas daftar. Beri ruang bawah halaman agar konten tidak tertutup dock.

## 7. Konten jujur
- Mulai dari kosong dengan empty state yang menjelaskan langkah pertama. Angka ringkasan dihitung dari data pengguna.
- Status dan peringatan memakai teks + simbol, bukan warna saja.

## 8. Verifikasi minimum bila tanpa browser
- Cek sintaks skrip (misalnya `node --check`), ukuran file, dan tidak ada dependency tak perlu.
- Uji klik, viewport, kontras, dan screen reader tetap NOT RUN sampai benar-benar dijalankan.
