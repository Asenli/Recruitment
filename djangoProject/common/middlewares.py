# coding=utf-8
from django.http import JsonResponse
import jwt


# 前端登录后全局保存token 每个请求前在header里面添加AUTHORIZATION token
# 中间键 用于在每个请求前 判断header里面是否有token 并验证token是否过期
def auth_middleware(get_response):
    def middleware(request):
        token = request.META.get('HTTP_X_TOKEN', None)
        if request.path != '/login' and request.path != '/register/' and request.path != '/repeat_pwd/':
            if not token:
                return JsonResponse({'code': 1003, 'msg': 'need token'})
            # 检查
            salt = 'ssasdgf14sd4s5gf4s5s4fs'
            payload = None
            msg = 'token有效'
            try:
                payload = jwt.decode(token, salt, True)
            except jwt.exceptions.ExpiredSignatureError:
                msg = 'token已失效'
            except jwt.DecodeError:
                msg = 'token认证失败'
            except jwt.InvalidTokenError:
                msg = '非法的token'
            if not payload:
                return JsonResponse({'code': 1003, 'msg': msg,
                                     'data': {"token": '', "id": '', "username": ''}})
        response = get_response(request)
        return response

    return middleware
