import json

import demjson
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView

from rcw.models import User
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
                where = where & Q(education=education)
            if major:
                where = where & Q(major=major)
            if username:
                where = where & Q(username=username)

            ## 关键词搜索 TODO

            if sort == '-id':
                datas = User.objects.filter(where).order_by("-add_time")
            if sort == '+id':
                datas = User.objects.filter(where).order_by("add_time")
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
            for i in datas:
                if i.config and eval(i.config):
                    config = eval(i.config)
                if config['form']['major']:
                    if config['form']['major'] not in major_list:
                        major_list.append(config['form']['major'])
                    data.append({
                        'username': i.username,
                        'img': str(i.img),
                        'phone': i.phone,
                        'email': i.email,
                        'type': i.type,
                        'id': i.id,
                        'config': demjson.decode(i.config) if i.config else [],
                        'education': i.education,
                        'name': i.username,
                        'date0': i.date0,
                        'date1': i.date1,
                        'major': i.major,
                        'workYear': i.workYear,
                        'city': i.city,
                        'address': i.address,
                        'age': i.age,
                        'myCotent': i.myCotent,
                        'statu': i.statu,
                        'expect': i.expect,
                        'sex': i.sex,
                        'sureWorks': i.sureWorks,
                        "add_time": i.add_time.strftime("%Y-%m-%d")

                    })
            #     data.append({"name": i.username, "email": i.email, "config": config,
            #                  "education": config['form']['education'],
            #                  "name_zh": config['form']['name'],
            #                  "major": config['form']['major'],
            #                  "sex": config['form']['sex'],
            #                  "age": config['form']['age'],
            #                  "workYear": config['form']['workYear'],
            #                  "statu": config['statu'],
            #                  "myContent": config['myCotent'],
            #                  "sureWorks": config['sureWorks'],
            #                  "expect": config['expect'],
            #                  "add_time": i.add_time.strftime("%Y-%m-%d")
            #                  # %H:%M:%S"add_time": i.add_time.strftime("%Y-%m-%d %H:%M:%S" )
            #                  })
            # data.append({'major_list': major_list})
            return JsonResponse({'code': 200, 'msg': '查询成功', 'data': data, "major_list": major_list})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'msg': '查询失败 %s' % e, 'data': ''})
