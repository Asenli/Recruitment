# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
#
#
# from tornado import httpserver
# from tornado import ioloop
# from tornado import web
# # 开启多进程
# from multiprocessing import Pool
#
#
# class TestHandler(web.RequestHandler):
#     # 允许跨域，否则报错
#     def set_default_headers(self):
#         self.set_header("Access-Control-Allow-Origin", "*")
#         self.set_header("Access-Control-Allow-Headers", "Content-Type")
#         self.set_header("Access-Control-Allow-Methods", "POST,GET,OPTIONS")
#
#     def get(self):
#         self.write("Hello, World!")
#
#
# def main(port):
#     application = web.Application([
#         (r"/", TestHandler),
#     ])
#     server = httpserver.HTTPServer(application)
#     server.listen(port)  # 单进程开启
#     # server.bind(port)
#     # server.start(3) # 方法指定开启几个进程，默认cpu核数
#     ioloop.IOLoop.instance().start()
#
#
# if __name__ == "__main__":
#     p = Pool(3)
#     for port in range(9000, 9002):
#         p.apply_async(main, args=(port,))
#     p.close()
#     p.join()



import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(21985)
    tornado.ioloop.IOLoop.current().start()