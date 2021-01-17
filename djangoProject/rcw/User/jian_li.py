from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from rcw.models import User, Roles, UserConfig


class JianLi(APIView):
    """
    保存简历信息
    """

    def post(self, request):
        data = request.data
        # id = data.get('id')
        education = data.get('education', None)
        name = data.get('username', None)
        date0 = data.get('date', None)
        date1 = data.get('date1', None)
        major = data.get('major', None)
        workYear = data.get('workYear', None)
        mobile = data.get('phone', None)
        city = data.get('city', None)
        sex = data.get('sex', None)
        address = data.get('address', None)
        age = data.get('age', None)
        email = data.get('email', None)
        expect = data.get('expect', None)
        statu = data.get('statu', None)
        myCotent = data.get('myCotent', None)
        sureWorks = data.get('sureWorks', None)

        token = request.META.get("HTTP_X_TOKEN", None)
        salt = 'ssasdgf14sd4s5gf4s5s4fs'
        payload = jwt.decode(token, salt, True)
        user_id = payload['user_id']
        try:
            obj = UserConfig.objects.filter(user_id=user_id)
            if obj:
                """
                更新
                """
                obj.update(
                    education=education,
                    name=name,
                    # date0=date0,
                    # date1=date1,
                    major=major,
                    workYear=workYear,
                    mobile=mobile,
                    city=city,
                    sex=sex,
                    address=address,
                    age=age,
                    email=email,
                    expect=expect,
                    statu=statu,
                    myCotent=myCotent,
                    sureWorks=sureWorks
                )
                return JsonResponse({'code': 200, 'status': True, 'msg': '修改成功'})
            else:
                config = UserConfig.objects.create(
                    user_id=user_id,
                    education=education,
                    name=name,
                    # date0=date0,
                    # date1=date1,
                    major=major,
                    workYear=workYear,
                    mobile=mobile,
                    city=city,
                    sex=sex,
                    address=address,
                    age=age,
                    email=email,
                    expect=expect,
                    statu=statu,
                    myCotent=myCotent,
                    sureWorks=sureWorks
                )
                config.save()
                return JsonResponse({'code': 200, 'status': True, 'msg': '修改成功'})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500,'status': False, 'msg': '%s' % e})

    def get(self, request):
        try:
            user_id = request.GET.get('user_id')
            if not user_id:
                return JsonResponse({'code': 1003, 'status': False, 'msg': '%s'})
            user_info = UserConfig.objects.filter(user_id=user_id).first()
            if user_info:
                data = {
                    "education": user_info.education,
                    "name": user_info.name,
                    "major": user_info.major,
                    "workYear": user_info.workYear,
                    "mobile": user_info.mobile,
                    "city": user_info.city,
                    "sex": user_info.sex,
                    "address": user_info.address,
                    "age": user_info.age,
                    "email": user_info.email,
                    "expect": user_info.expect,
                    "statu": user_info.statu,
                    "myCotent": user_info.myCotent,
                    "sureWorks": user_info.sureWorks
                }
            else:
                data = {
                    "education": '',
                    "name": '',
                    "major": '',
                    "workYear": 0,
                    "mobile": 0,
                    "city": 0,
                    "sex": '男',
                    "address": '',
                    "age": 0,
                    "email": '',
                    "expect": '',
                    "statu": '',
                    "myCotent": '',
                    "sureWorks": []
                }
            return JsonResponse({'code': 200, 'msg': '查询成功','status': True, 'data': data})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'status': False, 'msg': '%s' % e})