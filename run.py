
from app import create_app

# 创建应用实例
app = create_app()

if __name__ == '__main__':
    # 启动 Flask 开发服务器
    app.run(debug=True)
