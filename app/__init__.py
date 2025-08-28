import os
from flask import Flask
# Hapus import yang salah di sini

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi (Application Factory)."""
    app = Flask(__name__)
    
    # Atur konfigurasi dasar
    # (Sangat disarankan untuk memindahkannya ke file config.py seperti saran sebelumnya)
    app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-yang-kuat'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'db_dinkominfostasandi'
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads' # Nama folder yang lebih umum

    # Pastikan folder upload ada
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # --- PERBAIKAN UTAMA ADA DI SINI ---# app/__init__.py

import os
from flask import Flask

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi (Application Factory)."""
    app = Flask(__name__)
    
    # ... (kode konfigurasi Anda) ...
    app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-yang-kuat'
    # ... (dan konfigurasi lainnya) ...

    # Pastikan folder upload ada
    if not os.path.exists(app.config.get('UPLOAD_FOLDER', 'app/static/uploads')):
        os.makedirs(app.config.get('UPLOAD_FOLDER', 'app/static/uploads'))

    # Impor blueprint dari lokasi yang benar di dalam fungsi create_app
    from .public.routes import public_bp
    from .admin.routes import admin  # Ganti 'admin_bp' menjadi 'admin'

    # Daftarkan blueprint ke aplikasi
    app.register_blueprint(public_bp)
    app.register_blueprint(admin, url_prefix='/admin') # Ganti 'admin_bp' menjadi 'admin'

    return app
    # Impor blueprint dari lokasi yang benar di dalam fungsi create_app
    from .public.routes import public_bp
    from .admin.routes import admin

    # Daftarkan blueprint ke aplikasi
    app.register_blueprint(public_bp)
    app.register_blueprint(admin, url_prefix='/admin')

    return app