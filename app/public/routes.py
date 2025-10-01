from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from app.db import get_db   # ✅ tambahkan ini
import mysql.connector  # ✅ tambahkan ini
# Blueprint dengan template_folder yang benar
# Pastikan path ini benar sesuai dengan struktur folder Anda
public_bp = Blueprint('public', __name__, template_folder='../../templates')


# =============================================================================
# DATA HALAMAN STATIS (PENGGANTI DATABASE)
# =============================================================================
searchable_pages = [
    {'endpoint': 'public.index', 'title': 'Beranda', 'keywords': 'utama halaman depan home'},
    {'endpoint': 'public.about', 'title': 'Tentang Kami', 'keywords': 'about mengenai kami'},
    {'endpoint': 'public.profil', 'title': 'Profil', 'keywords': 'profil dinas gambaran umum'},
    {'endpoint': 'public.tugas_pokok', 'title': 'Tugas Pokok dan Fungsi', 'keywords': 'tupoksi tugas pokok fungsi'},
    {'endpoint': 'public.struktur_organisasi', 'title': 'Struktur Organisasi', 'keywords': 'organisasi struktur bagan'},
    {'endpoint': 'public.visi_misi', 'title': 'Visi dan Misi', 'keywords': 'visi misi tujuan sasaran'},
    {'endpoint': 'public.sekretariat', 'title': 'Sekretariat', 'keywords': 'sekretariat administrasi'},
    {'endpoint': 'public.subbagian_perencanaan', 'title': 'Subbagian Perencanaan dan Keuangan', 'keywords': 'perencanaan keuangan anggaran'},
    {'endpoint': 'public.subbagian_umum', 'title': 'Subbagian Umum dan Kepegawaian', 'keywords': 'umum kepegawaian sdm'},
    {'endpoint': 'public.bidang_ikp', 'title': 'Bidang IKP', 'keywords': 'ikp informasi komunikasi publik'},
    {'endpoint': 'public.bidang_tisp', 'title': 'Bidang TISP', 'keywords': 'tisp telematika informatika statistik persandian'},
    {'endpoint': 'public.bidang_pplkc', 'title': 'Bidang PPLKC', 'keywords': 'pplkc pengelolaan pengaduan layanan'},
    {'endpoint': 'public.profil_pejabat', 'title': 'Profil Pejabat', 'keywords': 'pejabat pimpinan kepala dinas'},
    {'endpoint': 'public.news', 'title': 'Berita', 'keywords': 'news berita artikel informasi terkini'},
    {'endpoint': 'public.galeri', 'title': 'Galeri', 'keywords': 'galeri foto video dokumentasi'},
    {'endpoint': 'public.foto', 'title': 'Galeri Foto', 'keywords': 'foto gambar album'},
    {'endpoint': 'public.video', 'title': 'Galeri Video', 'keywords': 'video klip rekaman'},
    {'endpoint': 'public.hoaks', 'title': 'Cek Fakta Hoaks', 'keywords': 'hoaks antihoax fakta berita palsu'},
    {'endpoint': 'public.laporan_hoaks', 'title': 'Laporan Isu Hoaks', 'keywords': 'lapor aduan isu hoaks'},
    {'endpoint': 'public.kegiatan', 'title': 'Kegiatan', 'keywords': 'kegiatan acara event agenda'},
    {'endpoint': 'public.download', 'title': 'Download', 'keywords': 'unduh berkas file dokumen'},
    {'endpoint': 'public.agenda', 'title': 'Agenda', 'keywords': 'agenda jadwal acara mendatang'},
    {'endpoint': 'public.hubungi_kami', 'title': 'Hubungi Kami', 'keywords': 'kontak alamat email telepon'},
    {'endpoint': 'public.smart_city', 'title': 'Smart City', 'keywords': 'smart city kota cerdas purworejo'},
    {'endpoint': 'public.ppid', 'title': 'PPID', 'keywords': 'ppid pejabat pengelola informasi dan dokumentasi'},
    {'endpoint': 'public.podkesdjo', 'title': 'podkesdjo', 'keywords': 'podkesdjo podcast audio'},
    {'endpoint': 'public.gendis', 'title': 'gendis', 'keywords': 'gendis podcast audio'},
    {'endpoint': 'public.ngobras', 'title': 'ngobras', 'keywords': 'ngobras podcast audio'},
    {'endpoint': 'public.cvp', 'title': 'cvp', 'keywords': 'cvp podcast audio'},
    {'endpoint': 'public.wisata', 'title': 'wisata', 'keywords': 'wisata travel pariwisata'},
    {'endpoint': 'public.rolasan', 'title': 'rolasan', 'keywords': 'rolasan podcast audio'},
    {'endpoint': 'public.gendhing', 'title': 'gendhing', 'keywords': 'gendhing setu legi'},
    {'endpoint': 'public.caangkir', 'title': 'cangkir', 'keywords': 'cangkir podcast audio'},
    {'endpoint': 'public.kominfogoes', 'title': 'kominfogoes', 'keywords': 'kominfogoes kominfo podcast audio'},
    {'endpoint': 'public.dokumen_anggaran', 'title': 'Dokumen Pelaksanaan Anggaran', 'keywords': 'dokumen anggaran keuangan'},
    {'endpoint': 'public.informasi_publik', 'title': 'Informasi Publik', 'keywords': 'informasi publik keterbukaan informasi'},
    {'endpoint': 'public.ljkip', 'title': 'LKjIP', 'keywords': 'lkjip laporan kinerja'},
    {'endpoint': 'public.lhkan', 'title': 'LHKAN', 'keywords': 'lhkan laporan hasil akuntabilitas kinerja'},
    {'endpoint': 'public.spbe', 'title': 'SPBE', 'keywords': 'spbe sistem pemerintahan berbasis elektronik'},
    {'endpoint': 'public.sosial', 'title': 'sosial', 'keywords': 'sosial sosial media'},
    {'endpoint': 'public.rekrutmen', 'title': 'rekrutmen', 'keywords': 'rekrutmen lowongan kerja'},
    {'endpoint': 'public.kim', 'title': 'kim', 'keywords': 'kim kelompok informasi masyarakat'},
    {'endpoint': 'public.budaya', 'title': 'budaya', 'keywords': 'budaya seni tradisi heritage '},   
    {'endpoint': 'public.moap', 'title': 'moap', 'keywords': 'moap podcast audio'},
    {'endpoint': 'public.kebijakan', 'title': 'kebijakan', 'keywords': 'kebijakan aturan regulasi'},
    {'endpoint': 'public.skm', 'title': 'skm', 'keywords': 'skm survei kepuasan masyarakat'},
    {'endpoint': 'public.pip', 'title': 'pip', 'keywords': 'pip pelayanan informasi publik'},
    {'endpoint': 'public.halaman_berita', 'title': 'Halaman Berita', 'keywords': 'berita artikel informasi terkini'},

]    
    
