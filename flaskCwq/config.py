import os
root_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
    "基础配置"
    SERVICE_IP = "0.0.0.0"
    SERVICE_PORT = 8000

    ROOT_DIR = root_dir
    #数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@%s/rcw" % os.getenv("MYSQL_ADDR","211.149.185.232:3306")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 安全key
    SECRET_KEY = "nL32qo3jejJ#oaitOe@aw"
    API_TOKEN_LIFETIME = 10800

config = {
    "develop": Config,
    "deploy": Config,
    "default": Config,
    "start_develop": "develop"
}