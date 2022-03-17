from django.urls import path
from . import views

urlpatterns = [
    path("",views.home ,name='app-home'),
    path("create_new",views.manageTodo ,name='app-create-form'),
    path("manage_todo",views.manageTodo ,name='app-update-form'),
    path("save_todo",views.save_todo ,name='app-save-todo'),
    path("ajax_update_state",views.todo_change_state ,name='app-ajax_update_state'),
    path("remove_todo",views.delete_todo ,name='app-delete_todo'),
]