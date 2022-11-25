from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from ..config import *

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 100

class AuthorListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        url = self.request.build_absolute_uri()
        # Replace value of id with value of url
        for item in data:
            item['id'] = item['host'] + "authors/" + item['id']
        return Response({
            "type": "authors",
            "items": data
        })
    
"""
class FollowersListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            "type": "followers",
            "items": data
        })
"""
        
    
class InboxListPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            "type": "inbox",
            "item": data
        })