from flask import jsonify


def json_response(code=200, msg="success", data=None, status=True):
    "返回格式化JSON"
    if data is None:
        return jsonify({"code": code, "msg": msg, "data": [], "status": status})
    return jsonify({"code": code, "msg": msg, "data": data, "status": status})


def key_check(data, keys):
    "检查json的key是否完备"
    for key in keys:
        if key not in data.keys():
            return False, key
    return True, None
