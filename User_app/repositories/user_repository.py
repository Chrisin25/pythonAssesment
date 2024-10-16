from User_app.config import client

class UserRepository:
    '''def __init__(self):
        self.db=client.UserDb
        self.collection=self.db.Users

    def add_new_user(self,data):
        self.collection.insert_one(data)

    def get_user(self,email):
        user=self.collection.find_one({"email":email})
        if user:
            user.pop('_id')
            return user
'''
    def __init__(self):
        if not (client.indices.exists(index="user")):
            client.indices.create(index="user")
        mapping = {
            "properties": {
                "email": {
                    "type": "keyword"
                },
                "name": {
                    "type": "text"
                },
                "age": {
                    "type": "integer"
                }
            }
        }
        client.indices.put_mapping(index="user", body=mapping)
        self.index = "user"
    def add_new_user(self, data):
        client.index(index=self.index,document=data)
        print("new document added")

    def get_user(self, email):
        print(email)
        res=client.search(index=self.index,query={'term':{"email":email}})
        print(res)
        hits=res['hits']['hits']
        print(hits)
        for doc in hits:
            return doc['_source']

