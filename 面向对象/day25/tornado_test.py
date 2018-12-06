# -*- coding: utf-8 -*-
# Time    : 2018/12/5 16:34
# Author  : NeoBY
# Email   : baiyangbbyy@163.com
# File    : tornado_test.py
# Software: PyCharm
"""
通过tornado示例演示单例模式
"""


import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        import time

        self.write(str(time.localtime()))

application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

