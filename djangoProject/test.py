# _*_coding: utf-8 _*
# @Time ：2020/9/9 21:17
# @Author: AsenLi

# 导入两个包使用

import requests as req

data = req.post("http://127.0.0.1:8000/register", data={"username": "yujia1",
                                                        "password1":"ldb886718959",
                                                        "password2":"ldb886718959",
                                                        "phone":"18000581752",
                                                        "email":"634163114@qq.com"
                                                        })
print(data.json())
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