# 处理身份验证路由
# app/auth/views.py

from flask import jsonify, request, Blueprint
from . import auth
from app.utils.response import ApiResponse
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return ApiResponse.success(data={"username": username}, message="Login successful")
    else:
        return ApiResponse.error(message="Invalid username or password")

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # 这里可以插入数据库保存用户的逻辑
    # 假设注册成功
    return jsonify({"message": "注册成功", "status": "success"}), 201
