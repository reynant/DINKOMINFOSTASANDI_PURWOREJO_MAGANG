import os
import datetime
from flask import Flask
from .db import close_db   # 🔥 tambahkan ini


def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key-here'

    # Konfigurasi DB
    app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-yang-kuat'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    # 🔥 pakai DB yang benar
    app.config['MYSQL_DB'] = 'db_dinkominfostasandi_dummy'
    app.config['UPLOAD_FOLDER'] = os.path.join(
        app.root_path, 'static', 'uploads')

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
