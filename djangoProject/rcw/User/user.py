# _*_coding: utf-8 _*
# @Time ：2020/10/11 15:04
# @Author: AsenLi
# 简历相关
import json

import demjson
from django.http import JsonResponse
from rest_framework.views import APIView

from rcw.models import User
import jwt


class UserInfo(APIView):
    def get(self, request):
        """
        个人信息
        config ： 简历信息 注册时间
        :param request:
        :return:
        """
        data = request.GET
        try:
            token = request.META.get("HTTP_X_TOKEN", None)
            # 检查
            salt = 'ssasdgf14sd4s5gf4s5s4fs'
            payload = None
            msg = 'token有效'
            payload = jwt.decode(token, salt, True)
            obj = User.objects.get(id=payload['user_id'])
            if obj:
                res = {
                    'username': obj.username,
                    'img': str(obj.img),
                    'phone': obj.phone,
                    'email': obj.email,
                    'type': obj.type,
                    'id': obj.id,
                    'config': demjson.decode(obj.config) if obj.config else []
                }
                return JsonResponse({'code': 200, 'msg': '', 'data': res})
            return JsonResponse({'code': 500, 'msg': "用户不存在", 'data': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'msg': '%s' % e, 'data': ''})

    def post(self, request):
        """
        个人信息里面 新增简历 {}
        :param request:
        :return:
        """
        data = request.data
        # id = data.get('user_id')
        phone = data.get('phone', None)
        email = data.get('email', None)
        username = data.get('username', None)
        try:
            if 'config' in data:
                config = data.get("config")


                token = request.META.get("HTTP_X_TOKEN", None)
                salt = 'ssasdgf14sd4s5gf4s5s4fs'
                payload = jwt.decode(token, salt, True)
                user_id = payload['user_id']
                obj = User.objects.filter(id=user_id)
                if obj:
                    obj.update(config=config)
                    obj.update(phone=phone)
                    obj.update(email=email)
                    obj.update(username=username)
                    return JsonResponse({'code': 200,'status': True, 'msg': '修改成功'})
                return JsonResponse({'code': 500,'status': False, 'msg': '用户不存在'})
            return JsonResponse({'code': 500,'status': False, 'msg': '缺少config'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': False, 'msg': '%s' % e})




#     // 要发送多次请求  把列表 变成了字段传到后台？？？？？？？？？？？？？？  前段里面搜索 这个