from rest_framework.routers import SimpleRouter
from api.user.viewsets import FollowersViewSet, UserViewSet, FollowersDetailedViewSet, UserDetailedViewSet
from api.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
# from api.post.viewsets import PostViewSet
from api import views
from django.urls import path, re_path, include

routes = SimpleRouter()
urlpatterns = [
    path('api/auth/register/', RegistrationViewSet.as_view({'post': 'create'})),
    path('api/auth/login/', LoginViewSet.as_view({'post': 'create'})),
    path('authors/', UserViewSet.as_view({'get': 'list'})),
    path('authors/<str:id>/', UserDetailedViewSet.as_view({'get': 'retrieve', 'post': 'create',})),
    path('authors/<str:id>/followers/', FollowersViewSet.as_view({'get': 'list'})),
    path('authors/<str:id>/followers/<str:foreign_author_id>/', FollowersDetailedViewSet.as_view({'get': 'retrieve', 'post': 'create', 'delete': 'destroy'})),
    path('authors/<str:id>/posts/', views.PostView.as_view({'get': 'list', 'post': 'create'})),
    path('authors/<str:id>/posts/<str:postID>/', views.PostDetailedView.as_view({'get': 'retrieve', 'post': 'create', 'delete': 'destroy'})),
    path('authors/<str:id>/posts/<str:postID>/comments/', views.CommentView.as_view({'get': 'list', 'post': 'create'})),
    path('authors/<str:id>/posts/<str:postID>/comments/<str:commentID>/', views.CommentDetailedView.as_view({'get': 'retrieve'})),
    path('authors/<str:id>/posts/<str:postID>/comments/<str:commentID>/likes/', views.LikeCommentView.as_view({'get': 'list', 'post': 'create'})),
    path('authors/<str:id>/posts/<str:postID>/likes/', views.LikePostView.as_view({'get': 'list', 'post': 'create'})),
    path('authors/<str:id>/liked/', views.LikedView.as_view({'get': 'list'})),
    path('authors/<str:id>/inbox/', views.InboxView.as_view({'get': 'list', 'post': 'create'})),
]