// Menunggu semua elemen HTML dimuat sebelum menjalankan skrip
document.addEventListener('DOMContentLoaded', () => {

    // Memeriksa apakah browser pengguna mendukung Web Speech API
    if ('speechSynthesis' in window) {
        
        // Mengambil elemen-elemen yang dibutuhkan dari HTML
        const tombolBaca = document.getElementById('tombol-baca-suara');
        const kontenUntukDibaca = document.getElementById('konten-utama');
        
        // Jika tombol atau area konten tidak ditemukan, hentikan skrip dan tampilkan pesan error di console
        if (!tombolBaca || !kontenUntukDibaca) {
            console.error("Tombol '#tombol-baca-suara' atau area '#konten-utama' tidak ditemukan di HTML.");
            if (tombolBaca) tombolBaca.style.display = 'none'; // Sembunyikan tombol jika ada tapi konten tidak ada
            return;
        }

        const spanTombol = tombolBaca.querySelectorAll('span');
        
        // Variabel untuk melacak status pembacaan (sedang membaca atau tidak)
        let sedangMembaca = false;
        
        // Fungsi untuk mengembalikan tampilan tombol ke keadaan semula
        const resetTombol = () => {
            sedangMembaca = false;
            tombolBaca.classList.remove('sedang-membaca');
            spanTombol[0].textContent = '🔊';
            spanTombol[1].textContent = 'Baca Halaman';
        };

        // Menambahkan fungsi yang akan dijalankan saat tombol di-klik
        tombolBaca.addEventListener('click', () => {
            // Jika sedang membaca, maka hentikan
            if (sedangMembaca) {
                window.speechSynthesis.cancel();
                // Tampilan tombol akan direset otomatis oleh event 'onend'
            } else {
                // Jika tidak sedang membaca, maka mulai membaca
                const teks = kontenUntukDibaca.innerText;
                const ucapan = new SpeechSynthesisUtterance(teks);

                // Mengatur bahasa ke Bahasa Indonesia agar logatnya pas
                ucapan.lang = 'id-ID';

                // Fungsi yang dijalankan tepat saat pembacaan dimulai
                ucapan.onstart = () => {
                    sedangMembaca = true;
                    tombolBaca.classList.add('sedang-membaca');
                    spanTombol[0].textContent = '⏹️';
                    spanTombol[1].textContent = 'Hentikan';
                };

                // Fungsi yang dijalankan saat pembacaan selesai (baik karena tuntas atau dihentikan paksa)
                ucapan.onend = () => {
                    resetTombol();
                };
                
                // Fungsi jika terjadi error saat membaca
                ucapan.onerror = (event) => {
                    console.error('Terjadi kesalahan pada SpeechSynthesis: ' + event.error);
                    resetTombol();
                };

                // Perintah untuk mulai berbicara
                window.speechSynthesis.speak(ucapan);
            }
        });

        // Tambahan: Pastikan suara berhenti jika pengguna menutup atau pindah halaman
        window.addEventListener('beforeunload', () => {
            window.speechSynthesis.cancel();
        });

    } else {
        // Jika browser tidak mendukung, sembunyikan tombol dan tampilkan pesan di console
        console.warn("Browser Anda tidak mendukung fitur Web Speech API.");
        const tombolBaca = document.getElementById('tombol-baca-suara');
        if (tombolBaca) {
            tombolBaca.style.display = 'none';
        }
    }
});