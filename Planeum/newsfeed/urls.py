from django import views
from django.urls import path
from . import views
from .views import PostListView
app_name = 'newsfeed'

urlpatterns = [
    path("",views.PostListView.as_view(), name='newsfeed'),
]
