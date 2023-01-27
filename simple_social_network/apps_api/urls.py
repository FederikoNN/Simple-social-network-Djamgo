from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PhotoPostsList.as_view(), name='posts_list'),
    path('posts/top10/', PhotoPostTop10.as_view(), name='top10_posts_list'),
    path('posts/create/', PhotoPostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/', PhotoPostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/comments/', CommentsToPhotoPost.as_view(),
         name='post_comments'),
    path('posts/<int:pk>/add_comment/', CommentAddToPhotoPost.as_view(),
         name='add_comment'),
    path('posts/<int:pk>/rating/', RatingAddPhotoPost.as_view(),
         name='add_rating_photo'),
    path('posts/<int:pk>/comments/<int:sk>/rating/',
         RatingAddComment.as_view(), name='add_rating_comment'),
    path('users/', UsersList.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='users_detail'),
    path('subscribe/', SubscribesUser.as_view(), name='users_subscribe'),
    path('add_subscribe/', SubscribeAdd.as_view(), name='add_subscribe'),
]
