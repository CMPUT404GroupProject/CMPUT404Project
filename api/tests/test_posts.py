from django.test import TestCase

class PostTests(TestCase):
    def test_posts_get_list(self):
        # Try to get list of posts, should return 200 OK
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        response = self.client.post('/authors/', data=data, content_type='application/json')

        # Try to get list of posts for that author
        response = self.client.get('/authors/1/posts/')
        self.assertEqual(response.status_code, 200)

    def test_posts_get_non_existing(self):
        # Try to get a non-existing post, should give 404
        # Create an author
        data = {'id':'1', 'displayName': "testuser", 'password': 'test_pass', 'github':'https://github.com'}
        self.client.post('/authors/', data=data, content_type='application/json')

        response = self.client.get('authors/1/posts/1333/')
        self.assertEqual(response.status_code, 404)

    def test_posts_create(self):
        # Try to create a post, should return 201 created
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
                'unlisted': False
            }
        response = self.client.post('/authors/1/posts/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_posts_get_existing(self):
        # Try to get an existing post, should return 200 OK
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

        # Try to get the created post
        response = self.client.get('/authors/1/posts/1/')
        self.assertEqual(response.status_code, 200)

    def test_posts_update(self):
        # Try to update an existing post, should return 200 OK
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

        # Update the post
        data = {
                'categories':'ded', 
                'title': 'update post', 
                'source': 'https://github.com', 
                'origin': 'https://github.com', 
                'description': 'test post', 
                'contentType': 'text/plain', 
                'visibility': 'PUBLIC', 
                'unlisted': False
            }
        # set content type to json
        response = self.client.patch('/authors/1/posts/1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_posts_delete(self):
        # Try to update an existing post, should return 200 OK
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

        # Delete the post
        response = self.client.delete('/authors/1/posts/1/')
        self.assertEqual(response.status_code, 204)