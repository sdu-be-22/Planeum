from django import views
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, CommentDeleteView

urlpatterns = [
    path("",views.PostListView.as_view(), name='newsfeed'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]
