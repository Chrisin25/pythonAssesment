import falcon
import json
from User_app.services.user_get_service import UserGetService


class UserGetResource:

    def __init__(self):
            self.service = UserGetService()

    def on_get(self,req,resp,email):

        if email=="":
            raise falcon.HTTPBadRequest(description="specify a valid email address")
        else:
           response = self.service.get_user_by_email(email)

           resp.status = falcon.HTTP_200
           resp.text = json.dumps(response)