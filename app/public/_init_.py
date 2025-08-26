from flask import Flask
from app.public.routes import public_bp   # harus sesuai nama di routes.py

def create_app():
    app = Flask(__name__)
    app.register_blueprint(public_bp)     # harus sama juga
    return app
