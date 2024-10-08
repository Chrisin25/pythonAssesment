import json
import falcon

from models.User import User
from repositories.user_repository import UserRepository

class UserService:

    def __init__(self):
        self.repository=UserRepository()

    def add_new_user(self,new_data):
        #dict to user object
        user = User.from_dict(new_data)
        #check if mail id is unique
        if self.repository.get_user({"email":new_data.get("email")}):
           raise falcon.HTTPBadRequest(description="User with this mail id already exist")
        # add to json file
        with open("data/user_data.json","r") as json_file:
            data=json.load(json_file)

        data.append(user.to_dict())

        with open("data/user_data.json", "w") as json_file:
            json.dump(data,json_file,indent=4)
        #add to db
        self.repository.add_new_user(user.to_dict())

    def get_user_by_email(self,email):

        user =self.repository.get_user(email)
        user_dict={}
        if user:
            user_dict["name"]=user.get("name")
            user_dict["email"]=user.get("email")
            user_dict["age"] = user.get("age")
        else:
            raise falcon.HTTPNotFound(description="No user found with this email")
        return user_dict