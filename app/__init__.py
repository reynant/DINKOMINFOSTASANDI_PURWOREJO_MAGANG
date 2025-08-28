import os
import datetime
from flask import Flask

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi (Application Factory)."""
    
    # Membuat instance aplikasi Flask. 
    # Flask secara otomatis akan mencari folder 'templates' di direktori root, 
    # jadi kita tidak perlu menentukannya secara manual.
    app = Flask(__name__)
    
    # Atur konfigurasi dasar
    app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-yang-kuat'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'db_dinkominfostasandi'
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

    # Pastikan folder upload ada
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Menambahkan fungsi 'now' ke konteks template Jinja2
    # Ini diperlukan untuk menampilkan tahun di footer base.html
    @app.context_processor
    def inject_now():
        return {'now': datetime.datetime.utcnow}

    # Impor blueprint dari lokasi yang benar di dalam fungsi create_app
    from .public.routes import public_bp
    from .admin.routes import admin

    # Daftarkan blueprint ke aplikasi
    app.register_blueprint(public_bp)
    app.register_blueprint(admin, url_prefix='/admin')

    return app