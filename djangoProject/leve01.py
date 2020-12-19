import json

import requests as rq



headers2 = {
    "Host":"level01-tech.com",
    "Proxy-Connection": "close",
    "Content-Length": "258",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y35A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36"
    # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarysA8jneYIJ8Z6n0vM"
}

print(rq.get('https://level01-tech.com', headers=headers2,verify=False))
# session = rq.Session()
# session.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
# session.get(url_login)
# token = session.cookies.get('csrftoken')
# print(token)




# url = 'https://level01-tech.com/user?lang=cn'
# s = rq.Session()
# s.keep_alive = False
# rts = rq.get(url)
# print(rts.json())

# "https://level01-tech.com/user?act=act_login"
# "https://level01-tech.com/user?lang=cn"
#
# ------WebKitFormBoundary2uHmBIfFPAgq7Yv0
# Content-Disposition: form-data; name="user_name"
#
# 18000581752
# ------WebKitFormBoundary2uHmBIfFPAgq7Yv0
# Content-Disposition: form-data; name="password"
#
# ldb886718959
# ------WebKitFormBoundary2uHmBIfFPAgq7Yv0--
