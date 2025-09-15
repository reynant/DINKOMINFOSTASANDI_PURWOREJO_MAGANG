/* =============================================== */
/* === JAVASCRIPT UNTUK FITUR UKURAN TEKS === */
/* =============================================== */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Ambil semua elemen tombol yang dibutuhkan dari HTML
    const increaseButton = document.getElementById('increase-font');
    const decreaseButton = document.getElementById('decrease-font');
    const resetButton = document.getElementById('reset-font');
    const rootElement = document.documentElement; // Target utama adalah tag <html>

    // 2. Tentukan batasan ukuran agar teks tidak terlalu besar atau kecil
    const step = 2; // Perubahan 1px pada ukuran dasar setiap kali klik
    const minSize = 10; // Ukuran dasar minimum (default Tailwind biasanya 16px)
    const maxSize = 24; // Ukuran dasar maksimum

    /**
     * Mengubah ukuran font dasar pada elemen <html>.
     * Karena website Anda menggunakan unit 'rem' (dari Tailwind CSS),
     * mengubah font-size di <html> akan secara otomatis menyesuaikan
     * ukuran semua elemen di halaman secara proporsional.
     * @param {number} change - Nilai perubahan (+1 untuk perbesar, -1 untuk perkecil)
     */
    const changeBaseFontSize = (change) => {
        const currentSize = parseFloat(getComputedStyle(rootElement).fontSize);
        let newSize = currentSize + change;

        // Pastikan ukuran baru tidak melebihi batas min/max
        newSize = Math.max(minSize, Math.min(newSize, maxSize));
        
        rootElement.style.fontSize = `${newSize}px`;
        
        // Simpan pilihan pengguna di browser agar tetap sama saat pindah halaman
        localStorage.setItem('preferredBaseFontSize', newSize);
    };

    /**
     * Mereset ukuran font kembali ke pengaturan awal.
     */
    const resetBaseFontSize = () => {
        rootElement.style.fontSize = ''; // Hapus style inline, kembali ke default dari CSS
        localStorage.removeItem('preferredBaseFontSize'); // Hapus data dari penyimpanan
    };

    /**
     * Memuat preferensi ukuran font yang tersimpan saat halaman dibuka.
     */
    const loadPreferences = () => {
        const savedSize = localStorage.getItem('preferredBaseFontSize');
        if (savedSize) {
            rootElement.style.fontSize = `${savedSize}px`;
        }
    };

    // 3. Tambahkan event listener untuk setiap tombol
    increaseButton.addEventListener('click', () => changeBaseFontSize(step));
    decreaseButton.addEventListener('click', () => changeBaseFontSize(-step));
    resetButton.addEventListener('click', resetBaseFontSize);
    
    // 4. Panggil fungsi untuk memuat preferensi saat halaman pertama kali dibuka
    loadPreferences();
});