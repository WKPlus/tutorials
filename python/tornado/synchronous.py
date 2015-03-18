import tornado.ioloop
import tornado.web
import time
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        t1 = time.time()
        time.sleep(2)
        t2 = time.time()
        self.write(json.dumps({'t1': t1, 't2': t2}))


application = tornado.web.Application(
    [
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

