from django.test import TestCase


class LikeTests(TestCase):
    def test_post_likes_get(self):
        # Try to get list of likes for a post 
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

    def test_comment_likes_get(self):
        # Try to get list of likes for a comment 
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

        # Get the likes for that comment
        response = self.client.get('/authors/'+ id +'/posts/1/comments/'+ comment_id +'/likes/')
        self.assertEqual(response.status_code, 200)

    def test_get_liked(self):
        # Try getting the list of liked posts and comments for an author
        # Create an author
        data = {'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com/'}
        response = self.client.post('/api/auth/register/', data=data, content_type='application/json')
        # Get body of response
        body = response.json()
        # Get id of author
        id = body['user']['id']
        # Get the liked objects for that author
        response = self.client.get('/authors/'+ id +'/liked/')
        self.assertEqual(response.status_code, 200) 
    
    def test_posts_like(self):
        # Try liking a post should get 201
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

    def test_comments_like(self):
        # Try liking a comment should get 201
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
        