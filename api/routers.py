from rest_framework.routers import SimpleRouter
from api.user.viewsets import FollowersViewSet, UserViewSet, FollowersDetailedViewSet, InboxViewSet, UserDetailedViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
# from api.post.viewsets import PostViewSet
from api.post.viewsets.viewsets import CreatePostViewSet, UpdatePostViewSet
from api import views

routes = SimpleRouter()
# AUTHENTICATION
routes.register(r'api/auth/login', LoginViewSet, basename='auth-login')
routes.register(r'api/auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'api/auth/refresh', RefreshViewSet, basename='auth-refresh')

# SERVICE ENDPOINTS REQUIRED
# /authors/
routes.register(r'authors/(?P<id>[0-9a-f-])', UserDetailedViewSet, basename='user1')
routes.register(r'authors', UserViewSet, basename='user')

# POSTS
#routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts/(?P<postID>[0-9a-f-]+)', UpdatePostViewSet, basename = 'post')
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts/(?P<postID>[0-9a-f-]+)', views.PostDetailedView, basename = 'post1')
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts', views.PostView, basename = 'post')

# Comments
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts/(?P<postID>[0-9a-f-]+)/comments', views.CommentView, basename = 'comment')
#routes.register(r'authors/(?P<id>[0-9a-f-]+)/comments', views.CommentView, basename = 'comment')

# Likes for posts
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts/(?P<postID>[0-9a-f-]+)/likes', views.LikePostView, basename = 'likepost')

# Likes for comments
routes.register(r'authors/(?P<id>[0-9a-f-]+)/posts/(?P<postID>[0-9a-f-]+)/comments/(?P<commentID>[0-9a-f-]+)/likes', views.LikeCommentView, basename = 'likecomment')

# Liked posts and comments
routes.register(r'authors/(?P<id>[0-9a-f-]+)/liked', views.LikedView, basename = 'liked')

# FOLLOWERS
routes.register(r'authors/(?P<id>[0-9a-f-]+)/followers/(?P<foreign_author_id>[0-9a-f-]+)', FollowersDetailedViewSet, basename = 'followers')
routes.register(r'authors/(?P<id>[0-9a-f-]+)/followers', FollowersViewSet, basename = 'followers')

# INBOX
routes.register(r'authors/(?P<id>[0-9a-f-]+)/inbox', InboxViewSet, basename='inbox')

urlpatterns = [
    *routes.urls
]