import json

import demjson
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
            page = requests_data.get('page')
            limit = requests_data.get('limit')
            importance = requests_data.get('importance')
            sort = requests_data.get('sort')
            if sort == '-id':
                datas = User.objects.all().order_by("-add_time")
            if sort == '+id':
                datas = User.objects.all().order_by("add_time")
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
            for i in datas:
                if eval(i.config):
                    config = eval(i.config)
                data.append({"name": i.username, "email": i.email, "config": config,
                             "education": config['form']['education'],
                             "name_zh": config['form']['name'],
                             "major": config['form']['major'],
                             "sex": config['form']['sex'],
                             "age": config['form']['age'],
                             "workYear": config['form']['workYear'],
                             "statu": config['statu'],
                             "myContent": config['myCotent'],
                             "sureWorks": config['sureWorks'],
                             "expect": config['expect'],
                             "add_time": i.add_time.strftime("%Y-%m-%d")
                             # %H:%M:%S"add_time": i.add_time.strftime("%Y-%m-%d %H:%M:%S" )
                             })
            return JsonResponse({'code': 200, 'msg': '查询成功', 'data': data})
            # token = request.META.get("HTTP_X_TOKEN", None)
            # # 检查
            # salt = 'ssasdgf14sd4s5gf4s5s4fs'
            # payload = None
            # msg = 'token有效'
            # payload = jwt.decode(token, salt, True)
            # obj = User.objects.get(id=payload['user_id'])
            # if obj:
            #     res = {
            #         'username': obj.username,
            #         'img': str(obj.img),
            #         'phone': obj.phone,
            #         'email': obj.email,
            #         'type': obj.type,
            #         'id': obj.id,
            #         'config': demjson.decode(obj.config) if obj.config else []
            #     }
            #     return JsonResponse({'code': 200, 'msg': '', 'data': res})
            # return JsonResponse({'code': 500, 'msg': "查询失败", 'data': ''})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'msg': '查询失败 %s' % e, 'data': ''})