# =============================================================================


# HALAMAN UTAMA

@public_bp.route('/search')
def search():
    """Menangani permintaan pencarian dari publik."""
    query = request.args.get('q')  # Ambil kata kunci dari URL

    if not query:
        # Jika tidak ada kata kunci, kembali ke halaman utama
        return redirect(url_for('public.index'))

    results = []
    search_term = query.lower()

    # Logika pencarian pada data halaman statis
    for page in searchable_pages:
        # Mencocokkan kata kunci dengan judul atau keywords halaman
        if search_term in page['title'].lower() or search_term in page['keywords'].lower():
            results.append(page)

    # Render halaman hasil pencarian
    return render_template('search_results.html',
                           results=results,
                           query=query,
                           title=f"Hasil Pencarian untuk '{query}'")

@public_bp.route('/')
@public_bp.route('/index.html')
def index():
    """Menampilkan halaman utama (dasbor publik) dengan berita terbaru."""
    conn = get_db()
    latest_news = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            # Mengambil 3 berita terbaru yang statusnya 'Publish'
            cursor.execute("""
                SELECT id_berita as id, judul, sub_judul, isi_berita, gambar, tanggal 
                FROM berita 
                WHERE status = 'Publish' 
                ORDER BY tanggal DESC, id_berita DESC 
                LIMIT 3
            """)
            latest_news = cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Database error in index route: {err}")
        finally:
            cursor.close()
            conn.close()
            
    # Kirim data berita ke template index.html
    return render_template('index.html', berita_list=latest_news)



@public_bp.route('/about')
@public_bp.route('/about.html')
def about():
    try:
        return render_template('about.html', title='Tentang Kami')
    except TemplateNotFound:
        abort(404)


# PROFIL & SUBMENU

@public_bp.route('/profil')
@public_bp.route('/profil.html')
def profil():
    try:
        return render_template('profil.html', title='Profil')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/tugas-pokok-dan-fungsi')
@public_bp.route('/tugas-pokok-dan-fungsi.html')
def tugas_pokok():
    try:
        return render_template('tugas-pokok-dan-fungsi.html', title='Tugas Pokok dan Fungsi')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/struktur-organisasi')
