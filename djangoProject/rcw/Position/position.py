# _*_coding: utf-8 _*
# @Time ：2020/10/14 23:08
# @Author: AsenLi
from django.http import JsonResponse
from rest_framework.views import APIView

from rcw import models


class Position(APIView):
    def get(self, request):
        """
        获取简历列表
        """
        pass
        res = []
        try:
            all = models.Position.objects.all()
            for postion in all:
                res.append({
                    "name": postion.name,
                    "salary": postion.salary,
                    "experience": postion.experience,
                    "education": postion.education,
                    "keyword": postion.keyword,
                    "company": postion.company,
                    "add_time": postion.add_time.strftime('%Y-%m-%d')
                })
            return JsonResponse({"code": 200, 'status': True, 'msg': '查询成功', 'data': res})
        except Exception as e:
            return JsonResponse({"code": 500, 'status': False, 'msg': '查询失败', 'data': []})

    def post(self, request):
        """
        新增职位
        """

        data = request.data
        name = data.get('name')
        city = data.get('city')
        salary = data.get('salary')
        experience = data.get('experience')
        education = data.get('education')
        fuli = data.get('fuli')
        company = data.get('company')
        try:
            models.Position.objects.create(name=name, salary=salary, experience=experience, education=education,
                                           fuli=fuli,
                                           company=company)
            return JsonResponse({"code": 200, 'status': True, 'msg': '新增成功'})
        except Exception as e:
            print(e)
            return JsonResponse({"code": 500, 'status': False, 'msg': '%s' % e})
