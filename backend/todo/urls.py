from django.urls import path
from .views import todo_list, todo, create_todo

urlpatterns = [
    path('todo-list/', todo_list, name='todo-list'),
    path('todo/<str:id>/', todo, name='todo'),
    path('create-todo/', create_todo, name='create-todo'),
]