from django.urls import path

from .views import PhotoPostsList, PhotoPostDetail
from .views import UsersList, UserDetail

urlpatterns = [
    path('posts/', PhotoPostsList.as_view(), name='posts_list'),
    path('posts/<int:pk>', PhotoPostDetail.as_view(), name='post_detail'),
    path('users/', UsersList.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='users_detail'),
]
