from django.urls import path
from .views import todo_list, todo, create_todo, update_todo, delete_todo

urlpatterns = [
    path('todo-list/', todo_list, name='todo-list'),
    path('todo/<str:id>/', todo, name='todo'),
    path('create-todo/', create_todo, name='create-todo'),
    path('update-todo/<str:id>/', update_todo, name='update-todo'),
    path('delete-todo/<str:id>/', delete_todo, name='delete-todo'),
]