import unittest
from unittest.mock import MagicMock

from bson import ObjectId
from falcon import HTTPNotFound
from User_app.repositories.user_repository import UserRepository
from User_app.services.user_get_service import UserGetService


class TestGetUserService(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock(spec=UserRepository)
        self.user_service = UserGetService()
        self.user_service.repository = self.mock_repo


    def test_get_user_by_email(self):
        self.mock_repo.get_user.return_value = {'age': 22, 'email': 'test@example.com', 'name': 'Test User'}

        result = self.user_service.get_user_by_email("test@example.com")

        self.assertEqual(result, {"name": "Test User","email":"test@example.com","age":22})

    def test_get_user_by_email_not_found(self):
        self.mock_repo.get_user.return_value = None

        with self.assertRaises(HTTPNotFound) as context:
            self.user_service.get_user_by_email("test@example.com")
        self.assertEqual(str(context.exception.description), "No user found with this email")
