from django.test import TestCase

class FollowerTests(TestCase):
    def test_followers_get(self):
        # Try to get list of followers for an author
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')

        # Get the followers for that author
        response = self.client.get('/authors/1/followers/')
        self.assertEqual(response.status_code, 200)
    
    def test_followers_put(self):
        # Try to add a follower to an author
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')

        # Create a follower
        data = {'id':'2', 'displayName': "testuser2", 'password': 'test_pass2', 'github':'https://github.com/2'}
        self.client.post('/authors/', data=data, content_type='application/json')

        # Add the follower to the author
        response = self.client.put('/authors/1/followers/2/')
        self.assertEqual(response.status_code, 200)
    
    def test_followers_delete(self):
        # Try to add a follower to an author and delete it
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')

        # Create a follower
        data = {'id':'2', 'displayName': "testuser2", 'password': 'test_pass2', 'github':'https://github.com/2'}
        self.client.post('/authors/', data=data, content_type='application/json')

        # Add the follower to the author
        response = self.client.put('/authors/1/followers/2/')
        self.assertEqual(response.status_code, 200)

        # Delete the follower from the author
        response = self.client.delete('/authors/1/followers/2/')
        self.assertEqual(response.status_code, 204)