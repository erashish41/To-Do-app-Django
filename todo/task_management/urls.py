from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from task_management.views import (
    TaskListView, TaskDetailView, TaskCreateView, 
    TaskUpdateView, TaskDeleteView,
    CommentCreateView, AttachmentCreateView, AttachmentDeleteView
    )

urlpatterns = [
    path('todos/', TaskListView.as_view(), name='todo_list'),
    path('todos/create/', TaskCreateView.as_view(), name='todo_create'),
    path('todos/<uuid:pk>/', TaskDetailView.as_view(), name='todo_details'),
    path('todos/<uuid:pk>/update/', TaskUpdateView.as_view(), name='todo_update'),
    path('todos/<uuid:pk>/delete/', TaskDeleteView.as_view(), name='todo_delete'),
    

    
    path('todos/<uuid:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    
    path('todos/<uuid:pk>/attachment/add/', AttachmentCreateView.as_view(), name='attachment_add'),
    path('attachment/<uuid:pk>/delete/', AttachmentDeleteView.as_view(), name='attachment_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)