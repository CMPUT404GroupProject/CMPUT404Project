from django.test import TestCase


class LikeTests(TestCase):
    def test_post_likes_get(self):
        # Try to get list of likes for a post 
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')
        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False,
                'id': '1'
            }
        self.client.post('/authors/1/posts/', data=data, content_type='application/json')
        response = self.client.get('/authors/1/posts/1/')
        self.assertEqual(response.status_code, 200)

        # Get the likes for that post
        response = self.client.get('/authors/1/posts/1/likes/')
        self.assertEqual(response.status_code, 200)  

    def test_comment_likes_get(self):
        # Try to get list of likes for a comment 
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')
        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False,
                'id': '1'
            }
        self.client.post('/authors/1/posts/', data=data, content_type='application/json')
        response = self.client.get('/authors/1/posts/1/')
        self.assertEqual(response.status_code, 200)

        # Create a comment
        data = {
                'comment': 'test comment',
                'contentType': 'text/plain',
                'author': '1',
                'id': '1'
            }
        response = self.client.post('/authors/1/posts/1/comments/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)      

        # Get the likes for that comment
        response = self.client.get('/authors/1/posts/1/comments/1/likes/')
        self.assertEqual(response.status_code, 200)  

    def test_get_liked(self):
        # Try getting the list of liked posts and comments for an author
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')
        # Get the liked objects for that author
        response = self.client.get('/authors/1/liked/')
        self.assertEqual(response.status_code, 200) 
    
    def test_posts_like(self):
        # Try liking a post should get 201
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')
        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False,
                'id': '1'
            }
        self.client.post('/authors/1/posts/', data=data, content_type='application/json')
        response = self.client.get('/authors/1/posts/1/')
        self.assertEqual(response.status_code, 200)

        # Like the post
        data = {
            "author": "1"
        }
        response = self.client.post('/authors/1/posts/1/likes/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_comments_like(self):
        # Try liking a comment should get 201
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')
        # Create a post
        data = {
                'categories':'ded', 
                'title': 'test post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False,
                'id': '1'
            }
        self.client.post('/authors/1/posts/', data=data, content_type='application/json')
        response = self.client.get('/authors/1/posts/1/')
        self.assertEqual(response.status_code, 200)

        # Create a comment
        data = {
                'comment': 'test comment',
                'contentType': 'text/plain',
                'author': '1',
                'id': '1'
            }
        response = self.client.post('/authors/1/posts/1/comments/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)      

        # Like the comment
        data = {
            "author": "1"
        }
        response = self.client.post('/authors/1/posts/1/comments/1/likes/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)