from django.test import TestCase

class CommentTests(TestCase):
    def test_comments_get_list(self):
        # Try to get list of comments, should return 200 OK
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

        # Try to get comments for that post
        response = self.client.get('/authors/'+ id +'/posts/1/comments/')
        self.assertEqual(response.status_code, 200)

    def test_comments_get_non_existing(self):
        # Try to get comments for a non-existing post, should return 404
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

        # Try to get non existing comment for that post
        response = self.client.get('/authors/'+ id +'/posts/1/comments/243/')
        self.assertEqual(response.status_code, 404)

    def test_comments_create(self):
        # Try to create a comment, should return 201
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

    def test_comments_get_existing(self):
        # Try to create a comment, and get it should return 200
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