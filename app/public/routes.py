from flask import Blueprint, render_template

# bikin blueprint
public_bp = Blueprint('public', __name__, template_folder='templates')

# route halaman utama
@public_bp.route('/')
def index():
    return render_template('index.html')

@public_bp.route('/profil')
def profil():
    return render_template('profil.html')

@public_bp.route('/news')
def news():
    return render_template('news.html')

@public_bp.route('/galeri')
def galeri():
    return render_template('galeri.html')

@public_bp.route('/video')
def video():
    return render_template('video.html')

@public_bp.route('/hoaks')
def hoaks():
    return render_template('hoaks.html')

@public_bp.route('/download')
def download():
    return render_template('download.html')

@public_bp.route('/agenda')
def agenda():
    return render_template('agenda.html')

@public_bp.route('/layanan')
def layanan():
    return render_template('layanan.html')

@public_bp.route('/ppid')
def ppid():
    return render_template('ppid.html')

@public_bp.route('/spbe')
def spbe():
    return render_template('spbe.html')

@public_bp.route('/kebijakan')
def kebijakan():
    return render_template('kebijakan.html')

@public_bp.route('/skm')
def skm():
    return render_template('skm.html')

@public_bp.route('/hubungi')
def hubungi():
    return render_template('hubungi.html')

@public_bp.route('/search')
def search():
    return render_template('search.html')
