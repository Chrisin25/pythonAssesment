import unittest
from falcon import testing
import falcon
from User_app.resources.user_post_resource import UserPostResource


class MockUserAddService:
    def add_new_user(self, data):
        pass  # Mock implementation

class TestUserResource(unittest.TestCase):
    def setUp(self):
        self.app = falcon.App()
        self.user_resource = UserPostResource()
        self.user_resource.service = MockUserAddService()
        self.app.add_route('/users', self.user_resource)
        self.app.add_route('/users/{email}', self.user_resource)
        self.client = testing.TestClient(self.app)

    def test_on_post_success(self):
        new_user = {"email": "test@example.com", "name": "Test User","age":45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_200)
        self.assertEqual(response.json, {"message": "successfully created"})

    def test_on_post_invalid_name(self):
        new_user = {"email": "test@example.com", "name": "","age":45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json,{'description': 'Enter a valid name', 'title': '400 Bad Request'})

    def test_on_post_no_email(self):
        new_user = {"name": "anu","age":45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json,{'description': 'Enter a valid email', 'title': '400 Bad Request'})

    def test_on_post_invalid_email(self):
        new_user = {"email": "test.com", "name": "anu","age":45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json,{'description': 'Invalid email format', 'title': '400 Bad Request'})

    def test_on_post_invalid_age(self):
        new_user = {"email": "test@example.com", "name": "test","age":-45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json, {'description': 'Enter a valid age', 'title': '400 Bad Request'})
    def test_on_post_no_age(self):
        new_user = {"email": "test@example.com", "name": "test"}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json, {'description': 'Enter a valid age', 'title': '400 Bad Request'})

