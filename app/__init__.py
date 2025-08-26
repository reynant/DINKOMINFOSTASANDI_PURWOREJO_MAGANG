import os
import mysql.connector
from flask import (Flask, redirect, url_for, session,
                   request, render_template)
from werkzeug.security import check_password_hash

# Impor blueprint 'main' dan 'admin'
from .routes import main as main_blueprint
from .admin.routes import admin as admin_blueprint

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi."""
    app = Flask(__name__)
    app.secret_key = 'ganti-dengan-kunci-rahasia-yang-kuat-dan-unik'

    # --- Konfigurasi Koneksi MySQL ---
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'web_kominfo'
    app.config['UPLOAD_FOLDER'] = 'static/favicon'

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    def get_db():
        """Fungsi helper untuk koneksi ke database MySQL."""
        return mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )

    # --- Daftarkan Blueprint ---
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app