from rest_framework.routers import SimpleRouter
from api.user.viewsets import UserViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

routes = SimpleRouter()
# AUTHENTICATION
routes.register(r'api/auth/login', LoginViewSet, basename='auth-login')
routes.register(r'api/auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'api/auth/refresh', RefreshViewSet, basename='auth-refresh')

# SERVICE ENDPOINTS REQUIRED
# /service/authors/
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

urlpatterns = [
    *routes.urls
]