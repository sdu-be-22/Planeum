from django import views
from django.urls import path
from . import views
from.views import PostListView
app_name = 'homepage'

urlpatterns = [
    path("",views.homepage, name='homepage'),
    path("",views.PostListView.as_view(), name='post-list'),
]
