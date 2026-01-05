from django.urls import path
from task_management.views import ToDoListView

urlpatterns = [
    path('todos/', ToDoListView.as_view(), name='todo_list')
]