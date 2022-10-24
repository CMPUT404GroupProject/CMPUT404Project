from rest_framework.routers import SimpleRouter
from api.user.viewsets import UserViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from api.post.viewsets import PostViewSet

routes = SimpleRouter()
# AUTHENTICATION
routes.register(r'api/auth/login', LoginViewSet, basename='auth-login')
routes.register(r'api/auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'api/auth/refresh', RefreshViewSet, basename='auth-refresh')

# SERVICE ENDPOINTS REQUIRED
# /service/authors/
routes.register(r'authors', UserViewSet, basename='user')
# /service/authors/{AUTHOR_ID}/
# /service/authors/{AUTHOR_ID}/followers
# /service/authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}

# /service/authors/{AUTHOR_ID}/posts/
# /service/authors/{AUTHOR_ID}/posts/{POST_ID}

# /service/authors/{AUTHOR_ID}/posts/{POST_ID}/image
# /service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments

# service/authors/{AUTHOR_ID}/inbox/
# /service/authors/{AUTHOR_ID}/posts/{POST_ID}/likes
# /service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/{COMMENT_ID}/likes
# /service/authors/{AUTHOR_ID}/liked


# USER
routes.register(r'api/user', UserViewSet, basename='user')

# POST
routes.register(r'authors/(?P<authorID>\d+)/posts/(?P<postID>\d+)', PostViewSet, basename = 'post')

urlpatterns = [
    *routes.urls
]