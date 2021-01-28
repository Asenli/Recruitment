import json

import demjson
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView

from rcw.models import User, UserConfig
import jwt


class AllInfo(APIView):
    def get(self, request):
        """
        获取全部人信息

        :param request:
        :return:
        """
        try:
            requests_data = request.GET['params']
            requests_data = json.loads(requests_data)
            # 分页
            page = requests_data.get('page')
            limit = requests_data.get('limit')
            # 状态
            statu = requests_data.get('importance')
            # 学历
            education = requests_data.get('importance2')
            # 专业
            major = requests_data.get('importance3')
            # 姓名
            username = requests_data.get('name')
            # 排序
            sort = requests_data.get('sort')
            where = Q()
            if statu:
                where = Q(statu=statu)
            if education:
                where = where & Q(education__icontains=education)
            if major:
                where = where & Q(major__icontains=major)
            if username:
                where = where & Q(name__icontains=username)

            ## 关键词搜索 TODO

            if sort == '-id':
                # datas = User.objects.filter(where).order_by("-add_time")
                user_data = UserConfig.objects.filter(where).order_by("-add_time").all()
            if sort == '+id':
                user_data = UserConfig.objects.filter(where).order_by("add_time").all()
                # datas = User.objects.filter(where).order_by("add_time")
            # data = [i for i in datas]
            data = []
            config = {
                "form": {
                    "education": "",
                    "name": "",
                    "major": "",
                    "sex": "",
                    "age": "",
                    "statu": "",
                    "workYear": ""
                },
                "statu": '',
                "myCotent": '',
                "sureWorks": '',
                "expect": ''

            }
            # 专业列表
            major_list = []
            for userConfigs in user_data:
                user_info = User.objects.filter(id=userConfigs.user_id).first()
                if userConfigs:
                    if userConfigs.major not in major_list:
                        major_list.append(userConfigs.major)
                    # if config['form']['major'] not in major_list:
                    #     major_list.append(config['form']['major'])
                    data.append({
                        'username': userConfigs.name,
                        'img': '',
                        'phone': userConfigs.mobile,
                        'email': userConfigs.email,
                        'type': '',
                        'id': userConfigs.id,
                        'user_id': userConfigs.user_id,
                        'config': demjson.decode(user_info.config) if user_info.config else [],
                        'education': userConfigs.education,
                        'name': userConfigs.name,
                        'date0': userConfigs.date0,
                        'date1': userConfigs.date1,
                        'major': userConfigs.major,
                        'workYear': userConfigs.workYear,
                        'city': userConfigs.city,
                        'address': userConfigs.address,
                        'age': userConfigs.age,
                        'myCotent': userConfigs.myCotent,
                        'statu': userConfigs.statu,
                        'expect': userConfigs.expect,
                        'sex': userConfigs.sex,
                        'sureWorks': userConfigs.sureWorks,
                        "add_time": userConfigs.add_time.strftime("%Y-%m-%d")

                    })
            return JsonResponse({'code': 200, 'msg': '查询成功', 'data': data, "major_list": major_list})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'msg': '查询失败 %s' % e, 'data': ''})
