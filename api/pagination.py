from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from api.user.models import User
from api.models import FollowRequest, Inbox, Comment
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
            item['id'] = item['author']['id'] + "/posts/" + item['id']
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
            "comments": data
        })
    
class LikesListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # Get the url of the request
        url = self.request.build_absolute_uri()
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
        return Response(data)
# Liked list pagination
class LikedListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        # Get the url of the request
        url = self.request.build_absolute_uri()
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
                "type": "liked",
                "items": data})

    
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
            if item['item']['type'] == "Follow":
                actor = User.objects.get(id=item['item']['actor'])
                object = User.objects.get(id=item['item']['object'])
                # Get the json of the actor
                item['item']['actor'] = {
                    "type": "author",
                    "id": actor.host + "authors/" + actor.id,
                    "url": actor.host + "authors/" + actor.id,
                    "host": actor.host,
                    "displayName": actor.displayName,
                    "github": actor.github,
                    "profileImage": actor.profileImage
                }
                # Get the json of the object
                item['item']['object'] = {
                    "type": "author",
                    "id": object.host + "authors/" + object.id,
                    "url": object.host + "authors/" + object.id,
                    "host": object.host,
                    "displayName": object.displayName,
                    "github": object.github,
                    "profileImage": object.profileImage
                }
            elif(item['item']['type'] == "comment"):
                # Get the comment with the id
                author = User.objects.get(id=item['item']['author'])
                item['item']['id'] = author.host + "posts/" + item['item']['post'] + "/comments/" + item['item']['id']
                item['item']['author'] = {
                    "type": "author",
                    "id": author.host + "authors/" + author.id,
                    "url": author.host + "authors/" + author.id,
                    "host": author.host,
                    "displayName": author.displayName,
                    "github": author.github,
                    "profileImage": author.profileImage
                }
            else:
                author = User.objects.get(id=item['author'])
                # Get the json of the author
                item['item']['author'] = {
                    "type": "author",
                    "id": author.host + "authors/" + author.id,
                    "url": author.host + "authors/" + author.id,
                    "host": author.host,
                    "displayName": author.displayName,
                    "github": author.github,
                    "profileImage": author.profileImage
                }
                # If type is post
                if item['item']['type'] == "post":
                    # Get the url of the post
                    item['item']['id'] = item['item']['author']['id'] + "/posts/" + item['item']['id']
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
    
class FollowRequestPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        # Create list of requests
        requests = []
        for item in data:
            request = {}
            request['type'] = "Follow"
            request['summary'] = item['summary']
            # Get user from actor
            actorUser = User.objects.get(id=item['actor'])
            objectUser = User.objects.get(id=item['object'])
            request['actor'] = {
                "type": "author",
                "id": actorUser.host + "authors/" + actorUser.id,
                "url": actorUser.host + "authors/" + actorUser.id,
                "host": actorUser.host,
                "displayName": actorUser.displayName,
                "github": actorUser.github,
                "profileImage": actorUser.profileImage
            }
            request['object'] = {
                "type": "author",
                "id": objectUser.host + "authors/" + objectUser.id,
                "url": objectUser.host + "authors/" + objectUser.id,
                "host": objectUser.host,
                "displayName": objectUser.displayName,
                "github": objectUser.github,
                "profileImage": objectUser.profileImage
            }
            requests.append(request)
        return Response({
            "type": "requests",
            "items": requests
        })