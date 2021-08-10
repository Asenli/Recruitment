from app import create_app

from config import Config
app = create_app("develop")
# from gevent import monkey
# from gevent.pywsgi import WSGIServer
# # 下面这句不加也能启动服务，但是你会发现Flask还是单线程，在一个请求未返回时，其他请求也会阻塞，所以请添加这句
# monkey.patch_all()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=Config.SERVICE_PORT)
    # http_server = WSGIServer(('0.0.0.0', Config.SERVICE_PORT), app)
    # http_server.serve_forever()


"""
cd flaskCwq
docker build -t flask_test .
docker run -p 10005:80 -d flask_test:latest

"""