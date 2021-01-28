# _*_coding: utf-8 _*
# @Time ：2020/9/9 21:17
# @Author: AsenLi

# 导入两个包使用

import requests as req

# data = req.post("http://127.0.0.1:8000/register", data={"username": "yujia1",
#                                                         "password1":"ldb886718959",
#                                                         "password2":"ldb886718959",
#                                                         "phone":"18000581752",
#                                                         "email":"634163114@qq.com"
#                                                         })
# print(data.json())
# data = req.post("http://127.0.0.1:8000/login/", data={"passowrd": "admin8888,","username":"admin" })
# print(data.json())
# #
# # data = req.post("http://127.0.0.1:8000/userinfo/", json={"config": {"a":2},"user_id": 4})
# # print(data.json())
#
# # data = req.get("http://127.0.0.1:8000/userinfo/?id=2")
# # print(data.json())
# # data = req.get("http://127.0.0.1:8000/position/")
# # print(data.json())
# #
# # data = req.post("http://127.0.0.1:8000/position/", json={
# #     "name": "python开发",
# #     "salary": "10k-15k",
# #     "experience": "1-3年",
# #     "education": "本科",
# #     "keyword": "爬虫 web"
# # })
# # print(data.json())
#
# # a = [
# #     {"id": 0,
# #      "data":
# #          [
# #              {"id": 0, "title": "标题", "name": "名称"},
# #              {"id": 1, "title": "标题", "name": "名称"},
# #              {"id": 2, "title": "标题", "name": "名称"},
# #              {"id": 3, "title": "标题", "name": "名称"},
# #          ],
# #      "links": [
# #          {"id": 0, "title": "标题", "to": 0, "from": 1},
# #          {"id": 1, "title": "标题", "to": 2, "from": 4}
# #      ]
# #      },
# #     {"id": 1,
# #      "data":
# #          [
# #              {"id": 0, "title": "标题", "name": "名称"},
# #              {"id": 1, "title": "标题", "name": "名称"},
# #              {"id": 2, "title": "标题", "name": "名称"},
# #              {"id": 3, "title": "标题", "name": "名称"}
# #          ],
# #      "links": [
# #          {"id": 0, "title": "标题", "to": 0, "from": 1},
# #          {"id": 1, "title": "标题", "to": 2, "from": 3}
# #      ]
# #      },
# #     {"id": 2,
# #      "data":
# #          [
# #              {"id": 0, "title": "标题", "name": "名称"},
# #              {"id": 1, "title": "标题", "name": "名称"},
# #              {"id": 2, "title": "标题", "name": "名称"}
# #          ],
# #      "links": [
# #          {"id": 0, "title": "标题", "to": 0, "from": 1},
# #          {"id": 1, "title": "标题", "to": 2, "from": 2}
# #      ]
# #      }
# # ]
# #
# # print(a)
#
# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "Hello, World!"
#
# app.run()

# [{"checkboxGroup2": [], "name": "", "tag": "22", "dept": "无线", "vocation": "python", "date1": "2019-01-28", "cotent": "2"}]

# {"form": {"education": "", "name": "", "date0": "", "date1": "", "major": "", "workYear": 0, "mobile": "", "city": "", "sex": "", "email": "", "address": "", "age": ""}, "myCotent": "<p>熟悉网络编程，了解HTTP/TCP/UDP等网络协议、Ajax等开发技术；</p><p>熟悉python多线程，多进程开发；</p><p>熟练运用web 开发框架Django、flask开发框架；</p><p>熟练使用MySQL数据库，非关系型数据库Redis、MongoDB的使用;</p><p>熟悉vue、Bootstrap、HTML5、CSS、AJAX等前端;</p><ol><li>了解docker、odoo；</li></ol>", "statu": "", "expect": "", "sureWorks": [{"checkboxGroup2": [], "name": "", "tag": "22", "dept": "无线", "vocation": "python", "date1": "2019-01-28", "cotent": "2"}]}


import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from websocket import create_connection

# websocket-client
# 通过socket路由访问
now = datetime.datetime.now()
print(now)


def send_query_webSocket():
    ws = create_connection("ws://192.168.1.2:5000/test")
    result_1 = ws.recv()  # 接收服务端发送的连接成功消息
    print(result_1)
    """
    上面recv()方法接收服务端 发送的第一条消息：ws.send(str("message test!"))  # 回传给clicent
    下面再要接收消息，必须先给服务端发送一条消息，不然服务端message = ws.receive() 的receive方法
    没有收到消息，而这里直接调用rece()方法去接收服务端消息，则会导致服务端关闭此次连接；
    底层方法介绍：Read and return a message from the stream. If `None` is returned, then
        the socket is considered closed/errored.
    虽然此次连接关闭了，但是对于客户端来说并不知情，而客户端recv()方法又是一个阻塞方式运行，所以会导致
    客户端永远阻塞在这里无法关闭，这也是flask_sockets 客户端服务端交互的一个缺点吧。
    """
    ws.send("1")
    result = ws.recv()
    print(result)
    ws.close()
    return True


if __name__ == '__main__':
    send_query_webSocket()

