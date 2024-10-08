import unittest
from falcon import testing
import falcon
from resources.user_resource import UserResource

class MockUserService:
    def add_new_user(self, data):
        pass  # Mock implementation

    def get_user_by_email(self, email):
        return {"email": email.get("email"), "name": "Test User"}

class TestUserResource(unittest.TestCase):
    def setUp(self):
        self.app = falcon.App()
        self.user_resource = UserResource()
        self.user_resource.service = MockUserService()
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

    def test_on_get_success(self):
        email = "test@example.com"
        response = self.client.simulate_get(f'/users/{email}')
        self.assertEqual(response.status, falcon.HTTP_200)
        self.assertEqual(response.json, {"email": "test@example.com", "name": "Test User"})

    def test_on_get_empty_email(self):
        email = ""
        response = self.client.simulate_get(f'/users/{email}')
        self.assertEqual(response.status, falcon.HTTP_400)
        self.assertEqual(response.json,{'title': '400 Bad Request', 'description': 'specify a valid email address'})

