from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='main'),
    path('post_creation_page/',
         views.PostCreationFormView.as_view()),
    path('posts/<int:pk>/post_single_page/',
         views.PostSinglePageView.as_view(), name='comments'),
    path('top10/',
         views.PostsListViewTop10.as_view(), name='top10'),
    path('subscribe/',
         views.PostListViewSubscribe.as_view(), name='subscribe'),
]
