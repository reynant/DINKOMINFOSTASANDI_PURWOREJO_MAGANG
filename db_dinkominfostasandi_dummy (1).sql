-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2025 at 10:16 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_dinkominfostasandi_dummy`
--

-- --------------------------------------------------------

--
-- Table structure for table `agenda_admin`
--

CREATE TABLE `agenda_admin` (
  `id` int(11) UNSIGNED NOT NULL,
  `tema` varchar(255) NOT NULL,
  `tgl_mulai` date DEFAULT NULL,
  `tgl_selesai` date DEFAULT NULL,
  `jam` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `agenda_admin`
--

INSERT INTO `agenda_admin` (`id`, `tema`, `tgl_mulai`, `tgl_selesai`, `jam`, `created_at`, `updated_at`) VALUES
(1, 'KGTR - Peningkatan Penggunaan Produk Dalam Negeri', '0000-00-00', '0000-00-00', '20.00 s.d selesai', '2025-08-13 02:39:22', '2025-08-13 02:39:22'),
(2, 'Command Center', '0000-00-00', '0000-00-00', NULL, '2025-08-13 02:39:22', '2025-08-13 02:39:22'),
(3, 'CVP', '0000-00-00', '2021-04-29', '09.00', '2025-08-13 02:40:34', '2025-08-13 02:40:34');

-- --------------------------------------------------------

--
-- Table structure for table `alamat_kontak`
--

CREATE TABLE `alamat_kontak` (
  `id` int(11) NOT NULL,
  `alamat` text NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `berita`
--

CREATE TABLE `berita` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `sub_judul` varchar(255) DEFAULT NULL,
  `video_youtube` varchar(255) DEFAULT NULL,
  `kategori` varchar(100) DEFAULT NULL,
  `headline` tinyint(1) DEFAULT 0,
  `berita_utama` tinyint(1) DEFAULT 0,
  `isi_berita` text DEFAULT NULL,
  `gambar` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `waktu_posting` datetime DEFAULT current_timestamp(),
  `tanggal` date DEFAULT NULL,
  `status` enum('Published','Draft') DEFAULT 'Draft',
  `id_penulis` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `berita`
--

INSERT INTO `berita` (`id`, `judul`, `sub_judul`, `video_youtube`, `kategori`, `headline`, `berita_utama`, `isi_berita`, `gambar`, `tag`, `waktu_posting`, `tanggal`, `status`, `id_penulis`) VALUES
(1, '[HOAKS] Video Batik Air Tergelincir di Kota Yogyakarta pada Februari 2025', NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, '2025-08-12 13:45:39', '2025-02-28', 'Published', NULL),
(4, '[HOAKS] Video Batik Air Tergelincir di Kota Yogyakarta pada Februari 2025', '', '', 'Hoaks', 0, 0, 'Peristiwa dalam video adalah pesawat Batik Air tergelincir di Bandara Adisutjipto, Daerah Istimewa Yogyakarta (DIY) pada 6 September 2015.\r\nKategori : Hoaks\r\n        ', NULL, '', '2025-02-28 08:03:25', NULL, 'Draft', NULL),
(9, '[HOAKS] Video Batik Air Tergelincir di Kota Yogyakarta pada Februari 2025', NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, '2025-08-13 13:44:26', '2025-08-13', 'Draft', NULL),
(27, 'mount merbaby', 'tes', '', 'tse', 0, 0, 'tes', '1758271982_Screenshot_261.png', '', '0000-00-00 00:00:00', '2025-09-19', 'Published', NULL),
(28, 'tes gambar ', 'tse', 'es', 'tes', 0, 0, 'ses', '1758274128_Screenshot_267.png', '', '0000-00-00 00:00:00', '2025-09-19', 'Published', NULL),
(29, 'tes gambar lagi', 'tes', 'tes', 'tse', 0, 0, 'ini tes gambar lagi', '1758506205_Screenshot_248.png', 'tes', '0000-00-00 00:00:00', '2025-09-22', 'Published', NULL),
(30, 'tes again', 'kucing ku', 't', 't', 0, 0, 't', '1758506600_Screenshot_249.png', '', '0000-00-00 00:00:00', '2025-09-22', 'Published', NULL),
(31, 'tes 1', 't', 'tse', 't', 0, 0, 't', '1758508846_Screenshot_254.png', '', '0000-00-00 00:00:00', '2025-09-22', 'Published', NULL),
(32, 'tes 2', 't', 't', 't', 0, 0, 't', '1758509258_Screenshot_253.png', 't', '0000-00-00 00:00:00', '2025-09-22', 'Published', NULL),
(38, 'tes kuy', 'tes', 'tes', 'tes', 0, 0, 'tes', '1758523350_Screenshot_189.png', 'tes', '0000-00-00 00:00:00', '2025-09-22', 'Published', NULL),
(39, 'tes tes', '', '', '', 0, 0, 'tes', '1758529603_Screenshot_240.png', '', '0000-00-00 00:00:00', '2025-09-22', 'Published', NULL),
(40, 'tes isi berita', 'tes', 'tes', 'tes', 0, 0, 'High dive into frozen waves where the past comes back to life\r\nFight fear for the selfish pain, it was worth it every time\r\nHold still right before we crash \'cause we both know how this ends\r\nA clock ticks \'til it breaks your glass and I drown in you again\r\n\r\n\'Cause you are the piece of me I wish I didn\'t need\r\nChasing relentlessly, still fight and I don\'t know why\r\nIf our love is tragedy, why are you my remedy?\r\nIf our love\'s insanity, why are you my clarity?\r\n\r\nIf our love is tragedy, why are you my remedy?\r\nIf our love\'s insanity, why are you my clarity?\r\n\r\nWalk on through a red parade and refuse to make amends\r\nIt cuts deep through our ground and makes us forget all common sense\r\nDon\'t speak as I try to leave \'cause we both know what we\'ll choose\r\nIf you pull, then I\'ll push too deep and I\'ll fall right back to you\r\n\r\n\'Cause you are the piece of me I wish I didn\'t need\r\nChasing relentlessly, still fight and I don\'t know why\r\nIf our love is tragedy, why are you my remedy?\r\nIf our love\'s insanity, why are you my clarity?\r\n\r\n\r\nWhy are you my clarity?\r\nWhy are you my remedy?\r\nWhy are you my clarity?\r\nWhy are you my remedy?\r\n\r\nIf our love is tragedy, why are you my remedy?\r\nIf our love\'s insanity, why are you my clarity?', '1758678579_Screenshot_391.png', '', '0000-00-00 00:00:00', '2025-09-24', 'Published', NULL),
(41, 'tes tag', 'tag', 'tag', 'tag', 0, 0, 'tag', '1758700663_Screenshot_392.png', 'KEGIATAN', '0000-00-00 00:00:00', '2025-09-24', 'Published', NULL),
(42, 'tes editor text', 'tes editor text', '', '', 0, 0, '<p>tes editor text</p>', NULL, 'KEGIATAN', '0000-00-00 00:00:00', '2025-10-02', 'Published', NULL),
(43, 'tes editor text 2', 'tes editor text 2', '', '', 0, 0, '<p>TES EDITOR TEXT 2</p>\r\n<p><span style=\"font-family: \'arial black\', sans-serif;\">TES EDITOR TEXT 2</span></p>\r\n<h2><strong><span style=\"font-family: \'times new roman\', times, serif; font-size: 36pt;\">TES EDITOR TEXT 2</span></strong></h2>\r\n<h3><em><span style=\"font-family: \'comic sans ms\', sans-serif; font-size: 24pt;\">TES EDITOR TEXT 2</span></em></h3>', '1759392863_WhatsApp_Image_2025-09-23_at_10.27.17.jpeg', '', '0000-00-00 00:00:00', '2025-10-02', 'Published', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `berita_foto`
--

CREATE TABLE `berita_foto` (
  `id` int(11) NOT NULL,
  `cover` varchar(255) DEFAULT NULL,
  `judul_berita_foto` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `aktif` enum('Y','N') DEFAULT 'Y'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `berita_foto`
--

INSERT INTO `berita_foto` (`id`, `cover`, `judul_berita_foto`, `url`, `aktif`) VALUES
(1, 'uploads/harganas.jpg', 'Harganas', 'album/detail/harganas', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `download_area`
--

CREATE TABLE `download_area` (
  `No` int(11) NOT NULL,
  `Judul` varchar(255) NOT NULL,
  `Link` varchar(255) NOT NULL,
  `Hits` int(11) DEFAULT NULL,
  `Tanggal` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `download_area`
--

INSERT INTO `download_area` (`No`, `Judul`, `Link`, `Hits`, `Tanggal`) VALUES
(1, 'Kebijakan Privasi Kabupaten Purworejo', 'files/kebijakan_privasi.pdf', 37, '08 Agu 2024'),
(2, 'Prosedur Pengamanan Area Fisik dan Lingkungan', 'files/prosedur_pengamanan.pdf', 36, '18 Jul 2024'),
(3, 'Masterplan Smart City Kabupaten Purworejo 2021-2026', 'files/masterplan_smartcity.pdf', 69, '30 Mei 2024'),
(4, 'Peraturan Bupati Nomor 23 Tahun 2023 TENTANG SISTEM PEMERINTAHAN BERBASIS ELEKTRONIK', 'files/perbup_23_2023.pdf', 56, '30 Nov 2023'),
(5, 'Kebijakan Umum Sistem Manajemen Keamanan Informasi Oktober 2023', 'files/kebijakan_umum_smki.pdf', 59, '29 Nov 2023'),
(6, 'Pengumuman Hasil Seleksi Administrasi Calon Dewan Pengawas LPPL Radio Publik Kabupaten Purworejo', 'files/pengumuman_seleksi_administrasi.pdf', 129, '01 Des 2022'),
(7, 'Pengumuman Pendaftaran Seleksi Dewan Pengawas LPPL Irama FM', 'files/pengumuman_pendaftaran.pdf', 150, '11 Nov 2022'),
(8, 'Hasil SKM Tahun 2021', 'files/hasil_skm_2021.pdf', 379, '10 Feb 2022'),
(9, 'Hasil SKM 2020', 'files/hasil_skm_2020.pdf', 558, '17 Juni 2021'),
(10, 'LKJIP 2020', 'files/lkjip_2020.pdf', 258, '13 Apr 2021');

-- --------------------------------------------------------

--
-- Table structure for table `halaman_baru`
--

CREATE TABLE `halaman_baru` (
  `id` int(11) NOT NULL,
  `judul` text NOT NULL,
  `link` text NOT NULL,
  `tanggal_posting` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `halaman_baru`
--

INSERT INTO `halaman_baru` (`id`, `judul`, `link`, `tanggal_posting`) VALUES
(1, 'LHKAN', 'halaman/detail/lhkan', '2025-01-08'),
(2, 'LKjIP', 'halaman/detail/lkjip', '2025-01-08');

-- --------------------------------------------------------

--
-- Table structure for table `identitas_website`
--

CREATE TABLE `identitas_website` (
  `id` int(11) NOT NULL,
  `nama_website` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `domain` varchar(255) DEFAULT NULL,
  `sosial_network` text DEFAULT NULL,
  `no_rekening` varchar(100) DEFAULT NULL,
  `no_telpon` varchar(50) DEFAULT NULL,
  `meta_deskripsi` text DEFAULT NULL,
  `meta_keyword` text DEFAULT NULL,
  `google_maps` text DEFAULT NULL,
  `favicon` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `identitas_website`
--

INSERT INTO `identitas_website` (`id`, `nama_website`, `email`, `domain`, `sosial_network`, `no_rekening`, `no_telpon`, `meta_deskripsi`, `meta_keyword`, `google_maps`, `favicon`) VALUES
(1, 'Dinas Komunikasi, Informatika, Statistik dan Persandian Kabupaten Purworejo', 'dinkominfo.purworejokab@gmail.com', 'https://purworejokab.go.id', '', 'None', '(0275) 7530915', 'None', 'None', 'None', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `jejak_pendapat`
--

CREATE TABLE `jejak_pendapat` (
  `id` int(11) NOT NULL,
  `pilihan` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `rating` int(11) NOT NULL,
  `aktif` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jejak_pendapat`
