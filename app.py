from wsgiref.simple_server import make_server

import falcon

from resources.user_resource import UserResource

app=falcon.App()
app.add_route('/users',UserResource())
app.add_route('/users/{email}',UserResource())



if __name__=='__main__':
    httpd=make_server('0.0.0.0',8080,app)
    httpd.serve_forever()