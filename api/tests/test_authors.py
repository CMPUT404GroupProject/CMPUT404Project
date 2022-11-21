from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
# Create your tests here.

class AuthorTests(TestCase):
    def test_authors_get(self):
        # Try to get list of authors, should return 200 OK
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)
    
    def test_authors_get_non_existing(self):
        # Try to get a non-existing author, should give ObjectDoesNotExist
        try:
            response = self.client.get('/authors/1333/')
            assert(False)
        except ObjectDoesNotExist:
            assert(True)

    def test_authors_create(self):
        # Try to create an author, should return 201 created
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/authors/', data=data)
        self.assertEqual(response.status_code, 201)

    def test_authors_get_existing(self):
        # Try to get an existing author, should return 200 OK
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        self.client.post('/authors/', data=data)

        # Try to get an existing author, should return 200 OK
        response = self.client.get('/authors/1/')
        self.assertEqual(response.status_code, 200)

    def test_authors_delete(self):
        # Try to delete an author, should return 204 No Content
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        self.client.post('/authors/', data=data)

        # Try to delete an existing author, should return 204 No Content
        response = self.client.delete('/authors/1/')
        self.assertEqual(response.status_code, 204)