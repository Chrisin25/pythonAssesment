import falcon

from User_app.resources.user_get_resource import UserGetResource
from User_app.resources.user_post_resource import UserPostResource

app=falcon.App()
app.add_route('/users',UserPostResource())
app.add_route('/users/{email}',UserGetResource())
