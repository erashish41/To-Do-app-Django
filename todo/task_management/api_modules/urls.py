# urls.py

from django.urls import path
from task_management.api_modules.views import (
    taskView, taskDetail
    )

urlpatterns = [
    path('v2/task/', taskView, name='task_list'),
    path('v2/task/<uuid:pk>/', taskDetail, name='task_detail'),
]
