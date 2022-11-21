from django.test import TestCase

class CommentTests(TestCase):
    def test_comments_get_list(self):
        # Try to get list of comments, should return 200 OK
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

        # Try to get comments for that post
        response = self.client.get('/authors/1/posts/1/comments/')
        self.assertEqual(response.status_code, 200)

    def test_comments_get_non_existing(self):
        # Try to get comments for a non-existing post, should return 404
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')

        # Try to get comments for non existing post should return 404
        response = self.client.get('/authors/1/posts/1/comments/1/')
        self.assertEqual(response.status_code, 404)

    def test_comments_create(self):
        # Try to create a comment, should return 201
        # Create an author
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
            }
        response = self.client.post('/authors/1/posts/1/comments/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_comments_get_existing(self):
        # Try to create a comment, and get it should return 200
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

        # Get the comment
        response = self.client.get('/authors/1/posts/1/comments/1/')
        self.assertEqual(response.status_code, 200)  

    def test_comment_update(self):
        # Try to update a comment, should return 200
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

        # Update the comment
        data = {
                'comment': 'updated comment',
                'contentType': 'text/plain',
                'author': '1',
                'id': '1'
            }
        response = self.client.patch('/authors/1/posts/1/comments/1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)  

    def test_comments_delete(self):
        # Try to delete an existing comment, should return 204
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

        # Delete the comment
        response = self.client.delete('/authors/1/posts/1/comments/1/')
        self.assertEqual(response.status_code, 204)