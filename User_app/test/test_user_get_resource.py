import unittest
from falcon import testing
import falcon

from User_app.resources.user_get_resource import UserGetResource


class MockUserGetService:
    def get_user_by_email(self, email):
        return {"email": email, "name": "Test User"}

class TestUserResource(unittest.TestCase):
    def setUp(self):
        self.app = falcon.App()
        self.user_resource = UserGetResource()
        self.user_resource.service = MockUserGetService()
        self.app.add_route('/users', self.user_resource)
        self.app.add_route('/users/{email}', self.user_resource)
        self.client = testing.TestClient(self.app)

    def test_on_get_success(self):
        email = "test@example.com"
        response = self.client.simulate_get(f'/users/{email}')
        self.assertEqual(response.status, falcon.HTTP_200)
        self.assertEqual(response.json, {"email": "test@example.com", "name": "Test User"})

    def test_on_get_empty_email(self):
        email=""
        response = self.client.simulate_get(f'/users/{email}')
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json,{'title': '400 Bad Request', 'description': 'specify a valid email address'})

