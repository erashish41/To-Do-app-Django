from django.urls import path
from task_management.views import (
    ToDoListView, ToDoDetailView, ToDoCreateView, 
    TodoUpdateView, TodoDeleteView
    )

urlpatterns = [
    path('todos/', ToDoListView.as_view(), name='todo_list'),
    path('todos/create/', ToDoCreateView.as_view(), name='todo_create'),
    path('todos/<uuid:pk>/', ToDoDetailView.as_view(), name='todo_details'),
    path('todos/<uuid:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('todos/<uuid:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete')
]