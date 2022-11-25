from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

# Test for authors
class AuthorTests(TestCase):
    def test_authors_get(self):
        # Try to get list of authors, should return 200 OK
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)
    
    def test_authors_get_non_existing(self):
        # Try to get a non-existing author, should give 404
        response = self.client.get('/authors/1333/')
        self.assertEqual(response.status_code, 404)

    def test_authors_create(self):
        # Try to create an author through registration, should return 201 created
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        self.assertEqual(response.status_code, 201)

    def test_authors_get_single(self):
        # Try to get an existing author, should return 200 OK
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        self.assertEqual(response.status_code, 201)
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Try to get author
        response = self.client.get('/authors/' + id + '/')
        self.assertEqual(response.status_code, 200)

    def test_authors_update(self):
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Try to update an existing author, should return 200 OK
        data = {'displayName': "testuser2", 'github':'https://github.com/2'}
        response = self.client.post('/authors/' + id + '/', data=data, content_type='application/json')
        
        # Make sure the author was updated
        response = self.client.get('/authors/' + id + '/')
        body = response.json()
        self.assertEqual(body['displayName'], "testuser2")
        self.assertEqual(response.status_code, 200)

    def test_authors_delete(self):
        # Delete isn't an allowed method, should return 405
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data)
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Try to delete an existing author, should return 405 Method Not Allowed
        response = self.client.delete('/authors/' + id + '/')
        self.assertEqual(response.status_code, 405)