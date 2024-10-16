import json
import falcon

from User_app.models.User import User
from User_app.repositories.user_repository import UserRepository

class UserAddService:

    def __init__(self):
        self.repository=UserRepository()

    def add_new_user(self,new_data):

        user=User.__new__(User)
        user.__dict__.update(new_data)

        #validate mail id is unique
        if self.repository.get_user(new_data.get("email")):
            raise falcon.HTTPBadRequest(description="User with this mail id already exist")
        print("validated duplicate mail id")
        # add to json file
        with open("User_app/data/user_data.json","r") as json_file:
            data=json.load(json_file)
        data.append(user.__dict__)
        with open("User_app/data/user_data.json", "w") as json_file:
            json.dump(data,json_file,indent=4)
        print("added to json file")
        #add to db
        self.repository.add_new_user(user.__dict__)
        print("added to db")


