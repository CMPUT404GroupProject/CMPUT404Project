from rest_framework.routers import SimpleRouter
from api.user.viewsets import UserViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from api.post.viewsets import PostViewSet

routes = SimpleRouter()
# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# POST
routes.register(r'authors/(?P<authorID>\d+)/posts/(?P<postID>\d+)', PostViewSet, basename = 'post')

urlpatterns = [
    *routes.urls
]