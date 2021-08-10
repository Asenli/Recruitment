import json
import os

from utils.tools.web import json_response
from flask import g, request
from app import auth, permission_required, db
from app.models import User, Role
from . import api


@auth.verify_token
def verify_token(token):
    g.current_user = User.verity_auth_token(token)
    return g.current_user is not None


@auth.error_handler
def auth_error():
    return json_response(code=401, msg="unauthorized")


@permission_required("permission_name")
@api.route("/login", methods=["POST"])
def login_op():
    "登录"
    data = json.loads(request.data)
    if "username" not in data:
        return json_response(code=500, msg="no username")
    if "password" not in data:
        return json_response(code=500, msg="no password")
    obj = User.query.filter_by(username=data.get("username")).first()
    if obj is None:
        return json_response(code=500, msg="username error")
    if obj.verify_password(data.get("password")) is False:
        return json_response(code=500, msg="password error")
    userInfo = User.query.filter_by(id=obj.id).first()

    return json_response(data={"token": obj.generate_auth_token(), "id": obj.id, "username": obj.username
                                  })


@api.route("/logout", methods=["POST", "GET"])
@auth.login_required
def logout_op():
    return json_response()


@api.route("/info")
@auth.login_required
def info_op():
    "获取用户信息"
    pass


@api.route("/register", methods=["POST"])
# @auth.login_required
def register():
    "添加用户"
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    password2 = request.form.get("password2", None)
    role_id = request.form.get("role", None)
    if not username:
        return json_response(code=500, msg="need username")
    if not password:
        return json_response(code=500, msg="need to set password")
    if password != password2:
        return json_response(code=500, msg="two passwords is not same")
    try:
        if User.query.filter_by(username=username).first():
            return json_response(code=500, msg="username is exist")
        # print(User(id=100, username=username, password=password))
        db.session.add(User(username=username, password=password))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return json_response(code=500, msg="register error {}".format(e))
    return json_response()

@api.route("/edit", methods=["PUT"])
@auth.login_required
def edit():
    "修改用户名 密码"
    pass