from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.auth import auth
from .auth.views import auth_bp
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # 创建 Flask 应用
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(Config)  # 从 Config 类中加载配置

    # 初始化数据库和数据库迁移
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝本
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
