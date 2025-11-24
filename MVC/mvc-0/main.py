from tornado import ioloop, httpserver
from tornado.web import Application

from controllers.produto_controller import index, Novo, Delete, Atualizar

class RunApp(Application):
    def __init__(self):
        handlers = [
            ('/', index),
            ('/produto/novo', Novo),
            (r'/delete/(\d+)', Delete),
            (r'/produto/atualizar/(\d+)/status/(\d+)', Atualizar),
        ]

        settings = dict(
            debug = True,
            template_path = 'views',
            static_path = 'static',
        )

        Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    ioloop.IOLoop.instance().start()