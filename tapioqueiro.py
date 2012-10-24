import tornado.ioloop
from tornado.httpserver import HTTPServer

from tapioca import TornadoRESTful, ResourceHandler


class ProjectsHandler(ResourceHandler):

    def get_collection(self, callback, *args, **kwargs):
        callback([])

    def get_model(self, key, *args, **kwargs):
        """Gets an model instance"""
        return {}

    def update_model(self, key, *args, **kwargs):
        self.application.db.users.update(key, self.values)


class CommentsHandler(ResourceHandler):

    def delete_model(self, key, *args, **kwargs):
        pass


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    main_loop = tornado.ioloop.IOLoop.instance()

    api = TornadoRESTful(
            version='', base_url='http://127.0.0.1:{:d}'.format(port), discovery=True)
    api.add_resource('projects', ProjectsHandler)
    api.add_resource('comments', CommentsHandler)
    application = tornado.web.Application(api.get_url_mapping())

    server = HTTPServer(application)
    server.bind(port, '127.0.0.1')
    server.start(1)
    main_loop.start()
