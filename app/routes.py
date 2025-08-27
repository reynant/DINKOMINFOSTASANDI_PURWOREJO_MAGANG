from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# Blueprint dengan template_folder yang benar
main = Blueprint('main', __name__, template_folder='public/templates')


# HALAMAN UTAMA


@main.route('/')
@main.route('/index.html')
def index():
    try:
        return render_template('public/index.html')
    except TemplateNotFound:
        abort(404)


@main.route('/about')
@main.route('/about.html')
def about():
    try:
        return render_template('public/about.html')
    except TemplateNotFound:
        abort(404)


# PROFIL & SUBMENU


@main.route('/profil')
@main.route('/profil.html')
def profil():
    try:
        return render_template('public/profil.html')
    except TemplateNotFound:
        abort(404)

@main.route('/tugas-pokok-dan-fungsi')
@main.route('/tugas-pokok-dan-fungsi.html')
def tugas_pokok():
    try:
        return render_template('public/tugas-pokok-dan-fungsi.html')
    except TemplateNotFound:
        abort(404)

@main.route('/struktur-organisasi')
@main.route('/struktur-organisasi.html')
def struktur_organisasi():
    try:
        return render_template('public/struktur-organisasi.html')
    except TemplateNotFound:
        abort(404)

@main.route('/visi-dan-misi')
@main.route('/visi-dan-misi.html')
def visi_misi():
    try:
        return render_template('public/visi-dan-misi.html')
    except TemplateNotFound:
        abort(404)

@main.route('/sekretariat')
@main.route('/sekretariat.html')
def sekretariat():
    try:
        return render_template('public/sekretariat.html')
    except TemplateNotFound:
        abort(404)

@main.route('/subbagian-perencanaan-dan-keuangan')
@main.route('/subbagian-perencanaan-dan-keuangan.html')
def subbagian_perencanaan():
    try:
        return render_template('public/subbagian-perencanaan-dan-keuangan.html')
    except TemplateNotFound:
        abort(404)

@main.route('/subbagian-umum-dan-kepegawaian')
@main.route('/subbagian-umum-dan-kepegawaian.html')
def subbagian_umum():
    try:
        return render_template('public/subbagian-umum-dan-kepegawaian.html')
    except TemplateNotFound:
        abort(404)

@main.route('/bidangIKP')
@main.route('/bidangIKP.html')
def bidang_ikp():
    try:
        return render_template('public/bidangIKP.html')
    except TemplateNotFound:
        abort(404)

@main.route('/bidangTISP')
@main.route('/bidangTISP.html')
def bidang_tisp():
    try:
        return render_template('public/bidangTISP.html')
    except TemplateNotFound:
        abort(404)

@main.route('/bidangPPLKC')
@main.route('/bidangPPLKC.html')
def bidang_pplkc():
    try:
        return render_template('public/bidangPPLKC.html')
    except TemplateNotFound:
        abort(404)

@main.route('/profil-pejabat') #  Belum Bisa
@main.route('/profil-pejabat.html')
def profil_pejabat():
    try:
        return render_template('public/profil-pejabat.html')
    except TemplateNotFound:
        abort(404)

@main.route('/kebijakan-umum-sistem-manajemen')
@main.route('/kebijakan-umum-sistem-manajemen.html')
def kebijakan_umum():
    try:
        return render_template('public/kebijakan-umum-sistem-manajemen.html')
    except TemplateNotFound:
        abort(404)


# KONTEN


@main.route('/news')
@main.route('/news.html')
def news():
    try:
        return render_template('public/news.html')
    except TemplateNotFound:
        abort(404)

@main.route('/galeri')
@main.route('/galeri.html')
def galeri():
    try:
        return render_template('public/galeri.html')
    except TemplateNotFound:
        abort(404)

@main.route('/foto')
@main.route('/foto.html')
def foto():
    try:
        return render_template('public/foto.html')
    except TemplateNotFound:
        abort(404)

@main.route('/vidio')
@main.route('/vidio.html')
def video():
    try:
        return render_template('public/vidio.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/podkesdjo')
@main.route('/podkesdjo.html')
def podkesdjo():
    try:
        return render_template('public/podkesdjo.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/gendis')
@main.route('/gendis.html')
def gendis():
    try:
        return render_template('public/gendis.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/ngobras')
@main.route('/ngobras.html')
def ngobras():
    try:
        return render_template('public/ngobras.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/cvp')
@main.route('/cvp.html')
def cvp():
    try:
        return render_template('public/cvp.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/wisata')
@main.route('/wisata.html')
def wisata():
    try:
        return render_template('public/wisata.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/rolasan')
@main.route('/rolasan.html')
def rolasan():
    try:
        return render_template('public/rolasan.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/gendhing')
@main.route('/gendhing.html')
def gendhing():
    try:
        return render_template('public/gendhing.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/cangkir')
