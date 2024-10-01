from config import client

class UserRepository:
    def __init__(self):
        self.db=client.UserDb
        self.collection=self.db.Users

    def add_new_user(self,data):
        self.collection.insert_one(data)

    def get_user(self,email):
        #print(self.collection.find(email))
        return self.collection.find_one(email)