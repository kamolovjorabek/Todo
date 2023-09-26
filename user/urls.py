from django.urls import path
from .views import todo, created_todo, update_todo, delete_todo

urlpatterns = [
    path('', todo, name='todo'),
    path('created_todo', created_todo, name='created_todo'),
    path('update_todo', update_todo, name='update_todo'),
    path('delete_todo', delete_todo, name='delete_todo')
]