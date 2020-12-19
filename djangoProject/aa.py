# import requests as rq
# url_login = "https://level01-tech.com/user?act=act_login"
# login_json = {'user_name': '18000581752', 'password': 'ldb886718959'}
# headers = {
#     "Host":"level01-tech.com",
#     "Connection": "keep-alive",
#     "Content-Length": "258",
#     "Accept":"application/json, text/javascript, */*; q=0.01",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y35A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
#     # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarysA8jneYIJ8Z6n0vM",
#     "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarynlRwzXrbA7LrYs8S",
#     "Cookie":"__cfduid=d716eee025f1434ab92356aeeda1933941606314382",
#     "Origin": "file://",
#     "Accept-Encoding": "Accept-Encoding",
#     "Accept-Language": "zh-CN,en-US;q=0.8",
#     "X-Requested-With": "com.levelone"
# }
# s = rq.Session()
# s.keep_alive = True
# login = rq.post(url_login, data=login_json,headers=headers,verify=False)
#
# print(login.json())

import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='49.232.202.208:9092')

producer.send('test', b"this is a python to kafka")

producer.close()


"""
docker run -dit --name mykafka1 --publish 9092:9092 --link zookeeper --env KAFKA_GROUP_ID=test_kafka1 --env KAFKA_BROKER_ID=1 --env KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 --env KAFKA_ADVERTISED_PORT=9092 --env KAFKA_ADVERTISED_HOST_NAME=kafka1 --volume /etc/localtime:/etc/localtime wurstmeister/kafka:latest

"""