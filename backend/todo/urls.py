from django.urls import path
from .views import todo_list, todo

urlpatterns = [
    path('todo-list/', todo_list, name='todo-list'),
    path('todo/<str:id>/', todo, name='todo'),
]