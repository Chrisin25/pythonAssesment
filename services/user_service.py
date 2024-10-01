import json

from falcon import HTTPBadRequest

from models.User import User
from repositories.user_repository import UserRepository

class UserService:

    def __init__(self):
        self.repository=UserRepository()

    def add_new_user(self,new_data):
        user = User.from_dict(new_data)
        emaildata=new_data.get("email")

        if list(self.repository.view_user({"email":new_data.get("email")})):
           raise HTTPBadRequest(description="User with this mail id already exist")

        with open("user_data.json","r") as json_file:
            data=json.load(json_file)

        data.append(user.to_dict())

        with open("user_data.json", "w") as json_file:
            json.dump(data,json_file,indent=4)

        self.repository.add_new_user(user.to_dict())

    def view_user_by_email(self,email):

        my_list = []
        all_docs =self.repository.view_user(email)
        for x in all_docs:
            my_list.append(x.get("name"))
        return my_list