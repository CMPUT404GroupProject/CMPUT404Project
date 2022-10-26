from rest_framework.routers import SimpleRouter
from api.user.viewsets import UserViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
# from api.post.viewsets import PostViewSet
from api.post.viewsets.viewsets import CreatePostViewSet, UpdatePostViewSet

routes = SimpleRouter()
# AUTHENTICATION
routes.register(r'api/auth/login', LoginViewSet, basename='auth-login')
routes.register(r'api/auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'api/auth/refresh', RefreshViewSet, basename='auth-refresh')

# SERVICE ENDPOINTS REQUIRED
# /authors/
routes.register(r'authors', UserViewSet, basename='user')
# /authors/{AUTHOR_ID}/
# /authors/{AUTHOR_ID}/followers
# /authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

# /authors/{AUTHOR_ID}/posts/
# /authors/{AUTHOR_ID}/posts/{POST_ID}

# /authors/{AUTHOR_ID}/posts/{POST_ID}/image
# /authors/{AUTHOR_ID}/posts/{POST_ID}/comments

# service/authors/{AUTHOR_ID}/inbox/
# /authors/{AUTHOR_ID}/posts/{POST_ID}/likes
# /authors/{AUTHOR_ID}/posts/{POST_ID}/comments/{COMMENT_ID}/likes
# /authors/{AUTHOR_ID}/liked


# USER
routes.register(r'api/user', UserViewSet, basename='user')

# POSTS
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts/(?P<postID>[0-9a-f-]+)', UpdatePostViewSet, basename = 'post')
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts', CreatePostViewSet, basename = 'post')
urlpatterns = [
    *routes.urls
]