@public_bp.route('/struktur-organisasi.html')
def struktur_organisasi():
    try:
        return render_template('struktur-organisasi.html', title='Struktur Organisasi')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/visi-dan-misi')
@public_bp.route('/visi-dan-misi.html')
def visi_misi():
    try:
        return render_template('visi-dan-misi.html', title='Visi dan Misi')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/sekretariat')
@public_bp.route('/sekretariat.html')
def sekretariat():
    try:
        return render_template('sekretariat.html', title='Sekretariat')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/subbagian-perencanaan-dan-keuangan')
@public_bp.route('/subbagian-perencanaan-dan-keuangan.html')
def subbagian_perencanaan():
    try:
        return render_template('subbagian-perencanaan-dan-keuangan.html', title='Subbagian Perencanaan dan Keuangan')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/subbagian-umum-dan-kepegawaian')
@public_bp.route('/subbagian-umum-dan-kepegawaian.html')
def subbagian_umum():
    try:
        return render_template('subbagian-umum-dan-kepegawaian.html', title='Subbagian Umum dan Kepegawaian')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/bidangIKP')
@public_bp.route('/bidangIKP.html')
def bidang_ikp():
    try:
        return render_template('bidangIKP.html', title='Bidang IKP')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/bidangTISP')
@public_bp.route('/bidangTISP.html')
def bidang_tisp():
    try:
        return render_template('bidangTISP.html', title='Bidang TISP')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/bidangPPLKC')
@public_bp.route('/bidangPPLKC.html')
def bidang_pplkc():
    try:
        return render_template('bidangPPLKC.html', title='Bidang PPLKC')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/profil-pejabat')
@public_bp.route('/profil-pejabat.html')
def profil_pejabat():
    try:
        return render_template('profil-pejabat.html', title='Profil Pejabat')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/kebijakan-umum-sistem-manajemen')
@public_bp.route('/kebijakan-umum-sistem-manajemen.html')
def kebijakan_umum():
    try:
        return render_template('kebijakan-umum-sistem-manajemen.html', title='Kebijakan Umum Sistem Manajemen')
    except TemplateNotFound:
        abort(404)


# KONTEN

@public_bp.route('/news')
@public_bp.route('/news.html')
def news():
    try:
        return render_template('news.html', title='news')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/galeri')
@public_bp.route('/galeri.html')
def galeri():
    try:
        return render_template('galeri.html', title='galeri')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/foto')
@public_bp.route('/foto.html')
def foto():
    try:
        return render_template('foto.html', title='foto')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/vidio')
@public_bp.route('/vidio.html')
def video():
    try:
        return render_template('vidio.html', title='vidio')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/podkesdjo')
@public_bp.route('/podkesdjo.html')
def podkesdjo():
    try:
        return render_template('podkesdjo.html', title='podkesdjo')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/gendis')
@public_bp.route('/gendis.html')
def gendis():
    try:
        return render_template('gendis.html', title='gendis')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/ngobras')
@public_bp.route('/ngobras.html')
def ngobras():
    try:
        return render_template('ngobras.html', title='ngobras')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/cvp')
@public_bp.route('/cvp.html')
def cvp():
    try:
        return render_template('cvp.html', title='cvp')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/wisata')
@public_bp.route('/wisata.html')
def wisata():
    try:
        return render_template('wisata.html', title='wisata')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/rolasan')
@public_bp.route('/rolasan.html')
def rolasan():
    try:
        return render_template('rolasan.html', title='rolasan')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/gendhing')
@public_bp.route('/gendhing.html')
def gendhing():
    try:
        return render_template('gendhing.html', title='gendhing')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/cangkir')
@public_bp.route('/cangkir.html')
def caangkir():
    try:
        return render_template('cangkir.html', title='cangkir')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/kominfogoes')
@public_bp.route('/kominfogoes.html')
def kominfogoes():
    try:
        return render_template('kominfogoes.html', title='kominfogoes')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/hoaks')
@public_bp.route('/hoaks.html')
def hoaks():
    try:
        return render_template('hoaks.html', title='hoaks')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/laporan-isu-hoaks')
@public_bp.route('/laporan-isu-hoaks.html')
def laporan_hoaks():
    try:
        return render_template('laporan-isu-hoaks.html', title='laporan-isu-hoaks')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/kegiatan')
@public_bp.route('/kegiatan.html')
def kegiatan():
    try:
        return render_template('kegiatan.html', title='kegiatan')
    except TemplateNotFound:
        abort(404)


