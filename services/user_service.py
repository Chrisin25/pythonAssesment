import json

from repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository=UserRepository()
    def add_new_user(self,new_data):
        print(new_data)

        with open("user_data.json","r") as json_file:
            data=json.load(json_file)
        print(data)
        #json_object = json.dumps(new_data)
        #print(json_object)
        data.append(new_data)
        print(data)
        with open("user_data.json", "w") as json_file:
            #json_file.write(json_object)
            json.dump(data,json_file,indent=4)
        self.repository.add_new_user(new_data)
    def view_user_by_email(self,email):
        my_list = []
        all_docs =self.repository.view_user(email)
        #print("all docs:",all_docs)
        for x in all_docs:
            my_list.append(x.get("name"))
        #print("my_list:",my_list)
        return my_list