from django import views
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, CommentDeleteView, AddLike, AddDislike, UserSearch,  PostEditView, PostDeleteView

urlpatterns = [
    path("",views.PostListView.as_view(), name='newsfeed'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('search/', UserSearch.as_view(), name='profile-search'),
]
