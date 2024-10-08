import unittest
from unittest.mock import patch,MagicMock
from falcon import HTTPBadRequest,HTTPNotFound

from services.user_service import UserService
from repositories.user_repository import UserRepository

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock(spec=UserRepository)
        self.user_service = UserService()
        self.user_service.repository = self.mock_repo

    def test_add_new_user_success(self):
        self.mock_repo.get_user.return_value = None
        new_data = {"email": "test@example.com", "name": "Test User","age":20}

        with patch('builtins.open', unittest.mock.mock_open(read_data='[]')) as mock_file:
            self.user_service.add_new_user(new_data)

            mock_file.assert_called_with("data/user_data.json", "w")
            self.mock_repo.add_new_user.assert_called_once_with(new_data)

    def test_add_new_user_existing_email(self):
        self.mock_repo.get_user.return_value = [{"email": "test@example.com"}]

        new_data = {"email": "test@example.com", "name": "Test User"}

        with self.assertRaises(HTTPBadRequest):
            self.user_service.add_new_user(new_data)

    def test_get_user_by_email(self):
        self.mock_repo.get_user.return_value = {"name": "Test User","email":"test@example.com","age":22}

        result = self.user_service.get_user_by_email("test@example.com")

        self.assertEqual(result, {"name": "Test User","email":"test@example.com","age":22})

    def test_get_user_by_email_not_found(self):
        self.mock_repo.get_user.return_value = None

        with self.assertRaises(HTTPNotFound) as context:
            self.user_service.get_user_by_email("test@example.com")
        self.assertEqual(str(context.exception.description), "No user found with this email")