# DOWNLOAD & AGENDA

@public_bp.route('/download')
@public_bp.route('/download.html')
def download():
    try:
        return render_template('download.html', title='download')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/agenda')
@public_bp.route('/agenda.html')
def agenda():
    try:
        return render_template('agenda.html', title='agenda')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/layanan-skpd')
@public_bp.route('/layanan-skpd.html')
def layananskpd():
    try:
        return render_template('layanan-skpd.html', title='layanan-skpd')
    except TemplateNotFound:
        abort(404)


# INFORMASI PUBLIK

@public_bp.route('/dokumen-pelaksanaan-anggaran')
@public_bp.route('/dokumen-pelaksanaan-anggaran.html')
def dokumen_anggaran():
    try:
        return render_template('dokumen-pelaksanaan-anggaran.html', title='Dokumen Pelaksanaan Anggaran')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/informasi-publik')
@public_bp.route('/informasi-publik.html')
def informasi_publik():
    try:
        return render_template('pip.html', title='Informasi Publik')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/LKjlP.')
@public_bp.route('/LKjlP.html')
def ljkip():
    try:
        return render_template('LKjlP.html', title='LKjIP')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/LHKAN')
@public_bp.route('/LHKAN.html')
def lhkan():
    try:
        return render_template('LHKAN.html', title='LHKAN')
    except TemplateNotFound:
        abort(404)

# LAIN-LAIN

@public_bp.route('/ppid')
@public_bp.route('/ppid.html')
def ppid():
    try:
        return render_template('ppid.html', title='ppid')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/spbe')
@public_bp.route('/spbe.html')
def spbe():
    try:
        return render_template('spbe.html', title='spbe')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/smart-city')
@public_bp.route('/smart-city.html')
def smart_city():
    try:
        return render_template('smart-city.html', title='smart-city')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/sosial')
@public_bp.route('/sosial.html')
def sosial():
    try:
        return render_template('sosial.html', title='sosial')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/rekrutmen')
@public_bp.route('/rekrutmen.html')
def rekrutmen():
    try:
        return render_template('rekrutmen.html', title='rekrutmen')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/kim')
@public_bp.route('/kim.html')
def kim():
    try:
        return render_template('kim.html', title='kim')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/budaya')
@public_bp.route('/budaya.html')
def budaya():
    try:
        return render_template('budaya.html', title='budaya')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/moap')
@public_bp.route('/moap.html')
def moap():
    try:
        return render_template('moap.html', title='moap')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/kebijakan')
@public_bp.route('/kebijakan.html')
def kebijakan():
    try:
        return render_template('kebijakan.html', title='kebijakan')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/skm')
@public_bp.route('/skm.html')
def skm():
    try:
        return render_template('skm.html', title='skm')
    except TemplateNotFound:
        abort(404)

# HUBUNGI KAMI

@public_bp.route('/hubungi')
@public_bp.route('/hubungi.html')
@public_bp.route('/hubungi-kami.html')
@public_bp.route('/Hubungi-Kami.html')
def hubungi_kami():
    try:
        return render_template('hubungi-kami.html', title='Hubungi Kami')
    except TemplateNotFound:
        abort(404)


@public_bp.route('/pip')
@public_bp.route('/pip.html')
def pip():
    try:
        return render_template('pip.html', title='pip')
    except TemplateNotFound:
        abort(404)

@public_bp.route('/halaman_berita')
@public_bp.route('/halaman_berita.html')
def halaman_berita():
    db = get_db()
    cur = db.cursor(dictionary=True)

    # Hanya tampilkan berita dengan status Published
    cur.execute("""
        SELECT id, judul, sub_judul, isi_berita, gambar, waktu_posting, tanggal
        FROM berita
        WHERE status = 'Published'
        ORDER BY waktu_posting DESC
    """)
    berita_list = cur.fetchall()

    cur.close()
    db.close()

    return render_template(
        'halaman_berita.html',
        title='Halaman Berita',
        berita_list=berita_list
    )

@public_bp.route('/halaman_berita/<int:id>')
def detail_berita(id):
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("""
        SELECT id, judul, sub_judul, isi_berita, gambar, waktu_posting, tanggal
        FROM berita
        WHERE id=%s AND status = 'Published'
    """, (id,))
    berita = cur.fetchone()
    cur.close()
    db.close()

    if not berita:
        abort(404)

    return render_template(
        'detail_berita.html',
        title=berita['judul'],
        berita=berita
    )