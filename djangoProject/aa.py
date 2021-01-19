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

import paramiko

# 49.232.202.208  22

# import paramiko  # 此模块用于连接虚拟机,ansible底层用此模块
#
# hostname = '49.232.202.208'
# port = 22
# username = 'root'
# password = '886718959ldb,'
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 忽略know_hosts文件
# ssh.connect(hostname=hostname, port=port, username=username, password=password)
# while True:
#     cmd = input('====>:')
#     stdin, stdout, stderr = ssh.exec_command(cmd)
#     print(stdout.read().decode('utf-8'))


import paramiko

hostname = '49.232.202.208'
port = 22
username = 'root'
password = '886718959ldb,'
t = paramiko.Transport((hostname, port))  # ftp
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(r'C:\Users\Administrator\Desktop\Recruitment\djangoProject\aa.py', '/home/aa.py')
# sftp.get('/home/python2.7.tar', r'C:\Users\Administrator\Desktop\test\python2.7.tar' )
sftp.close()

# import paramiko
#
# nimei = paramiko.Transport(('192.168.206.140', 22))
# nimei.connect(username='root', password='123456')
# p = paramiko.SFTPClient.from_transport(nimei)
# p.put(r'C:\Users\yhy\Desktop\1.txt', '/root/chedan2')  # 上传文件到远程机
