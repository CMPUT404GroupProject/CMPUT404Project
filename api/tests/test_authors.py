from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
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
    
    def test_authors_get_existing(self):
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        
        # Try to get an existing author, should return 200 OK
        response = self.client.get('/authors/1/')
        self.assertEqual(response.status_code, 200)

