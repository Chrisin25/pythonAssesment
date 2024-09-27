import unittest
from falcon import testing
import falcon
from resources.user_resource import UserResource

class MockUserService:
    def add_new_user(self, data):
        pass  # Mock implementation

    def view_user_by_email(self, email):
        return {"email": email, "name": "Test User"}  # Mock response

class TestUserResource(unittest.TestCase):
    def setUp(self):
        self.app = falcon.App()
        self.user_resource = UserResource()
        self.user_resource.service = MockUserService()  # Use the mock service
        self.app.add_route('/users', self.user_resource)
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

    def test_on_post_no_email(self):
        new_user = {"name": "anu","age":45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)

    def test_on_post_invalid_email(self):
        new_user = {"email": "teample.com", "name": "anu","age":45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)

    def test_on_post_invalid_age(self):
        new_user = {"email": "test@example.com", "name": "test","age":-45}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)

    def test_on_post_no_age(self):
        new_user = {"email": "test@example.com", "name": "test"}
        response = self.client.simulate_post('/users', json=new_user)
        self.assertEqual(response.status, falcon.HTTP_400)

    def test_on_get_success(self):
        email = "test@example.com"
        response = self.client.simulate_get('/users', json=email)
        self.assertEqual(response.status, falcon.HTTP_200)
        self.assertEqual(response.json, {"email": "test@example.com", "name": "Test User"})


if __name__ == '__main__':
    unittest.main()