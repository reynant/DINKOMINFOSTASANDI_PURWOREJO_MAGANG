# app/__init__.py
import os
import datetime
from flask import Flask
from .db import close_db
from .config import Config  # <-- Impor kelas Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # <-- Muat konfigurasi dari objek

    # Pastikan direktori UPLOAD_FOLDER ada
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    @app.context_processor
    def inject_now():
        return {'now': datetime.datetime.utcnow}

    # Import & register blueprint
    from .public.routes import public_bp
    from .admin.routes import admin_bp
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Tutup koneksi DB tiap request selesai
    @app.teardown_appcontext
    def teardown_db(exception):
        close_db()

    app.permanent_session_lifetime = datetime.timedelta(hours=1)

    return app