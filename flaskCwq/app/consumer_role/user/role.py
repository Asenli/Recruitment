
from flask import request
from utils.tools.web import json_response
from app import auth
from app.models import Role
from . import api


@api.route("/role", methods=["GET"])
@auth.login_required
def info_role():
    num = int(request.args.get("num", default=1))
    size = int(request.args.get("size", default=10))
    data = Role.query.filter_by()
    res = []
    for obj in data.paginate(page=num,per_page=size).items:
        res.append({"id": obj.id, "name": obj.name})
    return json_response(data={"page": {"total": data.count(),"num": num,"size": size},"data":res})