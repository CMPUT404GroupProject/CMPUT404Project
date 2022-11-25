from django.test import TestCase

# Test for registration and login
class AuthenticationTests(TestCase):
    def test_login_get(self):
        # Try to get login, should return 405 since we only post to this endpoint
        response = self.client.get('/api/auth/login/')
        self.assertEqual(response.status_code, 405)

    def test_register_get(self):
        # Try to get register, should return 405 since we only post to this endpoint
        response = self.client.get('/api/auth/register/')
        self.assertEqual(response.status_code, 405)
    
    def test_register_post(self):
        # Try to register an account, should return 201 created
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        self.assertEqual(response.status_code, 201)


    def test_login_non_existing(self):
        # Try to log in to an non-existing account, should return 401 unauthorized
        data = {'displayName': "testuser", 'password': 'test_pass'}
        response = self.client.post('/api/auth/login/', data=data)
        self.assertEqual(response.status_code, 401)

    def test_login_existing(self):
        # Try to log in to an existing account, should return 200 OK

        # First register an account
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        self.assertEqual(response.status_code, 201)

        # Then try to log in
        data = {'displayName': "testuser", 'password': 'test_pass'}
        response = self.client.post('/api/auth/login/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_login_existing_wrong_password(self):
        # Try to log in to an existing account with wrong password, should return 401 unauthorized

        # First register an account
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        self.assertEqual(response.status_code, 201)

        # Then try to log in
        data = {'displayName': "testuser", 'password': 'wrong_pass'}
        response = self.client.post('/api/auth/login/', data=data)
        self.assertEqual(response.status_code, 401)
        