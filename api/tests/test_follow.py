from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
# Tests for things related to follow requests, accepting followees, etc.
class FollowerTests(TestCase):
    # Test follow request
    def test_follow_request(self):
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create actor author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/2'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of actor
        actor_id = body['user']['id']

        # Create follow request
        data = {'actor': actor_id}
        response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
        
        # Should return 201 Created
        self.assertEqual(response.status_code, 201)
    
    # Test follow self
    def test_follow_request_self(self):
        # Should return 400 Bad Request, can't follow yourself

        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create follow request
        data = {'actor': object_id}
        response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
        
        # Should return 400 Bad Request
        self.assertEqual(response.status_code, 400)
    
    # Test follow request non-existing author
    def test_follow_request_non_existing(self):
        try:
            # Create object author
            data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
            response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
            # Get body of response
            body = response.json()
            # Get id of object
            object_id = body['user']['id']
            # Create follow request
            data = {'actor': '12309'}
            response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
            # Fail if no exception is thrown
            self.fail()
        # Expect does not exist exception
        except ObjectDoesNotExist:
            # Success if exception is thrown
            self.assertEqual(True, True)
    
    # Test get list of follow requests
    def test_get_follow_requests(self):
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']
        response = self.client.get('/authors/' + object_id + '/follow_requests/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)
    
    # Test accept follow request
    def test_accept_follow_request(self):
        # Create a follow request then accept it
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create actor author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/2'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of actor
        actor_id = body['user']['id']

        # Create follow request
        data = {'actor': actor_id}
        response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
        
        # Should return 201 Created
        self.assertEqual(response.status_code, 201)

        # Accept follow request
        response = self.client.put('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)

    # Test get list of followers
    def test_get_followers(self):
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create actor author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/2'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of actor
        actor_id = body['user']['id']

        # Create follow request
        data = {'actor': actor_id}
        response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
        
        # Should return 201 Created
        self.assertEqual(response.status_code, 201)

        # Accept follow request
        response = self.client.put('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)

        # Get list of followers
        response = self.client.get('/authors/' + object_id + '/followers/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)
    
    # Test accept follow request that doesn't exist
    def test_accept_follow_request_non_existing(self):
        # Try to add a follower without making a request first
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create actor author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/2'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of actor
        actor_id = body['user']['id']

        # Accept follow request
        response = self.client.put('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 400 Bad Request
        self.assertEqual(response.status_code, 400)
    
    # Test get single follower
    def test_get_single_follower(self):
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create actor author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/2'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of actor
        actor_id = body['user']['id']

        # Create follow request
        data = {'actor': actor_id}
        response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
        
        # Should return 201 Created
        self.assertEqual(response.status_code, 201)

        # Accept follow request
        response = self.client.put('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)

        # Get the single follower
        response = self.client.get('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)
    
    # Test delete a follower
    def test_delete_follower(self):
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        object_id = body['user']['id']

        # Create actor author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/2'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of actor
        actor_id = body['user']['id']

        # Create follow request
        data = {'actor': actor_id}
        response = self.client.post('/authors/' + object_id + '/follow_requests/', data=data, content_type='application/json')
        
        # Should return 201 Created
        self.assertEqual(response.status_code, 201)

        # Accept follow request
        response = self.client.put('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 200 OK
        self.assertEqual(response.status_code, 200)

        # Get the single follower
        response = self.client.delete('/authors/' + object_id + '/followers/' + actor_id + '/')
        # Should return 204 No Content 
        self.assertEqual(response.status_code, 204)