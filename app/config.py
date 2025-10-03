# app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kunci-rahasia-default-untuk-development'
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'db_dinkominfostasandi_dummy')
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'static', 'uploads')