import json
import re

import falcon

from User_app.services.user_post_service import UserAddService


class UserPostResource:

    def __init__(self):
        self.service=UserAddService()

    def on_post(self,req,res):

        new_data = req.media

        #validate req data
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
        res.text = json.dumps({"message": "successfully created"})



