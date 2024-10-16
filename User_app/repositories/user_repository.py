from User_app.config import client

class UserRepository:
    '''def __init__(self):
        self.db=client.UserDb
        self.collection=self.db.Users

    def add_new_user(self,data):
        self.collection.insert_one(data)

    def get_user(self,email):
        return self.collection.find_one({"email":new_data.get("email")}).pop("_id")'''

    def __init__(self):
        if not (client.indices.exists(index="user")):
            client.indices.create(index="user")
        self.index = "user"
    def add_new_user(self, data):
        client.index(index=self.index,document=data)

    def get_user(self, email):
        res=client.search(index=self.index,query={'match':{"email":email}})
        hits=res['hits']['hits']
        for doc in hits:
            return doc['_source']

