from django.urls import path
from . import views
from todo.views import todoappView, addTodoView 


urlpatterns = [
    path("", views.todo, name="todo"),
    path('addTodoItem/',addTodoView),
]