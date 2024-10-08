import json
import re

import falcon
from falcon import HTTPUnsupportedMediaType

from services.user_service import UserService

class UserResource:

    def __init__(self):
        self.service=UserService()

    def on_post(self,req,res):
        new_data = req.media
        #no value entered
        if req.content_type not in ('application/json', 'application/xml'):
            raise HTTPUnsupportedMediaType(
                title='415 Unsupported Media Type',
                description="specify details of new user"
            )
        else:
            if new_data.get("name")== "" or not new_data.get("name"):
                raise falcon.HTTPBadRequest(description="Enter a valid name")
            if not new_data.get("email"):
                raise falcon.HTTPBadRequest(description="Enter a valid email")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", new_data.get("email")):
                raise falcon.HTTPBadRequest(description='Invalid email format')
            if not new_data.get("age") or not new_data.get("age")>0:
                raise falcon.HTTPBadRequest(description="Enter a valid age")

            self.service.add_new_user(new_data)

            res.status = falcon.HTTP_200
            res.body = json.dumps({"message": "successfully created"})

    def on_get(self,req,resp,email):
        print(email)
        print(type(email))
        if email=="":
            raise falcon.HTTPBadRequest(description="specify a valid email address")
        else:
           response = self.service.get_user_by_email({"email":email})

           resp.status = falcon.HTTP_200
           resp.text = json.dumps(response)

