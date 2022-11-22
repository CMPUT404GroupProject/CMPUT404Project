from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 100

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