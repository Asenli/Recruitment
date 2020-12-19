import datetime
import json
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import JsonResponse
from jwt import exceptions
from rest_framework.views import APIView

from common.utils import random_str
from djangoProject.settings import EMAIL_HOST_USER
from rcw import models
from rcw.models import User
import jwt
import datetime


class Register(APIView):
    # 注册
    def post(self, request, *args, **kwargs):
        """
        注册
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            username = request.data.get('username')
            password = request.data.get('password1')
            password2 = request.data.get('password2')
            phone = request.data.get('phone')
            email = request.data.get('email')
            obj = models.User.objects.filter(username=username).first()
            if obj:
                return JsonResponse({'status': False, 'msg': '用户名已存在'})
            if email == "":
                # 验证邮箱
                return JsonResponse({'msg': '无效邮箱', 'status': False})
            if phone == "":
                # 验证邮箱
                return JsonResponse({'msg': '请填写正确手机号', 'status': False})
            if password == "":
                return JsonResponse({'msg': '请填写密码', 'status': False})
            if password != password2:
                return JsonResponse({'msg': '两次密码不一致', 'status': False})
            #
            user = User.objects.create(email=email, username=username, password=make_password(password), phone=phone)
            user.save()
            return JsonResponse({'msg': '注册成功', 'status': True})
        except Exception as e:
            ret = {'status': False, 'msg': ("请求异常: s%" % e)}
        return JsonResponse(ret)


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        """
        登录验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'msg': None}
        try:
            usr = request.data.get('username')
            pas = request.data.get('password')
            # 检查账户是否存在
            user = auth.authenticate(request, username=usr, password=pas)
            if not user:
                return JsonResponse({'code': 400, 'mes': '账户或密码错误'})
            salt = 'ssasdgf14sd4s5gf4s5s4fs'

            # 构造header
            headers = {
                'typ': 'jwt',
                'alg': 'HS256'
            }
            # 构造payload
            payload = {
                'user_id': user.id,  # 自定义用户ID
                'username': user.username,  # 自定义用户名
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)  # 超时时间30分钟
            }
            token = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers).decode('utf-8')
            print({'code': 200, 'msg': "成功",
                                 'data': {"token": token, "id": user.id, "username": user.username}
                                 })
            return JsonResponse({'code': 200, 'msg': "成功",
                                 'data': {"token": token, "id": user.id, "username": user.username}
                                 })
        except Exception as e:
            ret = {'code': 500, 'msg': "登录失败 %e" % e,
                   'data': {"token": '', "id": '', "username": ''}
                   }
            return JsonResponse(ret)

class AuthViewLoginOut(APIView):
    "退出"
    def post(self,request, *args, **kwargs):
        auth.logout(request)
        return JsonResponse({'code': 200, 'msg': "成功",'data': {}})

class FindpwdView(APIView):
    # 找回密码
    def get(self, request):
        """
        发送 验证码邮箱
        :param request:
        :return:
        """
        email = request.GET.get('email')
        email_title = "人才公会重置密码"
        code = random_str()  # 随机生成的验证码
        request.session["code"] = code  # 将验证码保存到session
        email_body = """
                  <table
        width="100%"
        style="box-sizing: border-box; font-size: 14px; margin: 0;">
        <tbody>
        <tr
          style=" box-sizing: border-box; font-size: 14px; margin: 0;">
          <td style="box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;"
              valign="top">
            您收到此邮件是因为您在人才公会申请了密码重置, 如果不是您申请的, 请忽略此邮件.
          </td>
        </tr>
        <tr
          style="box-sizing: border-box; font-size: 14px; margin: 0;">
          <td
            style="box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;"
            valign="top">
            若要开始重置密码, 输入验证码
          </td>
        </tr>
        <tr
          style="box-sizing: border-box; font-size: 14px; margin: 0;">
          <td itemprop="handler" itemscope="itemscope"
              style="box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;"
              valign="top">
            <el-button               style=" box-sizing: border-box; font-size: 14px; color: #FFF; text-decoration: none; line-height: 2em; font-weight: bold; text-align: center; cursor: pointer; display: inline-block; border-radius: 5px; text-transform: capitalize; background-color: #348eda; margin: 0; border-color: #348eda; border-style: solid; border-width: 10px 20px;"
            >验证码：{0}</el-button>
          </td>
        </tr>
        <tr
          style="box-sizing: border-box; font-size: 14px; margin: 0;">
          <td
            style="box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;"
            valign="top">
            — 人才公会
          </td>
        </tr>
        </tbody>
      </table>
        """.format(code)
        me = EMAIL_HOST_USER
        msg = MIMEMultipart()
        msg['Subject'] = email_title
        msg['From'] = me
        msg['To'] = email
        context = MIMEText(email_body, _subtype='html', _charset='utf-8')  # 解决乱码
        try:
            msg.attach(context)
            send_smtp = smtplib.SMTP()
            send_smtp.connect("smtp.qq.com")
            send_smtp.login('634163114@qq.com', "sgozhkwxoxajbdad")
            send_smtp.sendmail(me, email, msg.as_string())
            send_smtp.close()
            msg = "验证码已发送，请查收邮件"
            return JsonResponse({'status': True, 'msg': code})
        except Exception as e:
            print(e)
            return JsonResponse({'status': False, 'msg': e})

    def post(self, request):
        """
        修改密码 发送新密码 验证码
        :param request:
        :return:
        """
        email = request.data.get("email")
        code = request.data.get("code")  # 获取传递过来的验证码
        password = request.data.get("password1")  # 新密码
        # 支持手机号
        user = User.objects.get(email=email)
        msg = '验证码不正确'
        if not user:
            return JsonResponse({'status': False, 'msg': '邮箱不存在'})
        try:
            if code == request.session.get('code', default=None):
                user.password = make_password(password)
                user.save()
                del request.session["code"]  # 删除session
                msg = "密码已重置"
                return JsonResponse({'status': True, 'msg': msg})
            return JsonResponse({'status': False, 'msg': msg})
        except Exception as e:
            print(e)
            return JsonResponse({'status': False, 'msg': e})
