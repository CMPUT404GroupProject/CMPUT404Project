from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist


class InboxTests(TestCase):

    # Test getting list of inbox items
    def test_inbox_get(self):
        # Create object author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of object
        id = body['user']['id']

        # Try to get list of inbox items, should return 200 OK
        response = self.client.get('/authors/' + id + '/inbox/')

        # Make sure inbox is empty
        self.assertEqual(len(response.data['items']), 0)
        self.assertEqual(response.status_code, 200)

    # Test follow request
    def test_inbox_follow_request(self):
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

        # Get inbox items for object
        response = self.client.get('/authors/' + object_id + '/inbox/')
        # Make sure inbox is not empty
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.status_code, 200)
    
    def test_inbox_post(self):
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Create another author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/a'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id2 = body['user']['id']

        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False
            }
        response = self.client.put('/authors/'+ id +'/posts/1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/authors/'+ id +'/posts/1/')
        self.assertEqual(response.status_code, 200)
        # Get inbox items for author
        response = self.client.get('/authors/' + id + '/inbox/')
        # Make sure inbox is not empty
        self.assertEqual(len(response.data['items']), 1)
        # Make sure inbox item is a post
        self.assertEqual(response.data['items'][0]['type'], 'post')
        # Make sure other author also has inbox item
        response = self.client.get('/authors/' + id2 + '/inbox/')
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['type'], 'post')
        self.assertEqual(response.status_code, 200)

    def test_inbox_comment(self):
                # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Create another author
        data = {'displayName': "testuser2", 'password': 'test_pass', 'github':'https://github.com/a'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id2 = body['user']['id']

        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False
            }
        response = self.client.put('/authors/'+ id +'/posts/1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/authors/'+ id +'/posts/1/')
        self.assertEqual(response.status_code, 200)

        # Create a comment
        data = {
                'comment': 'test comment',
                'contentType': 'text/plain',
                'author': id2,
            }
        response = self.client.post('/authors/'+ id +'/posts/1/comments/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Get inbox items for author
        response = self.client.get('/authors/' + id + '/inbox/')
        # Make sure inbox is not empty
        self.assertEqual(len(response.data['items']), 2)
        # Make sure inbox has a post and a comment
        self.assertNotEqual(response.data['items'][0]['type'], response.data['items'][1]['type'])

        # Make sure other author also has inbox item for post only
        response = self.client.get('/authors/' + id2 + '/inbox/')
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['type'], 'post')
    
    def test_inbox_post_like(self):
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False
            }
        response = self.client.put('/authors/'+ id +'/posts/1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Get the likes for that post
        response = self.client.get('/authors/'+ id +'/posts/1/likes/')
        self.assertEqual(response.status_code, 200) 

        # Like the post
        response = self.client.post('/authors/'+ id +'/posts/1/likes/', data={"author": id}, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Get the check inbox
        response = self.client.get('/authors/'+ id +'/inbox/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['items']), 2)
        self.assertNotEqual(response.data['items'][0]['type'], response.data['items'][1]['type'])
    
    def test_inbox_comment_like(self):
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False
            }
        response = self.client.put('/authors/'+ id +'/posts/1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/authors/'+ id +'/posts/1/')
        self.assertEqual(response.status_code, 200)

        # Create a comment
        data = {
                'comment': 'test comment',
                'contentType': 'text/plain',
                'author': id,
            }
        response = self.client.post('/authors/'+ id +'/posts/1/comments/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        # Get comment id from response
        body = response.json()
        comment_id = body['id']
        # Get the comment
        response = self.client.get('/authors/'+ id +'/posts/1/comments/'+ comment_id +'/')
        self.assertEqual(response.status_code, 200)

        # Like the comment
        response = self.client.post('/authors/'+ id +'/posts/1/comments/'+ comment_id +'/likes/', data={"author": id}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
        # Get the check inbox
        response = self.client.get('/authors/'+ id +'/inbox/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['items']), 3)
