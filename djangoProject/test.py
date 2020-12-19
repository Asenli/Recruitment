# _*_coding: utf-8 _*
# @Time ：2020/9/9 21:17
# @Author: AsenLi

# 导入两个包使用

import requests as req

# data = req.post('http://127.0.0.1:8000/login/', data={"passowrd": 'admin8888,',"username":"admin" })
# print(data.json())

# data = req.post('http://127.0.0.1:8000/userinfo/', json={"config": {'a':2},'user_id': 4})
# print(data.json())

# data = req.get('http://127.0.0.1:8000/userinfo/?id=2')
# print(data.json())
# data = req.get('http://127.0.0.1:8000/position/')
# print(data.json())
#
# data = req.post('http://127.0.0.1:8000/position/', json={
#     'name': 'python开发',
#     'salary': '10k-15k',
#     'experience': '1-3年',
#     'education': '本科',
#     'keyword': '爬虫 web'
# })
# print(data.json())

# a = [
#     {"id": 0,
#      "data":
#          [
#              {"id": 0, "title": "标题", "name": "名称"},
#              {"id": 1, "title": "标题", "name": "名称"},
#              {"id": 2, "title": "标题", "name": "名称"},
#              {"id": 3, "title": "标题", "name": "名称"},
#          ],
#      "links": [
#          {"id": 0, "title": "标题", "to": 0, "from": 1},
#          {"id": 1, "title": "标题", "to": 2, "from": 4}
#      ]
#      },
#     {"id": 1,
#      "data":
#          [
#              {"id": 0, "title": "标题", "name": "名称"},
#              {"id": 1, "title": "标题", "name": "名称"},
#              {"id": 2, "title": "标题", "name": "名称"},
#              {"id": 3, "title": "标题", "name": "名称"}
#          ],
#      "links": [
#          {"id": 0, "title": "标题", "to": 0, "from": 1},
#          {"id": 1, "title": "标题", "to": 2, "from": 3}
#      ]
#      },
#     {"id": 2,
#      "data":
#          [
#              {"id": 0, "title": "标题", "name": "名称"},
#              {"id": 1, "title": "标题", "name": "名称"},
#              {"id": 2, "title": "标题", "name": "名称"}
#          ],
#      "links": [
#          {"id": 0, "title": "标题", "to": 0, "from": 1},
#          {"id": 1, "title": "标题", "to": 2, "from": 2}
#      ]
#      }
# ]
#
# print(a)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run()