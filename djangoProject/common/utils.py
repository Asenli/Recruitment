# _*_coding: utf-8 _*
# @Time ：2020/9/1 23:18
# @Author: AsenLi


# 导入加密库
import hashlib

# 加密方法
from random import Random

# 定义jwt 返回格式
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "code": 200,
        "msg": "登录成功",
        "data": {
            "id": user.id,
            "username": user.username,
            "token": token
        }
    }



# def make_password(mypass):
#     # md5 算法
#     mypass = hashlib.md5()
#     # 对字符串进行编译(加密操作)
#     mypass.update('sanjin'.encode(encoding='utf-8'))
#     # 返回密文
#     return mypass.hexdigest()


# 随机生成验证码
def random_str(randomlength=6):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
