import unittest
from unittest.mock import patch,MagicMock
from falcon import HTTPBadRequest
from services.user_service import UserService
from repositories.user_repository import UserRepository

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock(spec=UserRepository)
        self.user_service = UserService()
        self.user_service.repository = self.mock_repo

    def test_add_new_user_success(self):
        self.mock_repo.view_user.return_value = None

        new_data = {"email": "test@example.com", "name": "Test User"}

        with patch('builtins.open', unittest.mock.mock_open(read_data='[]')) as mock_file:
            self.user_service.add_new_user(new_data)

            mock_file.assert_called_with("user_data.json", "w")
            self.mock_repo.add_new_user.assert_called_once_with(new_data)

    def test_add_new_user_existing_email(self):
        self.mock_repo.view_user.return_value = [{"email": "test@example.com"}]

        new_data = {"email": "test@example.com", "name": "Test User"}

        with self.assertRaises(HTTPBadRequest):
            self.user_service.add_new_user(new_data)

    def test_view_user_by_email(self):
        self.mock_repo.view_user.return_value = [{"name": "Test User"}]

        result = self.user_service.view_user_by_email("test@example.com")

        self.assertEqual(result, ["Test User"])

if __name__ == '__main__':
    unittest.main()
