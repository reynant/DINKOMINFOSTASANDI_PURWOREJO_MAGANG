import os
from flask import Flask

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi (Application Factory)."""
    
    # --- PERBAIKAN UTAMA DI SINI ---
    # Beri tahu Flask bahwa folder 'templates' ada satu tingkat di atas folder 'app'
    app = Flask(__name__, template_folder='../templates')
    
    # Atur konfigurasi dasar
    app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-yang-kuat'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'db_dinkominfostasandi' # Nama DB sudah diperbarui
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

    # Pastikan folder upload ada
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Impor blueprint dari lokasi yang benar di dalam fungsi create_app
    from .public.routes import public_bp
    from .admin.routes import admin

    # Daftarkan blueprint ke aplikasi
    app.register_blueprint(public_bp)
    app.register_blueprint(admin, url_prefix='/admin')

    return app