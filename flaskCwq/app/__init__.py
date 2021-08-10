from config import config
from functools import wraps
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth

db = SQLAlchemy()

auth = HTTPTokenAuth(scheme="Token")


#创建app
def create_app(config_name):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config.from_object(config[config_name])
    db.init_app(app)
    from app.consumer_role.user import api as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/")

    return app


def permission_required(permission):
    "用户操作权限管理函数"
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if g.current_user is not None:
                if g.current_user.verify_permission(permission) is True:
                    return f(*args, **kwargs)
            return jsonify({"code": 500, "msg": "permission denied", "data": []})
        return decorated_function
    return decorator