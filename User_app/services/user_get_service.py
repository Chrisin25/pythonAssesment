import falcon

from User_app.repositories.user_repository import UserRepository


class UserGetService:

    def __init__(self):
            self.repository = UserRepository()

    def get_user_by_email(self,email):
        print("entered service")
        user =self.repository.get_user(email)
        print("user:",user)
        if user:
            return user
        else:
            raise falcon.HTTPNotFound(description="No user found with this email")