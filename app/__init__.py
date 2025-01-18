# app/__init__.py

from flask import Flask
from app.auth import auth

def create_app():
    app = Flask(__name__)

    # 配置应用，加载配置文件
    app.config.from_object('config')

    # 注册蓝本
    app.register_blueprint(auth, url_prefix='/auth')

    return app
