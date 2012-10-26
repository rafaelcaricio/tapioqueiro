import tornado.ioloop
from tornado.httpserver import HTTPServer

from tapioca import TornadoRESTful, ResourceHandler, validate


class ProjectsHandler(ResourceHandler):

    @validate(querystring={'name': (unicode, 'name of project you want to search')})
    def get_collection(self, callback, *args, **kwargs):
        callback([{'params': self.values['querystring']}])

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
            version='', base_url='http://tapioqueiro.herokuapp.com', discovery=True)
    api.add_resource('projects', ProjectsHandler)
    api.add_resource('comments', CommentsHandler)
    application = tornado.web.Application(api.get_url_mapping())

    server = HTTPServer(application)
    server.bind(port, '0.0.0.0')
    server.start(1)
    main_loop.start()