@main.route('/cangkir.html')
def caangkir():
    try:
        return render_template('public/cangkir.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/kominfogoes')
@main.route('/kominfogoes.html')
def kominfogoes():
    try:
        return render_template('public/kominfogoes.html')  
    except TemplateNotFound:
        abort(404)

@main.route('/hoaks')
@main.route('/hoaks.html')
def hoaks():
    try:
        return render_template('public/hoaks.html')
    except TemplateNotFound:
        abort(404)

@main.route('/laporan-isu-hoaks')
@main.route('/laporan-isu-hoaks.html')
def laporan_hoaks():
    try:
        return render_template('public/laporan-isu-hoaks.html')
    except TemplateNotFound:
        abort(404)

@main.route('/kegiatan')
@main.route('/kegiatan.html')
def kegiatan():
    try:
        return render_template('public/kegiatan.html')
    except TemplateNotFound:
        abort(404)


# DOWNLOAD & AGENDA


@main.route('/download')
@main.route('/download.html')
def download():
    try:
        return render_template('public/download.html')
    except TemplateNotFound:
        abort(404)

@main.route('/agenda')
@main.route('/agenda.html')
def agenda():
    try:
        return render_template('public/agenda.html')
    except TemplateNotFound:
        abort(404)

@main.route('/layanan-skpd')
@main.route('/layanan-skpd.html')
def layananskpd():
    try:
        return render_template('public/layanan-skpd.html')
    except TemplateNotFound:
        abort(404)


# INFORMASI PUBLIK


@main.route('/dokumen-pelaksanaan-anggaran')
@main.route('/dokumen-pelaksanaan-anggaran.html')
def dokumen_anggaran():
    try:
        return render_template('public/dokumen-pelaksanaan-anggaran.html')
    except TemplateNotFound:
        abort(404)

@main.route('/informasi-publik')
@main.route('/informasi-publik.html')
def informasi_publik():
    try:
        return render_template('public/pip.html')
    except TemplateNotFound:
        abort(404)

@main.route('/LKjlP.')
@main.route('/LKjlP.html')
def ljkip():
    try:
        return render_template('public/LKjlP.html')
    except TemplateNotFound:
        abort(404)

@main.route('/LHKAN')
@main.route('/LHKAN.html')
def lhkan():
    try:
        return render_template('public/LHKAN.html')
    except TemplateNotFound:
        abort(404)

# LAIN-LAIN

@main.route('/ppid')
@main.route('/ppid.html')
def ppid():
    try:
        return render_template('public/ppid.html')
    except TemplateNotFound:
        abort(404)

@main.route('/spbe')
@main.route('/spbe.html')
def spbe():
    try:
        return render_template('public/spbe.html')
    except TemplateNotFound:
        abort(404)

@main.route('/smart-city')
@main.route('/smart-city.html')
def smart_city():
    try:
        return render_template('public/smart-city.html')
    except TemplateNotFound:
        abort(404)

@main.route('/sosial')
@main.route('/sosial.html')
def sosial():
    try:
        return render_template('public/sosial.html')
    except TemplateNotFound:
        abort(404)

@main.route('/rekrutmen')
@main.route('/rekrutmen.html')
def rekrutmen():
    try:
        return render_template('public/rekrutmen.html')
    except TemplateNotFound:
        abort(404)

@main.route('/kim')
@main.route('/kim.html')
def kim():
    try:
        return render_template('public/kim.html')
    except TemplateNotFound:
        abort(404)

@main.route('/budaya')
@main.route('/budaya.html')
def budaya():
    try:
        return render_template('public/budaya.html')
    except TemplateNotFound:
        abort(404)

@main.route('/moap')
@main.route('/moap.html')
def moap():
    try:
        return render_template('public/moap.html')
    except TemplateNotFound:
        abort(404)

@main.route('/kebijakan')
@main.route('/kebijakan.html')
def kebijakan():
    try:
        return render_template('public/kebijakan.html')
    except TemplateNotFound:
        abort(404)

@main.route('/skm') #  Gak ada isi
@main.route('/skm.html')
def skm():
    try:
        return render_template('public/skm.html')
    except TemplateNotFound:
        abort(404)

# HUBUNGI KAMI

@main.route('/hubungi')
@main.route('/hubungi.html')
@main.route('/hubungi-kami.html')
@main.route('/Hubungi-Kami.html')
def hubungi_kami():
    try:
        return render_template('public/hubungi-kami.html')
    except TemplateNotFound:
        abort(404)

@main.route('/search')
@main.route('/search.html')
def search():
    try:
        return render_template('public/search.html')
    except TemplateNotFound:
        abort(404)

@main.route('/pip')
@main.route('/pip.html')
def pip():
    try:
        return render_template('public/pip.html')
    except TemplateNotFound:
        abort(404)