--

INSERT INTO `jejak_pendapat` (`id`, `pilihan`, `status`, `rating`, `aktif`) VALUES
(1, 'Bagaimana', 'Pertanyaan?', 0, 'N');

-- --------------------------------------------------------

--
-- Table structure for table `kategori_berita`
--

CREATE TABLE `kategori_berita` (
  `id` int(11) NOT NULL,
  `nama_kategori` varchar(100) NOT NULL,
  `link` varchar(100) NOT NULL,
  `artikel` varchar(100) NOT NULL,
  `posisi` varchar(100) NOT NULL,
  `aktif` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kategori_berita`
--

INSERT INTO `kategori_berita` (`id`, `nama_kategori`, `link`, `artikel`, `posisi`, `aktif`) VALUES
(1, 'Kominfo Goes To The Radio', 'kategori/detail/kominfo-goes-to-the-radio', '6', '0', 'Y'),
(2, 'CVP', 'kategori/detail/cvp', '10', '0', 'Y'),
(3, 'Pelayanan Informasi Publik', 'kategori/detail/pelayanan-informasi-publik', '8', '0', 'Y'),
(4, 'SMART CITY', 'kategori/detail/smart-city', '15', '0', 'Y'),
(5, 'KIM', 'kategori/detail/kim', '2', '0', 'Y'),
(7, 'Isu Hoaks', 'kategori/detail/isu-hoaks', '5755', '0', 'Y'),
(8, 'Kegiatan', '', '840', '2', 'Y'),
(9, 'Pemerintahan', 'kategori/detail/pemerintahan', '77', '1', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `komentar_berita`
--

CREATE TABLE `komentar_berita` (
  `id` int(11) NOT NULL,
  `nama_komentator` varchar(100) NOT NULL,
  `isi_komentar` text NOT NULL,
  `tanggal_komentar` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `komentar_berita`
--

INSERT INTO `komentar_berita` (`id`, `nama_komentator`, `isi_komentar`, `tanggal_komentar`) VALUES
(1, 'Bintang', 'Hati hati dgn penipu berkedok lazada..usut tuntas karena meresahkan..', '2025-08-01 15:20:27'),
(2, 'fadli', 'hoax harus d lawan dan perangi demi menjaga kenyamanan sosial', '2025-08-01 15:20:50'),
(3, 'dwgimron', 'sangat bermanfaat dan membantu sekali dengan adanya informasi hoaxs', '2025-08-01 15:21:13'),
(4, '', 'Saya kecewa.kenapa pemerintah tidk blok aja game setan ini.', '2025-08-01 15:23:34'),
(5, 'Wadim', 'Saya ditipu', '2025-08-19 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `komentar_video`
--

CREATE TABLE `komentar_video` (
  `id` int(11) NOT NULL,
  `nama_komentar` varchar(100) NOT NULL,
  `isi_komentar` text NOT NULL,
  `aktif` enum('Y','N') DEFAULT 'Y'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pesan_masuk`
--

CREATE TABLE `pesan_masuk` (
  `id` int(255) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subjek` varchar(255) NOT NULL,
  `tanggal` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pesan_masuk`
--

INSERT INTO `pesan_masuk` (`id`, `nama`, `email`, `subjek`, `tanggal`) VALUES
(1, 'ika', 'ikafajarintan@gmail.com', '114.10.1.73', '15 Nov 2022');

-- --------------------------------------------------------

--
-- Table structure for table `playlist_video`
--

CREATE TABLE `playlist_video` (
  `id` int(11) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `judul_playlist` varchar(150) NOT NULL,
  `aktif` enum('ya','tidak') NOT NULL DEFAULT 'ya',
  `action` enum('tampil','arsip') NOT NULL DEFAULT 'tampil'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `playlist_video`
--

INSERT INTO `playlist_video` (`id`, `cover`, `judul_playlist`, `aktif`, `action`) VALUES
(1, '', 'Ngobras', 'ya', 'tampil'),
(2, '', 'Gendis Broto', 'ya', 'tampil'),
(3, '', 'Podkesdjo', 'ya', 'tampil'),
(4, '', 'Gending Setu  Legi', 'ya', 'tampil');

-- --------------------------------------------------------

--
-- Table structure for table `sekilas_info`
--

CREATE TABLE `sekilas_info` (
  `id` int(11) NOT NULL,
  `isi_info` text NOT NULL,
  `aktif` enum('Y','N') DEFAULT 'Y',
  `posting` timestamp NOT NULL DEFAULT current_timestamp(),
  `foto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sekilas_info`
--

INSERT INTO `sekilas_info` (`id`, `isi_info`, `aktif`, `posting`, `foto`) VALUES
(1, 'Nant', 'Y', '2025-08-20 02:46:30', NULL),
(2, 'Rey', 'Y', '2025-08-20 02:46:30', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `sensor_komentar`
--

CREATE TABLE `sensor_komentar` (
  `id` int(11) NOT NULL,
  `kata_jelek` varchar(100) NOT NULL,
  `ganti_menjadi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sensor_komentar`
--

INSERT INTO `sensor_komentar` (`id`, `kata_jelek`, `ganti_menjadi`) VALUES
(1, 'dancuk', '&**k'),
(2, 'anjir', 'a***r'),
(3, 'pantat', 'p****t'),
(4, 'fuck', 'f**k'),
(5, 'sex', 's**'),
(6, 'bangsat', 'b******'),
(7, 'bajingan', 'b*******');

-- --------------------------------------------------------

--
-- Table structure for table `tag_berita`
--

CREATE TABLE `tag_berita` (
  `id` int(11) NOT NULL,
  `nama_tag` varchar(100) NOT NULL,
  `link` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tag_berita`
--

INSERT INTO `tag_berita` (`id`, `nama_tag`, `link`) VALUES
(1, 'Kominfo Goes To The Radio', 'berita/tag/spbe');

-- --------------------------------------------------------

--
-- Table structure for table `tag_video`
--

CREATE TABLE `tag_video` (
  `id` int(11) NOT NULL,
  `nama_tag` varchar(255) NOT NULL,
  `link_video` varchar(512) NOT NULL,
  `posisi` int(11) NOT NULL,
  `aktif` tinyint(1) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tag_video`
--

INSERT INTO `tag_video` (`id`, `nama_tag`, `link_video`, `posisi`, `aktif`, `created_at`, `updated_at`) VALUES
(1, 'kominfo fun games', 'https://www.youtube.com/watch?v=x3wyV_m2TzQ', 0, 1, '2025-08-20 01:31:48', '2025-08-20 01:31:48'),
(2, 'road to mas mba jateng', 'https://www.youtube.com/watch?v=ROUjO8Xzcws', 0, 1, '2025-08-20 01:34:00', '2025-08-20 02:16:20');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(100) DEFAULT NULL,
  `Nama_Lengkap` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Foto` varchar(255) DEFAULT NULL,
  `Blokir` varchar(5) DEFAULT NULL,
  `Kiriman` int(11) DEFAULT 0,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id` int(10) UNSIGNED NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('Admin','Editor','Operator','Kontributor') NOT NULL DEFAULT 'Kontributor'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `Nama_Lengkap`, `Email`, `Foto`, `Blokir`, `Kiriman`, `created_at`, `updated_at`, `id`, `password`, `level`) VALUES
('admin', 'admin ganteng', 'adminganteng@gmail.com', NULL, NULL, 0, '2025-09-11 10:52:57', '2025-09-11 11:13:19', 5, 'f865b53623b121fd34ee5426c792e5c33af8c227', 'Admin'),
('editor', 'editor ganteng', 'editorganteng@gmail.com', NULL, NULL, 0, '2025-09-11 10:54:25', '2025-09-11 11:14:09', 6, 'ef2ea8f0684b26279444be0cfc7ac395cc75df89', 'Editor'),
('operator', 'operator ganteng', 'operatorganteng@gmail.com', NULL, NULL, 0, '2025-09-11 10:55:07', '2025-09-11 11:17:02', 7, '4aed7fb4eed446796c59ab3fd911e359f063ec83', 'Operator'),
('kontributor', 'kontributor ganteng', 'kontributorganteng@gmail.com', NULL, NULL, 0, '2025-09-11 10:55:56', '2025-09-11 11:17:33', 8, 'abc54325e0a1a51e3166e47b33893c0af6c9c0b4', 'Kontributor');

-- --------------------------------------------------------

--
-- Table structure for table `video`
--

CREATE TABLE `video` (
  `id` int(11) NOT NULL,
  `judul_video` varchar(100) NOT NULL,
  `tanggal_video` date NOT NULL,
  `playlist` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `video`
--

INSERT INTO `video` (`id`, `judul_video`, `tanggal_video`, `playlist`) VALUES
(1, 'Ngobras DPRD', '2023-04-27', 'Ngobras'),
(2, 'PODKESDJO - Podkesnya Purworedjo', '2023-04-27', 'Podkesdjo'),
(3, 'Gendis Broto', '2023-04-27', 'Gendis Broto'),
(4, 'Forum Dengar Aspirasi Publik Critical Voice Point(CVP)', '2023-04-27', 'Critical Voice Point'),
(5, 'Kominfo Goes To The Radio', '2023-04-27', 'Kominfo Goes To The Radio');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agenda_admin`
--
ALTER TABLE `agenda_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alamat_kontak`
--
ALTER TABLE `alamat_kontak`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `berita`
--
ALTER TABLE `berita`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `berita_foto`
--
ALTER TABLE `berita_foto`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `download_area`
--
ALTER TABLE `download_area`
  ADD PRIMARY KEY (`No`);

--
-- Indexes for table `halaman_baru`
--
ALTER TABLE `halaman_baru`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `identitas_website`
--
ALTER TABLE `identitas_website`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `komentar_berita`
--
ALTER TABLE `komentar_berita`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `komentar_video`
--
ALTER TABLE `komentar_video`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pesan_masuk`
--
ALTER TABLE `pesan_masuk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlist_video`
--
ALTER TABLE `playlist_video`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sekilas_info`
--
ALTER TABLE `sekilas_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sensor_komentar`
--
ALTER TABLE `sensor_komentar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tag_video`
--
ALTER TABLE `tag_video`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agenda_admin`
--
ALTER TABLE `agenda_admin`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `alamat_kontak`
--
ALTER TABLE `alamat_kontak`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `berita`
--
ALTER TABLE `berita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `berita_foto`
--
ALTER TABLE `berita_foto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `download_area`
--
ALTER TABLE `download_area`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `halaman_baru`
--
ALTER TABLE `halaman_baru`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `identitas_website`
--
ALTER TABLE `identitas_website`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `komentar_berita`
--
ALTER TABLE `komentar_berita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `komentar_video`
--
ALTER TABLE `komentar_video`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pesan_masuk`
--
ALTER TABLE `pesan_masuk`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `playlist_video`
--
ALTER TABLE `playlist_video`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sekilas_info`
--
ALTER TABLE `sekilas_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sensor_komentar`
--
ALTER TABLE `sensor_komentar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tag_video`
--
ALTER TABLE `tag_video`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
