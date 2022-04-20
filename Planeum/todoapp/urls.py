from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.list, name = 'list'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('complete/<todo_id>', views.complete, name='complete'),
]
