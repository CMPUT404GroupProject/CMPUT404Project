from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from api.user.models import User
from .config import *



DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 100
"""
class AuthorListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # Replace value of id with value of url
        for item in data:
            item['id'] = item['url']
        return Response({
            "type": "authors",
            "items": data
        })
"""
class PostListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # Get the url of the request
        url = self.request.build_absolute_uri()
        # Replace value of id with value of url
        for item in data:
            item['id'] = url + item['id']
        # Show all fields for the author from the id
        for item in data:
            author = User.objects.get(id=item['author'])
            # Get the json of the author
            item['author'] = {
                "type": "author",
                "id": author.host + "authors/" + author.id,
                "url": author.host + "authors/" + author.id,
                "host": author.host,
                "displayName": author.displayName,
                "github": author.github,
                "profileImage": author.profileImage
            }
        return Response({
            "type": "posts",
            "items": data
        })

class CommentListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # Get the url of the request
        url = self.request.build_absolute_uri()
        # Replace value of id with value of url
        for item in data:
            item['id'] = url + item['id']
        # Show all fields for the author from the id
        for item in data:
            author = User.objects.get(id=item['author'])
            # Get the json of the author
            item['author'] = {
                "type": "author",
                "id": author.host + "authors/" + author.id,
                "url": author.host + "authors/" + author.id,
                "host": author.host,
                "displayName": author.displayName,
                "github": author.github,
                "profileImage": author.profileImage
            }
        return Response({
            "type": "comments",
            "post": url.split("/comments")[0],
            "id": url[:-1],
            "items": data
        })
# Liked list pagination
class LikedListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            "type": "liked",
            "items": data
        })
    
class InboxListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        # Remove all author from data ordered dict
        #for item in data:
            #item.pop('author')
        # Get author id from url
        authorID = self.request.build_absolute_uri()
        # Remove /inbox/ from the end of the url
        authorID = authorID[:-6]
        # Items is whatever is inside the item field in data
        items = []
        for item in data:
            items.append(item['item'])
        return Response({
            "type": "inbox",
            "author": authorID,
            "items": items
        })

class FollowerListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        # Create list of followers
        followers = []
        for item in data:
            follower = {}
            followerID = item['follower']
            # Get the user with the follower id
            followerUser = User.objects.get(id=followerID)
            # Get the json of the follower
            follower['type'] = "author"
            follower['id'] = followerUser.host + "authors/" + followerUser.id
            follower['url'] = followerUser.host + "authors/" + followerUser.id
            follower['host'] = followerUser.host
            follower['displayName'] = followerUser.displayName
            follower['github'] = followerUser.github
            follower['profileImage'] = followerUser.profileImage

            followers.append(follower)


        return Response({
            "type": "followers",
            "items": followers
        })