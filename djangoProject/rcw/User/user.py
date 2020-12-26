# _*_coding: utf-8 _*
# @Time ：2020/10/11 15:04
# @Author: AsenLi
# 简历相关
import json
import os

import demjson
from django.http import JsonResponse
from rest_framework.views import APIView

from djangoProject.settings import PROJECT_ROOT
from rcw.models import User, Roles
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
                    'config': demjson.decode(obj.config) if obj.config else [],
                    'education': obj.education,
                    'name': obj.username,
                    'date0': obj.date0,
                    'date1': obj.date1,
                    'major': obj.major,
                    'workYear': obj.workYear,
                    'city': obj.city,
                    'address': obj.address,
                    'age': obj.age,
                    'myCotent': obj.myCotent,
                    'statu': obj.statu,
                    'expect': obj.expect,
                    'sex': obj.sex,
                    'sureWorks': obj.sureWorks
                }
                role_name = Roles.objects.filter(user_id=obj.id).first()
                if not role_name:
                    return JsonResponse({'code': 500, 'msg': "用户未绑定角，请联系管理员", 'data': ''})
                role_name = role_name.name
                res['roles'] = role_name
                # 获取菜单权限
                # os.path.join(dir, 'admin.json')

                path = os.path.abspath('utils') + '\\menu\\' + '{}.json'.format(role_name)
                menus = []
                if not os.path.exists(path):
                    menus = []
                else:
                    try:
                        # 获取菜单列表json
                        with open(os.path.join(path), 'r', encoding='utf-8') as f:
                            menus = json.load(f)
                    except Exception as e:
                        print(e)
                res['menus'] = menus
                print(res)
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
        phone = data.get('phone', None)
        email = data.get('email', None)
        education = data.get('education', None)
        name = data.get('name', None)
        date0 = data.get('date0', None)
        date1 = data.get('date1', None)
        workYear = data.get('workYear', None)
        major = data.get('major', None)
        city = data.get('city', None)
        sex = data.get('sex', None)
        address = data.get('address', None)
        age = data.get('age', None)
        statu = data.get('statu', None)
        myCotent = data.get('myCotent', None)
        expect = data.get('expect', None)
        sureWorks = data.get('sureWorks', None)
        try:
            if 'config' in data:
                config = data.get("config")

                token = request.META.get("HTTP_X_TOKEN", None)
                salt = 'ssasdgf14sd4s5gf4s5s4fs'
                payload = jwt.decode(token, salt, True)
                user_id = payload['user_id']
                obj = User.objects.filter(id=user_id)
                if obj:
                    if config:
                        obj.update(config=config)
                    if education:
                        obj.update(education=education)
                    if phone:
                        obj.update(phone=phone)
                    if email:
                        obj.update(email=email)
                    if name:
                        obj.update(username=name)
                    if date0:
                        obj.update(date0=date0)
                    if date1:
                        obj.update(date1=date1)
                    if major:
                        obj.update(major=major)
                    if workYear:
                        obj.update(workYear=workYear)
                    if city:
                        obj.update(city=city)
                    if sex:
                        obj.update(sex=sex)
                    if address:
                        obj.update(address=address)
                    if age:
                        obj.update(age=age)
                    if statu:
                        obj.update(statu=statu)
                    if myCotent:
                        obj.update(myCotent=myCotent)
                    if expect:
                        obj.update(expect=expect)
                    if sureWorks:
                        obj.update(sureWorks=sureWorks)
                    return JsonResponse({'code': 200, 'status': True, 'msg': '修改成功'})
                return JsonResponse({'code': 500, 'status': False, 'msg': '用户不存在'})
            return JsonResponse({'code': 500, 'status': False, 'msg': '缺少config'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': False, 'msg': '%s' % e})

#     // 要发送多次请求  把列表 变成了字段传到后台？？？？？？？？？？？？？？  前段里面搜索 这个
